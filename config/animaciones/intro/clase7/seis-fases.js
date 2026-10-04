/* Las seis fases del ciclo de vida, en dos filas de tres. Cada fase entrega lo que la
 * siguiente necesita. Construccion es una de seis. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('seis-fases', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, S = m.sello || m.acento, W = lz.ancho;
      var fs = [['1 · Definición', 'qué y para quién'], ['2 · Requisitos', 'qué debe hacer'], ['3 · Diseño', 'cómo estará hecha'],
        ['4 · Construcción', 'se construye'], ['5 · Validación', 'con el usuario real'], ['6 · Operación', 'funciona y se retira']];
      var pos = [[30, 60], [290, 60], [550, 60], [550, 300], [290, 300], [30, 300]];
      var t0 = [0, 0.12, 0.3, 0.42, 0.56, 0.68];
      for (var i = 0; i < 6; i++) {
        var p = pos[i], dest = i === 3;
        UJ.caja(ctx, lz, p[0], p[1], 220, 120, fs[i][0], fs[i][1], dest ? L.tono(S, -0.4) : A, L.tramo(t, t0[i], t0[i] + 0.1));
        if (i < 5) {
          var q = pos[i + 1], ar = L.tramo(t, t0[i + 1] - 0.03, t0[i + 1]), col = L.tono(m.tinta, 0.4);
          if (i === 2) L.flecha(ctx, 660, 182, 660, 298, col, 4, ar);
          else if (i < 2) L.flecha(ctx, p[0] + 222, 120, q[0] - 2, 120, col, 4, ar);
          else L.flecha(ctx, p[0] - 2, 360, q[0] + 222, 360, col, 4, ar);
        }
      }
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.54), function () {
        L.rectRed(ctx, 560, 432, 200, 44, 22); L.rellena(ctx, S, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'es una de seis', 660, 442, { tam: 19, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'Cada fase produce lo que la siguiente necesita para no adivinar.', W / 2, 530, { tam: 23, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
