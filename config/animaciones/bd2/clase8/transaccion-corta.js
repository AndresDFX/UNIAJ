/* Tuning como habito: la transaccion corta. Leer y validar primero, abrir la transaccion solo
 * para escribir (milisegundos). Nunca esperar a una persona con la transaccion abierta: una pausa
 * de almuerzo deja filas bloqueadas todo ese tiempo. En cargas masivas, COMMIT por lotes. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('transaccion-corta', {
    duracion: 5,
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      function barra(x, y, an, txt, color, p, fondo) {
        if (p <= 0) return;
        L.rectRed(ctx, x, y, an * p, 50, 8); L.rellena(ctx, fondo || L.tono(color, 0.75), color, 2);
        if (p > 0.9) L.texto(ctx, txt, x + an / 2, y + 14, { tam: 17, peso: 700, color: m.tinta, alinear: 'center', ancho: an - 8, letra: lz.letra });
      }
      // Bien
      UJ.rotulo(ctx, lz, 'Bien: transacción corta', 30, 30, { tam: 22, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0, 0.06) });
      barra(30, 80, 470, 'leer y validar (sin transacción)', L.tono(m.tinta, 0.3), L.tramo(t, 0.06, 0.2), L.tono(m.tinta, 0.88));
      barra(510, 80, 220, 'BEGIN … COMMIT', V, L.tramo(t, 0.22, 0.28));
      UJ.rotulo(ctx, lz, 'milisegundos', 620, 140, { tam: 18, peso: 700, color: V, visible: L.tramo(t, 0.28, 0.36) });
      // Mal
      UJ.rotulo(ctx, lz, 'Mal: esperar a una persona con la transacción abierta', 30, 200, { tam: 22, peso: 800, color: R, alinear: 'left', ancho: 740, visible: L.tramo(t, 0.42, 0.48) });
      barra(30, 250, 110, 'BEGIN', R, L.tramo(t, 0.48, 0.52));
      var p = L.tramo(t, 0.52, 0.66);
      if (p > 0) {
        L.rectRed(ctx, 145, 250, 470 * p, 50, 8); L.rellena(ctx, L.tono(R, 0.88), R, 2);
        if (p > 0.9) UJ.rotulo(ctx, lz, '¿Confirmar? … almuerzo …', 380, 262, { tam: 18, peso: 700, color: R });
      }
      barra(620, 250, 140, 'COMMIT', R, L.tramo(t, 0.66, 0.7));
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.7), function () {
        var r = 18; for (var k = 0; k < 5; k++) { L.rectRed(ctx, 210 + k * 70, 318, 54, 30, 6); L.rellena(ctx, L.tono(R, 0.6)); }
        UJ.rotulo(ctx, lz, 'filas bloqueadas para el resto mientras nadie vuelve', 380, 360, { tam: 19, peso: 700, color: R, ancho: 500 });
      });
      // Cargas masivas
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.84), function () {
        L.rectRed(ctx, 30, 430, 740, 170, 16); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Cargas masivas: COMMIT por lotes', 400, 446, { tam: 22, peso: 800, color: L.tono(C, -0.35) });
      });
      var n = Math.floor(L.mezcla(0, 10, L.tramo(t, 0.82, 0.96)));
      for (var i = 0; i < n; i++) {
        L.rectRed(ctx, 60 + i * 68, 500, 58, 40, 6); L.rellena(ctx, L.tono(C, 0.6), L.tono(C, -0.3), 2);
      }
      UJ.rotulo(ctx, lz, 'ni un COMMIT por fila, ni uno gigante: lotes intermedios', 400, 552, { tam: 18, ancho: 700, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
