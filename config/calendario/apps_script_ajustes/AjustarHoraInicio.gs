/**
 * AjustarHoraInicio.gs — mueve el INICIO de los encuentros de Programación II y
 * Seminario de Sistemas de las 18:00 a las 18:30. El fin (20:00) no se toca.
 *
 * Por qué un script aparte y no `recrearTodo()` del script de encuentros:
 * recrear borra y vuelve a crear el evento, y con el evento se va su sala de Meet.
 * Cada sesión tiene su propio enlace, así que recrear 26 eventos significa 26 enlaces
 * nuevos y los que ya se compartieron con el grupo dejan de servir. Cambiar la hora de
 * un evento existente con `setTime()` conserva la sala: es la misma reunión, media hora
 * más tarde.
 *
 * Qué hace y qué NO hace:
 *   - Solo toca eventos cuyo título menciona uno de los dos cursos de CURSOS.
 *   - Solo si empiezan EXACTAMENTE a las 18:00 y terminan EXACTAMENTE a las 20:00.
 *     Un evento ya movido, o con otro horario, se reporta y se deja quieto.
 *   - No crea ni borra nada. No toca invitados (los eventos no tienen: son bloques del
 *     calendario personal del docente). No manda ningún correo.
 *   - No toca Bases de Datos II ni Arquitectura, que también están a las 18:00 y 10:00.
 *
 * Orden de uso:
 *   1. listarCalendarios()   -> copia el ID y pégalo en CALENDAR_ID
 *   2. verificar()           -> dice qué encontró y qué movería. No cambia nada.
 *   3. ajustarHoraInicio()   -> con SIMULAR = true primero; luego false.
 *   4. verificar()           -> confirma que quedaron en 18:30.
 *   revertir()               -> deshace (18:30 -> 18:00) si algo salió mal.
 */

// ─────────────────────────────────────────────────────────────────────────────
//  1. EL ID DEL CALENDARIO VA AQUÍ
// ─────────────────────────────────────────────────────────────────────────────
//  Se deja vacío a propósito: el calendario por omisión depende de la cuenta con la
//  que se abrió Apps Script, y con la cuenta equivocada este script no encontraría
//  nada (o peor, movería los eventos de otro calendario). Ejecuta listarCalendarios()
//  y pega abajo el ID del mismo calendario donde creaste los encuentros.
var CALENDAR_ID = '';

//  En true NO cambia nada: solo escribe en el registro lo que haría. Ponlo en false
//  cuando el registro diga lo que esperas.
var SIMULAR = true;

// ─────────────────────────────────────────────────────────────────────────────
//  2. QUÉ SE MUEVE
// ─────────────────────────────────────────────────────────────────────────────
//  Los nombres tal como aparecen DENTRO del título del evento. Los títulos son
//  «[SINCRONICO] 341C - Programación II - Sesión 3», así que basta el nombre del curso.
//  OJO con las tildes: van como están en el calendario.
var CURSOS = ['Programación II', 'Seminario de Sistemas'];

var HORA_ACTUAL = '18:00';   // la que tienen hoy
var HORA_NUEVA  = '18:30';   // la que deben tener
var HORA_FIN    = '20:00';   // el fin no se cambia; se exige para no tocar otra cosa

//  Ventana de búsqueda. Cubre el periodo 2026-2 con margen por los dos lados.
var DESDE = '2026-08-01';
var HASTA = '2027-01-15';

//  Zona del proyecto. Si no coincide, las horas que construye el script no son las que
//  ve el docente y el ajuste entraría corrido: por eso bloquea en vez de seguir.
var TZ = 'America/Bogota';


// ─────────────────────────────────────────────────────────────── funciones públicas

/** Imprime los calendarios visibles con su ID, para llenar CALENDAR_ID. */
function listarCalendarios() {
  var cals = CalendarApp.getAllCalendars();
  Logger.log('Calendarios visibles con esta cuenta (' + cals.length + '):');
  for (var i = 0; i < cals.length; i++) {
    Logger.log('  ' + cals[i].getName() + '  ->  ' + cals[i].getId());
  }
  Logger.log('Pega arriba, en CALENDAR_ID, el ID del calendario donde creaste los encuentros.');
}


/**
 * Informe de solo lectura: qué hay, qué se movería y qué se va a dejar quieto.
 * No modifica nada, así que se puede ejecutar antes y después sin riesgo.
 */
function verificar() {
  if (!_zonaCorrecta_()) {
    Logger.log('AVISO: la zona del proyecto es ' + _zonaDelProyecto_() + ' y deberia ser ' +
               TZ + '. Las horas de abajo pueden no ser las que ves en el calendario.');
  }
  var enc = _encontrar_();
  Logger.log('== Verificacion · ' + CURSOS.join(' + '));
  Logger.log('   ventana ' + DESDE + ' a ' + HASTA + ' · calendario ' +
             (CALENDAR_ID || '(sin CALENDAR_ID: fallara)'));
  Logger.log('');
  Logger.log('   eventos de estos cursos encontrados : ' + enc.todos.length);
  Logger.log('   ya en ' + HORA_NUEVA + '-' + HORA_FIN + ' (nada que hacer): ' + enc.hechos.length);
  Logger.log('   en ' + HORA_ACTUAL + '-' + HORA_FIN + ' (se moverian)      : ' + enc.mover.length);
  Logger.log('   con otro horario (NO se tocan)      : ' + enc.otros.length);

  if (enc.mover.length) {
    Logger.log('');
    Logger.log('   Se moverian estos:');
    for (var i = 0; i < enc.mover.length; i++) {
      Logger.log('     ' + _describir_(enc.mover[i]));
    }
  }
  if (enc.otros.length) {
    Logger.log('');
    Logger.log('   OJO, estos NO encajan en ' + HORA_ACTUAL + '-' + HORA_FIN +
               ' y se quedan como estan. Revisa si es lo que esperas:');
    for (var j = 0; j < enc.otros.length; j++) {
      Logger.log('     ' + _describir_(enc.otros[j]));
    }
  }
  if (!enc.todos.length) {
    Logger.log('');
    Logger.log('   No encontre NINGUN evento de estos cursos. Tres causas posibles:');
    Logger.log('     - CALENDAR_ID apunta a otro calendario;');
    Logger.log('     - los titulos no llevan el nombre del curso como esta en CURSOS');
    Logger.log('       (mira las tildes: «Programación II», no «Programacion II»);');
    Logger.log('     - las fechas caen fuera de la ventana DESDE/HASTA.');
  }
  Logger.log('');
  Logger.log('   Cuantos conservan su sala de Meet: ' + _conMeet_(enc.todos) + ' de ' +
             enc.todos.length + '. Este script NO las toca.');
  return enc;
}


/** Mueve el inicio de HORA_ACTUAL a HORA_NUEVA. Respeta SIMULAR. */
function ajustarHoraInicio() {
  _mover_(HORA_ACTUAL, HORA_NUEVA, 'ajustarHoraInicio');
}


/** Deshace el ajuste: devuelve el inicio de HORA_NUEVA a HORA_ACTUAL. */
function revertir() {
  _mover_(HORA_NUEVA, HORA_ACTUAL, 'revertir');
}


// ─────────────────────────────────────────────────────────────── motor

function _mover_(desde, hasta, quien) {
  if (_zonaMal_(quien)) return;
  var cal = _cal_();
  var enc = _encontrar_();
  var lista = (desde === HORA_ACTUAL) ? enc.mover : enc.hechos;

  Logger.log('== ' + quien + ' · ' + desde + ' -> ' + hasta + ' (fin ' + HORA_FIN + ' sin cambio)');
  if (!lista.length) {
    Logger.log('   No hay eventos en ' + desde + '-' + HORA_FIN + '. Nada que mover.');
    Logger.log('   Ejecuta verificar() para ver que hay en el calendario.');
    return;
  }
  if (SIMULAR) {
    Logger.log('   SIMULAR = true: no se cambio nada. Se moverian ' + lista.length + ':');
    for (var i = 0; i < lista.length; i++) Logger.log('     ' + _describir_(lista[i]));
    Logger.log('   Pon SIMULAR = false para aplicarlo.');
    return;
  }

  var hechos = 0, fallos = 0;
  for (var k = 0; k < lista.length; k++) {
    var ev = lista[k];
    var ini = _mismoDiaA_(ev.getStartTime(), hasta);
    var fin = ev.getEndTime();           // el fin se conserva tal cual
    try {
      ev.setTime(ini, fin);              // conserva la sala de Meet: es el mismo evento
      hechos++;
      Logger.log('   movido: ' + _describir_(ev));
    } catch (e) {
      fallos++;
      Logger.log('   FALLO en «' + ev.getTitle() + '»: ' + e);
    }
  }
  Logger.log('');
  Logger.log('   movidos: ' + hechos + ' · fallos: ' + fallos);
  Logger.log('   Nadie recibio ningun correo: estos eventos no tienen invitados.');
  Logger.log('   Ejecuta verificar() para confirmar.');
}


/** Clasifica los eventos de los cursos en {todos, mover, hechos, otros}. */
function _encontrar_() {
  var cal = _cal_();
  var todos = cal.getEvents(_fecha_(DESDE, '00:01'), _fecha_(HASTA, '23:59'));
  var out = { todos: [], mover: [], hechos: [], otros: [] };
  for (var i = 0; i < todos.length; i++) {
    var ev = todos[i];
    if (!_esDeLosCursos_(ev.getTitle())) continue;
    if (ev.isAllDayEvent()) continue;              // un dia completo no tiene hora que mover
    out.todos.push(ev);
    var ini = _hhmm_(ev.getStartTime());
    var fin = _hhmm_(ev.getEndTime());
    if (ini === HORA_ACTUAL && fin === HORA_FIN) out.mover.push(ev);
    else if (ini === HORA_NUEVA && fin === HORA_FIN) out.hechos.push(ev);
    else out.otros.push(ev);
  }
  return out;
}


function _esDeLosCursos_(titulo) {
  var t = String(titulo || '').toLowerCase();
  for (var i = 0; i < CURSOS.length; i++) {
    if (t.indexOf(String(CURSOS[i]).toLowerCase()) !== -1) return true;
  }
  return false;
}


/** Misma fecha del evento, con la hora `hhmm`. Evita recalcular la fecha a mano. */
function _mismoDiaA_(fecha, hhmm) {
  var h = String(hhmm).split(':');
  return new Date(fecha.getFullYear(), fecha.getMonth(), fecha.getDate(),
                  +h[0], +h[1], 0, 0);
}


function _fecha_(fechaIso, hhmm) {
  var p = String(fechaIso).split('-'), h = String(hhmm).split(':');
  return new Date(+p[0], +p[1] - 1, +p[2], +h[0], +h[1], 0);
}


function _hhmm_(d) {
  var h = d.getHours(), m = d.getMinutes();
  return (h < 10 ? '0' + h : h) + ':' + (m < 10 ? '0' + m : m);
}


function _describir_(ev) {
  var d = ev.getStartTime();
  var dia = ('0' + d.getDate()).slice(-2) + '/' + ('0' + (d.getMonth() + 1)).slice(-2) +
            '/' + d.getFullYear();
  return dia + '  ' + _hhmm_(ev.getStartTime()) + '-' + _hhmm_(ev.getEndTime()) + '  ' +
         ev.getTitle();
}


/** Cuantos de la lista conservan enlace de Meet, para poder decir que no se perdio. */
function _conMeet_(lista) {
  var n = 0;
  for (var i = 0; i < lista.length; i++) {
    var txt = (lista[i].getLocation() || '') + ' ' + (lista[i].getDescription() || '');
    if (txt.indexOf('meet.google.com') !== -1) n++;
  }
  return n;
}


function _cal_() {
  if (CALENDAR_ID) {
    var c = CalendarApp.getCalendarById(CALENDAR_ID);
    if (!c) throw new Error('CALENDAR_ID no corresponde a un calendario visible: ' + CALENDAR_ID);
    return c;
  }
  throw new Error('Falta CALENDAR_ID. Ejecuta listarCalendarios() y pega el ID arriba.');
}


function _zonaDelProyecto_() {
  return Session.getScriptTimeZone();
}


function _zonaCorrecta_() {
  return _zonaDelProyecto_() === TZ;
}


/**
 * Bloquea si la zona del proyecto no es TZ. No es paranoia: este script construye la
 * hora nueva con `new Date(...)`, que usa la zona del PROYECTO. Con el proyecto en UTC,
 * «18:30» serian las 13:30 en Bogota y los 26 eventos quedarian corridos cinco horas.
 */
function _zonaMal_(quien) {
  if (_zonaCorrecta_()) return false;
  Logger.log('BLOQUEADO: ' + quien + ' no corre con la zona del proyecto en ' +
             _zonaDelProyecto_() + '.');
  Logger.log('Ponla en ' + TZ + ': Configuracion del proyecto (engranaje) -> Zona horaria.');
  return true;
}
