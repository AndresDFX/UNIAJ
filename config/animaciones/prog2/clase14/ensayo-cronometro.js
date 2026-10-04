/* Ensayo cronometrado: planeado contra real por bloque; uno se paso; el total queda en 5-8 min. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ensayo-cronometro', {
    duracion: 4.5,
    pasos: [0.35, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, W = lz.ancho;
      var bl = [['Problema', 1, 1], ['Arquitectura', 1, 2], ['Demo 1', 2, 2], ['Demo 2', 2, 1.5], ['Cierre', 1, 1]];
      var x0 = 190, esc = 120, y0 = 90, fila = 72;
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () {
        L.rectRed(ctx, 200, 20, 22, 22, 4); L.rellena(ctx, L.tono(A, 0.3));
        UJ.rotulo(ctx, lz, 'planeado', 232, 20, { tam: 18, alinear: 'left' });
        L.rectRed(ctx, 360, 20, 22, 22, 4); L.rellena(ctx, C);
        UJ.rotulo(ctx, lz, 'real (cronómetro)', 392, 20, { tam: 18, alinear: 'left' });
      });
      for (var i = 0; i < 5; i++) {
        var y = y0 + i * fila;
        var a1 = L.tramo(t, 0.04 + i * 0.05, 0.1 + i * 0.05, 'frena');
        var a2 = L.tramo(t, 0.38 + i * 0.05, 0.44 + i * 0.05, 'frena');
        UJ.rotulo(ctx, lz, bl[i][0], x0 - 16, y + 16, { tam: 20, peso: 700, alinear: 'right', visible: a1 > 0 ? 1 : 0 });
        if (a1 > 0) { L.rectRed(ctx, x0, y, bl[i][1] * esc * a1, 26, 6); L.rellena(ctx, L.tono(A, 0.3)); }
        if (a2 > 0) {
          var paso = bl[i][2] > bl[i][1];
          L.rectRed(ctx, x0, y + 30, bl[i][2] * esc * a2, 26, 6); L.rellena(ctx, paso && a2 >= 1 ? R : C);
          UJ.rotulo(ctx, lz, String(bl[i][2]).replace('.', ',') + ' min', x0 + bl[i][2] * esc * a2 + 10, y + 32, { tam: 17, peso: 700, alinear: 'left', color: paso && a2 >= 1 ? R : m.tinta });
        }
      }
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.64), function () {
        UJ.rotulo(ctx, lz, 'se pasó: +1 min', x0 + 2 * esc + 100, y0 + fila + 32, { tam: 18, peso: 800, color: R, alinear: 'left' });
      });
      // Total
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.84), function () {
        var yT = 470, xs = function (min) { return 40 + min * 80; };
        L.rectRed(ctx, xs(0), yT, xs(9) - xs(0), 20, 10); L.rellena(ctx, L.tono(m.tinta, 0.88));
        L.rectRed(ctx, xs(5), yT, xs(8) - xs(5), 20, 0); L.rellena(ctx, L.tono(V, 0.55));
        for (var k = 0; k <= 9; k++) UJ.rotulo(ctx, lz, String(k), xs(k), yT + 26, { tam: 16 });
        UJ.rotulo(ctx, lz, 'Total del ensayo (min)', 40, yT - 30, { tam: 18, peso: 700, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'rango 5–8 min', (xs(5) + xs(8)) / 2, yT - 30, { tam: 18, peso: 700, color: V });
        L.circulo(ctx, xs(7.5), yT + 10, 14); L.rellena(ctx, C, m.papel, 3);
        UJ.rotulo(ctx, lz, 'Ejemplo: total real 7,5 min · dentro del rango; recortar la teoría, nunca la demo.', W / 2, 540, { tam: 19, ancho: W - 40, peso: 600 });
      });
    }
  });
})();
