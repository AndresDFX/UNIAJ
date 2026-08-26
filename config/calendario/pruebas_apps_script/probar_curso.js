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
  af('cada evento con los '+c.invitados.length+' invitados',
     h.cal.eventos.every(e=>e.guests.length===c.invitados.length));
  const inv=h.cal.eventos.reduce((a,e)=>a+e.invitacionesEnviadas,0);
  h.ctx.crearEncuentros();
  af('reejecutar no duplica', h.cal.eventos.length===c.sesiones.length, h.cal.eventos.length+'');
  af('reejecutar no reinvita', h.cal.eventos.reduce((a,e)=>a+e.invitacionesEnviadas,0)===inv);
  h.ctx.recrearTodo();
  af('recrearTodo deja la serie completa', h.cal.eventos.length===c.sesiones.length, h.cal.eventos.length+'');
  af('recrearTodo borro las anteriores', h.cal.borrados.length===c.sesiones.length, h.cal.borrados.length+'');
  h.ctx.eliminarEncuentros();
  af('eliminarEncuentros deja el calendario vacio', h.cal.eventos.length===0, h.cal.eventos.length+'');
}
console.log(`  ok=${ok} mal=${mal}`); if(mal) fallos.forEach(f=>console.log('   - '+f));
process.exit(mal?1:0);
