/* La firma de sp_facturar: dos arreglos emparejados por posicion (insumo i, cantidad i). Primero
 * se valida que midan lo mismo con IS DISTINCT FROM; luego la cabecera entra con total 0 y
 * RETURNING; el total sale del bucle: 22000x1 + 900x2 + 1200x3 = 27.400. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('sp-facturar-arreglos', {
    duracion: 5,
    pasos: [0.38, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 16, W - 40, 'CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);', L.tramo(t, 0, 0.12), 18);
      function arreglo(x, nombre, vals, color, a) {
        UJ.alfa(ctx, a, function () {
          UJ.rotulo(ctx, lz, nombre, x + 150, 80, { tam: 19, peso: 800, color: color });
          for (var i = 0; i < vals.length; i++) {
            L.rectRed(ctx, x + i * 100, 112, 90, 60, 10); L.rellena(ctx, L.tono(color, 0.9), color, 2);
            L.texto(ctx, String(vals[i]), x + i * 100 + 45, 126, { tam: 28, peso: 800, color: color, alinear: 'center', letra: lz.letra });
          }
        });
      }
      arreglo(50, 'p_insumos INT[]', [1, 6, 5], A, L.tramo(t, 0.1, 0.18));
      arreglo(450, 'p_cantidades INT[]', [1, 2, 3], C, L.tramo(t, 0.14, 0.22));
      for (var i = 0; i < 3; i++) {
        var p = L.tramo(t, 0.22 + i * 0.04, 0.3 + i * 0.04);
        if (p > 0) {
          ctx.save(); ctx.setLineDash([8, 6]);
          L.trazo(ctx, [[95 + i * 100, 172], [95 + i * 100, 200 + i * 14], [495 + i * 100, 200 + i * 14], [495 + i * 100, 172]], p, L.tono(m.tinta, 0.4), 2);
          ctx.restore();
        }
      }
      UJ.rotulo(ctx, lz, 'emparejados por posición: i = 1, 2, 3', W / 2, 252, { tam: 19, peso: 700, visible: L.tramo(t, 0.32, 0.38) });
      // Uno: validar longitudes
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.48), function () {
        L.rectRed(ctx, 30, 300, 740, 110, 14); L.rellena(ctx, L.tono(R, 0.93), R, 2);
        UJ.codigo(ctx, lz, 46, 314, 708, 'IF array_length(p_insumos,1) IS DISTINCT FROM array_length(p_cantidades,1)', 1, 15);
        UJ.rotulo(ctx, lz, 'longitudes distintas: RAISE EXCEPTION antes de tocar la base', 380, 364, { tam: 18, ancho: 600 });
      });
      UJ.sello(ctx, lz, 730, 370, 24, false, L.tramo(t, 0.5, 0.58));
      UJ.rotulo(ctx, lz, 'IS DISTINCT FROM: con un arreglo vacío, array_length da NULL', W / 2, 418, { tam: 17, color: R, ancho: 740, visible: L.tramo(t, 0.58, 0.66) });
      // Dos: cabecera y total
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        L.rectRed(ctx, 30, 460, 740, 150, 14); L.rellena(ctx, L.tono(A, 0.94), A, 2);
        UJ.codigo(ctx, lz, 46, 474, 708, 'INSERT INTO factura ... total 0 RETURNING id_factura INTO v_id_factura', 1, 15);
      });
      UJ.rotulo(ctx, lz, 'Total = 22000×1 + 900×2 + 1200×3', W / 2, 524, { tam: 20, peso: 600, visible: L.tramo(t, 0.8, 0.88) });
      UJ.rotulo(ctx, lz, '= 27.400', W / 2, 560, { tam: 28, peso: 800, color: A, visible: L.tramo(t, 0.88, 0.96) });
    }
  });
})();
