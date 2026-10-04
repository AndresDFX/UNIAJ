/* Los afectados de una app de turnos que nunca la usan: alrededor del usuario aparecen el
 * cajero, la senora sin datos, el vendedor de fichas y el plan de datos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('afectados', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', S = m.sello || C, W = lz.ancho;
      var cx = 400, cy = 300;
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.circulo(ctx, cx, cy, 250); L.rellena(ctx, L.tono(C, 0.94), L.tono(C, 0.4), 2);
      });
      var af = [
        ['El cajero', 'más trabajo', 140, 120, 0.12],
        ['Doña Rosa, sin datos', 'queda fuera', 660, 120, 0.32],
        ['El vendedor de fichas', 'lo desplaza', 140, 470, 0.57],
        ['El plan de datos', 'consumo que paga el cliente', 660, 470, 0.66]
      ];
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, af[i][4], af[i][4] + 0.1), x = af[i][2], y = af[i][3];
        L.trazo(ctx, [[cx, cy], [x, y]], a, L.tono(R, 0.4), 3);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x - 130, y - 50, 260, 100, 16); L.rellena(ctx, L.tono(R, 0.9), R, 3);
          UJ.rotulo(ctx, lz, af[i][0], x, y - 38, { tam: 21, peso: 800, color: R, ancho: 240 });
          UJ.rotulo(ctx, lz, af[i][1], x, y + 10, { tam: 18, ancho: 240 });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.circulo(ctx, cx, cy, 90); L.rellena(ctx, L.tono(A, 0.82), A, 3);
        UJ.rotulo(ctx, lz, 'quien usa la app', cx, cy - 22, { tam: 20, peso: 800, color: A, ancho: 150 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.86, 0.96), function () {
        L.rectRed(ctx, 150, 586, 500, 46, 23); L.rellena(ctx, S, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Afectados que nunca abren la app', W / 2, 597, { tam: 20, peso: 800 });
      });
    }
  });
})();
