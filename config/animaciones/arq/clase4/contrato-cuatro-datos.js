/* Un contrato son cuatro datos por flecha: la interaccion de negocio, quien llama a quien, con
 * que verbo y ruta, y el error de negocio que puede devolver (el 409 de la franja ocupada). */
(function () {
  FP_ANIMADOR.registrar('contrato-cuatro-datos', {
    duracion: 5,
    pasos: [0.25, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 30, y: 60, w: 210, h: 120, t: 'App web', s: 'React', en: 0 },
        { tipo: 'caja', x: 560, y: 60, w: 210, h: 120, t: 'API de turnos', s: 'Node.js', en: 0.02 },
        { tipo: 'flecha', de: [245, 120], a: [555, 120], grosor: 4, en: 0.05 },
        { tipo: 'caja', x: 40, y: 240, w: 350, h: 110, t: '1 · Interacción', s: 'Reservar turno', color: 'accion', tam: 22, tamSub: 20, en: 0.1 },
        { tipo: 'caja', x: 410, y: 240, w: 350, h: 110, t: '2 · Quién llama a quién', s: 'App web → API de turnos', color: 'accion', tam: 22, tamSub: 20, en: 0.3 },
        { tipo: 'caja', x: 40, y: 370, w: 350, h: 110, t: '3 · Verbo y ruta', s: 'POST /turnos', color: 'acento', tam: 22, tamSub: 20, en: 0.55 },
        { tipo: 'caja', x: 410, y: 370, w: 350, h: 110, t: '4 · Error de negocio', s: '409 · la franja ya está ocupada', color: 'malva', tam: 22, tamSub: 20, en: 0.8 },
        { tipo: 'texto', t: 'Si es asíncrono, el 3 es el nombre del evento.', x: 400, y: 530, tam: 22, ancho: 760, en: 0.88 }
      ]);
    }
  });
})();
