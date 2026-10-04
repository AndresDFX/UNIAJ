/* Ilustracion: el plan de la subconsulta correlacionada (contar mascotas por dueno) contra el
 * de la reescritura. ANTES: SubPlan con loops=2006 sobre mascota; DESPUES: un HashAggregate,
 * todo con loops=1. Cifras de una corrida real en PostgreSQL dentro del navegador. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-loops', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      // ANTES
      L.rectRed(ctx, 16, 12, W - 32, 292, 14); L.rellena(ctx, L.tono(R, 0.94), R, 2);
      UJ.rotulo(ctx, lz, 'ANTES · subconsulta en la lista de columnas', 34, 22, { tam: 19, peso: 800, color: R, alinear: 'left' });
      var a = ['Seq Scan on dueno d  (rows=2006 loops=1)', '  SubPlan 1',
               '    ->  Aggregate  (actual time=2.30  loops=2006)', '          ->  Seq Scan on mascota m  (loops=2006)',
               '                Rows Removed by Filter: 5006'];
      for (var i = 0; i < a.length; i++) UJ.codigo(ctx, lz, 30, 58 + i * 40, W - 60, a[i], 1, 15);
      // resaltar loops=2006
      ctx.strokeStyle = m.sello || '#FFD000'; ctx.lineWidth = 3;
      L.rectRed(ctx, 352, 138, 94, 30, 6); ctx.stroke();
      UJ.rotulo(ctx, lz, '2,3 ms × 2.006 vueltas ≈ 4,6 s: el nodo «barato» es el culpable', W / 2, 262, { tam: 17, peso: 800, color: R, ancho: W - 70 });
      // DESPUES
      L.rectRed(ctx, 16, 318, W - 32, 196, 14); L.rellena(ctx, L.tono(V, 0.92), V, 2);
      UJ.rotulo(ctx, lz, 'DESPUÉS · LEFT JOIN + GROUP BY', 34, 328, { tam: 19, peso: 800, color: V, alinear: 'left' });
      var d = ['HashAggregate  (rows=2006 loops=1)', '  ->  Hash Right Join  (loops=1)',
               '        ->  Seq Scan on mascota m  (loops=1)', '        ->  Seq Scan on dueno d  (loops=1)'];
      for (var k = 0; k < d.length; k++) UJ.codigo(ctx, lz, 30, 362 + k * 36, W - 60, d[k], 1, 15);
      // las dos condiciones del resultado correcto
      L.rectRed(ctx, 16, 528, 376, 96, 12); L.rellena(ctx, L.tono(A, 0.92), A, 2);
      UJ.rotulo(ctx, lz, 'LEFT, no INNER', 204, 538, { tam: 18, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'los 6 dueños sin mascotas siguen en la lista', 204, 568, { tam: 15, ancho: 340 });
      L.rectRed(ctx, 408, 528, 376, 96, 12); L.rellena(ctx, L.tono(A, 0.92), A, 2);
      UJ.rotulo(ctx, lz, 'COUNT(m.id_mascota)', 596, 538, { tam: 18, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'cuenta 0 donde COUNT(*) diría 1', 596, 568, { tam: 15, ancho: 340 });
    }
  });
})();
