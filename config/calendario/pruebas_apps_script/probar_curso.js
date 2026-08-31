'use strict';
/** El .gs de un solo curso: mismos motores, otros nombres de entrada. */
const fs=require('fs'), vm=require('vm'), {construir}=require('./google-mock');
const GS=process.argv[2];
const FUENTE=fs.readFileSync(GS,'utf8');
let ok=0,mal=0,fallos=[];
const af=(n,c,d)=>{ if(c){ok++;console.log('  OK   '+n);} else {mal++;fallos.push(n+(d?' -> '+d:''));console.log('  MAL  '+n+(d?' -> '+d:''));} };
function cargar(o){ const m=construir(o); const ctx=vm.createContext(m.sandbox);
  vm.runInContext(FUENTE,ctx,{filename:GS}); ctx.CALENDAR_ID=m.cal.getId(); ctx.SIMULAR=true;
  return Object.assign(m,{ctx}); }

console.log('\n'+GS.split(/[\/]/).pop());
{
  const h=cargar();
  af('un solo curso en CURSOS', h.ctx.CURSOS.length===1, h.ctx.CURSOS.length+'');
  af('las 4 funciones documentadas existen',
     ['verificar','crearEncuentros','eliminarEncuentros','recrearTodo','listarCalendarios']
       .every(f=>typeof h.ctx[f]==='function'));
  af('NO hay CONFIRMO_SEMESTRE_COMPLETO (solo el consolidado lo tiene)',
     typeof h.ctx.CONFIRMO_SEMESTRE_COMPLETO==='undefined');
  h.ctx.verificar(); h.ctx.crearEncuentros(); h.ctx.eliminarEncuentros(); h.ctx.recrearTodo();
  af('en simulacion no toca nada', h.cal.eventos.length===0 && h.cal.escrituras===0);
}
{
  const h=cargar(); h.ctx.SIMULAR=false;
  h.ctx.crearEncuentros();
  const c=h.ctx.CURSOS[0];
  const esperadasMeet=c.sesiones.filter(s=>s.meet).length;
  af('crea las '+c.sesiones.length+' sesiones', h.cal.eventos.length===c.sesiones.length, h.cal.eventos.length+'');
  af('cada sincronica con su sala distinta',
     new Set(h.cal.eventos.filter(e=>e.conferenceData).map(e=>e.conferenceData.entryPoints[0].uri)).size===esperadasMeet);
  // Son bloques del calendario del docente: ni un invitado, ni un correo.
  af('ningun evento tiene invitados', h.cal.eventos.every(e=>e.guests.length===0),
     h.cal.eventos.reduce((a,e)=>a+e.guests.length,0)+' invitados');
  af('el curso no declara lista de invitados', typeof c.invitados==='undefined');
  af('no se envio ninguna invitacion',
     h.cal.eventos.reduce((a,e)=>a+e.invitacionesEnviadas,0)===0);
  af('el .gs nunca llama a addGuest', h.cal.addGuestLlamado===0, h.cal.addGuestLlamado+' llamadas');
  h.ctx.crearEncuentros();
  af('reejecutar no duplica', h.cal.eventos.length===c.sesiones.length, h.cal.eventos.length+'');
  af('reejecutar sigue sin enviar correos',
     h.cal.eventos.reduce((a,e)=>a+e.invitacionesEnviadas,0)===0);
  h.ctx.recrearTodo();
  af('recrearTodo deja la serie completa', h.cal.eventos.length===c.sesiones.length, h.cal.eventos.length+'');
  af('recrearTodo borro las anteriores', h.cal.borrados.length===c.sesiones.length, h.cal.borrados.length+'');
  h.ctx.eliminarEncuentros();
  af('eliminarEncuentros deja el calendario vacio', h.cal.eventos.length===0, h.cal.eventos.length+'');
  af('borrar no mando ninguna cancelacion', h.cal.borrados.every(e=>!e.cancelacionEnviada));
}
{
  // Aunque el .gs sea de un solo curso, INICIO/FIN siguen siendo la UNION de los rangos del
  // periodo (los grupos de Introduccion a la Ingenieria llegan a diciembre y arrancan en
  // septiembre; los otros cuatro van del 24/08 al 22/11). El barrido de fantasmas tiene que
  // usar el rango DEL CURSO: con el global se metería en semanas donde este curso no tiene
  // clases y se llevaria apuntes personales del docente que nombren la asignatura a esa hora.
  // Se prueba por COMPORTAMIENTO: ver `inicio`/`fin` en el objeto del curso no dice nada sobre
  // si `_fantasmas_` los usa.
  const h=cargar(), c=h.ctx.CURSOS[0];
  const mover=(iso,d)=>new Date(Date.parse(iso+'T12:00:00')+d*864e5).toISOString().slice(0,10);
  const sondas=[];
  if(c.inicio>h.ctx.INICIO) sondas.push(['antes del inicio', mover(c.inicio,-3)]);
  if(c.fin<h.ctx.FIN)       sondas.push(['despues del fin',  mover(c.fin,3)]);
  if(!sondas.length){
    // Periodo de un solo curso: global y propio coinciden y las dos implementaciones no se
    // distinguen. Se dice, no se calla.
    console.log('  --   el rango del curso es el del periodo: esta prueba no aplica aqui');
  } else {
    h.ctx.SIMULAR=false; h.ctx.crearEncuentros();
    const [hh,mm]=c.sesiones[0].ini.split(':').map(Number);
    const apuntes=sondas.map(([que,f])=>{
      af('la sonda de '+que+' ('+f+') cae dentro del rango GLOBAL',
         f>=h.ctx.INICIO && f<=h.ctx.FIN, f+' vs '+h.ctx.INICIO+'..'+h.ctx.FIN);
      const [Y,M,D]=f.split('-').map(Number);
      return [que, h.cal.plantar(c.nombre+' · apunte personal', new Date(Y,M-1,D,hh,mm),
                                 new Date(Y,M-1,D,hh+1,mm), [])];
    });
    const antes=h.cal.eventos.length;
    h.ctx.SIMULAR=true; h.log.length=0; h.ctx.eliminarEncuentros();
    af('en simulacion no lista los apuntes como fantasmas',
       !h.log.some(l=>/fantasma:.*apunte personal/.test(l)),
       h.log.filter(l=>/fantasma:/.test(l)).join(' | '));
    h.ctx.SIMULAR=false; h.ctx.eliminarEncuentros();
    apuntes.forEach(([que,ev])=>af('un apunte personal '+que+' del curso (a su hora) NO se borra',
       h.cal.eventos.includes(ev), 'quedan: '+h.cal.eventos.map(e=>e.title).join(' | ')));
    af('y si borro los '+c.sesiones.length+' encuentros, que era su trabajo',
       h.cal.eventos.length===antes-c.sesiones.length,
       h.cal.eventos.length+' de '+(antes-c.sesiones.length));
  }
}
{
  // Este .gs vive en _privado/ porque antes llevaba la nomina entera como invitados. Ya no debe
  // llevar ni un correo de estudiante: se mide sobre el texto, que es lo que se pega en Google.
  af('ni un @estudiante.uniajc.edu.co en el texto',
     FUENTE.indexOf('@estudiante.uniajc.edu.co')===-1);
  af('no hay ATTENDEE, guests, addGuest ni sendUpdates all',
     !/ATTENDEE/i.test(FUENTE) && !/(^|[^/*\s])\s*guests\s*:/.test(FUENTE)
     && FUENTE.indexOf('addGuest')===-1 && !/sendUpdates\s*:\s*'all'/.test(FUENTE));
}
console.log(`  ok=${ok} mal=${mal}`); if(mal) fallos.forEach(f=>console.log('   - '+f));
process.exit(mal?1:0);
