/* La revision tecnica: un artefacto en el centro, cuatro roles alrededor, y se sale con un
 * producto escrito, el acta de hallazgos. No es avance, ni calificacion, ni demostracion. Y dos
 * reglas: se revisa el artefacto y no la persona, y el problema se registra, no se arregla ahi. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('revision-roles', {
    duracion: 5,
    // Pasos LOGICOS: 1) el objetivo y el artefacto; 2) los cuatro roles; 3) el producto, el
    // acta; 4) las dos reglas de la sesion.
    pasos: [0.28, 0.6, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.caja(ctx, lz, 290, 190, 220, 90, 'Artefacto', 'ER · DDL · script', A, L.tramo(t, 0, 0.1));
      UJ.rotulo(ctx, lz, 'Objetivo: encontrar defectos antes de que cuesten caro', W / 2, 20,
                { tam: 21, peso: 700, ancho: W - 60, color: A, visible: L.tramo(t, 0.1, 0.24) });
      var roles = [
        [30, 100, 'Autor', 'presenta'],
        [570, 100, 'Revisores', 'buscan defectos'],
        [30, 300, 'Moderador', 'cuida tiempo y tono'],
        [570, 300, 'Escriba', 'registra hallazgos']
      ];
      for (var i = 0; i < 4; i++) {
        var r = roles[i], a = L.tramo(t, 0.3 + i * 0.065, 0.37 + i * 0.065);
        UJ.caja(ctx, lz, r[0], r[1], 200, 80, r[2], r[3], C, a);
        var x1 = r[0] < 300 ? r[0] + 200 : r[0], y1 = r[1] + 40;
        var x2 = r[0] < 300 ? 290 : 510, y2 = 235;
        L.flecha(ctx, x1, y1, x2, y2, L.tono(C, -0.1), 3, L.tramo(t, 0.34 + i * 0.065, 0.4 + i * 0.065));
      }
      // 3 · El producto escrito
      L.flecha(ctx, W / 2, 284, W / 2, 396, A, 4, L.tramo(t, 0.62, 0.68, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.73), function () {
        L.rectRed(ctx, 250, 400, 300, 110, 10); L.rellena(ctx, m.papel, A, 3);
        UJ.rotulo(ctx, lz, 'Acta de hallazgos', W / 2, 412, { tam: 24, peso: 800, color: A });
        for (var k = 0; k < 3; k++) { L.rectRed(ctx, 280, 452 + k * 18, 240 - k * 40, 8, 4); L.rellena(ctx, L.tono(A, 0.6)); }
      });
      UJ.rotulo(ctx, lz, 'No es avance, ni nota, ni demostración.', W / 2, 520,
                { tam: 20, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.72, 0.79) });
      // 4 · Las dos reglas
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.9), function () {
        L.rectRed(ctx, 30, 556, 740, 76, 12); L.rellena(ctx, L.tono(R, 0.92), R, 2);
        UJ.rotulo(ctx, lz, '1 · Se revisa el artefacto, no la persona.', W / 2, 566, { tam: 18, peso: 700, color: L.tono(R, -0.2), ancho: 720 });
        UJ.rotulo(ctx, lz, '2 · El problema se registra; no se arregla en la reunión.', W / 2, 598, { tam: 18, peso: 700, color: L.tono(R, -0.2), ancho: 720 });
      });
    }
  });
})();
