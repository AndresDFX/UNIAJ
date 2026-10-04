/* Ilustracion: cinco equipos fijos todo el semestre. Lo fijo es el numero de equipos, no el
 * tamano (25 -> equipos de 5; 35 -> equipos de 7), por que cinco, y el vocero que rota. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-equipos', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, S = m.sello || C, W = lz.ancho;
      UJ.rotulo(ctx, lz, '5 equipos, los mismos todo el semestre', W / 2, 12, { tam: 26, peso: 800, color: A, ancho: W - 40 });
      for (var i = 0; i < 5; i++) {
        var x = 96 + i * 152;
        L.circulo(ctx, x, 110, 54); L.rellena(ctx, L.tono(A, 0.85), A, 3);
        UJ.rotulo(ctx, lz, String(i + 1), x, 82, { tam: 38, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'equipo', x, 126, { tam: 16, peso: 700, color: A });
      }
      UJ.rotulo(ctx, lz, 'Lo fijo es el número de equipos, no el tamaño', W / 2, 188, { tam: 22, peso: 800, ancho: W - 40 });
      var filas = [['Si somos 25', '5 equipos de 5'], ['Si somos 35', '5 equipos de 7']];
      for (var k = 0; k < 2; k++) {
        var y = 234 + k * 80;
        L.rectRed(ctx, 80, y, 250, 60, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, filas[k][0], 205, y + 16, { tam: 22, peso: 700 });
        L.flecha(ctx, 336, y + 30, 444, y + 30, L.tono(m.tinta, 0.4), 4, 1);
        L.rectRed(ctx, 450, y, 270, 60, 14); L.rellena(ctx, L.tono(A, 0.88), A, 2);
        UJ.rotulo(ctx, lz, filas[k][1], 585, y + 16, { tam: 22, peso: 800, color: A });
      }
      L.rectRed(ctx, 40, 410, W - 80, 70, 14); L.rellena(ctx, m.papel, L.tono(A, 0.5), 2);
      UJ.rotulo(ctx, lz, '¿Por qué cinco? 5 × 3 min = 15 min: cabe en el bloque', W / 2, 432, { tam: 21, peso: 700, ancho: W - 120 });
      L.rectRed(ctx, 40, 506, W - 80, 104, 16); L.rellena(ctx, L.tono(S, 0.55), L.tono(S, -0.35), 2);
      UJ.rotulo(ctx, lz, 'El vocero rota cada sesión', W / 2, 520, { tam: 24, peso: 800 });
      UJ.rotulo(ctx, lz, 'no hay «el que siempre habla»', W / 2, 562, { tam: 20 });
    }
  });
})();
