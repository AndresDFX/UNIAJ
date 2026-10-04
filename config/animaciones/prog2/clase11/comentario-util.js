/* Comentario de revision: el vago contra el util (evidencia, impacto, sugerencia + severidad). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('comentario-util', {
    duracion: 4.5,
    pasos: [0.3, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.alfa(ctx, L.tramo(t, 0, 0.12), function () {
        L.rectRed(ctx, 30, 24, W - 60, 90, 14); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, '«El manejo de errores está horrible.»', 60, 52, { tam: 23, peso: 700, alinear: 'left', color: R, ancho: 560 });
      });
      UJ.sello(ctx, lz, W - 80, 69, 28, false, L.tramo(t, 0.14, 0.24));
      UJ.rotulo(ctx, lz, 'No dice dónde, por qué importa ni qué hacer.', W / 2, 126, { tam: 18, ancho: W - 40, visible: L.tramo(t, 0.16, 0.26) });
      var partes = [
        ['Evidencia', 'Servicio.java:42 · catch vacío', A],
        ['Impacto', 'el fallo al guardar se pierde sin aviso', m.acento],
        ['Sugerencia', 'mostrar el mensaje y registrar el error', V]
      ];
      for (var i = 0; i < 3; i++) {
        var y = 180 + i * 92;
        UJ.alfa(ctx, L.tramo(t, 0.32 + i * 0.12, 0.42 + i * 0.12), function () {
          var c = partes[i][2];
          L.rectRed(ctx, 30, y, 200, 76, 12); L.rellena(ctx, c);
          UJ.rotulo(ctx, lz, partes[i][0], 130, y + 24, { tam: 22, peso: 800, color: m.papel });
          L.rectRed(ctx, 240, y, W - 270, 76, 12); L.rellena(ctx, L.tono(c, 0.9), c, 2);
          UJ.rotulo(ctx, lz, partes[i][1], 260, y + 24, { tam: 20, peso: 600, alinear: 'left', ancho: W - 310 });
        });
      }
      var et = [['bloqueante', R], ['mayor', m.sello], ['menor', m.gris || L.tono(m.tinta, 0.5)]];
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.9), function () {
        UJ.rotulo(ctx, lz, 'Severidad:', 40, 478, { tam: 20, peso: 700, alinear: 'left' });
        for (var k = 0; k < 3; k++) {
          var x = 180 + k * 190;
          L.rectRed(ctx, x, 468, 170, 44, 22); L.rellena(ctx, L.tono(et[k][1], 0.75), et[k][1], k === 0 ? 4 : 2);
          UJ.rotulo(ctx, lz, et[k][0], x + 85, 478, { tam: 19, peso: 700 });
        }
        UJ.rotulo(ctx, lz, 'Este comentario: bloqueante', W / 2, 540, { tam: 21, peso: 700, color: R });
      });
    }
  });
})();
