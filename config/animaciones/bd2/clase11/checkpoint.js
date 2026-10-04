/* El unico valor de un punto de control intermedio es que todavia hay tiempo para corregir.
 * Con hallazgos, el defecto se corrige antes de la entrega; con «todo bien», llega a la entrega. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('checkpoint', {
    duracion: 5,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      function linea(y, a) {
        L.trazo(ctx, [[60, y], [740, y]], a, L.tono(m.tinta, 0.6), 4);
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, 260, y, 12); L.rellena(ctx, C, m.papel, 3);
          L.circulo(ctx, 700, y, 12); L.rellena(ctx, A, m.papel, 3);
          UJ.rotulo(ctx, lz, 'checkpoint', 260, y + 20, { tam: 17, peso: 700, color: C });
          UJ.rotulo(ctx, lz, 'entrega', 700, y + 20, { tam: 17, peso: 700, color: A });
        });
      }
      linea(110, L.tramo(t, 0, 0.12));
      var tp = L.tramo(t, 0.12, 0.26, 'suave');
      if (tp > 0) {
        L.rectRed(ctx, 260, 50, 440 * tp, 32, 6); L.rellena(ctx, L.tono(V, 0.75));
        UJ.rotulo(ctx, lz, 'tiempo para corregir', 480, 55, { tam: 18, peso: 800, color: L.tono(V, -0.3), visible: L.tramo(t, 0.22, 0.28) });
      }
      // Con hallazgos
      linea(260, L.tramo(t, 0.32, 0.38));
      UJ.rotulo(ctx, lz, 'Con hallazgos concretos', 60, 196, { tam: 21, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0.32, 0.38) });
      var x = L.claves(t, [[0.38, 60], [0.5, 250, 'frena']]);
      if (t >= 0.38) UJ.alfa(ctx, 1 - L.tramo(t, 0.54, 0.6), function () { L.circulo(ctx, x, 260, 10); L.rellena(ctx, R); });
      UJ.rotulo(ctx, lz, 'defecto', 130, 222, { tam: 16, color: R, visible: L.tramo(t, 0.38, 0.42) });
      UJ.sello(ctx, lz, 480, 260, 22, true, L.tramo(t, 0.52, 0.6));
      UJ.rotulo(ctx, lz, 'se corrige a tiempo', 480, 290, { tam: 17, peso: 700, color: V, visible: L.tramo(t, 0.54, 0.62) });
      // Todo bien, sigan asi
      linea(430, L.tramo(t, 0.66, 0.72));
      UJ.rotulo(ctx, lz, '«Todo bien, sigan así»', 60, 366, { tam: 21, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0.66, 0.72) });
      var x2 = L.claves(t, [[0.72, 60], [0.88, 690, 'suave']]);
      if (t >= 0.72) { L.circulo(ctx, x2, 430, 10); L.rellena(ctx, R); }
      UJ.sello(ctx, lz, 700, 392, 20, false, L.tramo(t, 0.88, 0.94));
      UJ.rotulo(ctx, lz, 'el defecto llega a la entrega', 560, 466, { tam: 17, peso: 700, color: R, visible: L.tramo(t, 0.88, 0.94) });
      UJ.rotulo(ctx, lz, 'Sin hallazgos, el checkpoint se desperdicia.', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
