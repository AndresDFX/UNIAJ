/* Las dos fallas de un modelo: incompleto (le falta lo importante) o ruidoso (tiene todo y
 * nadie lo lee). El bueno responde su pregunta y nada más. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('modelo-dos-fallas', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un modelo puede fallar de dos formas', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var py = 80, ph = 330, pw = 236;
      function panel(x, tit, color, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, py, pw, ph, 14); L.rellena(ctx, L.tono(color, 0.94), color, 2.5);
          UJ.rotulo(ctx, lz, tit, x + pw / 2, py + 14, { tam: 22, peso: 800, color: L.tono(color, -0.2) });
        });
      }
      function cajita(x, y, an, al, txt, color) {
        L.rectRed(ctx, x, y, an, al, 6); L.rellena(ctx, m.papel, color, 2);
        if (txt) UJ.rotulo(ctx, lz, txt, x + an / 2, y + al / 2 - 10, { tam: 16, peso: 700, color: L.tono(color, -0.2) });
      }

      // Incompleto
      var xi = 20, ai = L.tramo(t, 0.04, 0.14);
      panel(xi, 'Incompleto', R, ai);
      UJ.alfa(ctx, ai, function () {
        cajita(xi + 20, py + 80, 90, 44, 'Dueño', A);
        cajita(xi + 20, py + 210, 90, 44, 'Cita', A);
        UJ.linea(ctx, xi + 65, py + 124, xi + 65, py + 210, A, 2);
      });
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.22), function () {
        ctx.save(); ctx.setLineDash([8, 6]);
        L.rectRed(ctx, xi + 132, py + 140, 86, 60, 8); L.rellena(ctx, L.tono(R, 0.9), R, 2.5);
        ctx.restore();
        UJ.rotulo(ctx, lz, '?', xi + 175, py + 150, { tam: 32, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'falta lo importante', xi + pw / 2, py + 280, { tam: 17, peso: 700, color: R });
      });

      // Ruido
      var xr = 544, ar = L.tramo(t, 0.32, 0.4);
      panel(xr, 'Ruido', R, ar);
      var n = 0;
      for (var f = 0; f < 8; f++) for (var c = 0; c < 5; c++) {
        var k = L.tramo(t, 0.34 + n * 0.003, 0.37 + n * 0.003); n++;
        if (k <= 0) continue;
        var cx = xr + 22 + c * 42, cy = py + 56 + f * 24;
        UJ.alfa(ctx, k, function () {
          L.rectRed(ctx, cx, cy, 30, 16, 3); L.rellena(ctx, L.tono(m.gris, 0.8), m.gris, 1.5);
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.54), function () {
        var l = [[0, 0, 4, 7], [4, 0, 1, 6], [2, 0, 3, 5], [0, 3, 4, 4], [1, 1, 3, 6], [3, 1, 0, 7], [4, 2, 2, 7], [0, 5, 4, 1]];
        for (var j = 0; j < l.length; j++) {
          L.trazo(ctx, [[xr + 37 + l[j][0] * 42, py + 64 + l[j][1] * 24], [xr + 37 + l[j][2] * 42, py + 64 + l[j][3] * 24]], 1, L.tono(m.tinta, 0.45), 1.5);
        }
        UJ.rotulo(ctx, lz, '40 elementos:', xr + pw / 2, py + 262, { tam: 17, peso: 700, color: R });
        UJ.rotulo(ctx, lz, 'nadie lo lee', xr + pw / 2, py + 286, { tam: 17, peso: 700, color: R });
      });

      // Centro: el bueno
      var xc = 282, ac = L.tramo(t, 0.62, 0.7);
      panel(xc, 'Suficiente', V, ac);
      UJ.alfa(ctx, ac, function () {
        cajita(xc + 20, py + 74, 90, 44, 'Dueño', A);
        cajita(xc + 126, py + 74, 90, 44, 'Mascota', A);
        cajita(xc + 73, py + 160, 90, 44, 'Cita', A);
        UJ.linea(ctx, xc + 110, py + 96, xc + 126, py + 96, A, 2);
        UJ.linea(ctx, xc + 171, py + 118, xc + 140, py + 160, A, 2);
      });
      UJ.sello(ctx, lz, xc + pw / 2, py + 244, 26, true, L.tramo(t, 0.7, 0.78));
      UJ.rotulo(ctx, lz, 'Responde su pregunta, nada más', xc + pw / 2, py + 280, { tam: 17, peso: 700, color: V, ancho: pw - 20, visible: L.tramo(t, 0.74, 0.82) });

      UJ.rotulo(ctx, lz, 'Prueba: un compañero lo explica en tres minutos.', W / 2, 520,
                { tam: 22, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
