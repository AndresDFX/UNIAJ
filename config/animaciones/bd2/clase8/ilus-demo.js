/* Ilustracion: que observar en la demo de transacciones. La foto inicial, el CALL que falla a
 * mitad (mensaje real) y la foto final identica: el descuento del insumo 3 se deshizo solo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar: dos fotos idénticas', W / 2, 8, { tam: 24, peso: 800, color: A });
      function foto(y, titulo, col) {
        L.rectRed(ctx, 16, y, W - 32, 140, 14); L.rellena(ctx, L.tono(col, 0.92), col, 2);
        UJ.rotulo(ctx, lz, titulo, 36, y + 10, { tam: 18, peso: 800, color: col, alinear: 'left' });
        var c = [['facturas', '1'], ['líneas', '3'], ['stock_3', '40'], ['stock_2', '3']];
        for (var i = 0; i < 4; i++) {
          var x = 40 + i * 185;
          L.rectRed(ctx, x, y + 44, 165, 82, 10); L.rellena(ctx, m.papel, L.tono(col, 0.3), 2);
          L.texto(ctx, c[i][0], x + 82, y + 52, { tam: 15, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, c[i][1], x + 82, y + 76, { tam: 32, peso: 800, color: A });
        }
      }
      foto(50, 'Foto inicial', A);
      // el CALL que falla
      L.rectRed(ctx, 16, 206, W - 32, 196, 14); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.codigo(ctx, lz, 30, 218, W - 60, 'CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);', 1, 16);
      UJ.rotulo(ctx, lz, 'insumo 3: hay 40, pide 2 → descuenta (40 → 38)', W / 2, 266, { tam: 17, peso: 700, ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'insumo 2: hay 3, pide 10 → 0 filas → RAISE EXCEPTION', W / 2, 300, { tam: 17, peso: 700, ancho: W - 60 });
      L.texto(ctx, 'ERROR: stock insuficiente del insumo 2 (se pidieron 10)', W / 2, 344, { tam: 15, peso: 700, color: R, alinear: 'center', letra: 'Consolas, monospace' });
      UJ.sello(ctx, lz, W - 50, 236, 20, false, 1);
      foto(418, 'Foto final: la misma consulta', V);
      UJ.rotulo(ctx, lz, 'El stock del insumo 3 volvió a 40 y nadie escribió ROLLBACK.', W / 2, 590, { tam: 18, peso: 800, color: V, ancho: W - 40 });
    }
  });
})();
