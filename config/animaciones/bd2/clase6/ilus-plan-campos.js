/* Ilustracion: una linea real del plan (Seq Scan on cita c, consulta del 2026-03-10) y lo que
 * significa cada campo. Los estimados y los reales, separados por color; abajo, la regla del
 * nodo mas costoso: tiempo POR VUELTA x loops. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-plan-campos', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Una línea del plan, campo por campo', W / 2, 10, { tam: 25, peso: 800, color: A });
      UJ.codigo(ctx, lz, 20, 54, W - 40, 'Seq Scan on cita c  (cost=0.00..701.15 rows=150 width=16)', 1, 16);
      UJ.codigo(ctx, lz, 20, 92, W - 40, '   (actual time=0.06..11.70 rows=150 loops=1)', 1, 16);
      UJ.rotulo(ctx, lz, 'lo que el motor ESTIMA (EXPLAIN)', 210, 142, { tam: 17, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'lo que PASÓ (EXPLAIN ANALYZE)', 600, 142, { tam: 17, peso: 800, color: V });
      var est = [['cost=0.00..701.15', 'arranque..total en unidad relativa (1 = leer una página), no ms'],
                 ['rows=150', 'filas que cree que saldrán'],
                 ['width=16', 'bytes promedio por fila']];
      var real = [['actual time', 'ms reales POR VUELTA del nodo'],
                  ['rows=150', 'filas que salieron: compárelas con las estimadas'],
                  ['loops=1', 'cuántas veces se repitió el nodo']];
      function columna(x, filas, col) {
        for (var i = 0; i < filas.length; i++) {
          var y = 176 + i * 100;
          L.rectRed(ctx, x, y, 370, 88, 12); L.rellena(ctx, L.tono(col, 0.9), col, 2);
          L.texto(ctx, filas[i][0], x + 14, y + 10, { tam: 18, peso: 700, color: L.tono(col, -0.25), letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, filas[i][1], x + 14, y + 40, { tam: 15, alinear: 'left', ancho: 344 });
        }
      }
      columna(20, est, A);
      columna(410, real, V);
      L.rectRed(ctx, 20, 488, W - 40, 128, 14); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.rotulo(ctx, lz, 'El nodo más costoso = actual time × loops', W / 2, 500, { tam: 21, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'y el tiempo de un nodo ya incluye el de sus hijos', W / 2, 536, { tam: 17, ancho: W - 80 });
      UJ.rotulo(ctx, lz, '0,5 ms con loops=2006 ≈ 1 segundo: parece el más barato y es el culpable', W / 2, 568, { tam: 17, peso: 700, ancho: W - 80 });
    }
  });
})();
