/* Las cuatro etapas de la huella de un sistema, en orden: fabricacion, uso, red y fin de vida.
 * En un celular, la mayor parte ya esta gastada en la fabricacion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('etapas-huella', {
    duracion: 5,
    pasos: [0.25, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var et = [
        ['1 · FABRICACIÓN', 'minería, ensamblaje, transporte', R],
        ['2 · USO', 'electricidad y enfriamiento', A],
        ['3 · RED', 'antenas, cables, equipos', C],
        ['4 · FIN DE VIDA', 'residuo electrónico (RAEE)', V]
      ];
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, i * 0.25, i * 0.25 + 0.1), y = 30 + i * 118;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 40, y, 420, 96, 14); L.rellena(ctx, L.tono(et[i][2], 0.88), et[i][2], 3);
          UJ.rotulo(ctx, lz, et[i][0], 64, y + 14, { tam: 25, peso: 800, color: et[i][2], alinear: 'left' });
          UJ.rotulo(ctx, lz, et[i][1], 64, y + 54, { tam: 20, alinear: 'left', ancho: 380 });
        });
        if (i < 3) L.flecha(ctx, 250, y + 98, 250, y + 116, L.tono(m.tinta, 0.4), 3, L.tramo(t, (i + 1) * 0.25 - 0.02, (i + 1) * 0.25 + 0.02));
      }
      // El celular: la mayor parte, antes de encenderlo
      UJ.alfa(ctx, L.tramo(t, 0.08, 0.2), function () {
        L.rectRed(ctx, 560, 40, 150, 260, 22); L.rellena(ctx, L.tono(m.tinta, 0.85), m.tinta, 4);
        var h = 200 * L.tramo(t, 0.1, 0.24, 'frena');
        L.rectRed(ctx, 578, 270 - h, 114, h, 8); L.rellena(ctx, L.tono(R, 0.4));
        UJ.rotulo(ctx, lz, 'Un celular: la mayor parte de su huella ya está gastada antes de encenderlo', 635, 316, { tam: 18, peso: 700, color: R, ancho: 300 });
      });
      UJ.rotulo(ctx, lz, 'Alargar la vida útil pesa más que ahorrar batería.', 635, 470, { tam: 20, peso: 700, ancho: 300, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
