/* Ilustracion: fn_descontar_stock por dentro (las tres partes) y su prueba en una consulta, con
 * la salida real: true | false | true, y stocks finales 5 y 0. Abajo, por que no se lee primero
 * y se decide despues: la ventana entre la lectura y la escritura. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-fn-boolean', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.codigo(ctx, lz, 16, 10, W - 32, 'fn_descontar_stock(p_id_insumo INT, p_cantidad INT) RETURNS BOOLEAN', 1, 15);
      var p = [['1', 'p_cantidad <= 0 → RAISE EXCEPTION: es una llamada mal hecha', R],
               ['2', 'UPDATE … AND stock >= p_cantidad: el mismo guardia', A],
               ['3', 'GET DIAGNOSTICS v_filas = ROW_COUNT; RETURN v_filas = 1;', V]];
      for (var i = 0; i < 3; i++) {
        var y = 56 + i * 54;
        L.circulo(ctx, 40, y + 20, 17); L.rellena(ctx, p[i][2]);
        UJ.rotulo(ctx, lz, p[i][0], 40, y + 9, { tam: 18, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, p[i][1], 70, y + 8, { tam: 16, peso: 600, alinear: 'left', ancho: W - 100 });
      }
      // la prueba
      L.rectRed(ctx, 16, 226, W - 32, 184, 14); L.rellena(ctx, L.tono(A, 0.94), A, 2);
      UJ.rotulo(ctx, lz, 'La prueba, en una sola consulta (stocks 8 y 3)', W / 2, 236, { tam: 17, peso: 800, color: A });
      var c = [['caso_ok', '(5, 3)', 'true', V], ['caso_sin_stock', '(2, 10)', 'false', C], ['caso_limite', '(2, 3)', 'true', V]];
      for (var k = 0; k < 3; k++) {
        var x = 40 + k * 245;
        L.rectRed(ctx, x, 270, 225, 120, 12); L.rellena(ctx, m.papel, L.tono(c[k][3], -0.1), 2);
        L.texto(ctx, c[k][0], x + 112, 282, { tam: 15, peso: 700, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
        L.texto(ctx, c[k][1], x + 112, 308, { tam: 15, peso: 500, color: L.tono(m.tinta, 0.2), alinear: 'center', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, c[k][2], x + 112, 336, { tam: 30, peso: 800, color: c[k][3] });
      }
      UJ.rotulo(ctx, lz, 'después: insumo 5 en 5 e insumo 2 en 0, ningún negativo', W / 2, 418, { tam: 16, peso: 700 });
      // la ventana
      L.rectRed(ctx, 16, 452, W - 32, 170, 14); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.rotulo(ctx, lz, 'Por qué no «leer primero y decidir después»', W / 2, 462, { tam: 18, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'recepción 1 lee stock 3 · recepción 2 lee stock 3', W / 2, 500, { tam: 16, ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'las dos deciden que alcanza y las dos descuentan', W / 2, 530, { tam: 16, ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'con el guardia en el WHERE, comprobar y escribir son una sola sentencia: no hay ventana', W / 2, 568, { tam: 16, peso: 700, color: L.tono(V, -0.3), ancho: W - 60 });
    }
  });
})();
