/* El guardia del stock: dentro del bucle, precio vigente con NOT FOUND, el UPDATE con la condicion
 * en el WHERE, GET DIAGNOSTICS ROW_COUNT y RAISE si toco 0 filas. Dos casos: alcanza (1 fila) y
 * no alcanza (0 filas, se lanza). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('guardia-stock', {
    duracion: 5,
    pasos: [0.42, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      var lineas = [
        ['1', 'SELECT precio_unit INTO v_precio ...;  IF NOT FOUND'],
        ['2', 'UPDATE insumo SET stock = stock - p_cantidades[i]'],
        ['', '  WHERE id_insumo = p_insumos[i]'],
        ['', '    AND stock >= p_cantidades[i];'],
        ['3', 'GET DIAGNOSTICS v_filas = ROW_COUNT;'],
        ['4', 'IF v_filas = 0 THEN RAISE EXCEPTION ...']
      ];
      for (var i = 0; i < lineas.length; i++) {
        var a = L.tramo(t, 0.02 + i * 0.05, 0.08 + i * 0.05);
        UJ.codigo(ctx, lz, 70, 20 + i * 44, 700, lineas[i][1], a, 17);
        if (lineas[i][0]) UJ.alfa(ctx, a, function () {
          L.circulo(ctx, 40, 37 + i * 44, 17); L.rellena(ctx, C);
          UJ.rotulo(ctx, lz, lineas[i][0], 40, 26 + i * 44, { tam: 18, peso: 800, color: m.papel });
        });
      }
      // Resaltar la condicion del WHERE
      UJ.alfa(ctx, L.tramo(t, 0.32, 0.38), function () {
        L.rectRed(ctx, 66, 150, 708, 40, 8); ctx.strokeStyle = m.sello || C; ctx.lineWidth = 4; ctx.stroke();
      });
      UJ.rotulo(ctx, lz, 'comprobar y escribir: una sola sentencia', W / 2, 290, { tam: 20, peso: 800, color: A, visible: L.tramo(t, 0.34, 0.42) });
      // Caso que alcanza
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        L.rectRed(ctx, 30, 340, 360, 220, 16); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'insumo 3: hay 40, pide 2', 210, 356, { tam: 19, peso: 700, ancho: 330 });
        UJ.rotulo(ctx, lz, 'ROW_COUNT = 1', 210, 404, { tam: 26, peso: 800, color: V, ancho: 330 });
        UJ.rotulo(ctx, lz, 'stock 40 → 38, sigue el bucle', 210, 454, { tam: 18, ancho: 330 });
      });
      UJ.sello(ctx, lz, 210, 516, 24, true, L.tramo(t, 0.56, 0.64));
      // Caso que no alcanza
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.82), function () {
        L.rectRed(ctx, 410, 340, 360, 220, 16); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'insumo 2: hay 3, pide 10', 590, 356, { tam: 19, peso: 700, ancho: 330 });
        UJ.rotulo(ctx, lz, 'ROW_COUNT = 0', 590, 404, { tam: 26, peso: 800, color: R, ancho: 330 });
        UJ.rotulo(ctx, lz, 'stock intacto → RAISE EXCEPTION', 590, 454, { tam: 18, ancho: 330 });
      });
      UJ.sello(ctx, lz, 590, 516, 24, false, L.tramo(t, 0.84, 0.92));
      UJ.rotulo(ctx, lz, 'El precio se lee de la tabla: se cobra el vigente.', W / 2, 590, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
