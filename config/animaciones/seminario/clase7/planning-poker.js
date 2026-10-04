/* Planning poker: escala de puntos con una historia de referencia; dos estimaciones distintas
 * abren la discusión y se acuerda; un 13 es la señal de partir. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('planning-poker', {
    duracion: 5,
    // Pasos LOGICOS: 1) la escala con su referencia; 2) dos estimaciones distintas abren la
    // pregunta; 3) se discute, se acuerda y por eso vale; 4) el 13 es la señal de partir.
    pasos: [0.24, 0.58, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Planning poker: comparar tamaños', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      function carta(x, y, w, hh, v, borde, fondo, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, w, hh, 10); L.rellena(ctx, fondo || m.papel, borde || A, 3);
          UJ.rotulo(ctx, lz, v, x + w / 2, y + hh / 2 - 19, { tam: 32, peso: 800, color: borde || A });
        });
      }
      var vals = ['1', '2', '3', '5', '8', '13'];
      var acuerdo = L.tramo(t, 0.62, 0.72), trece = L.tramo(t, 0.84, 0.92);
      for (var i = 0; i < 6; i++) {
        var x = 110 + i * 100, b = A, f = m.papel;
        if (i === 2) { b = L.tono(m.sello, -0.35); f = L.mezclaColor(m.papel, L.tono(m.sello, 0.7), L.tramo(t, 0.14, 0.2)); }
        if (i === 3 && acuerdo > 0) { b = L.mezclaColor(A, V, acuerdo); f = L.mezclaColor(m.papel, L.tono(V, 0.8), acuerdo); }
        if (i === 5 && trece > 0) { b = L.mezclaColor(A, R, trece); f = L.mezclaColor(m.papel, L.tono(R, 0.82), trece); }
        carta(x, 74, 80, 104, vals[i], b, f, L.tramo(t, 0.02 + i * 0.02, 0.08 + i * 0.02));
      }
      UJ.rotulo(ctx, lz, 'referencia: registrar un dueño = 3', 350, 192, { tam: 17, peso: 700, color: L.tono(m.sello, -0.45), visible: L.tramo(t, 0.14, 0.22) });
      UJ.rotulo(ctx, lz, '13: señal de partirla', 650, 192, { tam: 17, peso: 800, color: R, visible: trece });
      // Dos jugadores muestran a la vez
      var ju = L.tramo(t, 0.26, 0.34);
      UJ.monigote(ctx, lz, 140, 270, 120, 'Ana', A, ju);
      UJ.monigote(ctx, lz, 660, 270, 120, 'Luis', A, ju);
      var mu = L.tramo(t, 0.36, 0.42, 'frena');
      carta(220, 290, 80, 104, '2', A, m.papel, mu);
      carta(500, 290, 80, 104, '8', A, m.papel, mu);
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.54), function () {
        L.rectRed(ctx, 290, 236, 220, 40, 20); L.rellena(ctx, L.tono(m.sello, 0.82), L.tono(m.sello, -0.3), 2);
        UJ.rotulo(ctx, lz, '¿qué entendiste tú?', 400, 245, { tam: 19, peso: 700 });
      });
      UJ.pildora(ctx, lz, 400, 440, 'se discute y se acuerda: 5', V, acuerdo, { tam: 19, centrar: true, lleno: true });
      UJ.rotulo(ctx, lz, 'Lo que vale es la discusión cuando uno dice 2 y otro 8', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.72, 0.78) });
    }
  });
})();
