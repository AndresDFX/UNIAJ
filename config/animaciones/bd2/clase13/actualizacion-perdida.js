/* Caso cuatro, concurrencia: la actualizacion perdida. Dos procesos leen stock 5, cada uno resta 3
 * y ambos escriben 2: salieron 6 unidades y el sistema dice 2. Ningun mensaje de error. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('actualizacion-perdida', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      // El stock en el centro
      var valor = t < 0.5 ? '5' : '2';
      UJ.alfa(ctx, 1, function () {
        L.rectRed(ctx, 300, 30, 200, 110, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
        UJ.rotulo(ctx, lz, 'insumo.stock', 400, 42, { tam: 19, peso: 700, color: A });
        UJ.rotulo(ctx, lz, valor, 400, 72, { tam: 46, peso: 800, color: t < 0.5 ? m.tinta : R });
      });
      function proceso(x, nombre, col, k) {
        UJ.caja(ctx, lz, x, 200, 240, 70, nombre, '', col, 1);
        var l1 = L.tramo(t, 0.06 + k * 0.06, 0.16 + k * 0.06);
        UJ.alfa(ctx, l1, function () { UJ.rotulo(ctx, lz, 'lee 5', x + 120, 290, { tam: 21, peso: 700, color: col }); });
        UJ.alfa(ctx, L.tramo(t, 0.34 + k * 0.04, 0.42 + k * 0.04), function () { UJ.rotulo(ctx, lz, '5 − 3 = 2', x + 120, 330, { tam: 21, peso: 700, color: col }); });
        UJ.alfa(ctx, L.tramo(t, 0.46 + k * 0.06, 0.54 + k * 0.06), function () { UJ.rotulo(ctx, lz, 'escribe 2', x + 120, 370, { tam: 21, peso: 800, color: col }); });
        var cx = x + 120;
        L.flecha(ctx, cx, 196, k ? 470 : 330, 144, col, 3, L.tramo(t, 0.46 + k * 0.06, 0.54 + k * 0.06));
      }
      proceso(30, 'Proceso 1', A, 0);
      proceso(530, 'Proceso 2', C, 1);
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.76), function () {
        L.rectRed(ctx, 60, 430, 300, 80, 12); L.rellena(ctx, L.tono(m.tinta, 0.9), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'salieron 6 unidades', 210, 456, { tam: 21, peso: 800 });
        L.rectRed(ctx, 440, 430, 300, 80, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'el sistema dice 2', 590, 456, { tam: 21, peso: 800, color: R });
      });
      UJ.rotulo(ctx, lz, 'Sin mensaje de error: se descubre semanas después.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
