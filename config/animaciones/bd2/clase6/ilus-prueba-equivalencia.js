/* Ilustracion: las dos pruebas de que optimizar no cambio el resultado. Con filtro: los dos
 * COUNT(*) en la misma corrida (91 = 91). Conjunto completo: EXCEPT en los dos sentidos, cero
 * filas. Y el contraejemplo real: con COUNT(*) en el LEFT JOIN salen 12 filas (6 por lado). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-prueba-equivalencia', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Se prueba con un resultado que se conoce de antemano', W / 2, 10, { tam: 23, peso: 800, color: A, ancho: W - 40 });
      // Prueba 1
      L.rectRed(ctx, 16, 56, 376, 300, 14); L.rellena(ctx, L.tono(A, 0.93), A, 2);
      UJ.rotulo(ctx, lz, 'Prueba 1 · consulta con filtro', 204, 68, { tam: 19, peso: 800, color: A });
      UJ.codigo(ctx, lz, 30, 108, 348, 'SELECT (SELECT COUNT(*) … ANTES),', 1, 14);
      UJ.codigo(ctx, lz, 30, 142, 348, '       (SELECT COUNT(*) … DESPUÉS);', 1, 14);
      UJ.rotulo(ctx, lz, 'en la misma corrida', 204, 184, { tam: 15, color: L.tono(m.tinta, 0.3) });
      UJ.rotulo(ctx, lz, '91', 130, 222, { tam: 44, peso: 800, color: A });
      UJ.rotulo(ctx, lz, '=', 204, 222, { tam: 44, peso: 800, color: V });
      UJ.rotulo(ctx, lz, '91', 278, 222, { tam: 44, peso: 800, color: A });
      UJ.sello(ctx, lz, 204, 312, 22, true, 1);
      // Prueba 2
      L.rectRed(ctx, 408, 56, 376, 300, 14); L.rellena(ctx, L.tono(V, 0.92), V, 2);
      UJ.rotulo(ctx, lz, 'Prueba 2 · conjunto completo', 596, 68, { tam: 19, peso: 800, color: V });
      UJ.codigo(ctx, lz, 422, 108, 348, '(ANTES EXCEPT DESPUÉS)', 1, 15);
      UJ.rotulo(ctx, lz, 'UNION ALL', 596, 148, { tam: 16, peso: 700 });
      UJ.codigo(ctx, lz, 422, 174, 348, '(DESPUÉS EXCEPT ANTES)', 1, 15);
      UJ.rotulo(ctx, lz, '0 filas', 596, 226, { tam: 38, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'los dos sentidos: uno solo no basta', 596, 274, { tam: 15, ancho: 340 });
      UJ.sello(ctx, lz, 596, 322, 22, true, 1);
      // Contraejemplo
      L.rectRed(ctx, 16, 372, W - 32, 134, 14); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.rotulo(ctx, lz, 'Con COUNT(*) en el LEFT JOIN, la prueba 2 devuelve 12 filas', W / 2, 384, { tam: 19, peso: 800, color: R, ancho: W - 70 });
      UJ.rotulo(ctx, lz, '6 dueños sin mascotas: ANTES dice 0, DESPUÉS dice 1', W / 2, 424, { tam: 17, ancho: W - 70 });
      UJ.sello(ctx, lz, W / 2, 476, 20, false, 1);
      // Lo que no es prueba
      UJ.rotulo(ctx, lz, 'Sin LIMIT en la prueba: las filas que fallan suelen ser las últimas.', W / 2, 528, { tam: 17, peso: 700, ancho: W - 40 });
      UJ.rotulo(ctx, lz, '«Se ve igual» no es una prueba.', W / 2, 566, { tam: 17, peso: 700, color: R, ancho: W - 40 });
    }
  });
})();
