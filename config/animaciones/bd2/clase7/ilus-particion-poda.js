/* Ilustracion: las tres pruebas del particionamiento. El reparto (tableoid::regclass), la poda
 * en el plan (solo aparece cita_hist_2026) y el archivado (DROP de una particion contra DELETE
 * masivo). Salidas reales de PGlite con la siembra de la demo (todas las citas son de 2026). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-particion-poda', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      // 1 · reparto
      L.rectRed(ctx, 16, 12, W - 32, 196, 14); L.rellena(ctx, L.tono(A, 0.94), A, 2);
      UJ.rotulo(ctx, lz, '1 · ¿En qué partición quedó cada fila?', 32, 22, { tam: 18, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 56, W - 60, 'SELECT tableoid::regclass AS particion, COUNT(*) FROM cita_hist GROUP BY 1;', 1, 14);
      UJ.tabla(ctx, lz, 200, 100, 400, 'particion · count', ['cita_hist_2026 · 30010'], 1, A, 0);
      UJ.rotulo(ctx, lz, 'tableoid dice en qué tabla física vive la fila', W / 2, 190 - 2, { tam: 14, color: L.tono(m.tinta, 0.2) });
      // 2 · poda
      L.rectRed(ctx, 16, 222, W - 32, 170, 14); L.rellena(ctx, L.tono(V, 0.92), V, 2);
      UJ.rotulo(ctx, lz, '2 · La poda: una consulta de 2026 lee solo su partición', 32, 232, { tam: 18, peso: 800, color: V, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 266, W - 60, 'Aggregate', 1, 15);
      UJ.codigo(ctx, lz, 30, 302, W - 60, '  ->  Seq Scan on cita_hist_2026 cita_hist', 1, 15);
      UJ.rotulo(ctx, lz, 'cita_hist_2025 ni aparece en el plan: se descartó antes de leer', W / 2, 348, { tam: 15, peso: 700, color: L.tono(V, -0.3), ancho: W - 60 });
      // 3 · archivado
      L.rectRed(ctx, 16, 406, 376, 214, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
      UJ.rotulo(ctx, lz, '3 · Archivar un año', 204, 416, { tam: 18, peso: 800, color: V });
      UJ.codigo(ctx, lz, 30, 452, 348, 'DROP TABLE cita_hist_2025;', 1, 15);
      UJ.rotulo(ctx, lz, 'operación de metadatos: un instante', 204, 500, { tam: 16, peso: 700, ancho: 340 });
      UJ.rotulo(ctx, lz, '(DETACH PARTITION la separa sin borrarla)', 204, 540, { tam: 14, ancho: 340 });
      UJ.sello(ctx, lz, 204, 590, 18, true, 1);
      L.rectRed(ctx, 408, 406, 376, 214, 14); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.rotulo(ctx, lz, 'Sin particiones', 596, 416, { tam: 18, peso: 800, color: R });
      UJ.codigo(ctx, lz, 422, 452, 348, 'DELETE FROM cita WHERE fecha_hora < …', 1, 14);
      UJ.rotulo(ctx, lz, 'fila por fila: registro de transacciones enorme y bloqueos largos', 596, 500, { tam: 16, peso: 700, ancho: 340 });
      UJ.sello(ctx, lz, 596, 590, 18, false, 1);
    }
  });
})();
