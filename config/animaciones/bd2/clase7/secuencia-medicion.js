/* La secuencia de medicion en cuatro pasos y en ese orden: EXPLAIN ANALYZE antes, CREATE INDEX,
 * ANALYZE (que actualiza las estadisticas) y EXPLAIN ANALYZE despues. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('secuencia-medicion', {
    duracion: 5,
    // Pasos LOGICOS: un paso por etapa de la medicion; la flecha hacia una etapa aparece con ella.
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var p = [['1', 'EXPLAIN ANALYZE', 'ANTES de crear nada: sale Seq Scan, la línea base', A, 0.02],
               ['2', 'CREATE INDEX', 'los índices a probar, con su nombre exacto', A, 0.32],
               ['3', 'ANALYZE cita; ANALYZE mascota;', 'actualiza las estadísticas: no es opcional', R, 0.57],
               ['4', 'EXPLAIN ANALYZE', 'DESPUÉS: la misma consulta, sin cambiar una coma', A, 0.82]];
      for (var i = 0; i < 4; i++) {
        var y = 30 + i * 130;
        UJ.alfa(ctx, L.tramo(t, p[i][4], p[i][4] + 0.08), function () {
          var c = p[i][3];
          L.rectRed(ctx, 30, y, W - 60, 106, 14); L.rellena(ctx, L.tono(c, i === 2 ? 0.85 : 0.9), c, i === 2 ? 4 : 2);
          L.circulo(ctx, 80, y + 53, 30); L.rellena(ctx, c);
          UJ.rotulo(ctx, lz, p[i][0], 80, y + 36, { tam: 28, peso: 800, color: m.papel });
          L.texto(ctx, p[i][1], 130, y + 18, { tam: 22, peso: 700, color: c, letra: 'Consolas, monospace', ancho: W - 200 });
          UJ.rotulo(ctx, lz, p[i][2], 130, y + 60, { tam: 18, peso: 500, alinear: 'left', ancho: W - 200 });
        });
        if (i < 3) L.flecha(ctx, 80, y + 108, 80, y + 128, L.tono(m.tinta, 0.4), 3, L.tramo(t, p[i + 1][4], p[i + 1][4] + 0.04));
      }
      UJ.rotulo(ctx, lz, 'Cambiar el orden destruye la evidencia.', W / 2, 560, { tam: 22, ancho: W - 40, color: R, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
