/* Narrar contra sustentar: contar los documentos en el orden del calendario no defiende nada;
 * ordenar por problema, decisiones y evidencia, si. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('narrar-sustentar', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.36, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, R = m.malva, G = m.gris, T = m.tinta, W = lz.ancho;
      var px = [24, 412], pw = 364, py = 30, ph = 470;

      function panel(k, titulo, c, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, px[k], py, pw, ph, 14); L.rellena(ctx, L.tono(c, 0.94), c, 2.5);
          UJ.rotulo(ctx, lz, titulo, px[k] + pw / 2, py + 14, { tam: 25, peso: 800, color: L.tono(c, -0.2) });
        });
      }
      function bloque(k, y, h, cab, txt, c, a) {
        UJ.alfa(ctx, a, function () {
          var x = px[k] + 24, w = pw - 48;
          L.rectRed(ctx, x, y, w, h, 10); L.rellena(ctx, m.papel, c, 2.5);
          UJ.rotulo(ctx, lz, cab, x + w / 2, y + 10, { tam: 19, peso: 800, color: L.tono(c, -0.25), ancho: w - 20 });
          if (txt) UJ.rotulo(ctx, lz, txt, x + w / 2, y + 38, { tam: 17, peso: 500, color: T, ancho: w - 24 });
        });
      }

      // Narrar
      var gc = L.tono(G, -0.15);
      panel(0, 'Narrar', gc, L.tramo(t, 0, 0.06));
      var sem = [['Semana 1', 'casos de uso'], ['Semana 2', 'clases'], ['Semana 3', 'pantallas']];
      for (var i = 0; i < 3; i++) {
        var y = 92 + i * 104;
        bloque(0, y, 72, sem[i][0], sem[i][1], gc, L.tramo(t, 0.06 + i * 0.07, 0.12 + i * 0.07));
        if (i < 2) L.flecha(ctx, px[0] + pw / 2, y + 74, px[0] + pw / 2, y + 102, gc, 3, L.tramo(t, 0.11 + i * 0.07, 0.14 + i * 0.07));
      }
      UJ.sello(ctx, lz, px[0] + pw / 2 - 90, 446, 24, false, L.tramo(t, 0.28, 0.34));
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.35), function () {
        UJ.rotulo(ctx, lz, 'el orden del calendario', px[0] + pw / 2 + 24, 434, { tam: 18, peso: 700, color: R, ancho: 180 });
      });

      // Sustentar
      panel(1, 'Sustentar', A, L.tramo(t, 0.38, 0.44));
      var sus = [['Problema', 'se pierden fichas · 8 min por historial', R],
                 ['Decisiones', 'qué se diseñó para resolverlo', A],
                 ['Evidencia', 'el prototipo lo resuelve', V]];
      for (var k = 0; k < 3; k++) {
        var yy = 92 + k * 104;
        bloque(1, yy, 72, sus[k][0], sus[k][1], sus[k][2], L.tramo(t, 0.44 + k * 0.1, 0.52 + k * 0.1));
        if (k < 2) L.flecha(ctx, px[1] + pw / 2, yy + 74, px[1] + pw / 2, yy + 102, A, 3, L.tramo(t, 0.51 + k * 0.1, 0.54 + k * 0.1));
      }
      UJ.sello(ctx, lz, px[1] + pw / 2 - 90, 446, 24, true, L.tramo(t, 0.72, 0.78));
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.8), function () {
        UJ.rotulo(ctx, lz, 'el orden del argumento', px[1] + pw / 2 + 24, 434, { tam: 18, peso: 700, color: L.tono(V, -0.2), ancho: 180 });
      });

      UJ.rotulo(ctx, lz, 'Se ordena por problema resuelto, no por documento.', W / 2, 548,
                { tam: 23, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
