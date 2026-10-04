/* Nueve minutos repartidos en cinco tramos: 1 + 2 + 3 + 2 + 1. La barra se llena tramo a tramo
 * con lo que se dice en cada uno. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cinco-tramos', {
    duracion: 5,
    pasos: [0.3, 0.62, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, S = m.sello || C, R = m.malva || '#A02030', W = lz.ancho;
      var tr = [[1, 'El problema', '25 min de pie', A], [2, 'Afectados y decisión', 'qué se perdió', C],
        [3, 'Demo en vivo', '«Van 4 antes que usted»', L.tono(S, -0.35)], [2, 'Lo que cambió', 'tras probar', V], [1, 'Cierre', 'qué ahorra y a quién deja fuera', R]];
      var x0 = 40, ancho = 720, por = ancho / 9, x = x0;
      var t0 = [0, 0.12, 0.34, 0.64, 0.74];
      UJ.rotulo(ctx, lz, '9 minutos', W / 2, 30, { tam: 28, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 5; i++) {
        var w = tr[i][0] * por, a = L.tramo(t, t0[i], t0[i] + 0.1, 'frena'), col = tr[i][3];
        if (a > 0) {
          L.rectRed(ctx, x, 90, w * a, 90, 6); L.rellena(ctx, col, m.papel, 3);
          UJ.rotulo(ctx, lz, tr[i][0] + ' min', x + w / 2, 118, { tam: 24, peso: 800, color: m.papel, visible: L.tramo(a, 0.7, 1) });
          var ly = 220 + i * 74;
          UJ.alfa(ctx, L.tramo(a, 0.6, 1), function () {
            L.rectRed(ctx, x0 + 100, ly + 4, 44, 44, 8); L.rellena(ctx, col);
            UJ.rotulo(ctx, lz, String(tr[i][0]), x0 + 122, ly + 10, { tam: 22, peso: 800, color: m.papel });
            UJ.rotulo(ctx, lz, (i + 1) + ' · ' + tr[i][1], x0 + 164, ly, { tam: 22, peso: 800, color: col, alinear: 'left' });
            UJ.rotulo(ctx, lz, tr[i][2], x0 + 164, ly + 30, { tam: 18, alinear: 'left', ancho: 480 });
          });
        }
        x += w;
      }
      UJ.rotulo(ctx, lz, 'La demo es el tramo más largo.', W / 2, 600, { tam: 22, peso: 700, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
