/* Un clic en camara lenta: 1 la vista lee String con getText; 2 el controlador recorta, rechaza
 * vacios y convierte con parseInt dentro de try; 3 excepcion con mensaje o registra; 4 la vista
 * muestra el error en un JOptionPane, o limpia y refresca el listado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('clic-camara-lenta', {
    duracion: 5,
    pasos: [0.24, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, S = m.sello;
      function num(n, y, a) {
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, 44, y + 60, 24); L.rellena(ctx, m.tinta);
          UJ.rotulo(ctx, lz, String(n), 44, y + 47, { tam: 22, peso: 800, color: m.papel });
        });
      }
      function caja(x, y, an, titulo, linea, c, a, mono) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, an, 120, 12); L.rellena(ctx, L.tono(c, 0.9), c, 3);
          UJ.rotulo(ctx, lz, titulo, x + 16, y + 12, { tam: 20, peso: 700, color: c, alinear: 'left', ancho: an - 30 });
          if (mono) {
            L.rectRed(ctx, x + 14, y + 50, an - 28, 54, 8); L.rellena(ctx, L.tono(m.tinta, -0.55));
            L.texto(ctx, linea, x + 26, y + 64, { tam: 18, peso: 500, color: m.papel, letra: 'Consolas, monospace', ancho: an - 50 });
          } else UJ.rotulo(ctx, lz, linea, x + 16, y + 48, { tam: 17, alinear: 'left', ancho: an - 30 });
        });
      }
      var y1 = 20, y2 = 175, y3 = 330, y4 = 485;
      // 1
      num(1, y1, L.tramo(t, 0, 0.05));
      caja(84, y1, 696, 'Vista: lee texto crudo, todo es String (incluida la edad)', 'String edad = campoEdad.getText();  // " 4 "', C, L.tramo(t, 0.02, 0.1), true);
      // 2
      num(2, y2, L.tramo(t, 0.26, 0.3));
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.3), function () { L.flecha(ctx, 430, y1 + 122, 430, y2 - 4, m.tinta, 3, 1); });
      caja(84, y2, 696, 'Controlador: recorta, rechaza vacíos y convierte', '', A, L.tramo(t, 0.28, 0.34));
      var ch = ['trim()', '¿vacío?', 'Integer.parseInt(…) en try'];
      var cx = [104, 244, 404], cw = [120, 140, 356];
      for (var i = 0; i < 3; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.32 + i * 0.05, 0.37 + i * 0.05), function () {
          L.rectRed(ctx, cx[i], y2 + 56, cw[i], 46, 8); L.rellena(ctx, L.tono(S, 0.75), m.tinta, 2);
          UJ.rotulo(ctx, lz, ch[i], cx[i] + cw[i] / 2, y2 + 67, { tam: 18, peso: 700 });
          if (i > 0) L.flecha(ctx, cx[i - 1] + cw[i - 1] + 2, y2 + 79, cx[i] - 4, y2 + 79, m.tinta, 2, 1);
        });
      }
      // 3
      num(3, y3, L.tramo(t, 0.52, 0.56));
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.56), function () {
        L.flecha(ctx, 300, y2 + 122, 260, y3 - 4, R, 3, 1);
        L.flecha(ctx, 560, y2 + 122, 610, y3 - 4, V, 3, 1);
      });
      caja(84, y3, 340, 'Si algo falla', 'lanza una excepción con un mensaje para humanos', R, L.tramo(t, 0.54, 0.62));
      caja(440, y3, 340, 'Si todo está bien', 'registra la mascota', V, L.tramo(t, 0.58, 0.66));
      // 4
      num(4, y4, L.tramo(t, 0.78, 0.82));
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.82), function () {
        L.flecha(ctx, 254, y3 + 122, 254, y4 - 4, R, 3, 1);
        L.flecha(ctx, 610, y3 + 122, 610, y4 - 4, V, 3, 1);
      });
      caja(84, y4, 340, 'Vista: JOptionPane', 'muestra el mensaje de error', R, L.tramo(t, 0.8, 0.88));
      caja(440, y4, 340, 'Vista: limpia y refresca', 'vacía los campos y actualiza el listado', V, L.tramo(t, 0.84, 0.92));
    }
  });
})();
