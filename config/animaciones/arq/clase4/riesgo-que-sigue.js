/* Un riesgo de distribucion nombra UNA caja y dice que deja de funcionar y que SIGUE
 * funcionando: si se cae el worker de avisos, los turnos se siguen reservando y se pierde el correo. */
(function () {
  FP_ANIMADOR.registrar('riesgo-que-sigue', {
    duracion: 5,
    pasos: [0.3, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 60, w: 190, h: 100, t: 'App web', en: 0 },
        { tipo: 'caja', x: 300, y: 60, w: 200, h: 100, t: 'API de turnos', en: 0.03 },
        { tipo: 'cilindro', x: 590, y: 45, w: 190, h: 130, t: 'Base de turnos', color: 'acento', en: 0.06 },
        { tipo: 'caja', x: 300, y: 260, w: 200, h: 100, t: 'Worker de avisos', en: 0.09 },
        { tipo: 'flecha', de: [212, 110], a: [296, 110], en: 0.12 },
        { tipo: 'flecha', de: [502, 110], a: [586, 110], en: 0.14 },
        { tipo: 'flecha', de: [400, 162], a: [400, 256], r: 'cola', dx: 35, dy: -12, en: 0.16 },
        { tipo: 'tacha', x: 290, y: 250, w: 220, h: 120, en: 0.32 },
        { tipo: 'texto', t: 'se cae el worker', x: 650, y: 290, tam: 22, peso: 800, color: 'malva', ancho: 240, en: 0.34 },
        { tipo: 'caja', x: 30, y: 420, w: 350, h: 110, t: 'Deja de funcionar', s: 'el correo de confirmación', color: 'malva', tam: 24, tamSub: 21, en: 0.5 },
        { tipo: 'caja', x: 420, y: 420, w: 350, h: 110, t: 'SIGUE funcionando', s: 'la reserva de turnos', color: 'accion', tam: 24, tamSub: 21, en: 0.7 },
        { tipo: 'texto', t: 'La mitad que se olvida es la segunda.', x: 400, y: 570, tam: 23, ancho: 760, en: 0.88 }
      ]);
    }
  });
})();
