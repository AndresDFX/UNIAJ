/* Cuando NO se usa un trigger: cuatro casos, cada uno con su alternativa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cuando-no-trigger', {
    duracion: 4.6,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.23, 0.39, 0.55, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var casos = [
        ['Lo resuelve un CHECK o un UNIQUE', '→ la restricción'],
        ['La regla admite excepciones autorizadas', '→ la aplicación'],
        ['Envía un correo o llama un servicio', '→ fuera de la transacción'],
        ['Tiene varios pasos y decisiones', '→ un procedimiento']
      ];
      UJ.rotulo(ctx, lz, 'Aquí NO va un trigger', W / 2, 10, { tam: 28, peso: 800, color: R, visible: L.tramo(t, 0, 0.1) });
      for (var i = 0; i < 4; i++) {
        var y = 70 + i * 118, a = L.tramo(t, 0.08 + i * 0.16, 0.18 + i * 0.16);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 30, y, W - 60, 98, 14); L.rellena(ctx, L.tono(A, 0.93), L.tono(A, 0.4), 2);
          UJ.rotulo(ctx, lz, casos[i][0], 110, y + 18, { tam: 22, peso: 700, alinear: 'left', ancho: W - 180 });
          UJ.rotulo(ctx, lz, casos[i][1], 110, y + 56, { tam: 20, peso: 600, alinear: 'left', color: C });
        });
        UJ.sello(ctx, lz, 70, y + 49, 24, false, L.tramo(t, 0.14 + i * 0.16, 0.22 + i * 0.16));
      }
    }
  });
})();
