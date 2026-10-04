/* fn_precio_consulta: tres formas de escribir la especie llegan a UPPER y salen iguales; el
 * CASE elige la tarifa (con ELSE para la especie que nadie previo); COALESCE vuelve FALSE la
 * urgencia que llega nula. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('fn-precio-consulta', {
    duracion: 4.8,
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var entradas = ["'Canino'", "'canino'", "'CANINO'"];
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, 0.02 + i * 0.05, 0.12 + i * 0.05);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 24, 40 + i * 64, 150, 46, 10); L.rellena(ctx, L.tono(C, 0.85), C, 2);
          UJ.rotulo(ctx, lz, entradas[i], 99, 50 + i * 64, { tam: 20, peso: 600 });
        });
        L.flecha(ctx, 178, 63 + i * 64, 270, 127, C, 3, L.tramo(t, 0.2, 0.32, 'frena'));
      }
      UJ.caja(ctx, lz, 276, 92, 150, 70, 'UPPER()', null, A, L.tramo(t, 0.18, 0.28));
      L.flecha(ctx, 430, 127, 490, 127, A, 4, L.tramo(t, 0.32, 0.4, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.42), function () {
        L.rectRed(ctx, 494, 104, 150, 46, 10); L.rellena(ctx, m.sello || C);
        UJ.rotulo(ctx, lz, "'CANINO'", 569, 114, { tam: 20, peso: 800 });
      });
      // El CASE
      var elige = L.tramo(t, 0.5, 0.58) > 0.5 ? 0 : -1;
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () {
        UJ.tabla(ctx, lz, 300, 196, 380, 'CASE UPPER(p_especie)', ["WHEN 'CANINO' THEN 45000", "WHEN 'FELINO' THEN 40000", 'ELSE 35000'], 3, A, elige);
      });
      // COALESCE
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.7), function () {
        L.rectRed(ctx, 24, 440, 170, 46, 10); L.rellena(ctx, L.tono(m.tinta, 0.88), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'urgencia: NULL', 109, 450, { tam: 19, peso: 600 });
      });
      L.flecha(ctx, 198, 463, 270, 463, A, 4, L.tramo(t, 0.7, 0.76, 'frena'));
      UJ.caja(ctx, lz, 276, 428, 250, 70, 'COALESCE(…, FALSE)', null, A, L.tramo(t, 0.7, 0.78));
      L.flecha(ctx, 530, 463, 590, 463, A, 4, L.tramo(t, 0.78, 0.84, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.9), function () {
        L.rectRed(ctx, 594, 440, 180, 46, 10); L.rellena(ctx, m.sello || C);
        UJ.rotulo(ctx, lz, 'sin recargo', 684, 450, { tam: 20, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'Nunca devuelve nulo: toda entrada tiene tarifa.', W / 2, 560,
                { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
