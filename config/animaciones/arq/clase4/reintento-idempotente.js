/* El timeout corta la espera; el reintento vuelve a llamar. Si crear turno no es idempotente, el
 * reintento deja dos reservas para la misma franja; con una clave de idempotencia, una sola. */
(function () {
  FP_ANIMADOR.registrar('reintento-idempotente', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 190, h: 90, t: 'App web', en: 0 },
        { tipo: 'caja', x: 590, y: 30, w: 190, h: 90, t: 'API de turnos', tam: 20, en: 0.02 },
        { tipo: 'flecha', de: [215, 60], a: [585, 60], r: '1 · POST /turnos', dy: -30, en: 0.06 },
        { tipo: 'flecha', de: [585, 95], a: [400, 95], color: 'gris', punteada: true, en: 0.14 },
        { tipo: 'tacha', x: 385, y: 80, w: 30, h: 30, en: 0.2 },
        { tipo: 'chip', x: 300, y: 135, t: 'timeout: la respuesta se perdió', color: 'malva', en: 0.22 },
        { tipo: 'flecha', de: [215, 205], a: [585, 205], r: '2 · reintento: POST /turnos', dy: -30, en: 0.34 },
        { tipo: 'texto', t: 'Sin idempotencia', x: 200, y: 280, tam: 23, peso: 800, color: 'malva', en: 0.44 },
        { tipo: 'caja', x: 60, y: 320, w: 280, h: 60, t: 'turno · sábado 10:00', color: 'malva', r: 8, tam: 19, en: 0.48 },
        { tipo: 'caja', x: 60, y: 390, w: 280, h: 60, t: 'turno · sábado 10:00', color: 'malva', r: 8, tam: 19, en: 0.52 },
        { tipo: 'chip', x: 200, y: 470, t: 'dos reservas', color: 'malva', en: 0.56 },
        { tipo: 'texto', t: 'Con clave de idempotencia', x: 600, y: 280, tam: 23, peso: 800, color: 'accion', ancho: 340, en: 0.66 },
        { tipo: 'caja', x: 460, y: 320, w: 280, h: 60, t: 'turno · sábado 10:00', color: 'accion', r: 8, tam: 19, en: 0.7 },
        { tipo: 'texto', t: 'el 2.º POST devuelve el mismo turno', x: 600, y: 395, tam: 19, ancho: 300, en: 0.74 },
        { tipo: 'chip', x: 600, y: 470, t: 'una reserva', color: 'accion', en: 0.78 },
        { tipo: 'texto', t: 'Circuit breaker: tras varios fallos seguidos, deja de llamar un rato y responde de inmediato.', x: 400, y: 545, tam: 20, ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
