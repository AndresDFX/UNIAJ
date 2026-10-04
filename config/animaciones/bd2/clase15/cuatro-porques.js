/* Las cuatro preguntas de por que que casi siempre llegan: normalizacion, indice, tipo de dato y
 * la regla en un disparador. Cada una con la forma de la respuesta que se espera. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cuatro-porques', {
    duracion: 5,
    pasos: [0.28, 0.54, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var preg = [['¿Por qué esa normalización?', '3FN · y la desnormalización deliberada, declarada'],
                  ['¿Por qué ese índice?', 'la consulta que lo usa · medición antes y después'],
                  ['¿Por qué ese tipo de dato?', 'fecha TIMESTAMP · teléfono VARCHAR'],
                  ['¿Por qué en un disparador?', 'y no en la aplicación']];
      var t0 = [0.02, 0.3, 0.56, 0.82];
      for (var i = 0; i < 4; i++) {
        var y = 20 + i * 128, a = L.tramo(t, t0[i], t0[i] + 0.1), col = i === 3 ? C : A;
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, 60, y + 52, 34); L.rellena(ctx, col);
          UJ.rotulo(ctx, lz, String(i + 1), 60, y + 34, { tam: 30, peso: 800, color: m.papel });
          L.rectRed(ctx, 110, y, 660, 108, 14); L.rellena(ctx, L.tono(col, 0.9), col, 2);
          UJ.rotulo(ctx, lz, preg[i][0], 130, y + 14, { tam: 24, peso: 800, alinear: 'left', color: L.tono(col, -0.2) });
          UJ.rotulo(ctx, lz, preg[i][1], 130, y + 58, { tam: 19, peso: 500, alinear: 'left', ancho: 620 });
        });
      }
      UJ.rotulo(ctx, lz, 'La cuarta es la que más se falla.', W / 2, 545, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
