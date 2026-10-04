/* Ilustracion: el cuerpo de sp_facturar en sus cuatro partes, de arriba abajo, con el caso de
 * prueba real: CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]) -> factura por 27.400 y los
 * stocks de los insumos 1, 6 y 5 en 11, 58 y 5 (verificado en PGlite). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-molde-sp', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.codigo(ctx, lz, 16, 10, W - 32, 'CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);', 1, 16);
      var p = [
        ['1', 'Validar los arreglos', 'IF array_length(…) IS DISTINCT FROM array_length(…) THEN RAISE EXCEPTION', R],
        ['2', 'La cabecera', 'INSERT INTO factura … total 0 RETURNING id_factura INTO v_id_factura', A],
        ['3', 'El bucle, una vuelta por línea', 'precio vigente (NOT FOUND) · UPDATE con el guardia · GET DIAGNOSTICS · RAISE si 0 · INSERT de la línea · v_total :=', C],
        ['4', 'El total', 'UPDATE factura SET total = v_total WHERE id_factura = v_id_factura', V]
      ];
      var ys = [58, 170, 282, 414], hs = [98, 98, 118, 98];
      for (var i = 0; i < p.length; i++) {
        var y = ys[i], h = hs[i];
        L.rectRed(ctx, 16, y, W - 32, h, 14); L.rellena(ctx, L.tono(p[i][3], 0.92), p[i][3], 2);
        L.circulo(ctx, 52, y + 34, 22); L.rellena(ctx, p[i][3]);
        UJ.rotulo(ctx, lz, p[i][0], 52, y + 20, { tam: 22, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, p[i][1], 88, y + 12, { tam: 19, peso: 800, color: L.tono(p[i][3], -0.25), alinear: 'left' });
        L.texto(ctx, p[i][2], 88, y + 44, { tam: 14, peso: 500, color: m.tinta, letra: 'Consolas, monospace', ancho: W - 130 });
        if (i < 3) L.flecha(ctx, 52, y + h + 1, 52, ys[i + 1] - 1, L.tono(m.tinta, 0.4), 3, 1);
      }
      L.rectRed(ctx, 16, 532, W - 32, 92, 14); L.rellena(ctx, L.tono(V, 0.88), V, 2);
      UJ.rotulo(ctx, lz, 'Resultado: 22.000×1 + 900×2 + 1.200×3 = 27.400', W / 2, 542, { tam: 20, peso: 800, color: L.tono(V, -0.3), ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'stocks de los insumos 1, 6 y 5: de 12, 60 y 8 a 11, 58 y 5', W / 2, 582, { tam: 16, ancho: W - 60 });
    }
  });
})();
