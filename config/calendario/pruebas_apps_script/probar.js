'use strict';
/**
 * Ejecuta de verdad el .gs consolidado contra el simulacro de Google y comprueba lo que
 * el script promete: que no duplica, que sincroniza invitados, que el borrado no se lleva
 * eventos ajenos, que los interruptores frenan, y que cortarse por tiempo no pierde nada.
 */
const fs = require('fs');
const vm = require('vm');
const { construir } = require('./google-mock');

const GS = process.argv[2];
if (!GS) { console.error('uso: node probar.js <ruta al .gs>'); process.exit(2); }
const FUENTE = fs.readFileSync(GS, 'utf8');

let ok = 0, mal = 0;
const fallos = [];

function afirmar(nombre, cond, detalle) {
  if (cond) { ok++; console.log('  OK   ' + nombre); }
  else { mal++; fallos.push(nombre + (detalle ? '  -> ' + detalle : '')); console.log('  MAL  ' + nombre + (detalle ? '  -> ' + detalle : '')); }
}

/** Carga el .gs en un sandbox nuevo y devuelve {ctx, cal, log, ...}. */
function cargar(opciones) {
  const m = construir(opciones);
  const ctx = vm.createContext(m.sandbox);
  vm.runInContext(FUENTE, ctx, { filename: GS });
  ctx.CALENDAR_ID = m.cal.getId();
  ctx.SIMULAR = true;
  return Object.assign(m, { ctx });
}

function vivos(cal) { return cal.eventos.length; }
function conMeet(cal) { return cal.eventos.filter((e) => e.conferenceData).length; }
function invitacionesTotales(cal) {
  return cal.eventos.concat(cal.borrados).reduce((a, e) => a + e.invitacionesEnviadas, 0);
}

console.log('\n=== 1. Datos cargados ===');
{
  const { ctx } = cargar();
  const cursos = ctx.CURSOS;
  afirmar('4 cursos', cursos.length === 4, 'hay ' + cursos.length);
  afirmar('13 sesiones por curso', cursos.every((c) => c.sesiones.length === 13),
          cursos.map((c) => c.sesiones.length).join(','));
  const sinMeet = cursos.reduce((a, c) => a + c.sesiones.filter((s) => !s.meet).length, 0);
  afirmar('4 sesiones autonomas en total (sin Meet)', sinMeet === 4, 'hay ' + sinMeet);
  afirmar('titulo coherente con meet',
          cursos.every((c) => c.sesiones.every((s) =>
            s.meet ? s.subject.indexOf('[SINCRONICO]') === 0 : s.subject.indexOf('[AUTONOMO]') === 0)));
  afirmar('requestId distinto por curso',
          new Set(cursos.map((c) => c.requestId)).size === 4);
  afirmar('sin invitados duplicados dentro de un curso',
          cursos.every((c) => new Set(c.invitados.map((x) => x.toLowerCase())).size === c.invitados.length));
  afirmar('SIMULAR arranca en true', /var SIMULAR = true;/.test(FUENTE));
  afirmar('CONFIRMO_SEMESTRE_COMPLETO arranca en false', /var CONFIRMO_SEMESTRE_COMPLETO = false;/.test(FUENTE));
}

console.log('\n=== 2. SIMULAR frena todo ===');
{
  const h = cargar();
  h.ctx.verificarTodosLosCursos();
  h.ctx.crearTodosLosCursos();
  h.ctx.eliminarTodosLosCursos();
  h.ctx.recrearTodosLosCursos();
  afirmar('en simulacion no se creo ni un evento', vivos(h.cal) === 0, vivos(h.cal) + ' eventos');
  afirmar('en simulacion no se escribio nada', h.cal.escrituras === 0);
  afirmar('verificar dice cuantas sesiones', h.log.some((l) => /TOTAL 4 curso\(s\) · 52 sesion/.test(l)));
}

console.log('\n=== 3. El segundo interruptor bloquea ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;                  // real, pero sin confirmar
  h.ctx.crearTodosLosCursos();
  afirmar('crearTodosLosCursos bloqueado sin confirmar', vivos(h.cal) === 0, vivos(h.cal) + ' eventos');
  afirmar('el log explica como desbloquear',
          h.log.some((l) => /CONFIRMO_SEMESTRE_COMPLETO = true/.test(l)));
  h.ctx.eliminarTodosLosCursos();
  h.ctx.recrearTodosLosCursos();
  afirmar('eliminar y recrear tambien bloqueados', vivos(h.cal) === 0 && h.cal.borrados.length === 0);

  // Un solo curso NO necesita el segundo interruptor.
  h.ctx.crearBasesDatosII();
  afirmar('un curso suelto si corre sin el segundo interruptor', vivos(h.cal) === 13,
          vivos(h.cal) + ' eventos');
}

console.log('\n=== 4. Creacion completa y sala por sesion ===');
let baseline;
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearTodosLosCursos();
  baseline = h;
  afirmar('52 eventos creados', vivos(h.cal) === 52, vivos(h.cal) + '');
  afirmar('48 con sala de Meet (52 - 4 autonomas)', conMeet(h.cal) === 48, conMeet(h.cal) + '');
  const urls = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri);
  afirmar('48 enlaces de Meet DISTINTOS', new Set(urls).size === 48, new Set(urls).size + ' distintos');
  afirmar('las autonomas quedan en el calendario sin Meet',
          h.cal.eventos.filter((e) => !e.conferenceData).length === 4);
  afirmar('las autonomas no tienen enlace en Ubicacion',
          h.cal.eventos.filter((e) => !e.conferenceData).every((e) => e.location === ''));
  afirmar('el enlace queda tambien en Ubicacion',
          h.cal.eventos.filter((e) => e.conferenceData)
            .every((e) => e.location === e.conferenceData.entryPoints[0].uri));
  afirmar('el enlace queda en la descripcion',
          h.cal.eventos.filter((e) => e.conferenceData)
            .every((e) => e.description.indexOf(e.conferenceData.entryPoints[0].uri) !== -1));
  afirmar('invitaciones enviadas al crear', invitacionesTotales(h.cal) === 52 * 0 + h.cal.eventos.reduce((a, e) => a + e.guests.length, 0),
          invitacionesTotales(h.cal) + ' invitaciones');
  afirmar('cada evento lleva los invitados de SU curso',
          h.ctx.CURSOS.every((c) => c.sesiones.every((s) => {
            const e = h.cal.eventos.find((x) => x.title === s.subject);
            return e && e.guests.length === c.invitados.length;
          })));
}

console.log('\n=== 5. Reejecutar no duplica ===');
{
  const h = baseline;
  const antesEventos = vivos(h.cal), antesInv = invitacionesTotales(h.cal);
  const antesUrls = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri).sort().join('|');
  h.log.length = 0;
  h.ctx.crearTodosLosCursos();
  afirmar('sigue habiendo 52 eventos', vivos(h.cal) === antesEventos, vivos(h.cal) + '');
  afirmar('no se enviaron invitaciones nuevas', invitacionesTotales(h.cal) === antesInv,
          (invitacionesTotales(h.cal) - antesInv) + ' de mas');
  const ahoraUrls = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri).sort().join('|');
  afirmar('los enlaces de Meet NO cambiaron', ahoraUrls === antesUrls);
  afirmar('el log dice que reutilizo', h.log.some((l) => /52 reutilizado|reutilizado\(s\)/.test(l)));
}

console.log('\n=== 6. Nomina nueva: sincroniza invitados ===');
{
  const h = baseline;
  const c = h.ctx.CURSOS[0];
  const antes = c.invitados.length;
  c.invitados.push('nuevo.estudiante@estudiante.uniajc.edu.co');
  h.log.length = 0;
  h.ctx.crearTodosLosCursos();
  const conNuevo = h.cal.eventos.filter((e) =>
    e.guests.some((g) => g.getEmail() === 'nuevo.estudiante@estudiante.uniajc.edu.co')).length;
  afirmar('el estudiante nuevo entra en las 13 sesiones de su curso', conNuevo === 13, conNuevo + '');
  afirmar('no se creo ningun evento por eso', vivos(h.cal) === 52);
  afirmar('el log reporta los invitados agregados',
          h.log.some((l) => /13 invitado\(s\) agregado|agregados a eventos que ya existian: 13/.test(l)));
  // Y si se reejecuta otra vez, no lo agrega dos veces.
  h.ctx.crearTodosLosCursos();
  const dobles = h.cal.eventos.filter((e) =>
    e.guests.filter((g) => g.getEmail() === 'nuevo.estudiante@estudiante.uniajc.edu.co').length > 1).length;
  afirmar('no lo invita dos veces', dobles === 0, dobles + ' eventos con duplicado');
  c.invitados.length = antes;
}

console.log('\n=== 7. Un estudiante retirado NO se va solo ===');
{
  const h = baseline;
  const c = h.ctx.CURSOS[0];
  const retirado = c.invitados.pop();
  const antesDeQuitar = h.cal.eventos.filter((e) => e.guests.some((g) => g.getEmail() === retirado)).length;
  h.ctx.crearTodosLosCursos();
  const sigue = h.cal.eventos.filter((e) => e.guests.some((g) => g.getEmail() === retirado)).length;
  afirmar('el retirado sigue invitado (limitacion conocida, documentada en el manual)',
          sigue === antesDeQuitar && sigue > 0, sigue + ' de ' + antesDeQuitar + ' eventos');
  // De paso: Prog II y Seminario son el mismo grupo (341C), asi que hay estudiantes en los dos.
  const enDos = h.ctx.CURSOS[0].invitados.filter((x) => h.ctx.CURSOS[1].invitados.indexOf(x) !== -1);
  console.log('       (nota: ' + enDos.length + ' estudiantes estan en Programacion II y Seminario)');
  c.invitados.push(retirado);
}

console.log('\n=== 8. Borrado de un curso: no toca al otro del mismo dia ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearTodosLosCursos();
  const arq = h.ctx.CURSOS.find((c) => c.key === 'arquitectura');
  const bd = h.ctx.CURSOS.find((c) => c.key === 'bases_datos_ii');
  const lunesCompartidos = arq.sesiones.filter((s) => bd.sesiones.some((t) => t.fecha === s.fecha));
  afirmar('Arquitectura y BD II comparten fechas (el caso peligroso)', lunesCompartidos.length > 0,
          lunesCompartidos.length + ' fechas');
  const antesArq = h.cal.eventos.filter((e) => e.title.indexOf('Arquitectura') !== -1).length;
  h.ctx.eliminarBasesDatosII();
  const quedanArq = h.cal.eventos.filter((e) => e.title.indexOf('Arquitectura') !== -1).length;
  const quedanBd = h.cal.eventos.filter((e) => e.title.indexOf('Bases de Datos II') !== -1).length;
  afirmar('borro las 13 de BD II', quedanBd === 0, quedanBd + ' vivas');
  afirmar('no toco las de Arquitectura', quedanArq === antesArq, quedanArq + ' de ' + antesArq);
  afirmar('mando cancelaciones a los invitados de BD II',
          h.cal.borrados.every((e) => e.cancelacionEnviada));
}

console.log('\n=== 9. El barrido caza titulos viejos... y tambien eventos personales ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearBasesDatosII();
  const bd = h.ctx.CURSOS.find((c) => c.key === 'bases_datos_ii');
  const f = bd.sesiones[0].fecha.split('-').map(Number);
  // (a) un evento de una corrida anterior, con el titulo viejo (sin el prefijo nuevo)
  const viejo = h.cal.eventos.find((e) => e.title === bd.sesiones[3].subject);
  viejo.title = 'Sesion 4 · Bases de Datos II';       // como se llamaba antes
  // (b) un evento PERSONAL del docente que menciona el curso
  const personal = h.cal.plantar('Preparar quiz de Bases de Datos II',
    new Date(f[0], f[1] - 1, f[2], 8, 0), new Date(f[0], f[1] - 1, f[2], 9, 0), []);
  // (c) un evento ajeno que no menciona el curso
  const ajeno = h.cal.plantar('Reunion de area',
    new Date(f[0], f[1] - 1, f[2], 7, 0), new Date(f[0], f[1] - 1, f[2], 8, 0), []);

  h.ctx.SIMULAR = true;
  h.log.length = 0;
  h.ctx.eliminarBasesDatosII();
  const listados = h.log.filter((l) => /huerfano:/.test(l));
  afirmar('en simulacion LISTA el huerfano antes de borrar', listados.length === 1,
          listados.length + ' listados');
  afirmar('el titulo viejo aparece en la lista', listados.some((l) => /Sesion 4 · Bases de Datos II/.test(l)));
  afirmar('el evento PERSONAL no entra en la lista', !listados.some((l) => /Preparar quiz/.test(l)));

  h.ctx.SIMULAR = false;
  h.ctx.eliminarBasesDatosII();
  afirmar('borro el evento con titulo viejo', !h.cal.eventos.includes(viejo));
  afirmar('NO borro el evento personal del docente', h.cal.eventos.includes(personal));
  afirmar('no toco el evento ajeno', h.cal.eventos.includes(ajeno));
}

console.log('\n=== 10. Recrear: enlaces nuevos, eventos nuevos ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearSeminario();
  const antes = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri).sort().join('|');
  h.ctx.recrearSeminario();
  afirmar('vuelve a haber 13 eventos', vivos(h.cal) === 13, vivos(h.cal) + '');
  const despues = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri).sort().join('|');
  afirmar('los eventos son otros (se borraron y recrearon)', h.cal.borrados.length === 13,
          h.cal.borrados.length + ' borrados');
  afirmar('el requestId es el mismo, asi que Google devuelve la MISMA sala',
          despues === antes, 'antes!=despues');
}

console.log('\n=== 11. Corte por tiempo: no pierde nada ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.MINUTOS_MAX = -1;                 // el reloj vence de inmediato
  h.ctx.crearTodosLosCursos();
  afirmar('con el plazo vencido no crea nada', vivos(h.cal) === 0, vivos(h.cal) + '');
  afirmar('avisa del corte', h.log.some((l) => /CORTADO a los/.test(l)));
  h.ctx.MINUTOS_MAX = 25;
  h.ctx.crearTodosLosCursos();
  afirmar('al reejecutar con plazo normal completa las 52', vivos(h.cal) === 52, vivos(h.cal) + '');
}

console.log('\n=== 12. Sin servicio avanzado de Calendar ===');
{
  const h = cargar({ sinServicioAvanzado: true });
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearTodosLosCursos();
  afirmar('crea los 52 eventos igual', vivos(h.cal) === 52, vivos(h.cal) + '');
  afirmar('ninguno con Meet', conMeet(h.cal) === 0);
  afirmar('lo dice en el log', h.log.some((l) => /servicio avanzado/i.test(l)));
}

console.log('\n=== 13. Sala de Meet "pending" ===');
{
  const h = cargar({ meetPendiente: 3 });
  h.ctx.SIMULAR = false;
  h.ctx.crearArquitectura();
  const arq = h.ctx.CURSOS.find((c) => c.key === 'arquitectura');
  const esperadas = arq.sesiones.filter((s) => s.meet).length;
  afirmar('aun con respuestas "pending" acaba con todas las salas',
          conMeet(h.cal) === esperadas, conMeet(h.cal) + ' de ' + esperadas);
}

console.log('\n=== 14. Si `search` de Calendar no encuentra (riesgo de duplicar) ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearSeminario();
  afirmar('primera corrida: 13 eventos', vivos(h.cal) === 13, vivos(h.cal) + '');
  h.cal.searchInutil = true;              // Google deja de indexar los titulos
  h.ctx.crearSeminario();
  afirmar('aunque `search` no sirva, NO duplica (ya no depende de search)', vivos(h.cal) === 13,
          vivos(h.cal) + ' eventos (deberian ser 13)');
  afirmar('el .gs ya no pasa `search` a getEvents', !/search: s\.subject/.test(FUENTE));
}

console.log('\n=== 15. deleteEvent que falla ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearSeminario();
  h.cal.fallarDelete = true;
  h.log.length = 0;
  h.ctx.eliminarSeminario();
  afirmar('no revienta', true);
  afirmar('reporta Eliminados=0, no exito falso',
          h.log.some((l) => /Eliminados=0/.test(l)),
          h.log.filter((l) => /Eliminados/.test(l)).join(' / '));
  afirmar('avisa de cada fallo', h.log.filter((l) => /no pude borrar/.test(l)).length === 13);
}

console.log('\n=== 16. addGuest que falla (cuota) ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearSeminario();
  const c = h.ctx.CURSOS.find((x) => x.key === 'seminario');
  c.invitados.push('otro.nuevo@estudiante.uniajc.edu.co');
  h.cal.fallarAddGuest = true;
  h.log.length = 0;
  h.ctx.crearSeminario();
  afirmar('no revienta con la cuota agotada', true);
  afirmar('avisa del fallo', h.log.some((l) => /no pude invitar/.test(l)));
  afirmar('NO cuenta como invitado agregado lo que fallo',
          !h.log.some((l) => /agregados a eventos que ya existian: 13/.test(l)),
          h.log.filter((l) => /agregados/.test(l)).join(' / '));
}

console.log('\n=== 17. CALENDAR_ID vacio o equivocado ===');
{
  const h = cargar();
  h.ctx.CALENDAR_ID = '';
  let reventó = false;
  try { h.ctx.verificarTodosLosCursos(); } catch (e) { reventó = /Falta CALENDAR_ID/.test(String(e)); }
  afirmar('sin CALENDAR_ID revienta con mensaje util', reventó);
  h.ctx.CALENDAR_ID = 'noexiste@group.calendar.google.com';
  let reventó2 = false;
  try { h.ctx.verificarTodosLosCursos(); } catch (e) { reventó2 = /no corresponde a un calendario/.test(String(e)); }
  afirmar('con un ID inexistente revienta con mensaje util', reventó2);
}


console.log('\n=== 18. A - zona horaria del proyecto ===');
{
  const h = cargar();                       // zona correcta
  h.ctx.verificarTodosLosCursos();
  afirmar('verificar dice la zona y que esta bien',
          h.log.some((l) => /Zona del proyecto: America\/Bogota\s+\(correcta\)/.test(l)));
}
{
  const h = cargar({ zona: 'America/New_York' });
  h.log.length = 0;
  h.ctx.verificarTodosLosCursos();
  afirmar('verificar canta la zona equivocada',
          h.log.some((l) => /NO ES America\/Bogota/.test(l)));
  afirmar('y dice donde arreglarla',
          h.log.some((l) => /Configuracion del proyecto .* Zona horaria/.test(l)));

  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.log.length = 0;
  h.ctx.crearTodosLosCursos();
  afirmar('con la zona mal NO crea nada', vivos(h.cal) === 0, vivos(h.cal) + ' eventos');
  afirmar('lo dice como BLOQUEADO', h.log.some((l) => /BLOQUEADO: crear/.test(l)));

  h.ctx.eliminarTodosLosCursos();
  afirmar('con la zona mal tampoco borra', h.cal.borrados.length === 0);
}
{
  const bien = cargar();
  bien.ctx.SIMULAR = false; bien.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  bien.ctx.crearTodosLosCursos();
  afirmar('con la zona correcta crea las 52', vivos(bien.cal) === 52, vivos(bien.cal) + '');
}

console.log('\n=== 19. B - un titulo cambiado NO genera una segunda serie ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearSeminario();
  const c = h.ctx.CURSOS.find((x) => x.key === 'seminario');
  const antesTitulo = c.sesiones[6].subject;
  // Como si el JSON hubiera marcado la sesion 7 como parcial: cambia el titulo.
  c.sesiones[6].subject = '[SINCRONICO] Parcial 2 - Seminario de Sistemas';
  h.log.length = 0;
  h.ctx.crearSeminario();
  afirmar('NO crea el gemelo', vivos(h.cal) === 13, vivos(h.cal) + ' eventos');
  afirmar('avisa de que hay uno con otro titulo', h.log.some((l) => /con OTRO titulo/.test(l)));
  afirmar('cuenta el omitido', h.log.some((l) => /1 OMITIDO\(S\) por titulo cambiado/.test(l)));
  h.ctx.recrearSeminario();
  afirmar('recrear deja 13 con el titulo nuevo', vivos(h.cal) === 13, vivos(h.cal) + '');
  afirmar('el titulo nuevo esta en el calendario',
          h.cal.eventos.some((e) => e.title === '[SINCRONICO] Parcial 2 - Seminario de Sistemas'));
  afirmar('el titulo viejo ya no esta',
          !h.cal.eventos.some((e) => e.title === antesTitulo));
  c.sesiones[6].subject = antesTitulo;
}

console.log('\n=== 20. C - el barrido corre aunque el titulo actual SI exista ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearArquitectura();
  const c = h.ctx.CURSOS.find((x) => x.key === 'arquitectura');
  const s = c.sesiones[2];
  const f = s.fecha.split('-').map(Number), hh = s.ini.split(':').map(Number);
  // Un evento de una corrida ANTERIOR con el titulo viejo, junto al actual, a la misma hora.
  const viejo = h.cal.plantar('Sesion 3 - Arquitectura de Sistemas Computacionales',
    new Date(f[0], f[1] - 1, f[2], hh[0], hh[1]),
    new Date(f[0], f[1] - 1, f[2], hh[0] + 2, hh[1]), ['x@y.co']);
  h.ctx.SIMULAR = true; h.log.length = 0;
  h.ctx.eliminarArquitectura();
  afirmar('lo lista como huerfano aunque el titulo actual exista',
          h.log.some((l) => /huerfano:.*Sesion 3 - Arquitectura/.test(l)));
  h.ctx.SIMULAR = false;
  h.ctx.eliminarArquitectura();
  afirmar('y lo borra', !h.cal.eventos.includes(viejo));
  afirmar('deja el calendario vacio', vivos(h.cal) === 0, vivos(h.cal) + '');
}
{
  // Dos eventos con el MISMO titulo: antes el segundo era invisible para todo el script.
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearArquitectura();
  const c = h.ctx.CURSOS.find((x) => x.key === 'arquitectura');
  const s = c.sesiones[4];
  const f = s.fecha.split('-').map(Number), hh = s.ini.split(':').map(Number);
  h.cal.plantar(s.subject, new Date(f[0], f[1] - 1, f[2], hh[0], hh[1]),
    new Date(f[0], f[1] - 1, f[2], hh[0] + 2, hh[1]), ['x@y.co']);
  h.log.length = 0;
  h.ctx.eliminarArquitectura();
  afirmar('avisa del titulo duplicado', h.log.some((l) => /eventos con el mismo titulo/.test(l)));
  afirmar('borra los dos', vivos(h.cal) === 0, vivos(h.cal) + ' quedan');
}

console.log('\n=== 21. E - un evento en una fecha que ya no esta en el JSON ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearBasesDatosII();
  const c = h.ctx.CURSOS.find((x) => x.key === 'bases_datos_ii');
  const s = c.sesiones[8];
  const hh = s.ini.split(':').map(Number);
  // Como si esa sesion se hubiera movido en el JSON. Ojo con el desplazamiento: a 7 dias
  // exactos cae en el hueco de la sesion anterior y lo caza el barrido semanal, que es otra
  // ruta. Para probar el barrido del periodo hace falta una fecha FUERA de la rejilla.
  const vf = new Date(Date.parse(s.fecha + 'T00:00:00') - 3 * 864e5);
  const fantasma = h.cal.plantar(s.subject,
    new Date(vf.getFullYear(), vf.getMonth(), vf.getDate(), hh[0], hh[1]),
    new Date(vf.getFullYear(), vf.getMonth(), vf.getDate(), hh[0] + 2, hh[1]), ['x@y.co']);
  // Y un apunte personal dentro del periodo, a otra hora: NO debe caer.
  const apunte = h.cal.plantar('Calificar Bases de Datos II',
    new Date(vf.getFullYear(), vf.getMonth(), vf.getDate(), 7, 0),
    new Date(vf.getFullYear(), vf.getMonth(), vf.getDate(), 8, 0), []);
  h.ctx.SIMULAR = true; h.log.length = 0;
  h.ctx.eliminarBasesDatosII();
  const fant = h.log.filter((l) => /fantasma:/.test(l));
  afirmar('lo lista como fantasma', fant.length === 1, fant.length + ' listados');
  afirmar('no lista el apunte personal de otra hora', !fant.some((l) => /Calificar/.test(l)));
  h.ctx.SIMULAR = false;
  h.ctx.eliminarBasesDatosII();
  afirmar('borra el fantasma', !h.cal.eventos.includes(fantasma));
  afirmar('NO borra el apunte personal', h.cal.eventos.includes(apunte));
}

console.log('\n=== 22. D - el aviso de corte nombra la funcion correcta ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false; h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.MINUTOS_MAX = -1;
  h.log.length = 0;
  h.ctx.crearTodosLosCursos();
  afirmar('crear* manda reejecutar crear*',
          h.log.some((l) => /Para continuar ejecuta: crearTodosLosCursos\(\)/.test(l)));
  afirmar('crear* no advierte de nada destructivo',
          !h.log.some((l) => /NO vuelvas a ejecutar/.test(l)));
  h.log.length = 0;
  h.ctx.recrearTodosLosCursos();
  afirmar('recrear* advierte de NO reejecutarse',
          h.log.some((l) => /NO vuelvas a ejecutar recrearTodosLosCursos\(\)/.test(l)));
  afirmar('recrear* manda continuar con crear*',
          h.log.some((l) => /Para continuar ejecuta: crearTodosLosCursos\(\)/.test(l)));
  h.log.length = 0;
  h.ctx.recrearSeminario();
  afirmar('por curso, tambien nombra el par correcto',
          h.log.some((l) => /NO vuelvas a ejecutar recrearSeminario\(\)/.test(l)) &&
          h.log.some((l) => /Para continuar ejecuta: crearSeminario\(\)/.test(l)));
}

console.log('\n=== 23. El .gs declara INICIO y FIN, y TZ se usa ===');
{
  const h = cargar();
  afirmar('INICIO y FIN existen', /^\d{4}-\d{2}-\d{2}$/.test(h.ctx.INICIO) &&
          /^\d{4}-\d{2}-\d{2}$/.test(h.ctx.FIN), h.ctx.INICIO + '..' + h.ctx.FIN);
  afirmar('todas las sesiones caen dentro del periodo',
          h.ctx.CURSOS.every((c) => c.sesiones.every((s) =>
            s.fecha >= h.ctx.INICIO && s.fecha <= h.ctx.FIN)));
  afirmar('TZ se usa, no solo se declara', /Session\.getScriptTimeZone/.test(FUENTE));
}

console.log('\n─────────────────────────────────────────');
console.log(`ok=${ok}  mal=${mal}`);
if (mal) { console.log('\nFallos:'); fallos.forEach((f) => console.log('  - ' + f)); }
process.exit(mal ? 1 : 0);
