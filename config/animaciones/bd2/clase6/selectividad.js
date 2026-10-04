/* Cardinalidad = valores distintos de una columna. Selectividad = fraccion de filas que
 * sobreviven al filtro (0..1). Cifras reales de la base sembrada: estado = 'PROGRAMADA' deja
 * 18.187 de 30.010 (0,61); el dia 2026-03-10 deja 150 (0,005); los dos juntos, 91 (0,003). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('selectividad', {
    duracion: 5,
    // Pasos LOGICOS: 1) cardinalidad; 2) selectividad de tres filtros reales; 3) la decision.
    pasos: [0.3, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // 1 · cardinalidad
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.rectRed(ctx, 40, 24, W - 80, 128, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Cardinalidad = cantidad de valores distintos', W / 2, 36, { tam: 22, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'cita.estado → 3', 220, 84, { tam: 19, peso: 600 });
        UJ.rotulo(ctx, lz, 'dueno.id_dueno → 2.006', 570, 84, { tam: 19, peso: 600 });
        UJ.rotulo(ctx, lz, 'baja', 220, 116, { tam: 17, peso: 700, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'alta', 570, 116, { tam: 17, peso: 700, color: L.tono(C, -0.3) });
      });
      // 2 · selectividad
      UJ.rotulo(ctx, lz, 'Selectividad = filas que sobreviven / filas totales', W / 2, 172, { tam: 21, peso: 800, color: L.tono(C, -0.3), ancho: W - 40, visible: L.tramo(t, 0.32, 0.38) });
      function barra(y, nombre, f, txt, a0) {
        var p = L.tramo(t, a0 + 0.04, a0 + 0.12, 'suave');
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.06), function () {
          L.texto(ctx, nombre, 40, y, { tam: 17, peso: 700, color: m.tinta, letra: 'Consolas, monospace' });
          L.rectRed(ctx, 40, y + 28, 520, 34, 8); L.rellena(ctx, L.tono(m.tinta, 0.9), L.tono(m.tinta, 0.5), 1);
          if (p > 0) { L.rectRed(ctx, 40, y + 28, Math.max(6, 520 * f * p), 34, 8); L.rellena(ctx, C); }
          UJ.rotulo(ctx, lz, txt, 670, y + 32, { tam: 19, peso: 800, color: A, visible: p });
        });
      }
      barra(212, "estado = 'PROGRAMADA'", 18187 / 30010, '18.187 · 0,61', 0.38);
      barra(292, 'fecha_hora del 2026-03-10', 150 / 30010, '150 · 0,005', 0.48);
      barra(372, 'los dos filtros juntos', 91 / 30010, '91 · 0,003', 0.58);
      // 3 · la decision
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.9), function () {
        L.rectRed(ctx, 40, 476, 350, 110, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'Muchas filas', 215, 490, { tam: 21, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'conviene leer la tabla entera', 215, 528, { tam: 17, ancho: 320 });
        L.rectRed(ctx, 410, 476, 350, 110, 14); L.rellena(ctx, L.tono(A, 0.88), A, 2);
        UJ.rotulo(ctx, lz, 'Pocas filas', 585, 490, { tam: 21, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'conviene ir por un índice', 585, 528, { tam: 17, ancho: 320 });
      });
    }
  });
})();
