/* Lugar comun frente a leccion accionable: verbo concreto, artefacto, frecuencia o umbral, y la
 * manera de comprobar que se hizo. La segunda se puede auditar; la primera es una intencion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('leccion-accionable', {
    duracion: 5,
    pasos: [0.24, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.alfa(ctx, L.tramo(t, 0, 0.1) * (1 - 0.6 * L.tramo(t, 0.26, 0.32)), function () {
        L.rectRed(ctx, 40, 20, 720, 70, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, '«Hay que probar los respaldos»', 380, 40, { tam: 23, peso: 700, color: R });
      });
      UJ.sello(ctx, lz, 720, 55, 22, false, L.tramo(t, 0.1, 0.18));
      var partes = [['Verbo concreto', 'se restaura'], ['Artefacto', 'el respaldo más reciente, en un esquema temporal'],
                    ['Frecuencia', 'el primer lunes de cada mes'], ['Comprobación', 'conteos de filas contra producción + bitácora con fecha y resultado']];
      for (var i = 0; i < 4; i++) {
        var y = 116 + i * 100, a = L.tramo(t, 0.28 + i * 0.13, 0.36 + i * 0.13);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 40, y, 220, 84, 10); L.rellena(ctx, L.tono(A, 0.1 + i * 0.1));
          UJ.rotulo(ctx, lz, (i + 1) + ' · ' + partes[i][0], 150, y + 28, { tam: 19, peso: 800, color: m.papel, ancho: 200 });
          L.rectRed(ctx, 268, y, 492, 84, 10); L.rellena(ctx, L.tono(A, 0.92), A, 2);
          UJ.rotulo(ctx, lz, partes[i][1], 284, y + 14, { tam: 19, peso: 500, alinear: 'left', ancho: 460 });
        });
      }
      UJ.rotulo(ctx, lz, 'Se puede auditar: sin registro del mes, no hay respaldo.', W / 2, 545,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
