# -*- coding: utf-8 -*-
"""Genera, por curso, el Apps Script que crea los encuentros del semestre en Calendar.

Qué resuelve
------------
Importar un `.ics` deja los invitados dentro del evento pero **Google no envía las
invitaciones**. Este camino sí las envía: crea los eventos con la API de Calendar y
`sendUpdates: 'all'`.

Y le pone a **cada sesión su propia sala de Meet**: N encuentros, N enlaces distintos.
El estudiante no tiene que guardar ningún enlace — entra por la invitación de Calendar de
esa sesión, que ya lo trae dentro.

Cada sala se pide con un `requestId` determinista y **distinto por sesión**
(`<codigo>-<grupo>-sNN`). Eso es lo que hace la operación repetible: volver a ejecutar no
crea una segunda sala para la misma sesión, y el enlace de una sesión que ya existe no
cambia por reejecutar.

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
 *   - Crea {n_ses} eventos, uno por sesión. Las autónomas por festivo también quedan en
 *     el calendario (el estudiante debe ver la fecha de cierre), pero SIN Meet.
 *   - Le da a **cada sesión su propio enlace de Meet** (N sesiones = N salas distintas).
 *     El estudiante entra por la invitación de Calendar de esa sesión, que lo trae dentro.
 *   - Invita a los {n_inv} estudiantes del grupo y, si SEND_INVITES = true, **les envía**
 *     el correo de invitación (esto es lo que la importación de un .ics no hace).
 *
 * INSTALACIÓN Y PRUEBAS: `Manuales/01 - Alistar un curso …` en la raíz de Cursos.
 */

// ─────────────────────────────────────────────── CONFIGURACIÓN

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

/**
 * Base del requestId. Cada sesión pide su sala con REQUEST_ID + '-sNN', distinto por sesión:
 * así cada encuentro tiene SU enlace, y reejecutar no crea una segunda sala para la misma
 * sesión (Google devuelve la que ya existe para ese requestId).
 */
var REQUEST_ID = {request_id};

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
  Logger.log('Meet             : uno distinto por sesión (' + _conMeet_() + ' de ' +
             SESIONES.length + ' sesiones lo llevan; las autónomas no)');
  Logger.log('');
  var existen = 0, conSala = 0;
  for (var i = 0; i < SESIONES.length; i++) {{
    var s = SESIONES[i];
    var ya = _buscarEvento_(cal, s);
    var sala = '';
    if (ya) {{
      existen++;
      sala = s.meet ? _meetNativo_(_idApi_(ya)) : '';
      if (sala) conSala++;
    }}
    Logger.log((ya ? 'YA EXISTE  ' : 'se crearía ') + s.fecha + ' ' + s.ini + '-' + s.fin +
               '  ' + s.subject +
               (sala ? '   ' + sala : (ya && s.meet ? '   (sin Meet aún)' : '')));
  }}
  Logger.log('');
  Logger.log('Total: ' + SESIONES.length + ' sesión(es) · ya creadas: ' + existen +
             ' · con sala de Meet: ' + conSala + '/' + _conMeet_());
  if (!_apiCalendar_()) {{
    Logger.log('');
    Logger.log('Activa el servicio avanzado: Servicios (+) -> Google Calendar API -> Añadir.');
    Logger.log('Sin él los eventos se crean con invitados, pero SIN Meet.');
  }}
}}

/** Crea los encuentros, le da a cada uno su propia sala de Meet e invita al grupo. */
function crearEncuentros() {{
  var cal = _cal_();
  if (SIMULAR) {{
    Logger.log('SIMULAR = true: no se creó nada. Ponlo en false cuando verificar() se vea bien.');
    return;
  }}

  var eventos = [], creados = 0, reusados = 0, invAgregados = 0;
  for (var i = 0; i < SESIONES.length; i++) {{
    var s = SESIONES[i];
    var ya = _buscarEvento_(cal, s);
    if (ya) {{
      // El evento ya existe. Hay que SINCRONIZAR los invitados: si llego una nomina nueva,
      // un estudiante que entro tarde no recibiria invitacion nunca (los invitados solo se
      // pasan al crear el evento).
      invAgregados += _sincronizarInvitados_(ya);
      eventos.push(ya); reusados++; continue;
    }}
    eventos.push(cal.createEvent(s.subject, _fecha(s.fecha, s.ini), _fecha(s.fecha, s.fin), {{
      description: s.desc,
      guests: INVITADOS.join(','),
      sendInvites: SEND_INVITES
    }}));
    creados++;
    Utilities.sleep(300);   // no atropellar la cuota
  }}
  Logger.log('Eventos: ' + creados + ' creado(s) · ' + reusados + ' ya existía(n).');
  if (invAgregados) {{
    Logger.log('Invitados agregados a eventos que ya existían: ' + invAgregados +
               ' (nómina nueva).');
  }}

  if (!_apiCalendar_()) {{
    Logger.log('');
    Logger.log('Los encuentros quedaron creados, pero SIN enlace de Meet: el servicio');
    Logger.log('avanzado de Calendar no está activo. Actívalo (Servicios (+) -> Google');
    Logger.log('Calendar API) y vuelve a ejecutar: no duplica eventos ni salas.');
    return;
  }}

  // Una sala POR SESION. Cada una con su requestId, para que reejecutar no duplique.
  var nativos = 0, conMeet = 0;
  for (var j = 0; j < eventos.length; j++) {{
    if (!SESIONES[j].meet) continue;          // autonoma: no hay encuentro, no lleva Meet
    conMeet++;
    var url = _asegurarMeet_(eventos[j], j);
    if (url) {{ nativos++; Logger.log('  ' + SESIONES[j].fecha + '  ' + url); }}
  }}
  Logger.log('Meet: ' + nativos + '/' + conMeet + ' sesión(es) con su propia sala ' +
             '(las autónomas no llevan Meet a propósito).');
  Logger.log('');
  Logger.log('No hay enlace que pegar en el material: a cada estudiante le llega el de');
  Logger.log('cada sesión dentro de su invitación de Calendar.');
}}

/**
 * Agrega al evento los invitados de INVITADOS que todavia no esten. Devuelve cuantos agrego.
 * Necesario porque `createEvent` solo pone invitados al crear: sin esto, una nomina nueva no
 * llegaria nunca a los eventos ya creados.
 */
function _sincronizarInvitados_(evento) {{
  var actuales = {{}};
  var lista = evento.getGuestList();
  for (var i = 0; i < lista.length; i++) {{
    actuales[String(lista[i].getEmail()).toLowerCase()] = true;
  }}
  var n = 0;
  for (var j = 0; j < INVITADOS.length; j++) {{
    if (!actuales[String(INVITADOS[j]).toLowerCase()]) {{
      try {{ evento.addGuest(INVITADOS[j]); n++; }}
      catch (e) {{ Logger.log('AVISO: no pude invitar a un estudiante: ' + e); }}
    }}
  }}
  return n;
}}

/**
 * Borra los encuentros de esta serie. Dos pasadas:
 *   1. Por titulo exacto de cada sesion (lo que este script creo).
 *   2. Barrido por la ventana horaria de cada sesion, para cazar eventos de una corrida
 *      ANTERIOR cuyo titulo ya no coincide (paso al cambiar los prefijos o la modalidad).
 *      Solo borra si el titulo menciona el curso o su codigo: no toca eventos ajenos.
 *
 * OJO: borrar un evento con invitados le manda a cada estudiante un correo de cancelacion.
 * Si lo unico que cambio es la nomina, NO hace falta borrar: `crearEncuentros` ya sincroniza
 * los invitados de los eventos que existen.
 *
 * Al borrar un evento se va TAMBIEN su sala de Meet. Si despues recreas, esa sesion queda
 * con un enlace NUEVO — y ese es justo el que le llega al estudiante en la invitacion, asi
 * que no hay nada que republicar en el material.
 */
function eliminarEncuentros() {{
  var cal = _cal_();
  var exactos = [], huerfanos = [];

  for (var i = 0; i < SESIONES.length; i++) {{
    var s = SESIONES[i];
    var ev = _buscarEvento_(cal, s);
    if (ev) {{ exactos.push(ev); continue; }}
    // segunda pasada: mismo dia y hora, titulo distinto pero del curso
    var desde = _fecha(s.fecha, '00:01'), hasta = _fecha(s.fecha, '23:59');
    var enEseDia = cal.getEvents(desde, hasta);
    for (var j = 0; j < enEseDia.length; j++) {{
      var t = enEseDia[j].getTitle();
      if (_esDeEsteCurso_(t) && !_yaEsta_(exactos, enEseDia[j]) &&
          !_yaEsta_(huerfanos, enEseDia[j])) {{
        huerfanos.push(enEseDia[j]);
      }}
    }}
  }}

  Logger.log('Por titulo exacto : ' + exactos.length);
  Logger.log('Huerfanos del curso: ' + huerfanos.length +
             (huerfanos.length ? '  (titulo viejo, misma fecha)' : ''));
  for (var k = 0; k < huerfanos.length; k++) {{
    Logger.log('   huerfano: ' + huerfanos[k].getStartTime() + '  ' + huerfanos[k].getTitle());
  }}

  if (SIMULAR) {{
    Logger.log('');
    Logger.log('SIMULAR = true: no se borro nada. Se borrarian ' +
               (exactos.length + huerfanos.length) + ' evento(s).');
    return 0;
  }}

  var todos = exactos.concat(huerfanos), n = 0;
  for (var m = 0; m < todos.length; m++) {{
    try {{ todos[m].deleteEvent(); n++; Utilities.sleep(200); }}
    catch (e) {{ Logger.log('AVISO: no pude borrar «' + todos[m].getTitle() + '»: ' + e); }}
  }}
  Logger.log('Eliminados=' + n + '. Sus salas de Meet se fueron con ellos.');
  return n;
}}

/** true si el titulo es de este curso (nombre o codigo), para no borrar eventos ajenos. */
function _esDeEsteCurso_(titulo) {{
  var t = String(titulo || '').toLowerCase();
  return t.indexOf(String(CURSO).toLowerCase()) !== -1 ||
         t.indexOf(String(CODIGO).toLowerCase()) !== -1;
}}

function _yaEsta_(lista, ev) {{
  for (var i = 0; i < lista.length; i++) {{
    if (lista[i].getId() === ev.getId()) return true;
  }}
  return false;
}}

/**
 * Borra TODO y vuelve a crear, en una sola corrida. Es lo que se usa cuando cambio la
 * nomina de forma grande o se movieron fechas y se prefiere partir de cero.
 *
 * Manda cancelaciones y luego invitaciones nuevas a cada estudiante, y los enlaces de Meet
 * cambian (cada evento nuevo trae su propia sala). Si solo entraron o salieron algunas
 * personas, `crearEncuentros` sola es menos ruidosa: sincroniza invitados sin tocar los
 * eventos ni sus enlaces.
 */
function recrearTodo() {{
  if (SIMULAR) {{
    Logger.log('SIMULAR = true: no se toca nada. Esto es lo que pasaria:');
    eliminarEncuentros();
    Logger.log('');
    Logger.log('...y despues se crearian ' + SESIONES.length + ' evento(s) con ' +
               INVITADOS.length + ' invitado(s), cada uno con una sala de Meet NUEVA.');
    return;
  }}
  Logger.log('=== 1/2  BORRANDO ===');
  var borrados = eliminarEncuentros();
  Logger.log('');
  Logger.log('=== 2/2  CREANDO ===');
  crearEncuentros();
  Logger.log('');
  Logger.log('Listo: ' + borrados + ' borrado(s) y la serie recreada con ' +
             INVITADOS.length + ' invitado(s).');
}}

// ─────────────────────────────────────────────── MEET (una sala por sesión)

function _apiCalendar_() {{
  try {{ return typeof Calendar !== 'undefined' && !!Calendar.Events; }} catch (e) {{ return false; }}
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

/** Cuántas sesiones llevan Meet (las autónomas no). */
function _conMeet_() {{
  var n = 0;
  for (var i = 0; i < SESIONES.length; i++) if (SESIONES[i].meet) n++;
  return n;
}}

/** requestId de la sesión `i`: distinto por sesión, estable entre corridas. */
function _requestId_(i) {{
  var n = String(i + 1);
  return REQUEST_ID + '-s' + (n.length < 2 ? '0' + n : n);
}}

/**
 * Se asegura de que la sesión `i` tenga SU propia sala, y devuelve su URL ('' si no se pudo).
 * Si el evento ya tiene una, la respeta: no la reemplaza ni crea una segunda.
 */
function _asegurarMeet_(evento, i) {{
  var ya = _meetNativo_(_idApi_(evento));
  if (ya) {{ _anotarMeet_(evento, ya); return ya; }}
  var url = _crearSala_(evento, _requestId_(i));
  if (url) _anotarMeet_(evento, url);
  return url;
}}

/** Crea la sala de Meet de `evento` y devuelve su URL ('' si no se pudo). */
function _crearSala_(evento, requestId) {{
  var id = _idApi_(evento);
  try {{
    var res = Calendar.Events.patch({{
      conferenceData: {{
        createRequest: {{
          requestId: requestId,
          conferenceSolutionKey: {{ type: 'hangoutsMeet' }}
        }}
      }}
    }}, _calId_(), id, {{
      conferenceDataVersion: 1,
      sendUpdates: SEND_INVITES ? 'all' : 'none'
    }});

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

/** Escribe la URL en Ubicación y descripción, para que se vea sin abrir el chip. */
function _anotarMeet_(evento, url) {{
  try {{
    if (evento.getLocation() !== url) evento.setLocation(url);
    var d = evento.getDescription() || '';
    if (d.indexOf(url) < 0) {{
      evento.setDescription((d ? d + '\\n' : '') + 'Meet de esta sesión: ' + url);
    }}
  }} catch (e) {{
    Logger.log('AVISO: no pude escribir el enlace en «' + evento.getTitle() + '»: ' + e);
  }}
}}
"""


def _escribir_puntero(meta: dict, gs: Path, n_ses: int, n_inv: int) -> None:
    """Deja un LEEME VISIBLE al lado de la carpeta privada.

    El .gs lleva los correos de los estudiantes, asi que vive en `_privado/` y no se
    versiona: no aparece en GitHub, y en Drive una carpeta con guion bajo se pasa por alto.
    Este puntero SI se versiona (no tiene datos personales) y dice exactamente donde esta.
    """
    L = [
        f"# Apps Script del curso - {meta['nombre']} - {PERIODO}",
        "",
        "## Crear los encuentros en Calendar (cada sesión con su propio Meet)",
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
        "enviandoles la invitacion de verdad. Deja **la misma sala de Meet** en todas las",
        "sesiones sincronicas; las autonomas por festivo quedan en el calendario pero sin Meet.",
        "",
        "**Paso a paso:** `Manuales/01 - Alistar un curso (encuentros, Meet, correo e",
        "invitaciones).md` en la raiz de `Cursos`. Incluye como sacar el `CALENDAR_ID` y por",
        "que se ejecuta `verificar` antes de `crearEncuentros`.",
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
    destino = gs.parent.parent / "LEEME - Apps Script del curso.md"
    destino.write_text("\n".join(L), encoding="utf-8")


def _avisar_sin_nomina(meta: dict, privado) -> None:
    """Marca el LEEME del curso cuando NO se pudo generar el .gs.

    Importa porque el .gs de una corrida anterior sigue en disco con la nómina vieja: sin
    este aviso, se pega en Apps Script un archivo desactualizado sin que nada lo delate.
    """
    gs = privado / f"CrearEncuentros - {meta['nombre']}.gs"
    viejo = gs.exists()
    L = [
        f"# Apps Script del curso - {meta['nombre']} - {PERIODO}",
        "",
        "## ATENCION: este curso NO tiene Apps Script al dia",
        "",
        "La ultima regeneracion **no encontro la nomina** del grupo "
        f"`{meta['codigo']}` / `{meta['grupo']}`, asi que no se pudo generar el `.gs`.",
        "",
    ]
    if viejo:
        L += [
            "> **Hay un `.gs` viejo en `_privado/`. NO lo uses:** trae la nomina de la",
            "> corrida anterior, asi que invitaria a los estudiantes equivocados.",
            "",
        ]
    L += [
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


def main() -> None:
    total = 0
    for key, meta in DATA["cursos"].items():
        privado = ev.privado_de(meta)
        info = ev.cargar_nomina(meta, key, ev.cargar_correos_manuales(meta))
        if not info:
            print(f"  {meta['nombre']}: sin nómina -> no se genera el .gs")
            _avisar_sin_nomina(meta, privado)
            continue
        correos = sorted({e["correo"] for e in info["estudiantes"] if e["correo"]})
        ses = sesiones_de(meta)

        gs = PLANTILLA.format(
            nombre=meta["nombre"],
            periodo=PERIODO,
            periodo_us=js(PERIODO.replace("-", "_")),
            n_ses=len(ses),
            n_inv=len(correos),
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
        _escribir_puntero(meta, destino, len(ses), len(correos))
        print(f"  {meta['nombre'][:34]:<34} {len(ses)} sesiones · {len(correos)} invitados")
        print(f"      {destino}")
        total += 1

    print(f"\nOK: {total}/{len(DATA['cursos'])} cursos.")
    print("Los .gs viven en _privado/ de cada curso: llevan los correos de los estudiantes,")
    print("asi que NO se versionan y NO aparecen en GitHub. Al lado, visible, queda un")
    print("\"LEEME - Apps Script del curso.md\" con la ruta exacta.")
    print("")
    print("Instalación y pruebas: Manuales/01. Cada sesión lleva SU propio enlace de Meet,")
    print("así que no hay ningún enlace que pegar de vuelta en el material: al estudiante le")
    print("llega dentro de la invitación de Calendar de cada sesión.")


if __name__ == "__main__":
    main()
