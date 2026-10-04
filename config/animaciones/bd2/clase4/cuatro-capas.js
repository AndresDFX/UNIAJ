/* Las cuatro capas, en orden de preferencia, y una regla que cae en cada una. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cuatro-capas', {
    duracion: 5,
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      var capas = [
        ['1 · NOT NULL · CHECK · DEFAULT', 'una sola fila', 'stock >= 0'],
        ['2 · UNIQUE · FOREIGN KEY', 'entre filas y tablas', 'un veterinario, una franja'],
        ['3 · Trigger', 'OLD contra NEW, otra tabla', 'auditar el cambio de estado'],
        ['4 · Aplicación', 'lo que la base no puede saber', 'el formato del correo']
      ];
      for (var i = 0; i < 4; i++) {
        var y = 40 + i * 120, a = L.tramo(t, 0.02 + i * 0.07, 0.12 + i * 0.07);
        var col = L.tono(A, i * 0.18);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 24, y, 440, 100, 12); L.rellena(ctx, L.tono(A, 0.9 - i * 0.12), col, 3);
          UJ.rotulo(ctx, lz, capas[i][0], 40, y + 18, { tam: 21, peso: 800, alinear: 'left', color: L.tono(A, -0.2), ancho: 410 });
          UJ.rotulo(ctx, lz, capas[i][1], 40, y + 56, { tam: 18, peso: 500, alinear: 'left' });
        });
        // La regla que cae en su capa
        var t0 = 0.4 + i * 0.12, x = L.claves(t, [[t0, W + 20], [t0 + 0.1, 490, 'frena']]);
        if (t >= t0) {
          L.rectRed(ctx, x, y + 24, 286, 52, 26); L.rellena(ctx, m.sello || m.acento, m.tinta, 2);
          UJ.rotulo(ctx, lz, capas[i][2], x + 143, y + 37, { tam: 17, peso: 700, ancho: 270 });
        }
      }
      UJ.rotulo(ctx, lz, 'preferencia ↓', 470, 4, { tam: 16, color: m.tinta, alinear: 'left', visible: L.tramo(t, 0.3, 0.4) });
      UJ.rotulo(ctx, lz, 'Lo que solo vive en la app se salta por otra vía.', W / 2, 532, { tam: 21, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
