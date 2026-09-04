'use strict';
/**
 * Ejecuta de verdad el .gs consolidado contra el simulacro de Google y comprueba lo que
 * el script promete: que no duplica, que NO invita a nadie ni manda correos, que el borrado
 * no se lleva eventos ajenos, que los interruptores frenan, y que cortarse por tiempo no
 * pierde nada.
 *
 * Nada de cuentas cableadas: los numeros (cursos, sesiones, salas) se leen del propio .gs.
 * Antes decia "4 cursos / 13 sesiones / 52 eventos" y bastaba anadir un grupo al JSON para
 * que las pruebas fallaran sin que nada estuviera roto.
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
function invitadosTotales(cal) {
  return cal.eventos.reduce((a, e) => a + e.guests.length, 0);
}

// Cifras del .gs, leidas del .gs. Se usan en todas las secciones.
const REF = cargar().ctx;
const NCUR = REF.CURSOS.length;
const TOTAL = REF.CURSOS.reduce((a, c) => a + c.sesiones.length, 0);
const SIN_MEET = REF.CURSOS.reduce((a, c) => a + c.sesiones.filter((s) => !s.meet).length, 0);
const CON_MEET = TOTAL - SIN_MEET;
/** Cuantas sesiones tiene el curso `key`. */
const nses = (key) => REF.CURSOS.find((c) => c.key === key).sesiones.length;

console.log('\n=== 1. Datos cargados ===');
{
  const { ctx } = cargar();
  const cursos = ctx.CURSOS;
  console.log('       (' + NCUR + ' cursos · ' + TOTAL + ' sesiones · ' + CON_MEET +
              ' con Meet · ' + SIN_MEET + ' autonomas)');
  afirmar('hay cursos y todos con sesiones', NCUR > 0 && cursos.every((c) => c.sesiones.length > 0),
          cursos.map((c) => c.sesiones.length).join(','));
  afirmar('las sesiones de un curso no repiten fecha',
          cursos.every((c) => new Set(c.sesiones.map((s) => s.fecha)).size === c.sesiones.length));
  // Esquema «[SINCRONICO] GRUPO - Curso - Sesion N». El prefijo dice si a esa hora hay
  // encuentro (las [AUTONOMO] son las unicas sin sala de Meet) y el grupo va delante del
  // curso, que es lo que distingue a los 3 grupos de FI300101.
  afirmar('titulo coherente con meet',
          cursos.every((c) => c.sesiones.every((s) =>
            s.meet ? s.subject.indexOf('[SINCRONICO]') === 0 : s.subject.indexOf('[AUTONOMO]') === 0)));
  afirmar('titulo con el esquema GRUPO - Curso - Sesion',
          cursos.every((c) => c.sesiones.every((s) =>
            s.subject.indexOf('] ' + c.grupo + ' - ' + c.cursoBase + ' - ') !== -1)));
  afirmar('las sesiones con Meet numeran la sesion',
          cursos.every((c) => c.sesiones.every((s) => !s.meet || /- Sesión \d+/.test(s.subject))));
  afirmar('requestId distinto por curso',
          new Set(cursos.map((c) => c.requestId)).size === NCUR,
          new Set(cursos.map((c) => c.requestId)).size + ' de ' + NCUR);
  afirmar('titulo distinto entre cursos distintos',
          new Set(cursos.reduce((a, c) => a.concat(c.sesiones.map((s) => s.subject)), [])).size === TOTAL);
  // El corazon del cambio: son bloques del calendario del docente.
  afirmar('ningun curso declara invitados',
          cursos.every((c) => typeof c.invitados === 'undefined'));
  afirmar('el .gs no menciona guests ni sendInvites como codigo',
          !/(^|[^/*\s])\s*guests\s*:/.test(FUENTE) && !/sendInvites\s*:/.test(FUENTE));
  afirmar('cada curso trae su propio rango (inicio/fin)',
          cursos.every((c) => /^\d{4}-\d{2}-\d{2}$/.test(c.inicio) && /^\d{4}-\d{2}-\d{2}$/.test(c.fin)));
  afirmar('codigoCompartido marcado si y solo si el codigo se repite',
          cursos.every((c) => c.codigoCompartido ===
            (cursos.filter((o) => o.codigo === c.codigo).length > 1)));
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
  afirmar('verificar dice cuantas sesiones',
          h.log.some((l) => l.indexOf('TOTAL ' + NCUR + ' curso(s) · ' + TOTAL + ' sesion') === 0),
          h.log.filter((l) => /^TOTAL /.test(l)).join(' / '));
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
  afirmar('un curso suelto si corre sin el segundo interruptor',
          vivos(h.cal) === nses('bases_datos_ii'),
          vivos(h.cal) + ' de ' + nses('bases_datos_ii') + ' eventos');
}

console.log('\n=== 4. Creacion completa y sala por sesion ===');
let baseline;
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearTodosLosCursos();
  baseline = h;
  afirmar(TOTAL + ' eventos creados', vivos(h.cal) === TOTAL, vivos(h.cal) + '');
  afirmar(CON_MEET + ' con sala de Meet (' + TOTAL + ' - ' + SIN_MEET + ' autonomas)',
          conMeet(h.cal) === CON_MEET, conMeet(h.cal) + '');
  const urls = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri);
  afirmar(CON_MEET + ' enlaces de Meet DISTINTOS', new Set(urls).size === CON_MEET,
          new Set(urls).size + ' distintos');
  afirmar('las autonomas quedan en el calendario sin Meet',
          h.cal.eventos.filter((e) => !e.conferenceData).length === SIN_MEET);
  afirmar('las autonomas no tienen enlace en Ubicacion',
          h.cal.eventos.filter((e) => !e.conferenceData).every((e) => e.location === ''));
  afirmar('el enlace queda tambien en Ubicacion',
          h.cal.eventos.filter((e) => e.conferenceData)
            .every((e) => e.location === e.conferenceData.entryPoints[0].uri));
  afirmar('el enlace queda en la descripcion',
          h.cal.eventos.filter((e) => e.conferenceData)
            .every((e) => e.description.indexOf(e.conferenceData.entryPoints[0].uri) !== -1));
  afirmar('ningun evento tiene invitados', invitadosTotales(h.cal) === 0,
          invitadosTotales(h.cal) + ' invitados');
  afirmar('no se envio NI UNA invitacion', invitacionesTotales(h.cal) === 0,
          invitacionesTotales(h.cal) + ' invitaciones');
  afirmar('el .gs nunca llama a addGuest', h.cal.addGuestLlamado === 0,
          h.cal.addGuestLlamado + ' llamadas');
  afirmar('la sala se pide con sendUpdates none (nadie a quien notificar)',
          h.cal.eventos.every((e) => e.notificacionesDeUpdate === 0));
}

console.log('\n=== 5. Reejecutar no duplica ===');
{
  const h = baseline;
  const antesEventos = vivos(h.cal);
  const antesUrls = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri).sort().join('|');
  h.log.length = 0;
  h.ctx.crearTodosLosCursos();
  afirmar('sigue habiendo ' + TOTAL + ' eventos', vivos(h.cal) === antesEventos, vivos(h.cal) + '');
  afirmar('sigue sin enviar correos', invitacionesTotales(h.cal) === 0,
          invitacionesTotales(h.cal) + ' invitaciones');
  const ahoraUrls = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri).sort().join('|');
  afirmar('los enlaces de Meet NO cambiaron', ahoraUrls === antesUrls);
  afirmar('el log dice que reutilizo',
          h.log.some((l) => l.indexOf(TOTAL + ' reutilizado') !== -1),
          h.log.filter((l) => /reutilizado/.test(l)).join(' / '));
}

console.log('\n=== 6. Grupos que comparten codigo no se pisan ===');
{
  // FI300101 corre en 3 grupos. Comparten codigo y nombre de asignatura; el grupo va dentro
  // del titulo y `codigoCompartido` apaga el reconocimiento por codigo pelado. Si eso se
  // rompe, crear un grupo se lleva los eventos de otro.
  const grupos = REF.CURSOS.filter((c) => c.codigoCompartido);
  if (grupos.length < 2) {
    console.log('       (no hay codigos compartidos en este periodo: nada que probar)');
  } else {
    const h = cargar();
    h.ctx.SIMULAR = false;
    h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
    h.ctx.crearTodosLosCursos();
    afirmar('cada grupo tiene sus propios eventos',
            grupos.every((g) => h.cal.eventos.filter((e) => e.title.indexOf(g.grupo) !== -1).length
                                === g.sesiones.length),
            grupos.map((g) => g.grupo + '=' +
              h.cal.eventos.filter((e) => e.title.indexOf(g.grupo) !== -1).length).join(' '));
    // Borrar UNO no puede tocar a los otros dos, ni por titulo ni por barrido de fantasmas.
    const uno = grupos[0];
    const otros = grupos.slice(1).reduce((a, g) => a + g.sesiones.length, 0);
    // El generador bautiza las funciones por curso con el grupo dentro del nombre.
    const fn = Object.keys(h.ctx).find((k) =>
      k.indexOf('eliminar') === 0 && k.indexOf(uno.grupo) !== -1);
    afirmar('existe la funcion por grupo (' + fn + ')', typeof h.ctx[fn] === 'function');
    if (typeof h.ctx[fn] === 'function') {
      h.ctx[fn]();
      afirmar('borro solo su grupo',
              h.cal.eventos.filter((e) => e.title.indexOf(uno.grupo) !== -1).length === 0);
      const quedan = grupos.slice(1).reduce((a, g) =>
        a + h.cal.eventos.filter((e) => e.title.indexOf(g.grupo) !== -1).length, 0);
      afirmar('los otros grupos siguen enteros', quedan === otros, quedan + ' de ' + otros);
    }
  }
}

console.log('\n=== 7. Nadie recibe correos, ni al borrar ===');
{
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearTodosLosCursos();
  h.ctx.eliminarTodosLosCursos();
  afirmar('borro los ' + TOTAL + ' eventos', h.cal.borrados.length === TOTAL,
          h.cal.borrados.length + '');
  afirmar('ni una cancelacion enviada', h.cal.borrados.every((e) => !e.cancelacionEnviada));
  afirmar('ni una invitacion en toda la corrida', invitacionesTotales(h.cal) === 0,
          invitacionesTotales(h.cal) + '');
  afirmar('addGuest nunca se llamo', h.cal.addGuestLlamado === 0, h.cal.addGuestLlamado + '');
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
  afirmar('borro las ' + nses('bases_datos_ii') + ' de BD II', quedanBd === 0, quedanBd + ' vivas');
  afirmar('no toco las de Arquitectura', quedanArq === antesArq, quedanArq + ' de ' + antesArq);
  afirmar('borrar no notifico a nadie', h.cal.borrados.every((e) => !e.cancelacionEnviada));
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
  afirmar('vuelve a haber ' + nses('seminario') + ' eventos', vivos(h.cal) === nses('seminario'), vivos(h.cal) + '');
  const despues = h.cal.eventos.filter((e) => e.conferenceData)
    .map((e) => e.conferenceData.entryPoints[0].uri).sort().join('|');
  afirmar('los eventos son otros (se borraron y recrearon)', h.cal.borrados.length === nses('seminario'),
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
  afirmar('al reejecutar con plazo normal completa las ' + TOTAL, vivos(h.cal) === TOTAL, vivos(h.cal) + '');
}

console.log('\n=== 12. Sin servicio avanzado de Calendar ===');
{
  const h = cargar({ sinServicioAvanzado: true });
  h.ctx.SIMULAR = false;
  h.ctx.CONFIRMO_SEMESTRE_COMPLETO = true;
  h.ctx.crearTodosLosCursos();
  afirmar('crea los ' + TOTAL + ' eventos igual', vivos(h.cal) === TOTAL, vivos(h.cal) + '');
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
  afirmar('primera corrida: ' + nses('seminario') + ' eventos', vivos(h.cal) === nses('seminario'), vivos(h.cal) + '');
  h.cal.searchInutil = true;              // Google deja de indexar los titulos
  h.ctx.crearSeminario();
  afirmar('aunque `search` no sirva, NO duplica (ya no depende de search)',
          vivos(h.cal) === nses('seminario'),
          vivos(h.cal) + ' eventos (deberian ser ' + nses('seminario') + ')');
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
  afirmar('avisa de cada fallo',
          h.log.filter((l) => /no pude borrar/.test(l)).length === nses('seminario'));
}

console.log('\n=== 16. Eventos AJENOS con invitados: el script no los toca ===');
{
  // Antes esta seccion probaba el fallo de cuota de addGuest. Ya no hay invitados que agregar;
  // lo que queda por defender es lo contrario: que un evento del docente que SI tiene gente
  // invitada (una reunion, una asesoria) no se cuele en el barrido ni pierda a nadie.
  const h = cargar();
  h.ctx.SIMULAR = false;
  h.ctx.crearSeminario();
  const c = h.ctx.CURSOS.find((x) => x.key === 'seminario');
  const s = c.sesiones[2];
  const f = s.fecha.split('-').map(Number);
  const reunion = h.cal.plantar('Reunion de area con el decano',
    new Date(f[0], f[1] - 1, f[2], 7, 0), new Date(f[0], f[1] - 1, f[2], 8, 0),
    ['decanatura@uniajc.edu.co']);
  h.log.length = 0;
  h.ctx.crearSeminario();
  afirmar('no le agrego ni le quito invitados a la reunion ajena',
          reunion.guests.length === 1 && h.cal.addGuestLlamado === 0);
  h.ctx.eliminarSeminario();
  afirmar('borro su serie', h.cal.eventos.filter((e) => e.title.indexOf('Seminario') !== -1).length === 0);
  afirmar('la reunion ajena sigue viva', h.cal.eventos.includes(reunion));
  afirmar('y no se mando ninguna cancelacion', h.cal.borrados.every((e) => !e.cancelacionEnviada));
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
  afirmar('con la zona correcta crea las ' + TOTAL, vivos(bien.cal) === TOTAL, vivos(bien.cal) + '');
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
  afirmar('NO crea el gemelo', vivos(h.cal) === nses('seminario'), vivos(h.cal) + ' eventos');
  afirmar('avisa de que hay uno con otro titulo', h.log.some((l) => /con OTRO titulo/.test(l)));
  afirmar('cuenta el omitido', h.log.some((l) => /1 OMITIDO\(S\) por titulo cambiado/.test(l)));
  h.ctx.recrearSeminario();
  afirmar('recrear deja ' + nses('seminario') + ' con el titulo nuevo', vivos(h.cal) === nses('seminario'), vivos(h.cal) + '');
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

console.log('\n=== 24. Estan TODOS los cursos del periodo (contra los dos JSON) ===');
{
  // Las demas secciones derivan sus cifras del propio .gs, que es lo correcto para no cablear
  // numeros que cambian cada semestre. Pero eso deja un hueco: si el generador dejara de emitir
  // un curso, TOTAL y NCUR bajarian con el y todo seguiria en verde. Aqui se compara contra la
  // fuente de verdad -los dos JSON- para que una omision silenciosa falle.
  const dir = require('path').join(__dirname, '..');
  const leer = (n) => JSON.parse(fs.readFileSync(require('path').join(dir, n), 'utf8'));
  const J1 = leer('semestre_2026_2.json');
  const J2 = leer('introduccion_ingenieria_2026_2.json');

  const espCursos = Object.keys(J1.cursos).length + J2.grupos.length;
  const espSesiones = Object.keys(J1.cursos).reduce((a, k) => a + J1.cursos[k].clases.length, 0)
                    + J2.grupos.reduce((a, g) => a + g.sesiones.length, 0);
  const aut = (t) => String(t).indexOf('autonoma') === 0;
  const espAutonomas = Object.keys(J1.cursos)
        .reduce((a, k) => a + J1.cursos[k].clases.filter((c) => aut(c.tipo)).length, 0)
      + J2.grupos.reduce((a, g) => a + g.sesiones.filter((s) => aut(s.tipo)).length, 0);

  console.log('       (los JSON piden ' + espCursos + ' cursos · ' + espSesiones + ' sesiones · ' +
              espAutonomas + ' autonomas)');
  afirmar('el .gs declara exactamente ' + espCursos + ' cursos (7 este periodo)',
          NCUR === espCursos, NCUR + ' declarados');
  afirmar('y exactamente ' + espSesiones + ' sesiones', TOTAL === espSesiones, TOTAL + '');
  afirmar('y ' + espAutonomas + ' sesiones sin Meet', SIN_MEET === espAutonomas, SIN_MEET + '');

  // Uno por uno, para que el fallo diga CUAL falta y no solo que el total no cuadra.
  const esperados = Object.keys(J1.cursos).map((k) => ({
    codigo: J1.cursos[k].codigo, grupo: J1.cursos[k].grupo, n: J1.cursos[k].clases.length,
  })).concat(J2.grupos.map((g) => ({
    codigo: J2.curso.codigo, grupo: g.grupo, n: g.sesiones.length,
  })));
  const faltan = esperados.filter((e) =>
    !REF.CURSOS.some((c) => c.codigo === e.codigo && c.grupo === e.grupo && c.sesiones.length === e.n));
  afirmar('cada curso del JSON esta en el .gs con su grupo y sus sesiones',
          faltan.length === 0,
          faltan.map((e) => e.codigo + '/' + e.grupo + ' x' + e.n).join(' '));
  afirmar('los 3 grupos de ' + J2.curso.codigo + ' estan los tres',
          REF.CURSOS.filter((c) => c.codigo === J2.curso.codigo).length === J2.grupos.length,
          REF.CURSOS.filter((c) => c.codigo === J2.curso.codigo).length + '');
  afirmar('el .gs no trae cursos de mas',
          REF.CURSOS.every((c) => esperados.some((e) => e.codigo === c.codigo && e.grupo === c.grupo)),
          REF.CURSOS.filter((c) => !esperados.some((e) => e.codigo === c.codigo && e.grupo === c.grupo))
            .map((c) => c.key).join(' '));
  // Las semanas autonomas son el caso raro: sin numero de sesion y sin Meet. Antes las
  // ponian los grupos de Introduccion a la Ingenieria por el festivo del 08/12, pero desde
  // que sus 11 sesiones cierran en noviembre ningun festivo de 2026 cae en su dia de clase:
  // hoy no hay ninguna. Se prueba condicional para que la regla se siga comprobando el dia
  // que un festivo vuelva a caer en dia de clase, sin fallar mientras tanto.
  const sinN = REF.CURSOS.reduce((a, c) => a.concat(
    c.sesiones.filter((s) => s.subject.indexOf('Semana autónoma') !== -1)), []);
  if (sinN.length > 0) {
    afirmar('las semanas autonomas van sin Meet', sinN.every((s) => !s.meet), sinN.length + ' encontradas');
  } else {
    console.log('       (0 semanas autonomas en este periodo: nada que probar)');
  }
  afirmar('ningun titulo quedo con un hueco sin llenar (None/undefined/NaN)',
          !REF.CURSOS.some((c) => c.sesiones.some((s) =>
            /None|undefined|NaN/.test(s.subject) || /None|undefined|NaN/.test(s.desc || ''))));
}

console.log('\n=== 25. Ni un dato de estudiante en el .gs ===');
{
  // El .gs vive en _privado/ por historia: antes llevaba la nomina completa como invitados.
  // Ya no debe llevar ni un correo de estudiante. Se mide sobre el texto del archivo, que es
  // lo que de verdad se pega en el editor de Apps Script.
  afirmar('no aparece ningun @estudiante.uniajc.edu.co',
          FUENTE.indexOf('@estudiante.uniajc.edu.co') === -1,
          (FUENTE.match(/@estudiante\.uniajc\.edu\.co/g) || []).length + ' apariciones');
  const otros = (FUENTE.match(/[\w.+-]+@[\w.-]+/g) || [])
    .filter((c) => c.indexOf('@profesores.uniajc.edu.co') === -1
                && c.indexOf('@group.calendar.google.com') === -1
                && c.indexOf('@uniajc.edu.co') === -1);
  afirmar('los unicos correos que quedan son del docente / del calendario',
          otros.length === 0, otros.join(' '));
  afirmar('no hay ATTENDEE ni lista de invitados en el texto',
          !/ATTENDEE/i.test(FUENTE) && !/invitados\s*:/.test(FUENTE));
  afirmar('no queda ningun sendUpdates: all', !/sendUpdates\s*:\s*'all'/.test(FUENTE));
  afirmar('la unica mencion de addGuest seria un error: no hay',
          FUENTE.indexOf('addGuest') === -1);
}

console.log('\n=== 26. El barrido de fantasmas no se sale del rango DEL CURSO ===');
{
  // INICIO/FIN son la UNION de los rangos de los 7 cursos, asi que llegan a diciembre por los
  // grupos de Introduccion a la Ingenieria. Los 4 cursos cortos cierran en noviembre: si el
  // barrido usara el rango global en vez del del curso, `eliminar<Curso>` se metaria en
  // diciembre —donde ese curso ya no tiene clases— y se llevaria apuntes personales del
  // docente que nombren la asignatura a esa hora.
  //
  // Esto se prueba por COMPORTAMIENTO a proposito: comprobar que `c.inicio`/`c.fin` existen en
  // el objeto CURSOS (seccion 1) no dice nada sobre si `_fantasmas_` los usa.
  const h = cargar();
  const corto = h.ctx.CURSOS.filter((c) => c.fin < h.ctx.FIN)
                            .sort((a, b) => (a.fin < b.fin ? -1 : 1))[0];
  if (!corto) {
    // Con un solo rango en juego la prueba no puede distinguir las dos implementaciones.
    afirmar('hay algun curso que cierre antes que el periodo (si no, esta prueba no aplica)',
            false, 'todos los cursos cierran en ' + h.ctx.FIN);
  } else {
    // La funcion de ese curso, sacada del propio .gs (nada de nombres cableados):
    //   function eliminarBasesDatosII() { _eliminar_(_curso_('bases_datos_ii')); }
    const m = FUENTE.match(new RegExp(
      "function (eliminar\\w+)\\(\\)[^\\n]*_curso_\\('" + corto.key + "'\\)"));
    afirmar('existe la funcion de borrado de ' + corto.key, !!m, corto.key);
    const clave = m && m[1];
    if (!clave) throw new Error('sin funcion de borrado para ' + corto.key);
    h.ctx.SIMULAR = false;
    h.ctx[clave.replace('eliminar', 'crear')]();
    // Un apunte PERSONAL del docente: fuera del rango del curso, dentro del rango global, a
    // la hora del curso y con el nombre de la asignatura en el titulo. Es exactamente el
    // evento que el barrido global se llevaria.
    //
    // El offset NO es fijo: antes el hueco entre el fin de un curso corto y el FIN global
    // eran semanas (Introduccion a la Ingenieria llegaba a diciembre), pero desde que sus 11
    // sesiones cierran dentro de la ventana institucional el hueco puede ser de pocos dias.
    // Un offset fijo mas grande que el hueco disponible plantaria la sonda FUERA del rango
    // global y la prueba dejaria de probar nada sin que nadie lo notara.
    const ini = corto.sesiones[0].ini.split(':').map(Number);
    const gapDias = Math.round((Date.parse(h.ctx.FIN) - Date.parse(corto.fin)) / 864e5);
    if (gapDias < 1) {
      afirmar('hay margen entre el fin de un curso corto y el FIN global (si no, esta prueba no aplica)',
              false, 'gap=' + gapDias + ' dias entre ' + corto.fin + ' y ' + h.ctx.FIN);
    }
    const offset = Math.max(1, Math.min(21, gapDias));
    const d = new Date(Date.parse(corto.fin + 'T00:00:00') + offset * 864e5);
    const dentroDelGlobal = d.toISOString().slice(0, 10) <= h.ctx.FIN;
    afirmar('la fecha de la sonda cae dentro del rango GLOBAL (si no, no prueba nada)',
            dentroDelGlobal, d.toISOString().slice(0, 10) + ' vs ' + h.ctx.FIN);
    const apunte = h.cal.plantar(corto.nombre + ' · repaso de vacaciones' +
                                 (corto.codigoCompartido ? ' ' + corto.grupo : ''),
      new Date(d.getFullYear(), d.getMonth(), d.getDate(), ini[0], ini[1]),
      new Date(d.getFullYear(), d.getMonth(), d.getDate(), ini[0] + 1, ini[1]), []);
    const antes = vivos(h.cal);
    h.ctx.SIMULAR = true; h.log.length = 0;
    h.ctx[clave]();
    afirmar('en simulacion no lo lista como fantasma',
            !h.log.some((l) => /fantasma:.*repaso de vacaciones/.test(l)),
            h.log.filter((l) => /fantasma:/.test(l)).join(' | '));
    h.ctx.SIMULAR = false;
    h.ctx[clave]();
    afirmar('un apunte personal POSTERIOR al fin del curso (a su hora) NO se borra',
            h.cal.eventos.includes(apunte),
            'quedan: ' + h.cal.eventos.map((e) => e.title).join(' | '));
    afirmar('y si borro los eventos del curso, que era su trabajo',
            vivos(h.cal) === antes - corto.sesiones.length,
            vivos(h.cal) + ' de ' + (antes - corto.sesiones.length));
  }
}

console.log('\n─────────────────────────────────────────');
console.log(`ok=${ok}  mal=${mal}`);
if (mal) { console.log('\nFallos:'); fallos.forEach((f) => console.log('  - ' + f)); }
process.exit(mal ? 1 : 0);
