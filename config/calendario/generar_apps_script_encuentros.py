# -*- coding: utf-8 -*-
"""Genera, por curso, el Apps Script que crea los encuentros del semestre en Calendar.

Qué resuelve
------------
Importar un `.ics` deja los invitados dentro del evento pero **Google no envía las
invitaciones**. Este camino sí las envía: crea los eventos con la API de Calendar y
`sendUpdates: 'all'`.

Y deja **una sola sala de Meet para todas las sesiones del curso**, en vez de una sala
distinta por evento. Ese enlace único es el que se publica en el correo de bienvenida, así
el estudiante entra siempre por el mismo sitio.

El patrón de la sala única está portado de la implementación ya probada en producción en
`CUN/Cursos/config/slides/build_calendar_encuentros.py`: se crea **una** conferencia con un
`requestId` determinista y luego se copia a los demás eventos con `conferenceData`
**sin** `createRequest`, que es como Calendar duplica un Meet.

Salida
------
`<Curso>/Plan curso/<periodo>/_privado/CrearEncuentros - <Curso>.gs`

Va en `_privado/` porque **lleva los correos de los estudiantes**. Está en `.gitignore`.

Uso
---
    python config/calendario/generar_apps_script_encuentros.py

Requiere que exista la nómina del curso (la lee con el mismo lector que
`generar_eventos_calendario.py`).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import generar_eventos_calendario as ev

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads(Path(__file__).with_name("semestre_2026_2.json").read_text(encoding="utf-8"))
PERIODO = DATA["periodo"]
DOCENTE = DATA["docente"]["nombre_completo"]

TZ = "America/Bogota"


def js(s) -> str:
    """Literal JS de una cadena."""
    return "'" + str(s).replace("\\", "\\\\").replace("'", "\\'") + "'"


def sesiones_de(meta: dict) -> list[dict]:
    ini, fin = ev.hhmm(meta["horario"])          # '100000', '120000'
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


PLANTILLA = """/**
 * {nombre} — crear los encuentros del periodo {periodo} en Google Calendar.
 *
 * ARCHIVO GENERADO. No editarlo a mano: se regenera con
 *   python config/calendario/generar_apps_script_encuentros.py
 *
 * CONTIENE CORREOS DE ESTUDIANTES. Vive en _privado/ y no se versiona.
 *
 * Qué hace:
 *   - Crea {n_ses} eventos (las sesiones con encuentro; las autónomas por festivo no
 *     llevan evento con Meet porque no hay encuentro).
 *   - Deja **la misma sala de Meet en todos**, para que el estudiante entre siempre por el
 *     mismo enlace.
 *   - Invita a los {n_inv} estudiantes del grupo y, si SEND_INVITES = true, **les envía**
 *     el correo de invitación (esto es lo que la importación de un .ics no hace).
 *
 * INSTALACIÓN Y PRUEBAS: `Manuales/01 - Alistar un curso …` en la raíz de Cursos.
 */

// ─────────────────────────────────────────────── CONFIGURACIÓN

/** Enlace de Meet de la serie. Vacío = lo crea el script y lo imprime para que lo pegues. */
var MEET_URL = {meet_url};

/**
 * ID del calendario donde se crean los encuentros.
 *
 * Sale VACÍO a propósito. Cómo obtenerlo: ejecuta `listarCalendarios()` (está más abajo) y
 * copia el ID que te interese; o en Google Calendar, en «Mis calendarios», pasa el mouse
 * sobre el calendario -> tres puntos -> «Configuración y uso compartido» -> baja hasta
 * «Integrar calendario» -> copia «ID de calendario».
 *
 * El principal tiene el ID de tu correo; uno secundario se ve como
 * `abc123...@group.calendar.google.com`. Si usas un calendario aparte para clases, ese es el
 * que va aquí — y es también el que hay que poner en el script de grabaciones, para que los
 * dos miren el mismo sitio.
 */
var CALENDAR_ID = '';

/** true = envía los correos de invitación al crear/actualizar. */
var SEND_INVITES = true;

/** true = no crea ni modifica nada; solo dice qué haría. Empieza SIEMPRE en true. */
var SIMULAR = true;

var CURSO = {curso};
var CODIGO = {codigo};
var GRUPO = {grupo};
var TZ = {tz};

/** requestId determinista: si se repite, Google NO crea una segunda sala. */
var REQUEST_ID = {request_id};
var PROP_MEET = 'meet_' + CODIGO + '_' + GRUPO;

var INVITADOS = [
{invitados}
];

var SESIONES = [
{sesiones}
];

// ─────────────────────────────────────────────── CALENDARIO

/**
 * El calendario con el que trabaja el script.
 * Preferimos un ID explicito: el «por omision» depende de la cuenta con la que se abrio
 * Apps Script, y si un dia se ejecuta con otra sesion escribe en un calendario distinto sin
 * avisar. Con los eventos ya creados e invitaciones enviadas, eso no se deshace facil.
 */
function _cal_() {{
  if (CALENDAR_ID) {{
    var c = CalendarApp.getCalendarById(CALENDAR_ID);
    if (!c) throw new Error('CALENDAR_ID no corresponde a un calendario visible: ' + CALENDAR_ID);
    return c;
  }}
  // return CalendarApp.getDefaultCalendar();   // <- alternativa: calendario por omision
  throw new Error('Falta CALENDAR_ID. Ejecuta listarCalendarios() y pega el ID arriba, ' +
                  'o descomenta la linea de getDefaultCalendar() en _cal_().');
}}

/** El mismo calendario, para la API avanzada (que recibe el id, no el objeto). */
function _calId_() {{
  // return 'primary';   // <- alternativa: calendario por omision
  if (!CALENDAR_ID) throw new Error('Falta CALENDAR_ID (ver _cal_()).');
  return CALENDAR_ID;
}}

/** Imprime los calendarios de la cuenta con su ID, para copiar el que toque. */
function listarCalendarios() {{
  var todos = CalendarApp.getAllCalendars();
  var pormision = CalendarApp.getDefaultCalendar().getId();
  Logger.log('Calendarios visibles en esta cuenta (' + todos.length + '):');
  for (var i = 0; i < todos.length; i++) {{
    Logger.log('  ' + todos[i].getName() +
               (todos[i].getId() === pormision ? ' [por omision]' : '') +
               '  ->  ' + todos[i].getId());
  }}
  Logger.log('');
  Logger.log('Copia el ID que corresponda y pegalo en CALENDAR_ID, arriba del todo.');
  Logger.log('Usa el MISMO en el script de grabaciones (manual 02).');
}}

// ─────────────────────────────────────────────── ENTRADA

/** SOLO LECTURA: qué pasaría. Ejecútalo primero. */
function verificar() {{
  var cal = _cal_();
  Logger.log('Modo             : ' + (SIMULAR ? 'SIMULACIÓN (no toca nada)' : 'REAL'));
  Logger.log('Curso            : ' + CURSO + ' (' + CODIGO + ' · grupo ' + GRUPO + ')');
  Logger.log('Calendario       : ' + cal.getName() + '  [' + cal.getId() + ']');
  Logger.log('CALENDAR_ID      : ' + (CALENDAR_ID || '(vacio: usa listarCalendarios())'));
  Logger.log('Servicio avanzado: ' + (_apiCalendar_() ? 'activo' : 'NO ACTIVO — sin él no hay Meet'));
  Logger.log('Invitados        : ' + INVITADOS.length);
  Logger.log('Enviar correos   : ' + (SEND_INVITES ? 'sí' : 'no'));
  Logger.log('Meet configurado : ' + (_meetConfigurado_() ? MEET_URL : '(vacío: se creará uno)'));
  Logger.log('Sala guardada    : ' + (_salaGuardada_() || '(ninguna)'));
  Logger.log('');
  var existen = 0;
  for (var i = 0; i < SESIONES.length; i++) {{
    var s = SESIONES[i];
    var ya = _buscarEvento_(cal, s);
    if (ya) existen++;
    Logger.log((ya ? 'YA EXISTE  ' : 'se crearía ') + s.fecha + ' ' + s.ini + '-' + s.fin +
               '  ' + s.subject);
  }}
  Logger.log('');
  Logger.log('Total: ' + SESIONES.length + ' sesión(es) · ya creadas: ' + existen);
  if (!_apiCalendar_()) {{
    Logger.log('');
    Logger.log('Activa el servicio avanzado: Servicios (+) -> Google Calendar API -> Añadir.');
    Logger.log('Sin él los eventos se crean con invitados, pero SIN Meet.');
  }}
}}

/** Crea los encuentros, deja la misma sala de Meet en todos e invita al grupo. */
function crearEncuentros() {{
  var cal = _cal_();
  if (SIMULAR) {{
    Logger.log('SIMULAR = true: no se creó nada. Ponlo en false cuando verificar() se vea bien.');
    return;
  }}

  var eventos = [], creados = 0, reusados = 0;
  for (var i = 0; i < SESIONES.length; i++) {{
    var s = SESIONES[i];
    var ya = _buscarEvento_(cal, s);
    if (ya) {{ eventos.push(ya); reusados++; continue; }}
    eventos.push(cal.createEvent(s.subject, _fecha(s.fecha, s.ini), _fecha(s.fecha, s.fin), {{
      description: s.desc,
      guests: INVITADOS.join(','),
      sendInvites: SEND_INVITES
    }}));
    creados++;
    Utilities.sleep(300);   // no atropellar la cuota
  }}
  Logger.log('Eventos: ' + creados + ' creado(s) · ' + reusados + ' ya existía(n).');

  var semilla = null;
  for (var k = 0; k < eventos.length; k++) {{ if (SESIONES[k].meet) {{ semilla = eventos[k]; break; }} }}
  var url = _salaDeLaSerie_(cal, semilla);
  if (!url) {{
    Logger.log('Los encuentros quedaron creados, pero SIN enlace de Meet.');
    Logger.log('Activa el servicio avanzado de Calendar y vuelve a ejecutar (no duplica nada).');
    return;
  }}
  var nativos = 0, conMeet = 0;
  for (var j = 0; j < eventos.length; j++) {{
    if (!SESIONES[j].meet) continue;          // autonoma: no hay encuentro, no lleva Meet
    conMeet++;
    if (_aplicarMeet_(eventos[j], url)) nativos++;
  }}
  Logger.log('Meet ' + url + ' -> chip nativo en ' + nativos + '/' + conMeet +
             ' (las autonomas no llevan Meet a proposito)');
  Logger.log('');
  Logger.log('PEGA ESTE ENLACE EN EL MATERIAL:');
  Logger.log('  config/calendario/semestre_' + {periodo_us} + '.json -> cursos.<curso>.meet');
  Logger.log('  ' + url);
  Logger.log('y regenera para que el correo de bienvenida lo publique.');
}}

/** Borra los eventos de esta serie. NO olvida la sala (para eso, olvidarSalaMeet). */
function eliminarEncuentros() {{
  if (SIMULAR) {{ Logger.log('SIMULAR = true: no se borró nada.'); return; }}
  var cal = _cal_(), n = 0;
  for (var i = 0; i < SESIONES.length; i++) {{
    var ev = _buscarEvento_(cal, SESIONES[i]);
    if (ev) {{ ev.deleteEvent(); n++; }}
  }}
  Logger.log('Eliminados=' + n + '. La sala de Meet sigue guardada.');
}}

/** Suelta la sala guardada: la próxima corrida creará una nueva. */
function olvidarSalaMeet() {{
  PropertiesService.getScriptProperties().deleteProperty(PROP_MEET);
  Logger.log('Sala olvidada. Ojo: si ya publicaste el enlace, quedará desactualizado.');
}}

// ─────────────────────────────────────────────── MEET (una sala para toda la serie)

function _apiCalendar_() {{
  try {{ return typeof Calendar !== 'undefined' && !!Calendar.Events; }} catch (e) {{ return false; }}
}}

function _meetConfigurado_() {{
  return typeof MEET_URL === 'string' && MEET_URL.indexOf('https://meet.google.com/') === 0;
}}

function _salaGuardada_() {{
  return (PropertiesService.getScriptProperties().getProperty(PROP_MEET) || '').trim();
}}

function _idApi_(evento) {{ return evento.getId().split('@')[0]; }}

function _fecha(fechaIso, hhmm) {{
  var p = fechaIso.split('-'), h = hhmm.split(':');
  return new Date(+p[0], +p[1] - 1, +p[2], +h[0], +h[1], 0);
}}

/** Evento ya existente para esa sesión (mismo título, mismo día), o null. */
function _buscarEvento_(cal, s) {{
  var hallados = cal.getEvents(_fecha(s.fecha, '00:01'), _fecha(s.fecha, '23:59'),
                               {{ search: s.subject }})
    .filter(function (ev) {{ return ev.getTitle() === s.subject; }});
  return hallados.length ? hallados[0] : null;
}}

function _uriDeConferencia_(conf) {{
  if (!conf || !conf.entryPoints) return '';
  for (var i = 0; i < conf.entryPoints.length; i++) {{
    if (conf.entryPoints[i].entryPointType === 'video') return conf.entryPoints[i].uri || '';
  }}
  return '';
}}

function _meetNativo_(id) {{
  if (!_apiCalendar_()) return '';
  try {{
    var ev = Calendar.Events.get(_calId_(), id, {{ conferenceDataVersion: 1 }});
    return _uriDeConferencia_(ev && ev.conferenceData);
  }} catch (e) {{ return ''; }}
}}

function _meetDeLaSerieExistente_(cal) {{
  for (var i = 0; i < SESIONES.length; i++) {{
    if (!SESIONES[i].meet) continue;
    var ev = _buscarEvento_(cal, SESIONES[i]);
    if (ev) {{ var u = _meetNativo_(_idApi_(ev)); if (u) return u; }}
  }}
  return '';
}}

/**
 * conferenceData reutilizable a partir de una URL de Meet ya conocida.
 * SIN createRequest: así es como Calendar copia el Meet al duplicar un evento, y por eso
 * las N sesiones acaban con el MISMO enlace en vez de con N salas distintas.
 */
function _conferenciaDesdeUrl_(url) {{
  var id = String(url).replace(/^https?:\\/\\/meet\\.google\\.com\\//, '');
  return {{
    conferenceId: id,
    signature: null,
    conferenceSolution: {{ key: {{ type: 'hangoutsMeet' }}, name: 'Google Meet' }},
    entryPoints: [{{ entryPointType: 'video', uri: url, label: id }}]
  }};
}}

/** La sala de TODA la serie, sin crear nunca una segunda. */
function _salaDeLaSerie_(cal, semilla) {{
  if (_meetConfigurado_()) return MEET_URL;

  var guardado = _salaGuardada_();
  if (guardado) {{ Logger.log('Reutilizo la sala que creé antes: ' + guardado); return guardado; }}

  if (!_apiCalendar_()) return '';

  var enEvento = _meetDeLaSerieExistente_(cal);
  if (enEvento) {{
    PropertiesService.getScriptProperties().setProperty(PROP_MEET, enEvento);
    Logger.log('Reutilizo la sala que ya tenían los encuentros: ' + enEvento);
    return enEvento;
  }}
  if (!semilla) return '';

  var url = _crearSala_(semilla);
  if (!url) return '';
  PropertiesService.getScriptProperties().setProperty(PROP_MEET, url);
  Logger.log('SALA DE MEET CREADA: ' + url);
  return url;
}}

/** Crea UNA sala de Meet sobre `evento` y devuelve su URL ('' si no se pudo). */
function _crearSala_(evento) {{
  var id = _idApi_(evento);
  try {{
    var res = Calendar.Events.patch({{
      conferenceData: {{
        createRequest: {{
          requestId: REQUEST_ID,
          conferenceSolutionKey: {{ type: 'hangoutsMeet' }}
        }}
      }}
    }}, _calId_(), id, {{ conferenceDataVersion: 1, sendUpdates: 'none' }});

    var url = _uriDeConferencia_(res && res.conferenceData);
    // Google crea la sala de forma asíncrona: la primera respuesta puede venir «pending».
    for (var i = 0; !url && i < 10; i++) {{ Utilities.sleep(1500); url = _meetNativo_(id); }}
    if (!url) {{
      Logger.log('AVISO: Google aceptó la petición pero aún no devuelve el enlace.');
      Logger.log('Espera un minuto y vuelve a ejecutar crearEncuentros() (no duplica nada).');
    }}
    return url;
  }} catch (e) {{
    Logger.log('AVISO: no se pudo crear la sala de Meet: ' + e);
    return '';
  }}
}}

/** Deja `url` en el evento: Ubicación, descripción y chip nativo de Meet. */
function _aplicarMeet_(evento, url) {{
  try {{
    if (evento.getLocation() !== url) evento.setLocation(url);
    var d = evento.getDescription() || '';
    if (d.indexOf(url) < 0) {{
      evento.setDescription((d ? d + '\\n' : '') + 'Meet (mismo enlace toda la serie): ' + url);
    }}
  }} catch (e) {{
    Logger.log('AVISO: no pude escribir el enlace en «' + evento.getTitle() + '»: ' + e);
  }}
  if (!_apiCalendar_()) return false;
  try {{
    var id = _idApi_(evento);
    if (_meetNativo_(id) === url) return true;   // ya está bien
    Calendar.Events.patch({{ conferenceData: _conferenciaDesdeUrl_(url) }}, _calId_(), id, {{
      conferenceDataVersion: 1,
      sendUpdates: SEND_INVITES ? 'all' : 'none'
    }});
    return _meetNativo_(id) === url;
  }} catch (e) {{
    Logger.log('AVISO: sin chip nativo en «' + evento.getTitle() + '»: ' + e);
    return false;
  }}
}}
"""


def main() -> None:
    total = 0
    for key, meta in DATA["cursos"].items():
        privado = ev.privado_de(meta)
        info = ev.cargar_nomina(meta, key, ev.cargar_correos_manuales(meta))
        if not info:
            print(f"  {meta['nombre']}: sin nómina -> no se genera el .gs")
            continue
        correos = sorted({e["correo"] for e in info["estudiantes"] if e["correo"]})
        ses = sesiones_de(meta)
        meet = (meta.get("meet") or "").strip()

        gs = PLANTILLA.format(
            nombre=meta["nombre"],
            periodo=PERIODO,
            periodo_us=js(PERIODO.replace("-", "_")),
            n_ses=len(ses),
            n_inv=len(correos),
            meet_url=js(meet) if meet else "''",
            curso=js(meta["nombre"]),
            codigo=js(meta["codigo"]),
            grupo=js(meta["grupo"]),
            tz=js(TZ),
            request_id=js(f"uniajc-{meta['codigo']}-{meta['grupo']}-{PERIODO}"),
            invitados="\n".join(f"  {js(c)}," for c in correos),
            sesiones="\n".join(
                ("  {{ subject: {s}, fecha: {f}, ini: {i}, fin: {n}, meet: {m},"
                 " desc: {d} }},").format(
                    s=js(x["subject"]), f=js(x["fecha"]), i=js(x["ini"]),
                    n=js(x["fin"]), m=("true" if x["meet"] else "false"), d=js(x["desc"]))
                for x in ses
            ),
        )
        privado.mkdir(parents=True, exist_ok=True)
        destino = privado / f"CrearEncuentros - {meta['nombre']}.gs"
        destino.write_text(gs, encoding="utf-8")
        print(f"  {meta['nombre'][:34]:<34} {len(ses)} sesiones · {len(correos)} invitados "
              f"-> {destino.relative_to(ROOT)}")
        total += 1

    print(f"\nOK: {total}/{len(DATA['cursos'])} cursos.")
    print("Instalación y pruebas: Manuales/01 (crear los encuentros es el PRIMER paso:")
    print("de ahí sale el enlace de Meet que se publica en el correo de bienvenida).")


if __name__ == "__main__":
    main()
