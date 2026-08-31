# -*- coding: utf-8 -*-
"""Genera los Apps Script que crean los encuentros del semestre en Google Calendar.

Qué resuelve
------------
Los encuentros quedan como **bloques del calendario personal del docente**: sin lista de
invitados y sin enviar ningún correo. Lo que el docente necesita de este camino, y que
importar un `.ics` no le da, es que **cada sesión tenga su propia sala de Meet**:
N encuentros, N enlaces distintos, creados por la API de Calendar.

El enlace de cada sesión queda en **Ubicación** y al final de la **descripción** del evento.
No sale de ahí solo: no hay invitaciones, así que el docente publica el enlace de la sesión
que toca por el canal que use con el grupo.

Cada sala se pide con un `requestId` determinista y **distinto por sesión**
(`uniajc-<codigo>-<grupo>-<periodo>-sNN`). Eso es lo que hace la operación repetible: volver
a ejecutar no crea una segunda sala para la misma sesión, y el enlace de una sesión que ya
existe no cambia por reejecutar.

Dos fuentes de verdad, 7 cursos
-------------------------------
- `semestre_2026_2.json` -> los 4 cursos de 13 sesiones (24/08 a 22/11).
- `introduccion_ingenieria_2026_2.json` -> los 3 GRUPOS de Introducción a la Ingeniería
  (FI300101), cada uno con su día, su horario y su calendario propio. Van en un archivo
  aparte a propósito (16 sesiones de 90 min, dos días distintos, fechas que se pasan a
  diciembre): `validar_calendario.py` habría fallado con ellos dentro. Aquí NO se fusionan;
  un adaptador (`cursos_introduccion_ingenieria`) los pasa a la forma de curso que este
  generador ya consume, una entrada de `CURSOS` por grupo.

4 + 3 = 7 cursos. La nómina **no** hace falta para generar nada de esto (los eventos no
tienen invitados); sigue siendo necesaria para la planilla de asistencia, que la produce
`generar_eventos_calendario.py`.

Salidas
-------
1. Uno por curso (con el grupo en el nombre cuando varios comparten carpeta):
   `<Curso>/Plan curso/<periodo>/_privado/CrearEncuentros - <Curso>.gs`
2. Uno consolidado con los 7 cursos:
   `_privado/<periodo>/CrearEncuentros - TODO EL SEMESTRE <periodo>.gs`

Los dos salen de la **misma plantilla** (`PLANTILLA` + `MOTOR`), a propósito: mantener dos
copias del motor garantizaba que divergieran y que la desactualizada fuera la que alguien
acabara pegando en Apps Script.

Siguen en `_privado/` por convención del proyecto, aunque ya **no lleven datos personales**.

Uso
---
    python config/calendario/generar_apps_script_encuentros.py
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

import generar_eventos_calendario as ev

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads(Path(__file__).with_name("semestre_2026_2.json").read_text(encoding="utf-8"))
DATA_II = json.loads(
    Path(__file__).with_name("introduccion_ingenieria_2026_2.json").read_text(encoding="utf-8"))
PERIODO = DATA["periodo"]
DOCENTE = DATA["docente"]["nombre_completo"]

if DATA_II["periodo"] != PERIODO:
    raise SystemExit(
        f"Los dos JSON no son del mismo periodo: semestre={PERIODO!r} "
        f"introduccion_ingenieria={DATA_II['periodo']!r}. Revisa cuál está desactualizado.")

#: Rango del semestre «corto» (los 4 cursos de `semestre_2026_2.json`).
INICIO_SEM = DATA["inicio"]
FIN_SEM = DATA["fin"]

#: Rango GLOBAL del .gs: la unión de las dos fuentes.
#:
#: Los 3 grupos de Introducción a la Ingeniería llegan al 2026-12-17 y 2026-12-22, más de un
#: mes después del 2026-11-22 en que cierran los otros cuatro. Si el rango global se quedara
#: en noviembre, `_fantasmas_` no vería las últimas ~4 sesiones de cada grupo nuevo.
#:
#: Pero ampliarlo NO puede hacer que los 4 cursos viejos barran un mes de más del calendario
#: personal del docente buscando títulos que los mencionen. Por eso cada curso lleva TAMBIÉN
#: su propio `inicio`/`fin` en el array CURSOS, y `_fantasmas_` usa el del curso: el global
#: solo es el techo del periodo (y lo que verifican las pruebas).
INICIO = min([INICIO_SEM] + [g["inicio"] for g in DATA_II["grupos"]])
FIN = max([FIN_SEM] + [g["fin"] for g in DATA_II["grupos"]])

TZ = "America/Bogota"

#: Minutos que se permite correr a las funciones de todo el semestre antes de cortar sola.
#: Apps Script mata la ejecución a los 30 min en cuentas Workspace (y a los 6 en cuentas
#: gratuitas). Cortar antes y a propósito deja un log legible en vez de un error; como todo
#: es idempotente, volver a ejecutar retoma donde quedó.
MINUTOS_MAX = 25

ROMANOS = {"i", "ii", "iii", "iv", "v"}

#: Códigos de grupo tipo `SB141B` / `LB141F`, para no dejarlos como «Sb141b» en el nombre de
#: las funciones del .gs: el docente elige la función en un desplegable y ahí es lo único que
#: distingue un grupo de otro.
_GRUPO_SIGLA = re.compile(r"^[a-z]{2}\d{3}[a-z]$")

#: Cuántas veces aparece cada código de asignatura entre los 7 cursos del periodo. Se cuenta
#: sobre los DOS JSON, no sobre los cursos de un .gs concreto: FI300101 lo comparten los tres
#: grupos de Introducción a la Ingeniería aunque cada uno tenga su propio archivo.
_CUENTA_CODIGOS: dict[str, int] = {}
for _m in DATA["cursos"].values():
    _CUENTA_CODIGOS[_m["codigo"]] = _CUENTA_CODIGOS.get(_m["codigo"], 0) + 1
for _g in DATA_II["grupos"]:
    _c = DATA_II["curso"]["codigo"]
    _CUENTA_CODIGOS[_c] = _CUENTA_CODIGOS.get(_c, 0) + 1


def _codigo_compartido(codigo: str) -> bool:
    """True si otro curso del periodo usa el mismo código de asignatura.

    Lo consume `_esDeEsteCurso_` en el .gs: cuando el código está compartido, un evento cuyo
    título solo mencione `FI300101` podría ser de cualquiera de los tres grupos, y borrarlo a
    cuenta de uno se llevaría el encuentro de otro.
    """
    return _CUENTA_CODIGOS.get(codigo, 0) > 1


def js(s) -> str:
    """Literal JS de una cadena."""
    return "'" + str(s).replace("\\", "\\\\").replace("'", "\\'") + "'"


def nombre_js(key: str) -> str:
    """`bases_datos_ii` -> `BasesDatosII`; `..._sb141b` -> `...SB141B`."""
    partes = []
    for p in key.split("_"):
        low = p.lower()
        if low in ROMANOS or _GRUPO_SIGLA.match(low):
            partes.append(p.upper())
        else:
            partes.append(p.capitalize())
    return "".join(partes)


# ─────────────────────────────────────────── Introducción a la Ingeniería (3 grupos)

def _texto_cierre_corte(n_corte: int) -> str:
    """Frase del cierre de corte, con el porcentaje sacado del JSON (no escrito a mano)."""
    corte = next(c for c in DATA_II["cortes"] if c["corte"] == n_corte)
    return f"Cierra el Corte {corte['corte']} ({corte['pct']}): {corte['cierre']}."


def cursos_introduccion_ingenieria() -> list[tuple[str, dict]]:
    """Los 3 grupos de FI300101 con la MISMA forma que `semestre_2026_2.json['cursos'][k]`.

    Así `sesiones_de`, `bloque_curso`, `ev.titulo` y `ev.privado_de` funcionan sin ramas
    especiales. Lo que traduce el adaptador:

    - `grupos[i]['sesiones']` -> `clases[]`, con `sesion` -> `n` (y `None` en la semana
      autónoma: NO 0, que daría «Sesión 0» en el título y se quedaría así para siempre).
    - `tipo: 'autonoma_festivo'` -> `'autonoma'`. El motor y `ev.titulo` comparan contra
      `'autonoma'` exacto; sin la traducción, la semana del festivo del 08/12 saldría con
      sala de Meet y titulada `[SINCRONICO]`.
    - `tema_n` -> `tema`, tomando el título legible de `temas[].tema_acentos` (en `temas[]`
      NO hay clave `titulo`).
    - `cierra_corte` -> `cierre_corte`, ya redactado. NO se usa `parcial`: este curso no
      tiene parciales escritos y `ev.titulo` titularía los eventos «Parcial N · …».

    El GRUPO va dentro de `nombre`, y eso no es cosmético:

        `_esDeEsteCurso_` decide «este evento es mío» comparando el título contra
        `c.nombre`, y los tres grupos comparten nombre y código (FI300101). SB141B es
        jueves 14:30 y SB141C martes 14:30 — la MISMA hora. Con el nombre pelado, el
        barrido de fantasmas de un grupo se llevaría los encuentros de otro. Y SB141C y
        LB141F caen los dos en martes y en las mismas 17 fechas: con el mismo título,
        `_buscarEvento_` daría los eventos de uno por «ya existentes» del otro.

        No lo «simplifiques» quitando el grupo del nombre.
    """
    temas = {t["n"]: t["tema_acentos"] for t in DATA_II["temas"]}
    c = DATA_II["curso"]
    out: list[tuple[str, dict]] = []
    for g in DATA_II["grupos"]:
        clases = []
        for s in g["sesiones"]:
            tema_n = s.get("tema_n")
            autonoma = str(s.get("tipo", "")).startswith("autonoma")
            clases.append({
                "n": s.get("sesion"),
                "fecha": s["fecha"],
                "tipo": "autonoma" if autonoma else s["tipo"],
                "festivo": s.get("festivo"),
                "parcial": False,
                "clases_material": [tema_n] if tema_n else [],
                "tema": temas.get(tema_n) or (s.get("tarea") or "Trabajo autónomo del equipo"),
                "sesion_doble": False,
                "cierre_corte": (_texto_cierre_corte(s["cierra_corte"])
                                 if s.get("cierra_corte") else None),
                "tarea": s.get("tarea"),
            })
        out.append((f"{c['key']}_{g['grupo'].lower()}", {
            "folder": c["folder"],
            # El grupo, dentro del nombre: ver el docstring. Es la identidad del curso.
            "nombre": f"{c['nombre_acentos']} · {g['grupo']}",
            "nombre_base": c["nombre_acentos"],
            "codigo": c["codigo"],
            "grupo": g["grupo"],
            "dia": g["dia"],
            # Raya larga como los otros 4 cursos (el JSON nuevo usa guion normal). `ev.hhmm`
            # acepta las dos: solo busca pares HH:MM. Esto es para que la tabla del LEEME y
            # el log no mezclen dos separadores distintos.
            "horario": g["horario"].replace(" - ", " – "),
            "duracion_min": c["duracion_min"],
            "modalidad": c["modalidad"],
            "n_clases": c["n_sesiones"],
            # Rango PROPIO: `_fantasmas_` barre este, no el del semestre corto.
            "inicio": g["inicio"],
            "fin": g["fin"],
            "clases": clases,
        }))
    return out


def _titulo(meta: dict, cl: dict) -> str:
    """Título del evento. Es la IDENTIDAD del evento para `_buscarEvento_`.

    Reusa `ev.titulo` (misma cadena que el .ics y el CSV del otro generador) y solo resuelve
    el caso que `ev.titulo` todavía no sabe expresar: la semana autónoma por festivo de
    SB141C y LB141F, que no tiene número de sesión (`ev.titulo` diría «Sesión None»).
    """
    if cl.get("n") is None:
        return f"[AUTONOMO] Semana autónoma · {meta['nombre']}"
    return ev.titulo(meta, cl)


def _descripcion(meta: dict, cl: dict) -> str:
    """Descripción del evento.

    Los 4 cursos del semestre corto la toman de `ev.descripcion`. Los grupos de Introducción
    a la Ingeniería NO: esa función lleva «Sesión N de 13» cableado (diría «de 13» teniendo
    16), no sabe de cierres de corte y no tiene rama para una sesión sin número. Se redacta
    aquí, con el mismo estilo y el mismo orden de campos.
    """
    if not meta.get("nombre_base"):     # los 4 cursos de semestre_2026_2.json
        return ev.descripcion(meta, cl)

    total = meta["n_clases"]
    if cl.get("n") is None:
        partes = [
            f"{meta['nombre_base']} ({meta['codigo']}) · grupo {meta['grupo']}",
            f"Semana autónoma · {ev.TIPO_ETIQUETA['autonoma']}",
        ]
        if cl.get("festivo"):
            partes.append(f"Festivo: {cl['festivo']}")
        partes.append("No hay encuentro sincrónico: no lleva sala de Meet.")
        if cl.get("tarea"):
            partes.append(f"Trabajo del equipo: {cl['tarea']}")
    else:
        partes = [
            f"{meta['nombre_base']} ({meta['codigo']}) · grupo {meta['grupo']}",
            f"Sesión {cl['n']} de {total} · {ev.TIPO_ETIQUETA.get(cl['tipo'], cl['tipo'])}",
            f"Tema: {cl['tema']}",
            f"Material docente: Clase {cl['n']}",
        ]
        if cl.get("festivo"):
            partes.append(f"Festivo: {cl['festivo']}")
        if cl.get("cierre_corte"):
            partes.append(cl["cierre_corte"])
    partes.append(f"Docente: {DOCENTE} · {ev.CORREO_DOCENTE}")
    return " | ".join(partes)


def sesiones_de(meta: dict) -> list[dict]:
    ini, fin = ev.hhmm(meta["horario"])          # '180000', '200000'
    out = []
    for cl in meta["clases"]:
        # Las autonomas SI van al calendario (queda la fecha de cierre a la vista), pero NO
        # llevan Meet: no hay encuentro. Vale igual para las autonomas por festivo de los
        # grupos de Introduccion a la Ingenieria (el adaptador ya traduce el tipo).
        out.append({
            "subject": _titulo(meta, cl),
            "fecha": cl["fecha"],
            "ini": f"{ini[:2]}:{ini[2:4]}",
            "fin": f"{fin[:2]}:{fin[2:4]}",
            "desc": _descripcion(meta, cl),
            "meet": cl["tipo"] != "autonoma",
        })
    return out


def bloque_curso(key: str, meta: dict, ses: list[dict]) -> str:
    """El literal JS de un curso dentro del array CURSOS.

    No hay campo de invitados: los eventos son bloques del calendario del docente. Por eso
    este archivo ya no escribe ningún dato personal en el .gs.
    """
    sesiones = "\n".join(
        ("      {{ subject: {s}, fecha: {f}, ini: {i}, fin: {n}, meet: {m},"
         " desc: {d} }},").format(
            s=js(x["subject"]), f=js(x["fecha"]), i=js(x["ini"]), n=js(x["fin"]),
            m=("true" if x["meet"] else "false"), d=js(x["desc"]))
        for x in ses
    )
    return f"""  {{
    key:      {js(key)},
    nombre:   {js(meta['nombre'])},
    codigo:   {js(meta['codigo'])},
    grupo:    {js(meta['grupo'])},
    dia:      {js(meta['dia'])},
    horario:  {js(meta['horario'])},
    // Rango PROPIO del curso. `_fantasmas_` barre este, no el global: los 3 grupos de
    // Introduccion a la Ingenieria llegan a diciembre y los otros 4 cierran el 22/11, y
    // nadie tiene que rastrear un mes extra del calendario personal del docente.
    inicio:   {js(meta.get('inicio') or INICIO_SEM)},
    fin:      {js(meta.get('fin') or FIN_SEM)},
    // true cuando OTRO curso de este periodo comparte el codigo (los 3 grupos de FI300101).
    // Entonces el codigo solo, en un titulo, no basta para decir «este evento es mio».
    codigoCompartido: {'true' if _codigo_compartido(meta['codigo']) else 'false'},
    // Base del requestId. Cada sesion pide su sala con requestId + '-sNN': distinto por
    // sesion, y estable entre corridas para que reejecutar no cree una segunda sala.
    requestId: {js(f"uniajc-{meta['codigo']}-{meta['grupo']}-{PERIODO}")},
    sesiones: [
{sesiones}
    ]
  }},"""


# ───────────────────────────────────────────────────────────── MOTOR (compartido)
#
# Este texto es idéntico en los dos .gs. Va aparte para que no haya dos copias que puedan
# divergir. Se inserta como *argumento* de `.format()`, no como parte de la plantilla, así que
# las llaves van sencillas: es JavaScript literal.

MOTOR = """
// ═══════════════════════════════════════════════ CALENDARIO

/**
 * El calendario con el que trabaja el script.
 * Preferimos un ID explicito: el «por omision» depende de la cuenta con la que se abrio
 * Apps Script, y si un dia se ejecuta con otra sesion escribe en un calendario distinto sin
 * avisar. Con ~100 eventos y sus salas de Meet ya creados, eso no se deshace facil.
 */
function _cal_() {
  if (CALENDAR_ID) {
    var c = CalendarApp.getCalendarById(CALENDAR_ID);
    if (!c) throw new Error('CALENDAR_ID no corresponde a un calendario visible: ' + CALENDAR_ID);
    return c;
  }
  // return CalendarApp.getDefaultCalendar();   // <- alternativa: calendario por omision
  throw new Error('Falta CALENDAR_ID. Ejecuta listarCalendarios() y pega el ID arriba, ' +
                  'o descomenta la linea de getDefaultCalendar() en _cal_().');
}

/** El mismo calendario, para la API avanzada (que recibe el id, no el objeto). */
function _calId_() {
  // return 'primary';   // <- alternativa: calendario por omision
  if (!CALENDAR_ID) throw new Error('Falta CALENDAR_ID (ver _cal_()).');
  return CALENDAR_ID;
}

/** Imprime los calendarios de la cuenta con su ID, para copiar el que toque. */
function listarCalendarios() {
  var todos = CalendarApp.getAllCalendars();
  var pormision = CalendarApp.getDefaultCalendar().getId();
  Logger.log('Calendarios visibles en esta cuenta (' + todos.length + '):');
  for (var i = 0; i < todos.length; i++) {
    Logger.log('  ' + todos[i].getName() +
               (todos[i].getId() === pormision ? ' [por omision]' : '') +
               '  ->  ' + todos[i].getId());
  }
  Logger.log('');
  Logger.log('Copia el ID que corresponda y pegalo en CALENDAR_ID, arriba del todo.');
  Logger.log('Usa el MISMO en el script de grabaciones (manual 02).');
}

// ═══════════════════════════════════════════════ CURSOS Y RELOJ

/**
 * Zona horaria con la que Apps Script construye las fechas.
 *
 * Importa mas de lo que parece: `_fecha()` usa `new Date(anio, mes, dia, hora, min)`, y ese
 * constructor interpreta los componentes en la zona del PROYECTO — no en la del calendario ni
 * en la del curso. Si el proyecto se creo en otra zona (Google no siempre pone la local), los
 * eventos entran corridos y NO se arregla reejecutando: el evento ya existe con su sala de
 * Meet, y este script lo reutiliza tal cual.
 */
function _zonaDelProyecto_() {
  try { return Session.getScriptTimeZone(); } catch (e) { return '(no pude leerla)'; }
}

function _zonaCorrecta_() {
  return _zonaDelProyecto_() === TZ;
}

/**
 * Se planta si la zona no es la del curso. Devuelve true cuando hay que abortar.
 * Preferimos no hacer nada a hacerlo a la hora equivocada.
 */
function _zonaMal_(quien) {
  if (_zonaCorrecta_()) return false;
  Logger.log('BLOQUEADO: ' + quien + ' no corre con la zona del proyecto en ' +
             _zonaDelProyecto_() + '.');
  Logger.log('Ponla en ' + TZ + ': Configuracion del proyecto (engranaje) -> Zona horaria.');
  Logger.log('Con otra zona los eventos entrarian a otra hora, y reejecutar NO los mueve:');
  Logger.log('habria que borrarlos y volver a crearlos (con salas de Meet nuevas).');
  return true;
}

/** El curso con esa `key`, o revienta con un mensaje util. */
function _curso_(key) {
  for (var i = 0; i < CURSOS.length; i++) if (CURSOS[i].key === key) return CURSOS[i];
  throw new Error('No hay ningun curso con key=' + key + ' en este script.');
}

var _T0 = null;

/** Arranca el reloj de las funciones de varios cursos. */
function _arrancarReloj_() { _T0 = new Date().getTime(); }

/**
 * true cuando se agoto el plazo que nos dimos. Apps Script mata la ejecucion sola (30 min en
 * Workspace, 6 en cuentas gratuitas) y ahi el log se pierde a medias; cortar antes y a
 * proposito deja un resumen legible. Todo es idempotente: reejecutar retoma donde quedo.
 */
function _sinTiempo_() {
  if (_T0 === null) return false;
  return (new Date().getTime() - _T0) > MINUTOS_MAX * 60 * 1000;
}

/**
 * Aviso de corte. `reanudarCon` es la funcion que hay que ejecutar para continuar, y NO
 * siempre es la que se corto: reejecutar una `recrear*` vuelve a borrar lo que acababa de
 * recrear, y con cada evento se va la sala de Meet que acababa de crear. Solo `crear*`
 * reanuda de verdad.
 */
function _avisoDeCorte_(reanudarCon, noReejecutar) {
  Logger.log('');
  Logger.log('*** CORTADO a los ' + MINUTOS_MAX + ' min para no chocar con el limite de');
  Logger.log('*** Apps Script. NO se perdio nada.');
  if (noReejecutar) {
    Logger.log('*** OJO: NO vuelvas a ejecutar ' + noReejecutar + ' — volveria a BORRAR lo que');
    Logger.log('*** acaba de recrear, y a tirar las salas de Meet que acababa de crear.');
  }
  Logger.log('*** Para continuar ejecuta: ' + (reanudarCon || 'la funcion de crear') );
  Logger.log('*** (reutiliza los eventos y las salas que ya existen).');
}

/** Cabecera de una seccion de curso en el log. */
function _titulo_(c) {
  Logger.log('');
  Logger.log('══ ' + c.nombre + '  (' + c.codigo + ' · grupo ' + c.grupo + ' · ' +
             c.dia + ' ' + c.horario + ')');
}

// ═══════════════════════════════════════════════ MOTOR: VERIFICAR

/** SOLO LECTURA: que pasaria con este curso. */
function _verificar_(c) {
  var cal = _cal_();
  _titulo_(c);
  Logger.log('  Tipo             : bloque de TU calendario (sin invitados, sin correos)');
  Logger.log('  Rango del curso  : ' + c.inicio + ' .. ' + c.fin);
  Logger.log('  Meet             : uno distinto por sesion (' + _conMeet_(c) + ' de ' +
             c.sesiones.length + ' sesiones lo llevan; las autonomas no)');
  var existen = 0, conSala = 0;
  for (var i = 0; i < c.sesiones.length; i++) {
    var s = c.sesiones[i];
    var ya = _buscarEvento_(cal, s);
    var sala = '';
    if (ya) {
      existen++;
      sala = s.meet ? _meetNativo_(_idApi_(ya)) : '';
      if (sala) conSala++;
    }
    Logger.log('  ' + (ya ? 'YA EXISTE  ' : 'se crearia ') + s.fecha + ' ' + s.ini + '-' +
               s.fin + '  ' + s.subject +
               (sala ? '   ' + sala : (ya && s.meet ? '   (sin Meet aun)' : '')));
  }
  Logger.log('  -> ' + c.sesiones.length + ' sesion(es) · ya creadas: ' + existen +
             ' · con sala de Meet: ' + conSala + '/' + _conMeet_(c));
  return { sesiones: c.sesiones.length, existen: existen, conSala: conSala };
}

/** Lo que no depende del curso: calendario, permisos, modo. */
function _entorno_() {
  var cal = _cal_();
  Logger.log('Modo             : ' + (SIMULAR ? 'SIMULACION (no toca nada)' : 'REAL'));
  Logger.log('Calendario       : ' + cal.getName() + '  [' + cal.getId() + ']');
  Logger.log('CALENDAR_ID      : ' + (CALENDAR_ID || '(vacio: usa listarCalendarios())'));
  Logger.log('Servicio avanzado: ' + (_apiCalendar_() ? 'activo' : 'NO ACTIVO — sin el no hay Meet'));
  Logger.log('Zona del proyecto: ' + _zonaDelProyecto_() +
             (_zonaCorrecta_() ? '  (correcta)' : '  <-- NO ES ' + TZ));
  if (!_zonaCorrecta_()) {
    Logger.log('');
    Logger.log('*** LA ZONA HORARIA DEL PROYECTO NO ES ' + TZ + '.');
    Logger.log('*** Las horas de los eventos las construye Apps Script con la zona del');
    Logger.log('*** PROYECTO, asi que entrarian corridas. Arreglalo antes de crear nada:');
    Logger.log('***   Configuracion del proyecto (engranaje) -> Zona horaria -> ' + TZ);
    Logger.log('*** Crear y borrar estan bloqueados hasta entonces.');
  }
  if (!_apiCalendar_()) {
    Logger.log('');
    Logger.log('Activa el servicio avanzado: Servicios (+) -> Google Calendar API -> Anadir.');
    Logger.log('Sin el los eventos se crean, pero SIN sala de Meet.');
  }
}

// ═══════════════════════════════════════════════ MOTOR: CREAR

/**
 * Crea los encuentros del curso como BLOQUES DE TU CALENDARIO, cada uno con SU sala de Meet.
 *
 * Los eventos no tienen invitados y no se envia ningun correo: son tus bloques de agenda. El
 * enlace de Meet de cada sesion queda en Ubicacion y al final de la descripcion, para que lo
 * compartas con el grupo por donde quieras.
 */
function _crear_(c) {
  var cal = _cal_();
  _titulo_(c);
  if (!SIMULAR && _zonaMal_('crear ' + c.nombre)) {
    return { creados: 0, reusados: 0, meet: 0, cortado: false };
  }
  if (SIMULAR) {
    Logger.log('  SIMULAR = true: no se creo nada. Ponlo en false cuando verificar() se vea bien.');
    return { creados: 0, reusados: 0, meet: 0, cortado: false };
  }

  var eventos = [], creados = 0, reusados = 0, omitidos = 0, cortado = false;
  for (var i = 0; i < c.sesiones.length; i++) {
    if (_sinTiempo_()) { cortado = true; break; }
    var s = c.sesiones[i];
    var ya = _buscarEvento_(cal, s);
    if (ya) {
      // El evento ya existe: se reutiliza tal cual. Eso es la idempotencia — reejecutar no
      // duplica nada y no toca el evento. Lo unico que se le asegura es su sala de Meet,
      // mas abajo.
      eventos.push({ ev: ya, i: i }); reusados++; continue;
    }
    // Antes de crear: mirar si ya hay un encuentro de este curso ese dia a esa hora con OTRO
    // titulo. Pasa siempre que el titulo cambia en el JSON (se marca un parcial, una sesion
    // pasa a autonoma, cambian los prefijos). Sin esto se creaba una serie entera al lado de
    // la vieja, con dos bloques y dos salas de Meet para el mismo dia.
    var gemelos = _delCursoEsaHora_(cal, c, s, s.subject);
    if (gemelos.length) {
      Logger.log('  AVISO: ' + s.fecha + ' ' + s.ini + ' ya tiene un encuentro de este curso');
      Logger.log('         con OTRO titulo: «' + gemelos[0].getTitle() + '»');
      Logger.log('         NO creo «' + s.subject + '» para no dejar dos.');
      Logger.log('         El titulo cambio en el JSON: usa eliminar/recrear para rehacer.');
      omitidos++;
      continue;
    }
    // Sin `guests` y sin `sendInvites`: es un bloque de TU calendario. Google no manda
    // ningun correo porque no hay a quien mandarlo.
    var nuevo = cal.createEvent(s.subject, _fecha(s.fecha, s.ini), _fecha(s.fecha, s.fin), {
      description: s.desc
    });
    eventos.push({ ev: nuevo, i: i });
    creados++;
    Utilities.sleep(300);   // no atropellar la cuota
  }
  Logger.log('  Eventos: ' + creados + ' creado(s) · ' + reusados + ' ya existia(n)' +
             (omitidos ? ' · ' + omitidos + ' OMITIDO(S) por titulo cambiado' : '') + '.');
  if (omitidos) {
    Logger.log('  *** ' + omitidos + ' sesion(es) sin crear: hay un encuentro viejo con otro');
    Logger.log('  *** titulo en ese hueco. Ejecuta eliminar' + ' y luego crear, o recrear.');
  }

  if (!_apiCalendar_()) {
    Logger.log('  Sin enlace de Meet: el servicio avanzado de Calendar no esta activo.');
    Logger.log('  Activalo y vuelve a ejecutar: no duplica eventos ni salas.');
    return { creados: creados, reusados: reusados, meet: 0, cortado: cortado };
  }

  // Una sala POR SESION. Cada una con su requestId, para que reejecutar no duplique.
  var nativos = 0, conMeet = 0;
  for (var j = 0; j < eventos.length; j++) {
    var idx = eventos[j].i;
    if (!c.sesiones[idx].meet) continue;      // autonoma: no hay encuentro, no lleva Meet
    if (_sinTiempo_()) { cortado = true; break; }
    conMeet++;
    var url = _asegurarMeet_(c, eventos[j].ev, idx);
    if (url) { nativos++; Logger.log('    ' + c.sesiones[idx].fecha + '  ' + url); }
  }
  Logger.log('  Meet: ' + nativos + '/' + conMeet + ' sesion(es) con su propia sala ' +
             '(las autonomas no llevan Meet a proposito).');
  Logger.log('  El enlace de cada sesion quedo en Ubicacion y en la descripcion del evento.');
  return { creados: creados, reusados: reusados, meet: nativos, cortado: cortado };
}

// ═══════════════════════════════════════════════ MOTOR: ELIMINAR

/**
 * Borra los encuentros de un curso. Tres pasadas:
 *   1. Por titulo exacto de cada sesion (lo que este script creo).
 *   2. Barrido de la MISMA fecha Y HORA de cada sesion, para cazar eventos de una corrida
 *      ANTERIOR cuyo titulo ya no coincide (paso al cambiar los prefijos o la modalidad).
 *      Solo borra si empieza a la hora de la sesion Y el titulo menciona el curso o su
 *      codigo: no toca eventos ajenos, ni los de otro curso que caiga el mismo dia, ni los
 *      apuntes personales del docente que mencionen el curso a otra hora.
 *   3. `_fantasmas_`: eventos del curso DENTRO DEL RANGO DEL CURSO que ya no caen en ninguna
 *      fecha del .gs actual (una sesion que se movio o se quito del JSON). Ver esa funcion.
 *
 * Borrar NO notifica a nadie: los eventos son bloques de tu calendario, sin invitados.
 *
 * Lo que si se pierde es la sala de Meet: al borrar un evento se va con el. Si despues
 * recreas, esa sesion queda con un enlace NUEVO, asi que el que ya hubieras compartido con
 * el grupo deja de servir.
 */
function _eliminar_(c) {
  var cal = _cal_();
  _titulo_(c);
  if (!SIMULAR && _zonaMal_('eliminar ' + c.nombre)) return 0;
  var exactos = [], huerfanos = [];

  for (var i = 0; i < c.sesiones.length; i++) {
    var s = c.sesiones[i];
    var evento = _buscarEvento_(cal, s);
    if (evento) exactos.push(evento);
    // El barrido corre SIEMPRE, tambien cuando el titulo actual si aparecio. Antes llevaba un
    // `continue` aqui, y eso lo apagaba justo en el caso para el que existe: cuando el titulo
    // cambio, `crear` dejo el evento nuevo, y el viejo sigue al lado. Con el filtro de hora,
    // el nombre del curso y `_yaEsta_`, barrer siempre no alcanza nada ajeno.
    var candidatos = _delCursoEsaHora_(cal, c, s, null);
    for (var j = 0; j < candidatos.length; j++) {
      if (!_yaEsta_(exactos, candidatos[j]) && !_yaEsta_(huerfanos, candidatos[j])) {
        huerfanos.push(candidatos[j]);
      }
    }
  }

  // Fantasmas: encuentros de este curso dentro del rango DEL CURSO que NO caen en ninguna
  // fecha del .gs actual. Aparecen cuando una sesion se movio o se quito del JSON (este
  // semestre paso de 15 a 13 sesiones): las dos primeras pasadas solo miran las fechas que
  // el .gs conoce, asi que sin esto quedaban ahi y ninguna funcion los encontraba.
  var fantasmas = _fantasmas_(cal, c, exactos, huerfanos);

  Logger.log('  Por titulo exacto  : ' + exactos.length);
  Logger.log('  Huerfanos del curso: ' + huerfanos.length +
             (huerfanos.length ? '  (titulo viejo, misma fecha y hora)' : ''));
  for (var k = 0; k < huerfanos.length; k++) {
    Logger.log('     huerfano: ' + huerfanos[k].getStartTime() + '  ' + huerfanos[k].getTitle());
  }
  Logger.log('  Fantasmas          : ' + fantasmas.length +
             (fantasmas.length ? '  (fecha que ya no esta en el calendario del curso)' : ''));
  for (var q = 0; q < fantasmas.length; q++) {
    Logger.log('     fantasma: ' + fantasmas[q].getStartTime() + '  ' + fantasmas[q].getTitle());
  }

  if (SIMULAR) {
    Logger.log('  SIMULAR = true: no se borro nada. Se borrarian ' +
               (exactos.length + huerfanos.length + fantasmas.length) + ' evento(s).');
    return 0;
  }

  var todos = exactos.concat(huerfanos).concat(fantasmas), n = 0;
  for (var m = 0; m < todos.length; m++) {
    try { todos[m].deleteEvent(); n++; Utilities.sleep(200); }
    catch (e) { Logger.log('  AVISO: no pude borrar «' + todos[m].getTitle() + '»: ' + e); }
  }
  Logger.log('  Eliminados=' + n + '. Sus salas de Meet se fueron con ellos.');
  return n;
}

/**
 * Eventos del calendario que caen el dia de `s`, a la HORA de `s`, y cuyo titulo menciona el
 * curso. Es la definicion operativa de «esto es uno de mis encuentros»: la hora exacta deja
 * fuera los apuntes personales del docente que nombren la asignatura a otra hora, y el nombre
 * del curso deja fuera el otro curso que caiga el mismo dia (BD II y Arquitectura son los dos
 * lunes).
 *
 * `excluir` es el titulo que NO cuenta (el de la sesion tal como se llama ahora), para poder
 * preguntar «hay alguno con OTRO titulo».
 */
function _delCursoEsaHora_(cal, c, s, excluir) {
  var arranca = _fecha(s.fecha, s.ini).getTime();
  var out = [];
  var delDia = cal.getEvents(_fecha(s.fecha, '00:01'), _fecha(s.fecha, '23:59'));
  for (var i = 0; i < delDia.length; i++) {
    if (delDia[i].getStartTime().getTime() !== arranca) continue;
    var titulo = delDia[i].getTitle();
    if (excluir && titulo === excluir) continue;
    if (_esDeEsteCurso_(c, titulo)) out.push(delDia[i]);
  }
  return out;
}

/**
 * true si el titulo es de ESTE curso, para no borrar eventos ajenos.
 *
 * `c.nombre` lleva el grupo cuando el curso tiene varios (p. ej. «... · SB141B»), asi que un
 * evento de otro grupo del mismo curso NO cuenta como propio.
 *
 * El codigo de asignatura vale como segunda pista — caza los apuntes que el docente nombra
 * «FI303215 parcial 2» — pero SOLO si ningun otro curso del periodo lo comparte. Los tres
 * grupos de Introduccion a la Ingenieria son todos FI300101: un titulo que solo mencione el
 * codigo podria ser de cualquiera, y borrarlo por cuenta de uno se llevaria el de otro.
 */
function _esDeEsteCurso_(c, titulo) {
  var t = String(titulo || '').toLowerCase();
  if (t.indexOf(String(c.nombre).toLowerCase()) !== -1) return true;
  if (c.codigoCompartido) return false;
  return t.indexOf(String(c.codigo).toLowerCase()) !== -1;
}

/**
 * Encuentros de este curso dentro del rango del curso que no estan ya contados. Exige la HORA
 * del curso, no solo el nombre: asi un «Calificar Bases de Datos II» de un martes cualquiera
 * no entra, pero si el evento de una sesion que se movio de fecha.
 *
 * El rango es el DEL CURSO (`c.inicio`/`c.fin`), no el global del periodo: los grupos de
 * Introduccion a la Ingenieria llegan a diciembre y los otros cuatro cierran el 22/11. Con un
 * rango global de diciembre, los cuatro cursos cortos barrerian un mes extra de TU calendario
 * personal buscando titulos que los mencionen.
 */
function _fantasmas_(cal, c, exactos, huerfanos) {
  var out = [];
  var horas = {};
  for (var i = 0; i < c.sesiones.length; i++) horas[c.sesiones[i].ini] = true;
  var todos = cal.getEvents(_fecha(c.inicio || INICIO, '00:01'),
                            _fecha(c.fin || FIN, '23:59'));
  for (var j = 0; j < todos.length; j++) {
    var ev = todos[j];
    if (!_esDeEsteCurso_(c, ev.getTitle())) continue;
    if (!horas[_hhmm_(ev.getStartTime())]) continue;
    if (_yaEsta_(exactos, ev) || _yaEsta_(huerfanos, ev) || _yaEsta_(out, ev)) continue;
    out.push(ev);
  }
  return out;
}

/** 'HH:MM' de un Date, para comparar contra el horario del curso. */
function _hhmm_(d) {
  var h = d.getHours(), m = d.getMinutes();
  return (h < 10 ? '0' + h : h) + ':' + (m < 10 ? '0' + m : m);
}

function _yaEsta_(lista, evento) {
  for (var i = 0; i < lista.length; i++) {
    if (lista[i].getId() === evento.getId()) return true;
  }
  return false;
}

// ═══════════════════════════════════════════════ MOTOR: RECREAR

/**
 * Borra TODO lo del curso y lo vuelve a crear, en una sola corrida. Se usa cuando se movieron
 * fechas o cambiaron los titulos y se prefiere partir de cero.
 *
 * No notifica a nadie (los eventos no tienen invitados), pero los enlaces de Meet CAMBIAN:
 * cada evento nuevo trae su propia sala. Si ya habias compartido el enlace de una sesion con
 * el grupo, hay que volver a compartirlo.
 */
function _recrear_(c) {
  if (SIMULAR) {
    _eliminar_(c);
    Logger.log('  ...y despues se crearian ' + c.sesiones.length +
               ' evento(s), cada uno con una sala de Meet NUEVA.');
    return { borrados: 0, creados: 0, cortado: false };
  }
  var borrados = _eliminar_(c);
  var r = _crear_(c);
  return { borrados: borrados, creados: r.creados, cortado: r.cortado };
}

// ═══════════════════════════════════════════════ MEET (una sala por sesion)

function _apiCalendar_() {
  try { return typeof Calendar !== 'undefined' && !!Calendar.Events; } catch (e) { return false; }
}

function _idApi_(evento) { return evento.getId().split('@')[0]; }

function _fecha(fechaIso, hhmm) {
  var p = fechaIso.split('-'), h = hhmm.split(':');
  return new Date(+p[0], +p[1] - 1, +p[2], +h[0], +h[1], 0);
}

/**
 * Evento ya existente para esa sesion (mismo titulo, mismo dia), o null.
 *
 * A proposito NO usa el parametro `search` de getEvents: esa es la busqueda de texto de
 * Google, que tokeniza y normaliza a su manera, y los titulos llevan `[SINCRONICO]`, `·` y
 * tildes. Si no casara, esta funcion devolveria null con el evento delante y el script
 * crearia un duplicado. Enumerar el dia y comparar el titulo exacto no depende del indice de
 * Google y en un dia hay un punado de eventos.
 *
 * Cuando varios coinciden en titulo, gana el que empieza a la HORA de la sesion. Es defensa en
 * profundidad para los cursos con varios grupos: SB141C y LB141F caen los dos en martes y en
 * las mismas 17 fechas, y hoy solo los separa el grupo dentro del titulo. Si algun dia el
 * titulo dejara de distinguirlos, la hora si lo hace. Si NINGUNO empieza a esa hora se cae al
 * comportamiento de siempre (el primero con ese titulo), para seguir reutilizando un evento
 * que el docente movio de hora a mano en vez de crearle un duplicado.
 */
function _buscarEvento_(cal, s) {
  var delDia = cal.getEvents(_fecha(s.fecha, '00:01'), _fecha(s.fecha, '23:59'));
  var iguales = [], aLaHora = [];
  for (var i = 0; i < delDia.length; i++) {
    if (delDia[i].getTitle() !== s.subject) continue;
    iguales.push(delDia[i]);
    if (_hhmm_(delDia[i].getStartTime()) === s.ini) aLaHora.push(delDia[i]);
  }
  var candidatos = aLaHora.length ? aLaHora : iguales;
  if (candidatos.length > 1) {
    // Devolver el primero y callar dejaba al resto invisible para todas las funciones.
    Logger.log('  AVISO: ' + candidatos.length + ' eventos con el mismo titulo el ' + s.fecha +
               ' («' + s.subject + '»). Borra los sobrantes a mano o usa recrear.');
  }
  return candidatos.length ? candidatos[0] : null;
}

function _uriDeConferencia_(conf) {
  if (!conf || !conf.entryPoints) return '';
  for (var i = 0; i < conf.entryPoints.length; i++) {
    if (conf.entryPoints[i].entryPointType === 'video') return conf.entryPoints[i].uri || '';
  }
  return '';
}

function _meetNativo_(id) {
  if (!_apiCalendar_()) return '';
  try {
    var ev = Calendar.Events.get(_calId_(), id, { conferenceDataVersion: 1 });
    return _uriDeConferencia_(ev && ev.conferenceData);
  } catch (e) { return ''; }
}

/** Cuantas sesiones del curso llevan Meet (las autonomas no). */
function _conMeet_(c) {
  var n = 0;
  for (var i = 0; i < c.sesiones.length; i++) if (c.sesiones[i].meet) n++;
  return n;
}

/** requestId de la sesion `i` de este curso: distinto por sesion, estable entre corridas. */
function _requestId_(c, i) {
  var n = String(i + 1);
  return c.requestId + '-s' + (n.length < 2 ? '0' + n : n);
}

/**
 * Se asegura de que la sesion `i` tenga SU propia sala, y devuelve su URL ('' si no se pudo).
 * Si el evento ya tiene una, la respeta: no la reemplaza ni crea una segunda.
 */
function _asegurarMeet_(c, evento, i) {
  var ya = _meetNativo_(_idApi_(evento));
  if (ya) { _anotarMeet_(evento, ya); return ya; }
  var url = _crearSala_(evento, _requestId_(c, i));
  if (url) _anotarMeet_(evento, url);
  return url;
}

/** Crea la sala de Meet de `evento` y devuelve su URL ('' si no se pudo). */
function _crearSala_(evento, requestId) {
  var id = _idApi_(evento);
  try {
    var res = Calendar.Events.patch({
      conferenceData: {
        createRequest: {
          requestId: requestId,
          conferenceSolutionKey: { type: 'hangoutsMeet' }
        }
      }
    }, _calId_(), id, {
      conferenceDataVersion: 1,
      // 'none' fijo: el evento no tiene invitados, asi que no hay a quien notificar.
      sendUpdates: 'none'
    });

    var url = _uriDeConferencia_(res && res.conferenceData);
    // Google crea la sala de forma asincrona: la primera respuesta puede venir «pending».
    for (var i = 0; !url && i < 10; i++) { Utilities.sleep(1500); url = _meetNativo_(id); }
    if (!url) {
      Logger.log('  AVISO: Google acepto la peticion pero aun no devuelve el enlace.');
      Logger.log('  Espera un minuto y vuelve a ejecutar (no duplica nada).');
    }
    return url;
  } catch (e) {
    Logger.log('  AVISO: no se pudo crear la sala de Meet: ' + e);
    return '';
  }
}

/** Escribe la URL en Ubicacion y descripcion, para que se vea sin abrir el chip. */
function _anotarMeet_(evento, url) {
  try {
    if (evento.getLocation() !== url) evento.setLocation(url);
    var d = evento.getDescription() || '';
    if (d.indexOf(url) < 0) {
      evento.setDescription((d ? d + '\\n' : '') + 'Meet de esta sesion: ' + url);
    }
  } catch (e) {
    Logger.log('  AVISO: no pude escribir el enlace en «' + evento.getTitle() + '»: ' + e);
  }
}
"""


PLANTILLA = """/**
 * {titulo}
 *
 * ARCHIVO GENERADO. No editarlo a mano: se regenera con
 *   python config/calendario/generar_apps_script_encuentros.py
 *
 * NO lleva datos personales: los encuentros son bloques de TU calendario, sin invitados y
 * sin envio de correos. Se sigue guardando en _privado/ por convencion del proyecto.
 *
 * Que hace:
{resumen}
 *   - Le da a **cada sesion su propio enlace de Meet** (N sesiones = N salas distintas).
 *     El enlace de cada sesion queda en Ubicacion y al final de la descripcion del evento.
 *   - Las sesiones autonomas por festivo tambien quedan en el calendario (deja la fecha de
 *     cierre a la vista), pero SIN Meet: no hay encuentro.
 *
 * Lo que NO hace: no invita a nadie y no manda ningun correo — ni de invitacion al crear, ni
 * de cancelacion al borrar. El enlace de cada sesion lo compartes tu con el grupo.
 *
 * INSTALACION Y PRUEBAS: `Manuales/01 - Alistar un curso …` en la raiz de Cursos.
 */

// ═══════════════════════════════════════════════ CONFIGURACION

/**
 * ID del calendario donde se crean los encuentros.
 *
 * Sale VACIO a proposito. Como obtenerlo: ejecuta `listarCalendarios()` (esta mas abajo) y
 * copia el ID que te interese; o en Google Calendar, en «Mis calendarios», pasa el mouse
 * sobre el calendario -> tres puntos -> «Configuracion y uso compartido» -> baja hasta
 * «Integrar calendario» -> copia «ID de calendario».
 *
 * Estos eventos son bloques de tu agenda, asi que lo normal es tu calendario principal, cuyo
 * ID es tu propio correo. Si prefieres un calendario aparte para clases, uno secundario se ve
 * como `abc123...@group.calendar.google.com`; ese es tambien el que hay que poner en el script
 * de grabaciones, para que los dos miren el mismo sitio.
 */
var CALENDAR_ID = '';

/** true = no crea ni modifica nada; solo dice que haria. Empieza SIEMPRE en true. */
var SIMULAR = true;
{extra_config}
var PERIODO = {periodo};
var TZ = {tz};

/**
 * Rango del periodo, union de las dos fuentes: los 4 cursos de `semestre_2026_2.json`
 * (24/08 - 22/11) y los 3 grupos de `introduccion_ingenieria_2026_2.json`, que llegan a
 * diciembre. Es el techo del periodo, no el rango de busqueda: `_fantasmas_` usa el
 * `inicio`/`fin` DE CADA CURSO, para que los cursos que cierran en noviembre no rastreen un
 * mes extra de tu calendario personal.
 */
var INICIO = {inicio};
var FIN = {fin};

/**
 * Minutos que se deja correr una funcion antes de cortar sola. Apps Script mata la ejecucion
 * a los 30 min en cuentas Workspace (y a los 6 en cuentas gratuitas): cortar antes y a
 * proposito deja un resumen legible en vez de un error a medias. Si tu cuenta es gratuita,
 * bajalo a 4.
 */
var MINUTOS_MAX = {minutos_max};

var CURSOS = [
{cursos}
];

// ═══════════════════════════════════════════════ QUE EJECUTAR
{funciones}{motor}"""


# ─────────────────────────────────────────────────────── funciones de entrada

def funciones_un_curso() -> str:
    """Las 4 funciones del .gs de un solo curso, con los nombres que documenta el manual."""
    return f"""
/** SOLO LECTURA: que pasaria. Ejecutalo primero. */
function verificar() {{
  _entorno_();
  _verificar_(CURSOS[0]);
}}

/** Crea los encuentros en TU calendario, cada uno con su propia sala de Meet. */
function crearEncuentros() {{
  _arrancarReloj_();
  var r = _crear_(CURSOS[0]);
  if (r.cortado) _avisoDeCorte_('crearEncuentros()');
  else if (!SIMULAR) {{
    Logger.log('');
    Logger.log('El enlace de cada sesion esta en el evento (Ubicacion y descripcion).');
    Logger.log('No se envio a nadie: comparte con el grupo el de la sesion que toca.');
  }}
}}

/** Borra los encuentros de la serie. No notifica a nadie; se van sus salas de Meet. */
function eliminarEncuentros() {{
  _eliminar_(CURSOS[0]);
}}

/** Borra y vuelve a crear, en una sola corrida. Los enlaces de Meet cambian. */
function recrearTodo() {{
  _arrancarReloj_();
  var r = _recrear_(CURSOS[0]);
  // Para continuar hay que llamar a crearEncuentros(), NO a recrearTodo(): esta ultima
  // volveria a borrar lo que acaba de recrear.
  if (r.cortado) _avisoDeCorte_('crearEncuentros()', 'recrearTodo()');
  else if (!SIMULAR) {{
    Logger.log('');
    Logger.log('Listo: ' + r.borrados + ' borrado(s) y ' + CURSOS[0].sesiones.length +
               ' sesion(es) recreada(s), cada una con una sala de Meet NUEVA.');
  }}
}}
"""


def funciones_semestre(cursos: list[tuple[str, dict]], n_ses: int, n_meet: int) -> str:
    """Las funciones del .gs consolidado: 4 por curso + 4 para todo el semestre.

    `n_ses` y `n_meet` entran como texto ya contado por main() para que la justificacion del
    segundo interruptor diga el numero real del periodo y no una cifra escrita a mano.
    """
    out = [f"""
/** SOLO LECTURA de todo el semestre. Ejecutalo primero, siempre. */
function verificarTodosLosCursos() {{
  _entorno_();
  var ses = 0, hay = 0;
  for (var i = 0; i < CURSOS.length; i++) {{
    var r = _verificar_(CURSOS[i]);
    ses += r.sesiones; hay += r.existen;
  }}
  Logger.log('');
  Logger.log('TOTAL ' + CURSOS.length + ' curso(s) · ' + ses + ' sesion(es) · ya creadas: ' + hay);
}}

/**
 * Crea los encuentros de LOS {len(cursos)} CURSOS del periodo. Reutiliza lo que ya exista, asi que es
 * seguro reejecutarla.
 *
 * Pide CONFIRMO_SEMESTRE_COMPLETO = true ademas de SIMULAR = false: son {n_ses} eventos y {n_meet}
 * salas de Meet de golpe (roza la cuota diaria de Calendar y tarda), y en el desplegable de
 * Apps Script es facil elegir esta en vez de la de un curso. La primera vez conviene ir curso
 * por curso.
 */
function crearTodosLosCursos() {{
  if (!_confirmado_('crearTodosLosCursos')) return;
  _arrancarReloj_();
  var creados = 0, reusados = 0, meet = 0, cortado = false;
  for (var i = 0; i < CURSOS.length; i++) {{
    if (_sinTiempo_()) {{ cortado = true; break; }}
    var r = _crear_(CURSOS[i]);
    creados += r.creados; reusados += r.reusados; meet += r.meet;
    if (r.cortado) {{ cortado = true; break; }}
  }}
  Logger.log('');
  Logger.log('TOTAL: ' + creados + ' evento(s) creado(s) · ' + reusados + ' reutilizado(s) · ' +
             meet + ' con sala de Meet.');
  if (cortado) _avisoDeCorte_('crearTodosLosCursos()');
}}

/**
 * Borra los encuentros de LOS {len(cursos)} CURSOS del periodo.
 *
 * No manda ningun correo (los eventos no tienen invitados), pero se lleva las {n_meet} salas de
 * Meet: los enlaces que ya hubieras compartido con los grupos dejan de servir.
 */
function eliminarTodosLosCursos() {{
  if (!_confirmado_('eliminarTodosLosCursos')) return;
  var n = 0;
  for (var i = 0; i < CURSOS.length; i++) n += _eliminar_(CURSOS[i]);
  Logger.log('');
  Logger.log('TOTAL eliminados: ' + n + ' evento(s) en ' + CURSOS.length + ' curso(s).');
}}

/** Borra y vuelve a crear LOS {len(cursos)} CURSOS. Es lo mas ruidoso que hace este script. */
function recrearTodosLosCursos() {{
  if (!_confirmado_('recrearTodosLosCursos')) return;
  _arrancarReloj_();
  var borrados = 0, creados = 0, cortado = false;
  for (var i = 0; i < CURSOS.length; i++) {{
    if (_sinTiempo_()) {{ cortado = true; break; }}
    var r = _recrear_(CURSOS[i]);
    borrados += r.borrados; creados += r.creados;
    if (r.cortado) {{ cortado = true; break; }}
  }}
  Logger.log('');
  Logger.log('TOTAL: ' + borrados + ' borrado(s) y ' + creados + ' creado(s).');
  // Continuar con crearTodosLosCursos(): reejecutar recrearTodosLosCursos() volveria a borrar
  // los cursos que ya habia recreado, y con ellos las salas de Meet que acaba de crear.
  if (cortado) _avisoDeCorte_('crearTodosLosCursos()', 'recrearTodosLosCursos()');
}}

/**
 * Rejilla de seguridad de las funciones de todo el semestre. En simulacion deja pasar
 * siempre (no toca nada); en real exige el segundo interruptor.
 */
function _confirmado_(quien) {{
  if (SIMULAR) return true;
  if (CONFIRMO_SEMESTRE_COMPLETO) return true;
  Logger.log('BLOQUEADO: ' + quien + ' toca los ' + CURSOS.length + ' cursos a la vez.');
  Logger.log('');
  Logger.log('Si es lo que quieres, pon arriba:');
  Logger.log('    var CONFIRMO_SEMESTRE_COMPLETO = true;');
  Logger.log('Si querias un solo curso, usa la funcion de ese curso en el desplegable.');
  return false;
}}
"""]

    for key, meta in cursos:
        n = nombre_js(key)
        out.append(f"""
// ── {meta['nombre']}  ({meta['codigo']} · grupo {meta['grupo']})

function verificar{n}() {{ _entorno_(); _verificar_(_curso_({js(key)})); }}

function crear{n}() {{
  _arrancarReloj_();
  var r = _crear_(_curso_({js(key)}));
  if (r.cortado) _avisoDeCorte_('crear{n}()');
}}

/** No notifica a nadie, pero se lleva las salas de Meet de este curso. */
function eliminar{n}() {{ _eliminar_(_curso_({js(key)})); }}

function recrear{n}() {{
  _arrancarReloj_();
  var r = _recrear_(_curso_({js(key)}));
  if (r.cortado) _avisoDeCorte_('crear{n}()', 'recrear{n}()');
}}
""")
    return "".join(out)


# ─────────────────────────────────────────────────────── punteros visibles

def _nombre_leeme(meta: dict) -> str:
    """Nombre del LEEME visible del curso.

    Los tres grupos de Introduccion a la Ingenieria comparten carpeta (`folder` es el mismo),
    asi que si todos escribieran `LEEME - Apps Script del curso.md` el ultimo se comeria a los
    otros dos. Solo en ese caso se le pega el grupo al nombre; los cursos con carpeta propia
    conservan el nombre de siempre para no dejar archivos huerfanos ya versionados.
    """
    if _codigo_compartido(meta["codigo"]):
        return f"LEEME - Apps Script del curso - {meta['grupo']}.md"
    return "LEEME - Apps Script del curso.md"


def _puntero_curso(meta: dict, gs: Path, n_ses: int, n_meet: int, consolidado: Path,
                   n_cursos: int) -> None:
    """LEEME VISIBLE al lado de la carpeta privada del curso.

    El .gs ya NO lleva datos personales (los eventos son bloques del calendario del docente,
    sin invitados), pero se sigue guardando en `_privado/` por convencion del proyecto: es
    donde el manual dice que esta y donde el docente ya lo busca. Este puntero SI se versiona
    y dice exactamente donde encontrarlo.
    """
    autonomas = n_ses - n_meet
    L = [
        f"# Apps Script del curso - {meta['nombre']} - {PERIODO}",
        "",
        "## Bloquear los encuentros en TU calendario (cada sesion con su propio Meet)",
        "",
        "El script **existe** y esta aqui:",
        "",
        "```",
        f"{gs.parent.name}/{gs.name}",
        "```",
        "",
        "Ruta completa desde la raiz de `Cursos`:",
        "",
        "```",
        gs.relative_to(ROOT).as_posix(),
        "```",
        "",
        "> **Por que no lo ves en GitHub:** los `.gs` de encuentros viven en `_privado/`, que",
        "> esta en `.gitignore`. Existe en tu disco y en Drive, no en el repositorio remoto.",
        "> Si no aparece, regeneralo:",
        ">",
        "> ```bash",
        "> python config/calendario/generar_apps_script_encuentros.py",
        "> ```",
        "",
        f"Crea **{n_ses} eventos** (uno por sesion) en **tu** calendario. **No invita a nadie y",
        "no manda ningun correo:** son bloques tuyos, para que la agenda quede reservada y cada",
        "sesion traiga su enlace a mano.",
        "",
        (f"{n_meet} eventos llevan **su propia sala de Meet**; "
         + (f"{autonomas} es una semana autonoma por festivo, que queda"
            if autonomas == 1 else
            f"{autonomas} son semanas autonomas por festivo, que quedan")
         + " en el calendario **sin Meet**."
         if autonomas else
         f"Los {n_meet} son sincronicos y cada uno lleva **su propia sala de Meet**."),
        "",
        "El enlace de cada sesion queda en **Ubicacion** y al final de la descripcion del",
        "evento: de ahi lo copias para compartirlo con el grupo por donde de verdad les",
        "escribes.",
        "",
        "Funciones: `verificar` · `crearEncuentros` · `eliminarEncuentros` · `recrearTodo`.",
        "",
        "**Paso a paso:** `Manuales/01 - Alistar un curso (encuentros, Meet, correo e",
        "invitaciones).md` en la raiz de `Cursos`. Incluye como sacar el `CALENDAR_ID` y por",
        "que se ejecuta `verificar` antes de `crearEncuentros`.",
        "",
        f"## Si prefieres un solo script para los {n_cursos} cursos",
        "",
        "Hay uno consolidado, con las funciones de creacion y borrado **de cada curso** mas",
        "las de todo el semestre. Sale de la misma plantilla que este, asi que hacen lo mismo:",
        "",
        "```",
        consolidado.relative_to(ROOT).as_posix(),
        "```",
        "",
        "Puntero visible: `LEEME - Apps Script del semestre.md` en la raiz de `Cursos`.",
        "",
        "## Archivar las grabaciones de Meet",
        "",
        "Ese script es **uno solo** y vive en",
        "`config/calendario/apps_script_grabaciones/MoverGrabaciones.gs`.",
        "Paso a paso: `Manuales/02 - Instalar y probar el Apps Script de grabaciones.md`.",
        "",
        "---",
        "",
        "*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*",
        "",
    ]
    (gs.parent.parent / _nombre_leeme(meta)).write_text("\n".join(L), encoding="utf-8")


def _choques(cursos: list[tuple[str, dict, int, int]]) -> list[tuple[str, str, str, str]]:
    """Cursos del docente que se pisan en el calendario: mismo dia y horas que se cruzan.

    Sustituye a la vieja deteccion de estudiantes matriculados en dos cursos: sin invitados,
    a nadie le llega nada por duplicado, pero el docente sigue siendo uno solo. Con 7 grupos
    en la misma semana, dos bloques a la misma hora significan que uno de los dos horarios
    esta mal transcrito en el JSON, y eso hay que verlo ANTES de meter 100 eventos.
    """
    def rango(meta: dict) -> tuple[int, int]:
        # ev.hhmm() devuelve 'HHMMSS' ('143000'), no 'HH:MM'.
        return tuple(int(x[:2]) * 60 + int(x[2:4]) for x in ev.hhmm(meta["horario"]))

    out = []
    for i in range(len(cursos)):
        for j in range(i + 1, len(cursos)):
            a, b = cursos[i][1], cursos[j][1]
            if a["dia"].strip().lower() != b["dia"].strip().lower():
                continue
            (ai, af), (bi, bf) = rango(a), rango(b)
            if ai < bf and bi < af:          # se cruzan de verdad, no solo se tocan
                out.append((a["nombre"], b["nombre"],
                            f"{a['dia']} {a['horario']}", f"{b['dia']} {b['horario']}"))
    return out


def _puntero_semestre(gs: Path, cursos: list[tuple[str, dict, int, int]],
                      choques: list[tuple[str, str, str, str]]) -> None:
    """LEEME visible en la raiz para el script consolidado."""
    n_ses = sum(s for _, _, s, _ in cursos)
    n_meet = sum(m for _, _, _, m in cursos)
    autonomas = n_ses - n_meet
    al = DATA_II.get("alerta_calendario") or {}
    L = [
        f"# Apps Script del semestre - {PERIODO}",
        "",
        "Un **solo** Apps Script con los cursos del periodo y, para cada uno, sus funciones",
        f"de creacion y de borrado. Sirve cuando no quieres pegar {len(cursos)} proyectos distintos.",
        "",
        "Los eventos son **bloques de tu calendario**: reservan tu agenda y guardan el enlace",
        "de Meet de cada sesion. **No llevan invitados y no mandan ningun correo**; el enlace",
        "se comparte a mano por donde de verdad le escribes al grupo.",
        "",
        "El script **existe** y esta aqui:",
        "",
        "```",
        gs.relative_to(ROOT).as_posix(),
        "```",
        "",
        "> **Por que no lo ves en GitHub:** los `.gs` de encuentros viven en `_privado/`, que",
        "> esta en `.gitignore`. Existe en tu disco y en Drive, no en el repositorio remoto.",
        "> Si no aparece, regeneralo:",
        ">",
        "> ```bash",
        "> python config/calendario/generar_apps_script_encuentros.py",
        "> ```",
        "",
        "## Que trae",
        "",
        f"`{len(cursos)}` cursos · `{n_ses}` sesiones · `{n_meet}` salas de Meet "
        f"(`{autonomas}` semanas autonomas por festivo van al calendario sin Meet).",
        "",
        "| Curso | Codigo | Grupo | Dia y hora | Sesiones | Meet |",
        "|---|---|---|---|---|---|",
    ]
    for _, meta, s, m in cursos:
        L.append(f"| {meta['nombre']} | `{meta['codigo']}` | `{meta['grupo']}` | "
                 f"{meta['dia']} {meta['horario']} | {s} | {m} |")
    L += [
        "",
        "## Choques en TU horario",
        "",
    ]
    if choques:
        L += [
            f"**Hay {len(choques)}.** Dos cursos caen el mismo dia a horas que se cruzan, asi que",
            "uno de los dos horarios esta mal en el JSON o de verdad no puedes dictar los dos:",
            "",
            "| Curso | Curso | Bloque | Bloque |",
            "|---|---|---|---|",
        ]
        L += [f"| {a} | {b} | {ha} | {hb} |" for a, b, ha, hb in choques]
        L += ["", "Arreglalo en el JSON antes de crear nada: el script no sabe cual es el bueno."]
    else:
        L += [
            f"**Ninguno.** Se compararon los {len(cursos)} cursos por pares (mismo dia + horas que",
            "se cruzan) y no hay dos bloques encima. Se revisa en cada regeneracion, porque con",
            f"{len(cursos)} grupos en la misma semana es facil que un horario nuevo se pise con otro.",
        ]
    if al:
        L += [
            "",
            f"## Aviso del calendario: {al.get('titulo', '')}",
            "",
            al.get("detalle", ""),
            "",
            f"**Plan B si el programa exige cerrar antes:** {al.get('plan_b', '')}",
            "",
            "> Mientras no se confirme, el script crea las fechas **tal como estan en el JSON**.",
            "> Ninguna fecha se movio para escribir este aviso.",
        ]
    L += [
        "",
        "## Funciones",
        "",
        "En el desplegable de Apps Script, **por curso**:",
        "",
        "| Funcion | Que hace |",
        "|---|---|",
    ]
    for key, meta, _, _ in cursos:
        n = nombre_js(key)
        L.append(f"| `verificar{n}` / `crear{n}` / `eliminar{n}` / `recrear{n}` "
                 f"| solo ese curso ({meta['nombre']}) |")
    L += [
        "",
        "Y **para todo el semestre**:",
        "",
        "| Funcion | Que hace |",
        "|---|---|",
        "| `verificarTodosLosCursos` | Solo lectura. Ejecutala primero, siempre. |",
        "| `crearTodosLosCursos` | Crea lo que falte en los "
        f"{len(cursos)} cursos. Reejecutable: reutiliza lo que ya existe. |",
        "| `eliminarTodosLosCursos` | Borra los "
        f"{n_ses} eventos. No notifica a nadie, pero se lleva las {n_meet} salas de Meet. |",
        "| `recrearTodosLosCursos` | Borra y vuelve a crear todo. Lo mas ruidoso: **todos** los "
        "enlaces de Meet cambian. |",
        "| `listarCalendarios` | Imprime los IDs de calendario, para llenar `CALENDAR_ID`. |",
        "",
        "## Antes que nada: la zona horaria del proyecto",
        "",
        "En Apps Script, **Configuracion del proyecto -> Zona horaria -> `America/Bogota`**.",
        "",
        "Las horas de los eventos las construye Apps Script con la zona del **proyecto**, no con",
        "la del calendario. Si el proyecto queda en otra (Google no siempre pone la local), los",
        f"{n_ses} eventos entran corridos y con ellos las {n_meet} salas de Meet. `verificar*`",
        "imprime la zona, y si no es la correcta **crear y borrar quedan bloqueados**.",
        "",
        "## Dos interruptores antes de que toque nada",
        "",
        "```js",
        "var SIMULAR = true;                        // no crea ni borra: solo dice que haria",
        "var CONFIRMO_SEMESTRE_COMPLETO = false;    // exigido por las funciones *TodosLosCursos*",
        "```",
        "",
        "`SIMULAR = true` es el modo de siempre: las funciones listan lo que harian, incluidos",
        "los eventos «huerfanos» (los de una corrida anterior con el titulo viejo) y los",
        "«fantasmas» (los que quedaron en una fecha que ya no esta en el calendario del curso).",
        "Para ejecutar de verdad se pone en `false`.",
        "",
        "El segundo interruptor lo piden **solo** las cuatro funciones `*TodosLosCursos`. Ya no",
        "hay correos que enviar, pero sigue teniendo sentido: de un golpe tocan "
        f"`{n_ses}` eventos y",
        f"crean o destruyen `{n_meet}` salas de Meet, roza la cuota diaria de Calendar, tarda lo",
        "suyo, y en el desplegable de Apps Script es facil elegir una de esas en vez de la de un",
        "curso. Deshacerlo a mano son "
        f"{n_ses} borrados. Las funciones por curso no lo necesitan.",
        "",
        "## Si se corta a la mitad",
        "",
        "Apps Script mata cualquier ejecucion a los 30 minutos (6 en cuentas gratuitas). El",
        "script se corta **solo** antes de eso (`MINUTOS_MAX`) y lo dice en el log. No se",
        "pierde nada: vuelve a ejecutar la misma funcion y retoma donde quedo, porque reutiliza",
        "los eventos y las salas de Meet que ya existen.",
        "",
        "## Lo mismo, pero por curso",
        "",
        "Si prefieres un proyecto por curso, cada uno tiene el suyo:",
        "",
        "```",
        f"<Curso>/Plan curso/{PERIODO}/_privado/CrearEncuentros - <Curso>.gs",
        "```",
        "",
        "Salen de la **misma plantilla** que este, asi que hacen exactamente lo mismo; solo",
        "cambian los nombres de las funciones (`verificar`, `crearEncuentros`,",
        "`eliminarEncuentros`, `recrearTodo`). Cada curso tiene su",
        "`LEEME - Apps Script del curso.md` visible en `Plan curso/" + PERIODO + "/`. Los grupos",
        "que comparten asignatura (y por tanto carpeta) llevan el grupo en el nombre:",
        "`LEEME - Apps Script del curso - <GRUPO>.md`.",
        "",
        "**Paso a paso:** `Manuales/01 - Alistar un curso (encuentros, Meet, correo e",
        "invitaciones).md`.",
        "",
        "## Si tocaste el generador",
        "",
        "Los `.gs` no se editan a mano. Y el generador tiene pruebas que ejecutan el `.gs` de",
        "verdad contra un simulacro de las APIs de Google:",
        "",
        "```bash",
        "bash config/calendario/pruebas_apps_script/probar.sh",
        "```",
        "",
        "Comprueban que reejecutar no duplica, que cada sesion tiene su sala, que el borrado no",
        "se lleva nada ajeno y que los dos interruptores frenan. Detalle:",
        "`config/calendario/pruebas_apps_script/LEEME.md`.",
        "",
        "---",
        "",
        "*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*",
        "",
    ]
    (ROOT / "LEEME - Apps Script del semestre.md").write_text("\n".join(L), encoding="utf-8")


# ─────────────────────────────────────────────────────── main

def _nombre_archivo(meta: dict) -> str:
    """Nombre del .gs por curso, con el grupo cuando la asignatura lo comparte.

    `nombre` de los grupos nuevos trae el separador ' · ', que en un nombre de archivo queda
    raro; se cambia por ' - '. Sin esto los 3 grupos de FI300101 escribirian el MISMO archivo
    en la MISMA carpeta y solo sobreviviria el ultimo.
    """
    return f"CrearEncuentros - {meta['nombre'].replace(' · ', ' - ')}.gs"


def main() -> None:
    # Dos fuentes de verdad, sin mezclarlas: semestre_2026_2.json (los 4 cursos de siempre) e
    # introduccion_ingenieria_2026_2.json (3 grupos de la misma asignatura). El adaptador
    # traduce los grupos al mismo contrato que ya consume el generador, asi que de aqui para
    # abajo un grupo es un curso mas.
    declarados = len(DATA["cursos"]) + len(DATA_II["grupos"])
    listos: list[tuple[str, dict, list[dict]]] = [
        (key, meta, sesiones_de(meta))
        for key, meta in list(DATA["cursos"].items()) + cursos_introduccion_ingenieria()
    ]
    # La nomina ya no hace falta aqui: los eventos no llevan invitados. Sigue haciendo falta
    # para la planilla de asistencia, que la genera generar_eventos_calendario.py.
    if len(listos) != declarados:
        raise SystemExit(f"Se armaron {len(listos)} cursos y los JSON declaran {declarados}.")

    consolidado = ROOT / "_privado" / PERIODO / f"CrearEncuentros - TODO EL SEMESTRE {PERIODO}.gs"

    # ── uno por curso ────────────────────────────────────────────────────────
    for key, meta, ses in listos:
        privado = ev.privado_de(meta)
        n_meet = sum(1 for s in ses if s["meet"])
        gs = PLANTILLA.format(
            titulo=f"{meta['nombre']} — encuentros del periodo {PERIODO} en Google Calendar.",
            resumen=(f" *   - Crea {len(ses)} eventos (uno por sesion) en TU calendario, "
                     f"{n_meet} con sala de Meet.\n"
                     f" *     Grupo {meta['grupo']}. Sin invitados: no se envia ningun correo."),
            extra_config="",
            periodo=js(PERIODO),
            tz=js(TZ),
            inicio=js(INICIO),
            fin=js(FIN),
            minutos_max=MINUTOS_MAX,
            cursos=bloque_curso(key, meta, ses),
            funciones=funciones_un_curso(),
            motor=MOTOR,
        )
        privado.mkdir(parents=True, exist_ok=True)
        destino = privado / _nombre_archivo(meta)
        destino.write_text(gs, encoding="utf-8")
        _puntero_curso(meta, destino, len(ses), n_meet, consolidado, len(listos))
        print(f"  {meta['nombre'][:38]:<38} {len(ses)} sesiones · {n_meet} con Meet")

    # ── consolidado ──────────────────────────────────────────────────────────
    n_ses = sum(len(s) for _, _, s in listos)
    n_meet = sum(1 for _, _, ses in listos for s in ses if s["meet"])
    gs = PLANTILLA.format(
        titulo=f"TODO EL SEMESTRE {PERIODO} — encuentros de los {len(listos)} cursos.",
        resumen=(f" *   - Crea {n_ses} eventos ({len(listos)} cursos x sus sesiones) en TU\n"
                 f" *     calendario, {n_meet} de ellos con su propia sala de Meet.\n"
                 " *   - Sin invitados y sin correos: son bloques de tu agenda.\n"
                 " *   - Trae funciones POR CURSO (crear/eliminar/recrear cada uno) y para\n"
                 " *     todo el semestre de una vez."),
        extra_config=f"""
/**
 * Segundo interruptor, exigido SOLO por las funciones *TodosLosCursos. No es por los correos
 * (los eventos no tienen invitados): es porque esas funciones tocan {n_ses} eventos y {n_meet} salas
 * de Meet de una sola vez, y en el desplegable de Apps Script es facil elegir una de esas en
 * vez de la de un curso.
 */
var CONFIRMO_SEMESTRE_COMPLETO = false;
""",
        periodo=js(PERIODO),
        tz=js(TZ),
        inicio=js(INICIO),
        fin=js(FIN),
        minutos_max=MINUTOS_MAX,
        cursos="\n".join(bloque_curso(k, m, s) for k, m, s in listos),
        funciones=funciones_semestre([(k, m) for k, m, _ in listos], n_ses, n_meet),
        motor=MOTOR,
    )
    consolidado.parent.mkdir(parents=True, exist_ok=True)
    consolidado.write_text(gs, encoding="utf-8")

    tabla = [(k, m, len(s), sum(1 for x in s if x["meet"])) for k, m, s in listos]
    choques = _choques(tabla)
    _puntero_semestre(consolidado, tabla, choques)
    if choques:
        for a, b, ha, hb in choques:
            print(f"  CHOQUE DE HORARIO: «{a}» ({ha}) se cruza con «{b}» ({hb}).")
            print("         Revisa el JSON: no puedes dictar los dos a la vez.")
    else:
        print(f"\n  Horario del docente: sin choques entre los {len(listos)} cursos "
              "(mismo día + horas cruzadas).")

    print(f"\n  CONSOLIDADO  {len(listos)} cursos · {n_ses} sesiones · {n_meet} con Meet "
          f"· {n_ses - n_meet} autónomas sin Meet")
    print(f"      {consolidado}")
    print(f"\nOK: {len(listos)}/{declarados} cursos.")
    print("Los eventos son bloques de TU calendario: sin invitados y sin envío de correos.")
    print("Los .gs se siguen guardando en _privado/ (está en .gitignore) por convención del")
    print("proyecto, aunque ya no lleven datos personales. Al lado, visibles, los LEEME:")
    print("  <Curso>/Plan curso/<periodo>/LEEME - Apps Script del curso.md")
    print("  (los grupos que comparten carpeta llevan el grupo en el nombre del LEEME)")
    print("  LEEME - Apps Script del semestre.md   (raíz de Cursos)")
    print("")
    print("Instalación y pruebas: Manuales/01. Cada sesión lleva SU propio enlace de Meet, que")
    print("queda en Ubicación y en la descripción del evento: de ahí lo copias para compartirlo")
    print("con el grupo. Las semanas autónomas por festivo van al calendario SIN Meet.")
    al = DATA_II.get("alerta_calendario") or {}
    if al:
        print("")
        print(f"AVISO ({DATA_II['curso']['codigo']}): {al.get('titulo', '')}")
        print("  Las fechas de diciembre pasan del cierre institucional 2026-11-22 y están")
        print("  PENDIENTES de confirmar con el programa. No se movió ninguna fecha.")
        print("  Detalle y plan B: LEEME - Apps Script del semestre.md")
    # La nómina no bloquea este generador, pero sí la planilla de asistencia del otro script.
    # Se avisa solo si de verdad no hay ningún listado, para que la nota no envejezca mintiendo.
    plan = ROOT / DATA_II["curso"]["folder"] / "Plan curso" / PERIODO
    if not any(plan.glob("*.xls*")) and not any(plan.glob("*.csv")):
        print("")
        print(f"Nota: en {plan.as_posix()} no hay ningún listado de")
        print(f"Academusoft, así que los {len(DATA_II['grupos'])} grupos de "
              f"{DATA_II['curso']['codigo']} no tienen planilla de asistencia todavía.")
        print("Eso no bloquea estos .gs (ya no necesitan nómina); la planilla la genera")
        print("generar_eventos_calendario.py cuando aparezca el listado.")


if __name__ == "__main__":
    # Sin esto, en la consola de Windows (cp1252) un print con tildes revienta o sale
    # ilegible, y aquí eso se come justo el AVISO de las fechas de diciembre que el docente
    # tiene que leer. Igual que en generar_eventos_calendario.py.
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
