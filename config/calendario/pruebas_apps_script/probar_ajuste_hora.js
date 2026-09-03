/**
 * Pruebas de `AjustarHoraInicio.gs` contra el simulacro de las APIs de Google.
 *
 * Por qué existen: el script mueve la hora de 26 eventos reales que ya tienen su sala de
 * Meet compartida con el grupo. Un error ahí no se deshace con «volver a ejecutar»: o
 * movió lo que no debía, o dejó los eventos corridos. Lo que se comprueba es justo lo que
 * no se puede comprobar leyendo:
 *
 *   - mueve SOLO los dos cursos, y solo los de 18:00-20:00;
 *   - no toca Bases de Datos II ni Arquitectura ni los apuntes personales del docente,
 *     aunque caigan a la misma hora;
 *   - conserva la sala de Meet (no borra ni recrea: `deleteEvent` nunca se llama);
 *   - no invita ni notifica a nadie;
 *   - `SIMULAR = true` no cambia nada;
 *   - `revertir()` deja el calendario como estaba;
 *   - es idempotente: ejecutarlo dos veces no mueve nada la segunda;
 *   - con la zona del proyecto equivocada se BLOQUEA en vez de correr los eventos.
 *
 * Uso:  node probar_ajuste_hora.js [ruta al .gs]
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { construir } = require('./google-mock');

const GS = process.argv[2] ||
  path.join(__dirname, '..', 'apps_script_ajustes', 'AjustarHoraInicio.gs');

let ok = 0, mal = 0;
function afirmar(nombre, cond, detalle) {
  if (cond) { ok++; console.log('  OK   ' + nombre); }
  else { mal++; console.log('  MAL  ' + nombre + (detalle ? '  -> ' + detalle : '')); }
}

/** Carga el .gs en un contexto nuevo con el simulacro inyectado. */
function cargar(opciones) {
  const fuente = fs.readFileSync(GS, 'utf8');
  const m = construir(opciones || {});
  const ctx = vm.createContext(m.sandbox);
  vm.runInContext(fuente, ctx, { filename: GS });
  ctx.CALENDAR_ID = m.cal.getId();
  ctx.SIMULAR = false;
  return { ctx, cal: m.cal, log: m.log };
}

const D = (m, d, hh, mm) => new Date(2026, m - 1, d, hh, mm, 0);

/** Planta el calendario tal como está hoy: 13 sesiones de cada curso a las 18:00. */
function sembrar(cal) {
  const puestos = { prog: [], sem: [], ajenos: [] };
  for (let i = 1; i <= 13; i++) {
    const dia = 2 + i * 7;                       // miercoles sucesivos de septiembre en adelante
    const e1 = cal.plantar('[SINCRONICO] 341C - Programación II - Sesión ' + i,
      D(9, dia, 18, 0), D(9, dia, 20, 0));
    e1.setLocation('https://meet.google.com/prog-' + i);
    puestos.prog.push(e1);
    const e2 = cal.plantar('[SINCRONICO] 341C - Seminario de Sistemas - Sesión ' + i,
      D(9, dia + 1, 18, 0), D(9, dia + 1, 20, 0));
    e2.setLocation('https://meet.google.com/sem-' + i);
    puestos.sem.push(e2);
  }
  // Lo que NO se debe tocar, a la misma hora y con nombres parecidos
  puestos.ajenos.push(cal.plantar('[SINCRONICO] 641A-2 - Bases de Datos II - Sesión 4',
    D(9, 21, 18, 0), D(9, 21, 20, 0)));
  puestos.ajenos.push(cal.plantar('[SINCRONICO] 6303C - Arquitectura de Sistemas Computacionales - Sesión 4',
    D(9, 21, 10, 0), D(9, 21, 12, 0)));
  puestos.ajenos.push(cal.plantar('Cita medica', D(9, 23, 18, 0), D(9, 23, 20, 0)));
  puestos.ajenos.push(cal.plantar('Reunion de padres', D(9, 24, 18, 0), D(9, 24, 19, 0),
    ['alguien@ejemplo.com']));
  return puestos;
}

const hhmm = (d) => ('0' + d.getHours()).slice(-2) + ':' + ('0' + d.getMinutes()).slice(-2);

console.log('=== 1. verificar() clasifica sin cambiar nada ===');
{
  const h = cargar();
  const p = sembrar(h.cal);
  const antes = h.cal.eventos.map((e) => hhmm(e.start) + hhmm(e.end)).join('|');
  const enc = h.ctx.verificar();
  afirmar('encuentra los 26 eventos de los dos cursos', enc.todos.length === 26,
          String(enc.todos.length));
  afirmar('los 26 estan en la lista de «se moverian»', enc.mover.length === 26,
          String(enc.mover.length));
  afirmar('ninguno cuenta como ya hecho', enc.hechos.length === 0);
  afirmar('ninguno queda en «otro horario»', enc.otros.length === 0);
  afirmar('verificar() no escribio nada', h.cal.escrituras === 0 + p.prog.length + p.sem.length,
          'escrituras=' + h.cal.escrituras);   // solo los setLocation de la siembra
  afirmar('verificar() no cambio ninguna hora',
          h.cal.eventos.map((e) => hhmm(e.start) + hhmm(e.end)).join('|') === antes);
}

console.log('\n=== 2. SIMULAR = true no toca nada ===');
{
  const h = cargar();
  const p = sembrar(h.cal);
  h.ctx.SIMULAR = true;
  h.ctx.ajustarHoraInicio();
  afirmar('no llamo a setTime', h.cal.setTimeLlamado === 0, String(h.cal.setTimeLlamado));
  // Se comprueban los 26 de los dos cursos, no «cuantos hay a las 18:00» en todo el
  // calendario: la siembra pone ademas tres eventos ajenos a esa hora, y contarlos juntos
  // solo invita a equivocarse con la aritmetica.
  afirmar('los 26 de los dos cursos siguen a las 18:00',
          p.prog.concat(p.sem).every((e) => hhmm(e.start) === '18:00'),
          p.prog.concat(p.sem).map((e) => hhmm(e.start)).join(','));
  afirmar('el registro dice que simulo', h.log.some((l) => /SIMULAR = true/.test(l)));
}

console.log('\n=== 3. El ajuste mueve solo lo que debe ===');
{
  const h = cargar();
  const p = sembrar(h.cal);
  h.ctx.ajustarHoraInicio();
  const dosCursos = p.prog.concat(p.sem);
  afirmar('los 26 quedaron 18:30-20:00',
          dosCursos.every((e) => hhmm(e.start) === '18:30' && hhmm(e.end) === '20:00'),
          dosCursos.map((e) => hhmm(e.start)).join(','));
  afirmar('setTime se llamo 26 veces', h.cal.setTimeLlamado === 26, String(h.cal.setTimeLlamado));
  afirmar('Bases de Datos II sigue 18:00-20:00',
          hhmm(p.ajenos[0].start) === '18:00' && hhmm(p.ajenos[0].end) === '20:00');
  afirmar('Arquitectura sigue 10:00-12:00', hhmm(p.ajenos[1].start) === '10:00');
  afirmar('la cita medica del docente sigue 18:00', hhmm(p.ajenos[2].start) === '18:00');
  afirmar('la reunion con invitados no se toco', hhmm(p.ajenos[3].start) === '18:00');
  // lo que hace que valga la pena no recrear
  afirmar('no borro ni recreo ningun evento', h.cal.borrados.length === 0);
  afirmar('los 26 conservan su enlace de Meet',
          dosCursos.every((e) => /meet\.google\.com/.test(e.getLocation())));
  afirmar('nadie recibio invitacion ni notificacion',
          h.cal.addGuestLlamado === 0 &&
          h.cal.eventos.every((e) => e.invitacionesEnviadas === 0 && e.notificacionesDeUpdate === 0));
}

console.log('\n=== 4. Es idempotente: la segunda vez no mueve nada ===');
{
  const h = cargar();
  sembrar(h.cal);
  h.ctx.ajustarHoraInicio();
  const primera = h.cal.setTimeLlamado;
  h.ctx.ajustarHoraInicio();
  afirmar('la segunda pasada no llama a setTime', h.cal.setTimeLlamado === primera,
          primera + ' -> ' + h.cal.setTimeLlamado);
  const enc = h.ctx.verificar();
  afirmar('verificar() los ve como ya hechos', enc.hechos.length === 26 && enc.mover.length === 0,
          'hechos=' + enc.hechos.length + ' mover=' + enc.mover.length);
}

console.log('\n=== 5. revertir() deja el calendario como estaba ===');
{
  const h = cargar();
  const p = sembrar(h.cal);
  h.ctx.ajustarHoraInicio();
  h.ctx.revertir();
  afirmar('vuelven a 18:00-20:00',
          p.prog.concat(p.sem).every((e) => hhmm(e.start) === '18:00' && hhmm(e.end) === '20:00'));
  afirmar('sigue sin borrar nada', h.cal.borrados.length === 0);
}

console.log('\n=== 6. Un evento con otro horario se reporta y NO se toca ===');
{
  const h = cargar();
  sembrar(h.cal);
  const raro = h.cal.plantar('[SINCRONICO] 341C - Programación II - Sesión 14 (reprogramada)',
    D(10, 7, 15, 0), D(10, 7, 17, 0));
  const enc = h.ctx.verificar();
  afirmar('lo clasifica como «otro horario»', enc.otros.length === 1 &&
          enc.otros[0] === raro, 'otros=' + enc.otros.length);
  afirmar('lo nombra en el registro', h.log.some((l) => /reprogramada/.test(l)));
  h.ctx.ajustarHoraInicio();
  afirmar('el ajuste no lo movio', hhmm(raro.start) === '15:00');
}

console.log('\n=== 7. Con la zona del proyecto mal, se BLOQUEA ===');
{
  const h = cargar({ zona: 'UTC' });
  const p = sembrar(h.cal);
  h.ctx.ajustarHoraInicio();
  afirmar('no movio nada', h.cal.setTimeLlamado === 0, String(h.cal.setTimeLlamado));
  afirmar('los eventos siguen a las 18:00', hhmm(p.prog[0].start) === '18:00');
  afirmar('el registro dice BLOQUEADO', h.log.some((l) => /BLOQUEADO/.test(l)));
  afirmar('dice cual es la zona esperada', h.log.some((l) => /America\/Bogota/.test(l)));
}

console.log('\n=== 8. Sin CALENDAR_ID falla con un mensaje util ===');
{
  const h = cargar();
  sembrar(h.cal);
  h.ctx.CALENDAR_ID = '';
  let msg = '';
  try { h.ctx.verificar(); } catch (e) { msg = String(e.message || e); }
  afirmar('lanza error', !!msg, msg);
  afirmar('el mensaje dice que ejecute listarCalendarios',
          /listarCalendarios/.test(msg), msg);
}

console.log('\n=== 9. Si Google falla en un evento, sigue con los demas ===');
{
  const h = cargar();
  const p = sembrar(h.cal);
  h.cal.fallarSetTime = true;
  h.ctx.ajustarHoraInicio();
  afirmar('reporta los fallos', h.log.some((l) => /FALLO en/.test(l)));
  afirmar('cuenta 26 fallos y 0 movidos', h.log.some((l) => /movidos: 0 · fallos: 26/.test(l)),
          h.log.filter((l) => /movidos:/.test(l)).join(' | '));
  afirmar('no dejo ninguno a medias', p.prog.every((e) => hhmm(e.start) === '18:00'));
}

console.log('\n' + '─'.repeat(41));
console.log('ok=' + ok + '  mal=' + mal);
process.exit(mal ? 1 : 0);
