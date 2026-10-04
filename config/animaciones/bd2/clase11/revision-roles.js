/* La revision tecnica: un artefacto en el centro, cuatro roles alrededor, y se sale con un
 * producto escrito, el acta de hallazgos. No es avance, ni calificacion, ni demostracion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('revision-roles', {
    duracion: 4.6,
    pasos: [0.3, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.caja(ctx, lz, 290, 190, 220, 90, 'Artefacto', 'ER · DDL · script', A, L.tramo(t, 0, 0.12));
      UJ.rotulo(ctx, lz, 'Objetivo: encontrar defectos antes de que cuesten caro', W / 2, 20,
                { tam: 21, peso: 700, ancho: W - 60, color: A, visible: L.tramo(t, 0.1, 0.28) });
      var roles = [
        [30, 100, 'Autor', 'presenta'],
        [570, 100, 'Revisores', 'buscan defectos'],
        [30, 300, 'Moderador', 'cuida tiempo y tono'],
        [570, 300, 'Escriba', 'registra hallazgos']
      ];
      for (var i = 0; i < 4; i++) {
        var r = roles[i], a = L.tramo(t, 0.32 + i * 0.08, 0.42 + i * 0.08);
        UJ.caja(ctx, lz, r[0], r[1], 200, 80, r[2], r[3], C, a);
        var x1 = r[0] < 300 ? r[0] + 200 : r[0], y1 = r[1] + 40;
        var x2 = r[0] < 300 ? 290 : 510, y2 = 235;
        L.flecha(ctx, x1, y1, x2, y2, L.tono(C, -0.1), 3, L.tramo(t, 0.38 + i * 0.08, 0.46 + i * 0.08));
      }
      // El producto escrito
      L.flecha(ctx, W / 2, 284, W / 2, 404, A, 4, L.tramo(t, 0.7, 0.78, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.86), function () {
        L.rectRed(ctx, 250, 408, 300, 120, 10); L.rellena(ctx, m.papel, A, 3);
        UJ.rotulo(ctx, lz, 'Acta de hallazgos', W / 2, 420, { tam: 24, peso: 800, color: A });
        for (var k = 0; k < 3; k++) { L.rectRed(ctx, 280, 462 + k * 20, 240 - k * 40, 8, 4); L.rellena(ctx, L.tono(A, 0.6)); }
      });
      UJ.rotulo(ctx, lz, 'No es avance, ni nota, ni demostración.', W / 2, 560,
                { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
