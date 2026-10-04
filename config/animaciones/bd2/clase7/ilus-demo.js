/* Ilustracion: que observar en la demo de indices. La misma consulta antes y despues de crear
 * los indices y correr ANALYZE (planes reales de PGlite), y la poda de la particion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 8, { tam: 25, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'La agenda del 2026-03-10 (91 filas), sin cambiar una coma', W / 2, 50, { tam: 17, peso: 700, ancho: W - 40 });
      // antes
      L.rectRed(ctx, 16, 84, W - 32, 120, 14); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.rotulo(ctx, lz, 'ANTES', 40, 94, { tam: 17, peso: 800, color: R, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 124, W - 60, 'Seq Scan on cita  (rows=91)', 1, 15);
      UJ.rotulo(ctx, lz, 'Rows Removed by Filter: 29919', W / 2, 168, { tam: 15, peso: 700 });
      // en medio
      L.flecha(ctx, W / 2, 208, W / 2, 238, L.tono(m.tinta, 0.4), 4, 1);
      UJ.codigo(ctx, lz, 180, 242, 440, 'CREATE INDEX …;   ANALYZE cita;', 1, 16);
      L.flecha(ctx, W / 2, 278, W / 2, 304, L.tono(m.tinta, 0.4), 4, 1);
      // despues
      L.rectRed(ctx, 16, 308, W - 32, 124, 14); L.rellena(ctx, L.tono(V, 0.92), V, 2);
      UJ.rotulo(ctx, lz, 'DESPUÉS', 40, 318, { tam: 17, peso: 800, color: V, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 348, W - 60, 'Bitmap Heap Scan on cita  (rows=91)', 1, 15);
      UJ.codigo(ctx, lz, 30, 384, W - 60, '  ->  Bitmap Index Scan on idx_cita_programada_fecha', 1, 15);
      // particion
      L.rectRed(ctx, 16, 450, W - 32, 120, 14); L.rellena(ctx, L.tono(A, 0.93), A, 2);
      UJ.rotulo(ctx, lz, 'Partición: una consulta de 2026', 40, 460, { tam: 17, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 490, W - 60, '  ->  Seq Scan on cita_hist_2026 cita_hist', 1, 15);
      UJ.rotulo(ctx, lz, 'solo aparece la partición de 2026', W / 2, 534, { tam: 15, peso: 700 });
      UJ.rotulo(ctx, lz, 'Con estadísticas viejas el plan puede ignorar el índice: ANALYZE no es opcional.', W / 2, 590, { tam: 18, peso: 800, color: R, ancho: W - 40 });
    }
  });
})();
