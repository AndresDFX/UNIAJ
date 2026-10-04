/* Cardinalidad = valores distintos de una columna. Selectividad = fraccion de filas que
 * sobreviven al filtro (0..1). Pocas filas -> indice; muchas -> lectura completa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('selectividad', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.rectRed(ctx, 40, 30, W - 80, 150, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Cardinalidad = cantidad de valores distintos', W / 2, 44, { tam: 22, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'cita.estado → 3', 220, 98, { tam: 19, peso: 600 });
        UJ.rotulo(ctx, lz, 'dueno.id_dueno → 2.006', 570, 98, { tam: 19, peso: 600 });
        UJ.rotulo(ctx, lz, 'baja', 220, 136, { tam: 17, peso: 700, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'alta', 570, 136, { tam: 17, peso: 700, color: L.tono(C, -0.3) });
      });
      UJ.rotulo(ctx, lz, 'Selectividad = filas que sobreviven / filas totales', W / 2, 206, { tam: 22, peso: 800, color: L.tono(C, -0.3), ancho: W - 40, visible: L.tramo(t, 0.32, 0.4) });
      function barra(y, nombre, f, txt, a0) {
        var p = L.tramo(t, a0 + 0.06, a0 + 0.18, 'suave');
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.08), function () {
          L.texto(ctx, nombre, 40, y, { tam: 18, peso: 700, color: m.tinta, letra: 'Consolas, monospace' });
          L.rectRed(ctx, 40, y + 32, 560, 40, 8); L.rellena(ctx, L.tono(m.tinta, 0.9), L.tono(m.tinta, 0.5), 1);
          if (p > 0) { L.rectRed(ctx, 40, y + 32, Math.max(6, 560 * f * p), 40, 8); L.rellena(ctx, C); }
          UJ.rotulo(ctx, lz, txt, 690, y + 40, { tam: 22, peso: 800, color: A, visible: p });
        });
      }
      barra(256, "estado = 'PROGRAMADA'", 0.61, '0,61', 0.38);
      barra(366, 'dueno.id_dueno = 125', 1 / 2006, '≈ 0,0005', 0.5);
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.9), function () {
        L.rectRed(ctx, 40, 486, 350, 100, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'Muchas filas', 215, 500, { tam: 21, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'conviene leer la tabla entera', 215, 538, { tam: 17, ancho: 320 });
        L.rectRed(ctx, 410, 486, 350, 100, 14); L.rellena(ctx, L.tono(A, 0.88), A, 2);
        UJ.rotulo(ctx, lz, 'Pocas filas', 585, 500, { tam: 21, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'conviene ir por un índice', 585, 538, { tam: 17, ancho: 320 });
      });
    }
  });
})();
