/* Que es una excepcion: un objeto que sube por la pila de llamadas hasta que alguien lo atrapa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('excepcion-sube', {
    duracion: 4.5,
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Pila de llamadas', 220, 18, { tam: 22, peso: 700, visible: L.tramo(t, 0, 0.05) });
      var marcos = ['main()', 'registrar()', 'setEdad("tres")', 'Integer.parseInt("tres")'];
      for (var i = 0; i < 4; i++) {
        var y = 380 - i * 100;
        UJ.alfa(ctx, L.tramo(t, 0.03 + i * 0.06, 0.09 + i * 0.06), function () {
          L.rectRed(ctx, 40, y, 360, 76, 10); L.rellena(ctx, L.tono(A, 0.9 - i * 0.04), A, 2);
          UJ.rotulo(ctx, lz, marcos[i], 220, y + 24, { tam: 21, peso: 700, ancho: 340 });
        });
      }
      UJ.rotulo(ctx, lz, '↑ cada llamada se apila encima', 220, 470, { tam: 18, color: A, visible: L.tramo(t, 0.2, 0.26) });
      // El objeto excepcion nace arriba y baja hacia main
      var nace = L.tramo(t, 0.32, 0.4);
      var yEx = L.claves(t, [[0.4, 100], [0.48, 200, 'suave'], [0.56, 300, 'suave'], [0.64, 400, 'suave']]);
      if (t > 0.4) L.flecha(ctx, 605, 120, 605, yEx - 4, L.tono(R, 0.4), 3, 1);
      UJ.alfa(ctx, nace, function () {
        L.rectRed(ctx, 440, yEx, 330, 56, 28); L.rellena(ctx, L.tono(R, 0.85), R, 3);
        UJ.rotulo(ctx, lz, 'NumberFormatException', 605, yEx + 15, { tam: 19, peso: 800, color: R });
      });
      UJ.rayo(ctx, 410, 90, 50, R, L.tramo(t, 0.32, 0.36));
      [[0.48, 180], [0.56, 280]].forEach(function (p) {
        UJ.rotulo(ctx, lz, 'sin catch: sigue', 615, p[1] + 64, { tam: 16, alinear: 'left', color: L.tono(m.tinta, 0.3), visible: L.tramo(t, p[0], p[0] + 0.04) });
      });
      UJ.rotulo(ctx, lz, 'cada método se corta y la excepción vuelve a quien lo llamó, rumbo a main', 605, 30, { tam: 17, ancho: 330, color: R, peso: 600, visible: L.tramo(t, 0.4, 0.46) });
      // Desenlace
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.86), function () {
        L.rectRed(ctx, 40, 510, 350, 90, 12); L.rellena(ctx, L.tono(m.verde, 0.88), m.verde, 2);
        UJ.rotulo(ctx, lz, 'catch en main', 215, 520, { tam: 21, peso: 800, color: m.verde });
        UJ.rotulo(ctx, lz, 'se atrapa y el programa sigue', 215, 554, { tam: 17, ancho: 330 });
        L.rectRed(ctx, 410, 510, 350, 90, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'nadie la atrapa', 585, 520, { tam: 21, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'el hilo muere con la traza', 585, 554, { tam: 17, ancho: 330 });
      });
    }
  });
})();
