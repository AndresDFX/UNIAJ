/* Wireframe anotado: cada campo numerado tiene su respaldo (atributo, regla o requisito); un
 * campo sin respaldo delata que falta un requisito o sobra el campo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('wireframe-anotado', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, G = m.gris, T = m.tinta, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Wireframe anotado', W / 2, 18, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      var wx = 24, wy = 66, ww = 290, wh = 476;
      function marca(n, x, y, c) {
        L.circulo(ctx, x, y, 14); L.rellena(ctx, c || A);
        UJ.rotulo(ctx, lz, String(n), x, y - 10, { tam: 17, peso: 800, color: m.papel });
      }
      UJ.alfa(ctx, L.tramo(t, 0.03, 0.1), function () {
        L.rectRed(ctx, wx, wy, ww, wh, 12); L.rellena(ctx, m.papel, G, 2.5);
        L.rectRed(ctx, wx, wy, ww, 40, 12); L.rellena(ctx, L.tono(G, 0.6));
        L.rectRed(ctx, wx, wy + 28, ww, 12, 0); L.rellena(ctx, L.tono(G, 0.6));
        UJ.rotulo(ctx, lz, 'Registrar mascota', wx + ww / 2, wy + 9, { tam: 18, peso: 800, color: T });
      });
      var campos = [['Nombre', 0], ['Especie  ▾', 1], ['Dueño', 2]];
      for (var i = 0; i < 3; i++) {
        (function (i) {
          UJ.alfa(ctx, L.tramo(t, 0.08 + i * 0.05, 0.13 + i * 0.05), function () {
            var y = wy + 60 + i * 72;
            L.rectRed(ctx, wx + 40, y, ww - 60, 40, 5); L.rellena(ctx, L.tono(G, 0.85), G, 1.5);
            UJ.rotulo(ctx, lz, campos[i][0], wx + 52, y + 10, { tam: 17, peso: 600, color: T, alinear: 'left' });
            marca(i + 1, wx + 20, y + 20);
          });
        })(i);
      }
      UJ.alfa(ctx, L.tramo(t, 0.23, 0.28), function () {
        var y = wy + 60 + 3 * 72;
        L.rectRed(ctx, wx + 40, y, ww - 60, 40, 5); L.rellena(ctx, L.tono(m.verde, 0.82), m.verde, 1.5);
        UJ.rotulo(ctx, lz, 'Ficha guardada', wx + 52, y + 10, { tam: 17, peso: 600, color: T, alinear: 'left' });
        marca(4, wx + 20, y + 20);
      });
      // Campo sin respaldo
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.76), function () {
        var y = wy + 60 + 4 * 72;
        L.rectRed(ctx, wx + 40, y, ww - 60, 40, 5); L.rellena(ctx, L.tono(R, 0.88), R, 2);
        UJ.rotulo(ctx, lz, 'Color del collar', wx + 52, y + 10, { tam: 17, peso: 600, color: T, alinear: 'left' });
        marca('?', wx + 20, y + 20, R);
      });
      UJ.alfa(ctx, L.tramo(t, 0.05, 0.1), function () {
        L.rectRed(ctx, wx + ww - 120, wy + wh - 50, 100, 38, 5); L.rellena(ctx, L.tono(G, 0.6), G, 1.5);
        UJ.rotulo(ctx, lz, 'Guardar', wx + ww - 70, wy + wh - 41, { tam: 17, peso: 700, color: T });
      });

      // Tabla de respaldo
      var tx = 336, tw = W - 24 - tx, fh = 74;
      UJ.alfa(ctx, L.tramo(t, 0.32, 0.37), function () {
        L.rectRed(ctx, tx, wy, tw, 40, 8); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'Campo → respaldo', tx + tw / 2, wy + 9, { tam: 18, peso: 800, color: m.papel });
      });
      var filas = [
        ['Nombre', 'Mascota.nombre · texto 60 · RF-03'],
        ['Especie', 'lista cerrada'],
        ['Dueño', 'debe existir'],
        ['Aviso de confirmación', 'RNF-02']
      ];
      for (var k = 0; k < 5; k++) {
        (function (k) {
          var s = k < 4 ? 0.37 + k * 0.07 : 0.78;
          UJ.alfa(ctx, L.tramo(t, s, s + 0.06), function () {
            var y = wy + 40 + k * fh, c = k < 4 ? A : R;
            L.rectRed(ctx, tx, y, tw, fh, 0); L.rellena(ctx, k < 4 ? (k % 2 ? L.tono(A, 0.94) : m.papel) : L.tono(R, 0.9), L.tono(c, 0.5), 1);
            marca(k < 4 ? k + 1 : '?', tx + 26, y + fh / 2, c);
            if (k < 4) {
              UJ.rotulo(ctx, lz, filas[k][0], tx + 52, y + 10, { tam: 17, peso: 800, color: T, alinear: 'left', ancho: tw - 64 });
              UJ.rotulo(ctx, lz, '→ ' + filas[k][1], tx + 52, y + 38, { tam: 17, peso: 500, color: T, alinear: 'left', ancho: tw - 64 });
            } else {
              UJ.rotulo(ctx, lz, 'Color del collar', tx + 52, y + 10, { tam: 17, peso: 800, color: R, alinear: 'left' });
              UJ.rotulo(ctx, lz, '→ sin respaldo', tx + 52, y + 38, { tam: 17, peso: 600, color: R, alinear: 'left' });
            }
          });
        })(k);
      }
      UJ.rotulo(ctx, lz, 'O falta un requisito, o sobra el campo.', W / 2, 560,
                { tam: 23, peso: 800, color: R, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
