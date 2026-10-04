/* La ley de Brooks contada como parejas que se tienen que poner de acuerdo: 2 personas -> 1,
 * 5 -> 10, 10 -> 45. La formula n x (n - 1) / 2 al final. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ley-brooks', {
    duracion: 5,
    pasos: [0.25, 0.5, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      function grupo(cx, cy, r, n, a, color, titulo, pares) {
        if (a <= 0) return;
        var pts = [];
        for (var i = 0; i < n; i++) {
          var ang = -Math.PI / 2 + i * 2 * Math.PI / n;
          pts.push([cx + Math.cos(ang) * r, cy + Math.sin(ang) * r]);
        }
        var total = n * (n - 1) / 2, k = 0, ver = Math.round(total * L.tramo(a, 0.3, 1));
        for (var p = 0; p < n; p++) for (var q = p + 1; q < n; q++) {
          if (k++ < ver) L.trazo(ctx, [pts[p], pts[q]], 1, L.tono(color, 0.45), 2);
        }
        UJ.alfa(ctx, L.tramo(a, 0, 0.3), function () {
          for (var j = 0; j < n; j++) { L.circulo(ctx, pts[j][0], pts[j][1], 13); L.rellena(ctx, color, m.papel, 2); }
        });
        UJ.rotulo(ctx, lz, titulo, cx, cy + r + 30, { tam: 22, peso: 700, visible: L.tramo(a, 0, 0.3) });
        UJ.rotulo(ctx, lz, pares, cx, cy + r + 62, { tam: 26, peso: 800, color: color, visible: L.tramo(a, 0.8, 1) });
      }
      grupo(130, 200, 70, 2, L.tramo(t, 0, 0.2), A, '2 personas', '1 pareja');
      grupo(400, 200, 100, 5, L.tramo(t, 0.26, 0.46), C, '5 personas', '10 parejas');
      grupo(660, 200, 115, 10, L.tramo(t, 0.52, 0.74), R, '10 personas', '45 parejas');
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.9), function () {
        L.rectRed(ctx, 110, 470, 580, 76, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
        UJ.rotulo(ctx, lz, 'parejas = n × (n − 1) ÷ 2', W / 2, 490, { tam: 30, peso: 800, color: A });
      });
      UJ.rotulo(ctx, lz, 'Con 20 personas: 190 parejas.', W / 2, 570, { tam: 22, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
