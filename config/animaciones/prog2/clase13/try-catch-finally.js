/* try-catch-finally: el camino sin error y el camino con error; catch mas especifico primero. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('try-catch-finally', {
    duracion: 4.5,
    pasos: [0.25, 0.65, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, W = lz.ancho;
      var bloques = [
        ['try', 'leer("citas.txt")', A, 40],
        ['catch (FileNotFoundException e)', 'más específico: primero', C, 160],
        ['catch (IOException e)', 'más general: después', C, 280],
        ['finally', 'cerrar el archivo: siempre', m.sello, 400]
      ];
      for (var i = 0; i < 4; i++) {
        var b = bloques[i];
        UJ.alfa(ctx, L.tramo(t, 0.02 + i * 0.05, 0.08 + i * 0.05), function () {
          L.rectRed(ctx, 40, b[3], 430, 92, 12); L.rellena(ctx, L.tono(b[2], 0.88), b[2], 3);
          UJ.rotulo(ctx, lz, b[0], 60, b[3] + 14, { tam: 20, peso: 800, alinear: 'left', ancho: 400, color: L.tono(b[2], -0.4) });
          UJ.rotulo(ctx, lz, b[1], 60, b[3] + 52, { tam: 18, alinear: 'left', ancho: 400 });
        });
      }
      // Camino sin error: try -> finally (por la derecha)
      var p1 = L.tramo(t, 0.28, 0.42);
      if (p1 > 0) L.trazo(ctx, [[474, 86], [560, 86], [560, 446], [478, 446]], p1, V, 6);
      if (p1 >= 1) L.flecha(ctx, 500, 446, 476, 446, V, 6, 1);
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.48), function () {
        UJ.rotulo(ctx, lz, 'sin error', 575, 220, { tam: 22, peso: 800, alinear: 'left', color: V });
        UJ.rotulo(ctx, lz, 'try → finally', 575, 254, { tam: 18, alinear: 'left' });
      });
      // Camino con error: try -> catch FNF -> finally (por la izquierda)
      var p2 = L.tramo(t, 0.68, 0.84);
      if (p2 > 0) L.trazo(ctx, [[36, 100], [20, 100], [20, 206], [36, 206]], Math.min(1, p2 * 2), R, 6);
      if (p2 > 0.5) L.trazo(ctx, [[36, 220], [20, 220], [20, 460], [36, 460]], (p2 - 0.5) * 2, R, 6);
      UJ.rayo(ctx, 440, 50, 40, R, L.tramo(t, 0.66, 0.7));
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.9), function () {
        UJ.rotulo(ctx, lz, 'con error', 575, 330, { tam: 22, peso: 800, alinear: 'left', color: R });
        UJ.rotulo(ctx, lz, 'try → catch → finally', 575, 364, { tam: 18, alinear: 'left', ancho: 210 });
      });
      UJ.rotulo(ctx, lz, 'Entra al primer catch que encaja; si el general va primero, el específico no compila.', W / 2, 530, { tam: 19, ancho: W - 60, visible: L.tramo(t, 0.88, 0.97) });
    }
  });
})();
