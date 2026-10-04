/* Ilustracion: la app funciono y la fila siguio. Por que, y con que se juzga un proyecto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-app-fila', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', V = m.verde || A, S = m.sello || m.acento, W = lz.ancho;
      L.rectRed(ctx, 20, 20, 370, 300, 16); L.rellena(ctx, L.tono(V, 0.92), V, 3);
      L.rectRed(ctx, 70, 50, 110, 200, 18); L.rellena(ctx, L.tono(m.tinta, -0.2));
      L.rectRed(ctx, 80, 70, 90, 160, 8); L.rellena(ctx, m.papel);
      UJ.sello(ctx, lz, 280, 140, 44, true, 1);
      UJ.rotulo(ctx, lz, 'La app funciona', 205, 268, { tam: 24, peso: 800, color: V });
      L.rectRed(ctx, 410, 20, 370, 300, 16); L.rellena(ctx, L.tono(R, 0.92), R, 3);
      UJ.rotulo(ctx, lz, '5:00 a. m.', 595, 36, { tam: 22, peso: 800, color: R });
      for (var i = 0; i < 6; i++) {
        var px = 460 + i * 55;
        L.circulo(ctx, px, 130, 14); L.rellena(ctx, L.tono(R, 0.3));
        L.rectRed(ctx, px - 16, 148, 32, 60, 10); L.rellena(ctx, L.tono(R, 0.55));
      }
      UJ.rotulo(ctx, lz, 'La fila sigue igual', 595, 268, { tam: 24, peso: 800, color: R });
      UJ.rotulo(ctx, lz, '¿Por qué?', W / 2, 338, { tam: 24, peso: 800 });
      var r = ['sin datos en el celular', 'no confían en la app', 'la secretaria sigue en el cuaderno'];
      for (var k = 0; k < 3; k++) {
        L.rectRed(ctx, 20 + k * 260, 380, 240, 90, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, r[k], 140 + k * 260, 400, { tam: 20, peso: 700, ancho: 220 });
      }
      L.rectRed(ctx, 20, 500, W - 40, 110, 16); L.rellena(ctx, L.tono(S, 0.55), L.tono(S, -0.35), 2);
      UJ.rotulo(ctx, lz, 'Se juzga si el problema se redujo, no si la app funciona', W / 2, 526, { tam: 23, peso: 800, ancho: W - 80 });
    }
  });
})();
