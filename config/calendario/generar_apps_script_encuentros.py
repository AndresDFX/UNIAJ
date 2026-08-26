# -*- coding: utf-8 -*-
"""Genera los Apps Script que crean los encuentros del semestre en Google Calendar.

Qué resuelve
------------
Importar un `.ics` deja los invitados dentro del evento pero **Google no envía las
invitaciones**. Este camino sí las envía: crea los eventos con la API de Calendar y
`sendUpdates: 'all'`.

Y le pone a **cada sesión su propia sala de Meet**: N encuentros, N enlaces distintos.
El estudiante no tiene que guardar ningún enlace — entra por la invitación de Calendar de
esa sesión, que ya lo trae dentro.

Cada sala se pide con un `requestId` determinista y **distinto por sesión**
(`uniajc-<codigo>-<grupo>-<periodo>-sNN`). Eso es lo que hace la operación repetible: volver
a ejecutar no crea una segunda sala para la misma sesión, y el enlace de una sesión que ya
existe no cambia por reejecutar.

Salidas
-------
1. Uno por curso:
   `<Curso>/Plan curso/<periodo>/_privado/CrearEncuentros - <Curso>.gs`
2. Uno consolidado con los 4 cursos:
   `_privado/<periodo>/CrearEncuentros - TODO EL SEMESTRE <periodo>.gs`

Los dos salen de la **misma plantilla** (`PLANTILLA` + `MOTOR`), a propósito: mantener dos
copias del motor garantizaba que divergieran y que la desactualizada fuera la que alguien
acabara pegando en Apps Script.

Van en `_privado/` porque **llevan los correos de los estudiantes**. Está en `.gitignore`.

Uso
---
    python config/calendario/generar_apps_script_encuentros.py

Requiere la nómina de cada curso (la lee con el mismo lector que
`generar_eventos_calendario.py`). Un curso sin nómina se omite y queda avisado en su LEEME.
"""
from __future__ import annotations

import json
from pathlib import Path

import generar_eventos_calendario as ev

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads(Path(__file__).with_name("semestre_2026_2.json").read_text(encoding="utf-8"))
PERIODO = DATA["periodo"]
DOCENTE = DATA["docente"]["nombre_completo"]
INICIO = DATA["inicio"]
FIN = DATA["fin"]

TZ = "America/Bogota"

#: Minutos que se permite correr a las funciones de todo el semestre antes de cortar sola.
#: Apps Script mata la ejecución a los 30 min en cuentas Workspace (y a los 6 en cuentas
#: gratuitas). Cortar antes y a propósito deja un log legible en vez de un error; como todo
#: es idempotente, volver a ejecutar retoma donde quedó.
MINUTOS_MAX = 25

ROMANOS = {"i", "ii", "iii", "iv", "v"}


def js(s) -> str:
    """Literal JS de una cadena."""
    return "'" + str(s).replace("\\", "\\\\").replace("'", "\\'") + "'"


def nombre_js(key: str) -> str:
    """`bases_datos_ii` -> `BasesDatosII`, para nombrar las funciones por curso."""
    partes = []
    for p in key.split("_"):
        partes.append(p.upper() if p.lower() in ROMANOS else p.capitalize())
    return "".join(partes)


def sesiones_de(meta: dict) -> list[dict]:
    ini, fin = ev.hhmm(meta["horario"])          # '180000', '200000'
    out = []
    for cl in meta["clases"]:
        # Las autonomas SI van al calendario (el estudiante debe ver la fecha de cierre),
        # pero NO llevan Meet: no hay encuentro.
        out.append({
            "subject": ev.titulo(meta, cl),
            "fecha": cl["fecha"],
            "ini": f"{ini[:2]}:{ini[2:4]}",
            "fin": f"{fin[:2]}:{fin[2:4]}",
            "desc": ev.descripcion(meta, cl),
            "meet": cl["tipo"] != "autonoma",
        })
    return out


def bloque_curso(key: str, meta: dict, correos: list[str], ses: list[dict]) -> str:
    """El literal JS de un curso dentro del array CURSOS."""
    invitados = "\n".join(f"      {js(c)}," for c in correos)
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
    // Base del requestId. Cada sesion pide su sala con requestId + '-sNN': distinto por
    // sesion, y estable entre corridas para que reejecutar no cree una segunda sala.
    requestId: {js(f"uniajc-{meta['codigo']}-{meta['grupo']}-{PERIODO}")},
    invitados: [
{invitados}
    ],
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
 * avisar. Con los eventos ya creados e invitaciones enviadas, eso no se deshace facil.
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
 * eventos entran corridos y las invitaciones ya salieron: no se deshace reejecutando, porque
 * el evento existe y se reutiliza.
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
  Logger.log('Con otra zona los eventos entrarian a otra hora, y las invitaciones ya enviadas');
  Logger.log('no se arreglan reejecutando.');
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
 * recrear, con una cancelacion por invitado y por evento. Solo `crear*` reanuda de verdad.
 */
function _avisoDeCorte_(reanudarCon, noReejecutar) {
  Logger.log('');
  Logger.log('*** CORTADO a los ' + MINUTOS_MAX + ' min para no chocar con el limite de');
  Logger.log('*** Apps Script. NO se perdio nada.');
  if (noReejecutar) {
    Logger.log('*** OJO: NO vuelvas a ejecutar ' + noReejecutar + ' — volveria a BORRAR lo que');
    Logger.log('*** acaba de recrear, y a mandar otra cancelacion a cada invitado.');
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
  Logger.log('  Invitados        : ' + c.invitados.length);
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
  Logger.log('Enviar correos   : ' + (SEND_INVITES ? 'si' : 'no'));
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
    Logger.log('Sin el los eventos se crean con invitados, pero SIN Meet.');
  }
}

// ═══════════════════════════════════════════════ MOTOR: CREAR

/** Crea los encuentros del curso, cada uno con SU sala de Meet, e invita al grupo. */
function _crear_(c) {
  var cal = _cal_();
  _titulo_(c);
  if (!SIMULAR && _zonaMal_('crear ' + c.nombre)) {
    return { creados: 0, reusados: 0, invitados: 0, meet: 0, cortado: false };
  }
  if (SIMULAR) {
    Logger.log('  SIMULAR = true: no se creo nada. Ponlo en false cuando verificar() se vea bien.');
    return { creados: 0, reusados: 0, invitados: 0, meet: 0, cortado: false };
  }

  var eventos = [], creados = 0, reusados = 0, invAgregados = 0, omitidos = 0, cortado = false;
  for (var i = 0; i < c.sesiones.length; i++) {
    if (_sinTiempo_()) { cortado = true; break; }
    var s = c.sesiones[i];
    var ya = _buscarEvento_(cal, s);
    if (ya) {
      // El evento ya existe. Hay que SINCRONIZAR los invitados: si llego una nomina nueva,
      // un estudiante que entro tarde no recibiria invitacion nunca (los invitados solo se
      // pasan al crear el evento).
      invAgregados += _sincronizarInvitados_(c, ya);
      eventos.push({ ev: ya, i: i }); reusados++; continue;
    }
    // Antes de crear: mirar si ya hay un encuentro de este curso ese dia a esa hora con OTRO
    // titulo. Pasa siempre que el titulo cambia en el JSON (se marca un parcial, una sesion
    // pasa a autonoma, cambian los prefijos). Sin esto se creaba una serie entera al lado de
    // la vieja, con dos invitaciones y dos salas para el mismo dia.
    var gemelos = _delCursoEsaHora_(cal, c, s, s.subject);
    if (gemelos.length) {
      Logger.log('  AVISO: ' + s.fecha + ' ' + s.ini + ' ya tiene un encuentro de este curso');
      Logger.log('         con OTRO titulo: «' + gemelos[0].getTitle() + '»');
      Logger.log('         NO creo «' + s.subject + '» para no dejar dos.');
      Logger.log('         El titulo cambio en el JSON: usa eliminar/recrear para rehacer.');
      omitidos++;
      continue;
    }
    var nuevo = cal.createEvent(s.subject, _fecha(s.fecha, s.ini), _fecha(s.fecha, s.fin), {
      description: s.desc,
      guests: c.invitados.join(','),
      sendInvites: SEND_INVITES
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
  if (invAgregados) {
    Logger.log('  Invitados agregados a eventos que ya existian: ' + invAgregados +
               ' (nomina nueva).');
  }

  if (!_apiCalendar_()) {
    Logger.log('  Sin enlace de Meet: el servicio avanzado de Calendar no esta activo.');
    Logger.log('  Activalo y vuelve a ejecutar: no duplica eventos ni salas.');
    return { creados: creados, reusados: reusados, invitados: invAgregados, meet: 0,
             cortado: cortado };
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
  return { creados: creados, reusados: reusados, invitados: invAgregados, meet: nativos,
           cortado: cortado };
}

/**
 * Agrega al evento los invitados del curso que todavia no esten. Devuelve cuantos agrego.
 * Necesario porque `createEvent` solo pone invitados al crear: sin esto, una nomina nueva no
 * llegaria nunca a los eventos ya creados.
 */
function _sincronizarInvitados_(c, evento) {
  var actuales = {};
  var lista = evento.getGuestList();
  for (var i = 0; i < lista.length; i++) {
    actuales[String(lista[i].getEmail()).toLowerCase()] = true;
  }
  var n = 0;
  for (var j = 0; j < c.invitados.length; j++) {
    if (!actuales[String(c.invitados[j]).toLowerCase()]) {
      try { evento.addGuest(c.invitados[j]); n++; }
      catch (e) { Logger.log('  AVISO: no pude invitar a un estudiante: ' + e); }
    }
  }
  return n;
}

// ═══════════════════════════════════════════════ MOTOR: ELIMINAR

/**
 * Borra los encuentros de un curso. Dos pasadas:
 *   1. Por titulo exacto de cada sesion (lo que este script creo).
 *   2. Barrido de la MISMA fecha Y HORA de cada sesion, para cazar eventos de una corrida
 *      ANTERIOR cuyo titulo ya no coincide (paso al cambiar los prefijos o la modalidad).
 *      Solo borra si empieza a la hora de la sesion Y el titulo menciona el curso o su
 *      codigo: no toca eventos ajenos, ni los de otro curso que caiga el mismo dia, ni los
 *      apuntes personales del docente que mencionen el curso a otra hora.
 *
 * OJO: borrar un evento con invitados le manda a cada estudiante un correo de cancelacion.
 * Si lo unico que cambio es la nomina, NO hace falta borrar: crear() ya sincroniza los
 * invitados de los eventos que existen.
 *
 * Al borrar un evento se va TAMBIEN su sala de Meet. Si despues recreas, esa sesion queda
 * con un enlace NUEVO — y ese es justo el que le llega al estudiante en la invitacion, asi
 * que no hay nada que republicar en el material.
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

  // Fantasmas: encuentros de este curso dentro del periodo que NO caen en ninguna fecha del
  // .gs actual. Aparecen cuando una sesion se movio o se quito del JSON (este semestre paso de
  // 15 a 13 sesiones): las dos pasadas de arriba solo miran las fechas que el .gs conoce, asi
  // que sin esto quedaban en el calendario de los estudiantes y ninguna funcion los encontraba.
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

/** true si el titulo es de ESTE curso (nombre o codigo), para no borrar eventos ajenos. */
function _esDeEsteCurso_(c, titulo) {
  var t = String(titulo || '').toLowerCase();
  return t.indexOf(String(c.nombre).toLowerCase()) !== -1 ||
         t.indexOf(String(c.codigo).toLowerCase()) !== -1;
}

/**
 * Encuentros de este curso dentro del periodo que no estan ya contados. Exige la HORA del
 * curso, no solo el nombre: asi un «Calificar Bases de Datos II» de un martes cualquiera no
 * entra, pero si el evento de una sesion que se movio de fecha.
 */
function _fantasmas_(cal, c, exactos, huerfanos) {
  var out = [];
  var horas = {};
  for (var i = 0; i < c.sesiones.length; i++) horas[c.sesiones[i].ini] = true;
  var todos = cal.getEvents(_fecha(INICIO, '00:01'), _fecha(FIN, '23:59'));
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
 * Borra TODO lo del curso y lo vuelve a crear, en una sola corrida. Es lo que se usa cuando
 * cambio la nomina de forma grande o se movieron fechas y se prefiere partir de cero.
 *
 * Manda cancelaciones y luego invitaciones nuevas a cada estudiante, y los enlaces de Meet
 * cambian (cada evento nuevo trae su propia sala). Si solo entraron o salieron algunas
 * personas, crear() sola es menos ruidosa: sincroniza invitados sin tocar los eventos.
 */
function _recrear_(c) {
  if (SIMULAR) {
    _eliminar_(c);
    Logger.log('  ...y despues se crearian ' + c.sesiones.length + ' evento(s) con ' +
               c.invitados.length + ' invitado(s), cada uno con una sala de Meet NUEVA.');
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
 * crearia un duplicado, invitando dos veces a todo el grupo. Enumerar el dia y comparar el
 * titulo exacto no depende del indice de Google y en un dia hay un punado de eventos.
 */
function _buscarEvento_(cal, s) {
  var delDia = cal.getEvents(_fecha(s.fecha, '00:01'), _fecha(s.fecha, '23:59'));
  var iguales = [];
  for (var i = 0; i < delDia.length; i++) {
    if (delDia[i].getTitle() === s.subject) iguales.push(delDia[i]);
  }
  if (iguales.length > 1) {
    // Devolver el primero y callar dejaba al resto invisible para todas las funciones.
    Logger.log('  AVISO: ' + iguales.length + ' eventos con el mismo titulo el ' + s.fecha +
               ' («' + s.subject + '»). Borra los sobrantes a mano o usa recrear.');
  }
  return iguales.length ? iguales[0] : null;
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
      sendUpdates: SEND_INVITES ? 'all' : 'none'
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
 * CONTIENE CORREOS DE ESTUDIANTES. Vive en _privado/ y no se versiona.
 *
 * Que hace:
{resumen}
 *   - Le da a **cada sesion su propio enlace de Meet** (N sesiones = N salas distintas).
 *     El estudiante entra por la invitacion de Calendar de esa sesion, que lo trae dentro.
 *   - Las sesiones autonomas por festivo tambien quedan en el calendario (el estudiante
 *     debe ver la fecha de cierre), pero SIN Meet: no hay encuentro.
 *   - Invita a los estudiantes y, si SEND_INVITES = true, **les envia** el correo de
 *     invitacion (esto es lo que la importacion de un .ics no hace).
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
 * El principal tiene el ID de tu correo; uno secundario se ve como
 * `abc123...@group.calendar.google.com`. Si usas un calendario aparte para clases, ese es el
 * que va aqui — y es tambien el que hay que poner en el script de grabaciones, para que los
 * dos miren el mismo sitio.
 */
var CALENDAR_ID = '';

/** true = no crea ni modifica nada; solo dice que haria. Empieza SIEMPRE en true. */
var SIMULAR = true;

/** true = envia los correos de invitacion al crear/actualizar. */
var SEND_INVITES = true;
{extra_config}
var PERIODO = {periodo};
var TZ = {tz};

/** Rango del periodo. `_fantasmas_` lo usa para encontrar encuentros en fechas que ya no
 *  estan en el calendario del curso (una sesion que se movio o se quito del JSON). */
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

def funciones_un_curso(nombre_curso: str) -> str:
    """Las 4 funciones del .gs de un solo curso, con los nombres que documenta el manual."""
    return f"""
/** SOLO LECTURA: que pasaria. Ejecutalo primero. */
function verificar() {{
  _entorno_();
  _verificar_(CURSOS[0]);
}}

/** Crea los encuentros, cada uno con su propia sala de Meet, e invita al grupo. */
function crearEncuentros() {{
  _arrancarReloj_();
  var r = _crear_(CURSOS[0]);
  if (r.cortado) _avisoDeCorte_('crearEncuentros()');
  else if (!SIMULAR) {{
    Logger.log('');
    Logger.log('No hay enlace que pegar en el material: a cada estudiante le llega el de');
    Logger.log('cada sesion dentro de su invitacion de Calendar.');
  }}
}}

/** Borra los encuentros de la serie. OJO: manda un correo de cancelacion a cada invitado. */
function eliminarEncuentros() {{
  _eliminar_(CURSOS[0]);
}}

/** Borra y vuelve a crear, en una sola corrida. */
function recrearTodo() {{
  _arrancarReloj_();
  var r = _recrear_(CURSOS[0]);
  // Para continuar hay que llamar a crearEncuentros(), NO a recrearTodo(): esta ultima
  // volveria a borrar lo que acaba de recrear.
  if (r.cortado) _avisoDeCorte_('crearEncuentros()', 'recrearTodo()');
  else if (!SIMULAR) {{
    Logger.log('');
    Logger.log('Listo: ' + r.borrados + ' borrado(s) y la serie recreada con ' +
               CURSOS[0].invitados.length + ' invitado(s).');
  }}
}}
"""


def funciones_semestre(cursos: list[tuple[str, dict]]) -> str:
    """Las funciones del .gs consolidado: 4 por curso + 4 para todo el semestre."""
    out = ["""
/** SOLO LECTURA de todo el semestre. Ejecutalo primero, siempre. */
function verificarTodosLosCursos() {
  _entorno_();
  var ses = 0, hay = 0;
  for (var i = 0; i < CURSOS.length; i++) {
    var r = _verificar_(CURSOS[i]);
    ses += r.sesiones; hay += r.existen;
  }
  Logger.log('');
  Logger.log('TOTAL ' + CURSOS.length + ' curso(s) · ' + ses + ' sesion(es) · ya creadas: ' + hay);
}

/**
 * Crea los encuentros de LOS CUATRO CURSOS. Reutiliza lo que ya exista y sincroniza los
 * invitados, asi que es seguro reejecutarla.
 *
 * Pide CONFIRMO_SEMESTRE_COMPLETO = true ademas de SIMULAR = false: son ~52 eventos y mas de
 * mil invitaciones, y en el desplegable de Apps Script es facil elegir esta en vez de la de
 * un curso.
 */
function crearTodosLosCursos() {
  if (!_confirmado_('crearTodosLosCursos')) return;
  _arrancarReloj_();
  var creados = 0, reusados = 0, meet = 0, inv = 0, cortado = false;
  for (var i = 0; i < CURSOS.length; i++) {
    if (_sinTiempo_()) { cortado = true; break; }
    var r = _crear_(CURSOS[i]);
    creados += r.creados; reusados += r.reusados; meet += r.meet; inv += r.invitados;
    if (r.cortado) { cortado = true; break; }
  }
  Logger.log('');
  Logger.log('TOTAL: ' + creados + ' evento(s) creado(s) · ' + reusados + ' reutilizado(s) · ' +
             meet + ' con sala de Meet · ' + inv + ' invitado(s) agregado(s).');
  if (cortado) _avisoDeCorte_('crearTodosLosCursos()');
}

/**
 * Borra los encuentros de LOS CUATRO CURSOS.
 *
 * OJO: cada evento con invitados manda un correo de cancelacion a cada estudiante. Son ~52
 * eventos y mas de mil correos. Si lo unico que cambio es la nomina, NO uses esto:
 * crearTodosLosCursos() sincroniza los invitados sin borrar nada.
 */
function eliminarTodosLosCursos() {
  if (!_confirmado_('eliminarTodosLosCursos')) return;
  var n = 0;
  for (var i = 0; i < CURSOS.length; i++) n += _eliminar_(CURSOS[i]);
  Logger.log('');
  Logger.log('TOTAL eliminados: ' + n + ' evento(s) en ' + CURSOS.length + ' curso(s).');
}

/** Borra y vuelve a crear LOS CUATRO CURSOS. Es lo mas ruidoso que hace este script. */
function recrearTodosLosCursos() {
  if (!_confirmado_('recrearTodosLosCursos')) return;
  _arrancarReloj_();
  var borrados = 0, creados = 0, cortado = false;
  for (var i = 0; i < CURSOS.length; i++) {
    if (_sinTiempo_()) { cortado = true; break; }
    var r = _recrear_(CURSOS[i]);
    borrados += r.borrados; creados += r.creados;
    if (r.cortado) { cortado = true; break; }
  }
  Logger.log('');
  Logger.log('TOTAL: ' + borrados + ' borrado(s) y ' + creados + ' creado(s).');
  // Continuar con crearTodosLosCursos(): reejecutar recrearTodosLosCursos() volveria a borrar
  // los cursos que ya habia recreado, con una cancelacion por invitado y por evento.
  if (cortado) _avisoDeCorte_('crearTodosLosCursos()', 'recrearTodosLosCursos()');
}

/**
 * Rejilla de seguridad de las funciones de todo el semestre. En simulacion deja pasar
 * siempre (no toca nada); en real exige el segundo interruptor.
 */
function _confirmado_(quien) {
  if (SIMULAR) return true;
  if (CONFIRMO_SEMESTRE_COMPLETO) return true;
  Logger.log('BLOQUEADO: ' + quien + ' toca los ' + CURSOS.length + ' cursos a la vez.');
  Logger.log('');
  Logger.log('Si es lo que quieres, pon arriba:');
  Logger.log('    var CONFIRMO_SEMESTRE_COMPLETO = true;');
  Logger.log('Si querias un solo curso, usa la funcion de ese curso en el desplegable.');
  return false;
}
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

/** OJO: manda un correo de cancelacion a cada invitado de este curso. */
function eliminar{n}() {{ _eliminar_(_curso_({js(key)})); }}

function recrear{n}() {{
  _arrancarReloj_();
  var r = _recrear_(_curso_({js(key)}));
  if (r.cortado) _avisoDeCorte_('crear{n}()', 'recrear{n}()');
}}
""")
    return "".join(out)


# ─────────────────────────────────────────────────────── punteros visibles

def _puntero_curso(meta: dict, gs: Path, n_ses: int, n_inv: int, consolidado: Path) -> None:
    """LEEME VISIBLE al lado de la carpeta privada del curso.

    El .gs lleva los correos de los estudiantes, asi que vive en `_privado/` y no se
    versiona: no aparece en GitHub, y en Drive una carpeta con guion bajo se pasa por alto.
    Este puntero SI se versiona (no tiene datos personales) y dice exactamente donde esta.
    """
    L = [
        f"# Apps Script del curso - {meta['nombre']} - {PERIODO}",
        "",
        "## Crear los encuentros en Calendar (cada sesion con su propio Meet)",
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
        f"> **Por que no lo ves en GitHub:** el `.gs` incluye los correos de los {n_inv}",
        "> estudiantes del grupo, asi que la carpeta `_privado/` esta en `.gitignore`.",
        "> Existe en tu disco y en Drive, no en el repositorio remoto. Si no aparece,",
        "> regeneralo:",
        ">",
        "> ```bash",
        "> python config/calendario/generar_apps_script_encuentros.py",
        "> ```",
        "",
        f"Crea **{n_ses} eventos** (uno por sesion) e invita a los **{n_inv} estudiantes**,",
        "enviandoles la invitacion de verdad. Cada sesion sincronica lleva **su propia sala",
        "de Meet**; las autonomas por festivo quedan en el calendario pero sin Meet.",
        "",
        "Funciones: `verificar` · `crearEncuentros` · `eliminarEncuentros` · `recrearTodo`.",
        "",
        "**Paso a paso:** `Manuales/01 - Alistar un curso (encuentros, Meet, correo e",
        "invitaciones).md` en la raiz de `Cursos`. Incluye como sacar el `CALENDAR_ID` y por",
        "que se ejecuta `verificar` antes de `crearEncuentros`.",
        "",
        "## Si prefieres un solo script para los 4 cursos",
        "",
        "Hay uno consolidado, con las funciones de creacion y borrado **de cada curso** mas",
        f"las de todo el semestre. Sale de la misma plantilla que este, asi que hacen lo mismo:",
        "",
        "```",
        consolidado.relative_to(ROOT).as_posix(),
        "```",
        "",
        "Puntero visible: `LEEME - Apps Script del semestre.md` en la raiz de `Cursos`.",
        "",
        "## Archivar las grabaciones de Meet",
        "",
        "Ese script es **uno solo para los 4 cursos** y vive en",
        "`config/calendario/apps_script_grabaciones/MoverGrabaciones.gs`.",
        "Paso a paso: `Manuales/02 - Instalar y probar el Apps Script de grabaciones.md`.",
        "",
        "---",
        "",
        "*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*",
        "",
    ]
    (gs.parent.parent / "LEEME - Apps Script del curso.md").write_text(
        "\n".join(L), encoding="utf-8")


def _avisar_sin_nomina(meta: dict, privado: Path) -> None:
    """Marca el LEEME del curso cuando NO se pudo generar el .gs.

    Importa porque el .gs de una corrida anterior sigue en disco con la nómina vieja: sin
    este aviso, se pega en Apps Script un archivo desactualizado sin que nada lo delate.
    """
    gs = privado / f"CrearEncuentros - {meta['nombre']}.gs"
    L = [
        f"# Apps Script del curso - {meta['nombre']} - {PERIODO}",
        "",
        "## ATENCION: este curso NO tiene Apps Script al dia",
        "",
        "La ultima regeneracion **no encontro la nomina** del grupo "
        f"`{meta['codigo']}` / `{meta['grupo']}`, asi que no se pudo generar el `.gs`.",
        "",
    ]
    if gs.exists():
        L += [
            "> **Hay un `.gs` viejo en `_privado/`. NO lo uses:** trae la nomina de la",
            "> corrida anterior, asi que invitaria a los estudiantes equivocados.",
            "",
        ]
    L += [
        "Este curso tampoco entra en el script consolidado del semestre.",
        "",
        "### Como arreglarlo",
        "",
        "1. Exporta de Academusoft la **Lista de Alumnos por Grupo** de "
        f"`{meta['codigo']}` (grupo `{meta['grupo']}`).",
        f"2. Dejala en `{meta['folder']}/Plan curso/{PERIODO}/`.",
        "3. Vuelve a correr, desde la raiz de `Cursos`:",
        "",
        "```",
        "python config/calendario/generar_eventos_calendario.py",
        "python config/calendario/generar_apps_script_encuentros.py",
        "```",
        "",
        "Si el listado que dejaste es de OTRA asignatura, el generador lo dice y lo omite:",
        "compara el codigo `FI######` del archivo con el del curso.",
        "",
        "---",
        "",
        "*Archivo generado por `config/calendario/generar_apps_script_encuentros.py`.*",
        "",
    ]
    (privado.parent / "LEEME - Apps Script del curso.md").write_text(
        "\n".join(L), encoding="utf-8")


def _solapes(listos: list[tuple[str, dict, list[str], list[dict]]]) -> list[tuple[str, str, int]]:
    """Pares de cursos que comparten estudiantes, con cuantos.

    No es un detalle: quien esta en dos cursos recibe el doble de invitaciones y el doble de
    cancelaciones cada vez que se hace algo «para los 4 cursos».
    """
    out = []
    for i in range(len(listos)):
        for j in range(i + 1, len(listos)):
            a = {c.lower() for c in listos[i][2]}
            b = {c.lower() for c in listos[j][2]}
            comunes = len(a & b)
            if comunes:
                out.append((listos[i][1]["nombre"], listos[j][1]["nombre"], comunes))
    return sorted(out, key=lambda x: -x[2])


def _puntero_semestre(gs: Path, cursos: list[tuple[str, dict, int, int]],
                      faltan: list[dict],
                      solapes: list[tuple[str, str, int]], personas: int) -> None:
    """LEEME visible en la raiz para el script consolidado."""
    n_ses = sum(s for _, _, s, _ in cursos)
    n_inv = sum(i for _, _, _, i in cursos)
    L = [
        f"# Apps Script del semestre - {PERIODO}",
        "",
        "Un **solo** Apps Script con los cursos del periodo y, para cada uno, sus funciones",
        "de creacion y de borrado. Sirve cuando no quieres pegar cuatro proyectos distintos.",
        "",
        "El script **existe** y esta aqui:",
        "",
        "```",
        gs.relative_to(ROOT).as_posix(),
        "```",
        "",
        f"> **Por que no lo ves en GitHub:** lleva los correos de los {personas} estudiantes",
        f"> matriculados en los {len(cursos)} cursos, asi que `_privado/` esta en `.gitignore`.",
        "> Existe en tu disco y en Drive, no en el repositorio remoto. Si no aparece,",
        "> regeneralo:",
        ">",
        "> ```bash",
        "> python config/calendario/generar_apps_script_encuentros.py",
        "> ```",
        "",
        "## Que trae",
        "",
        f"`{len(cursos)}` cursos · `{n_ses}` sesiones · `{n_inv}` matriculas "
        f"(`{personas}` personas distintas).",
        "",
        "| Curso | Codigo | Grupo | Dia y hora | Sesiones | Invitados |",
        "|---|---|---|---|---|---|",
    ]
    for _, meta, s, i in cursos:
        L.append(f"| {meta['nombre']} | `{meta['codigo']}` | `{meta['grupo']}` | "
                 f"{meta['dia']} {meta['horario']} | {s} | {i} |")
    if faltan:
        L += ["", "> **Fuera del script:** " +
              ", ".join(f"{m['nombre']} (`{m['codigo']}`)" for m in faltan) +
              " — sin nomina en `Plan curso/" + PERIODO + "/`. Ver el "
              "`LEEME - Apps Script del curso.md` de ese curso."]
    if solapes:
        L += [
            "",
            "## Ojo: hay estudiantes en mas de un curso",
            "",
            f"Las {n_inv} matriculas son **{personas} personas**: hay quien esta en dos cursos.",
            "",
            "| Cursos | Estudiantes en comun |",
            "|---|---|",
        ]
        L += [f"| {a} + {b} | **{n}** |" for a, b, n in solapes]
        L += [
            "",
            "A esas personas, **cada operacion «de los 4 cursos» les llega por duplicado**: dos",
            "invitaciones por semana, y dos cancelaciones si se borra todo. Cuando solo hay que",
            "arreglar un curso, usa la funcion de ese curso.",
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
        f"{len(cursos)} cursos y sincroniza invitados. Reejecutable. |",
        "| `eliminarTodosLosCursos` | Borra los "
        f"{n_ses} eventos. **Manda ~{n_ses * n_inv // max(len(cursos), 1)} cancelaciones.** |",
        "| `recrearTodosLosCursos` | Borra y vuelve a crear todo. Lo mas ruidoso. |",
        "| `listarCalendarios` | Imprime los IDs de calendario, para llenar `CALENDAR_ID`. |",
        "",
        "## Antes que nada: la zona horaria del proyecto",
        "",
        "En Apps Script, **Configuracion del proyecto -> Zona horaria -> `America/Bogota`**.",
        "",
        "Las horas de los eventos las construye Apps Script con la zona del **proyecto**, no con",
        "la del calendario. Si el proyecto queda en otra (Google no siempre pone la local), los",
        f"{n_ses} eventos entran corridos y las invitaciones ya salieron. `verificar*` imprime la",
        "zona, y si no es la correcta **crear y borrar quedan bloqueados**.",
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
        "El segundo interruptor lo piden **solo** las cuatro funciones `*TodosLosCursos`, "
        f"porque tocan `{n_ses}` eventos y mas de mil correos de golpe, y en el desplegable es",
        "facil elegir esa en vez de la de un curso. Las funciones por curso no lo necesitan.",
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
        "`LEEME - Apps Script del curso.md` visible en `Plan curso/" + PERIODO + "/`.",
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

def main() -> None:
    listos: list[tuple[str, dict, list[str], list[dict]]] = []
    faltan: list[dict] = []

    for key, meta in DATA["cursos"].items():
        privado = ev.privado_de(meta)
        info = ev.cargar_nomina(meta, key, ev.cargar_correos_manuales(meta))
        if not info:
            print(f"  {meta['nombre']}: sin nómina -> no se genera el .gs")
            _avisar_sin_nomina(meta, privado)
            faltan.append(meta)
            continue
        correos = sorted({e["correo"] for e in info["estudiantes"] if e["correo"]})
        listos.append((key, meta, correos, sesiones_de(meta)))

    if not listos:
        raise SystemExit("Ningún curso tiene nómina: no hay nada que generar.")

    consolidado = ROOT / "_privado" / PERIODO / f"CrearEncuentros - TODO EL SEMESTRE {PERIODO}.gs"

    # ── uno por curso ────────────────────────────────────────────────────────
    for key, meta, correos, ses in listos:
        privado = ev.privado_de(meta)
        gs = PLANTILLA.format(
            titulo=f"{meta['nombre']} — encuentros del periodo {PERIODO} en Google Calendar.",
            resumen=(f" *   - Crea {len(ses)} eventos, uno por sesion, e invita a los "
                     f"{len(correos)} estudiantes\n *     del grupo {meta['grupo']}."),
            extra_config="",
            periodo=js(PERIODO),
            tz=js(TZ),
            inicio=js(INICIO),
            fin=js(FIN),
            minutos_max=MINUTOS_MAX,
            cursos=bloque_curso(key, meta, correos, ses),
            funciones=funciones_un_curso(meta["nombre"]),
            motor=MOTOR,
        )
        privado.mkdir(parents=True, exist_ok=True)
        destino = privado / f"CrearEncuentros - {meta['nombre']}.gs"
        destino.write_text(gs, encoding="utf-8")
        _puntero_curso(meta, destino, len(ses), len(correos), consolidado)
        print(f"  {meta['nombre'][:34]:<34} {len(ses)} sesiones · {len(correos)} invitados")

    # ── consolidado ──────────────────────────────────────────────────────────
    n_ses = sum(len(s) for _, _, _, s in listos)
    n_inv = sum(len(c) for _, _, c, _ in listos)
    gs = PLANTILLA.format(
        titulo=f"TODO EL SEMESTRE {PERIODO} — encuentros de los {len(listos)} cursos.",
        resumen=(f" *   - Crea {n_ses} eventos ({len(listos)} cursos x sus sesiones) e invita\n"
                 f" *     a {n_inv} estudiantes en total.\n"
                 " *   - Trae funciones POR CURSO (crear/eliminar/recrear cada uno) y para\n"
                 " *     todo el semestre de una vez."),
        extra_config="""
/**
 * Segundo interruptor, exigido SOLO por las funciones *TodosLosCursos. Esas tocan todos los
 * cursos de golpe (decenas de eventos, mas de mil correos) y en el desplegable de Apps
 * Script es facil elegir una de esas en vez de la de un curso.
 */
var CONFIRMO_SEMESTRE_COMPLETO = false;
""",
        periodo=js(PERIODO),
        tz=js(TZ),
        inicio=js(INICIO),
        fin=js(FIN),
        minutos_max=MINUTOS_MAX,
        cursos="\n".join(bloque_curso(k, m, c, s) for k, m, c, s in listos),
        funciones=funciones_semestre([(k, m) for k, m, _, _ in listos]),
        motor=MOTOR,
    )
    consolidado.parent.mkdir(parents=True, exist_ok=True)
    consolidado.write_text(gs, encoding="utf-8")
    solapes = _solapes(listos)
    personas = len({c.lower() for _, _, correos, _ in listos for c in correos})
    _puntero_semestre(consolidado,
                      [(k, m, len(s), len(c)) for k, m, c, s in listos], faltan,
                      solapes, personas)
    for a, b, n in solapes:
        print(f"  AVISO: {n} estudiante(s) estan en «{a}» y «{b}» a la vez:")
        print(f"         una operacion de todo el semestre les llega por duplicado.")

    print(f"\n  CONSOLIDADO  {len(listos)} cursos · {n_ses} sesiones · {n_inv} invitados")
    print(f"      {consolidado}")
    print(f"\nOK: {len(listos)}/{len(DATA['cursos'])} cursos.")
    print("Los .gs viven en _privado/: llevan los correos de los estudiantes, asi que NO se")
    print("versionan y NO aparecen en GitHub. Al lado, visibles, quedan los LEEME con la ruta:")
    print("  <Curso>/Plan curso/<periodo>/LEEME - Apps Script del curso.md")
    print("  LEEME - Apps Script del semestre.md   (raiz de Cursos)")
    print("")
    print("Instalación y pruebas: Manuales/01. Cada sesión lleva SU propio enlace de Meet,")
    print("así que no hay ningún enlace que pegar de vuelta en el material: al estudiante le")
    print("llega dentro de la invitación de Calendar de cada sesión.")


if __name__ == "__main__":
    main()
