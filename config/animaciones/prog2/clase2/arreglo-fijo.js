/* El arreglo tiene tamano fijo: new Mascota[3] se llena; la cuarta da
 * ArrayIndexOutOfBoundsException; crecer es crear otro mas grande y copiar una por una. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('arreglo-fijo', {
    duracion: 4.8,
    pasos: [0.28, 0.54, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      var nom = ['Luna', 'Michi', 'Rocky'], cw = 130, ch = 70;
      function casilla(x, y, i, texto, a, color) {
        L.rectRed(ctx, x, y, cw, ch, 8); L.rellena(ctx, m.papel, A, 2);
        UJ.rotulo(ctx, lz, '[' + i + ']', x + cw / 2, y + ch + 6, { tam: 16, color: m.gris, letra: 'Consolas, monospace' });
        if (texto) UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x + 6, y + 6, cw - 12, ch - 12, 6); L.rellena(ctx, L.tono(color || V, 0.82));
          UJ.rotulo(ctx, lz, texto, x + cw / 2, y + 22, { tam: 20, peso: 700 });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0, 0.04), function () { UJ.codigo(ctx, lz, 24, 20, 470, 'Mascota[] arr = new Mascota[3];', L.tramo(t, 0, 0.08), 18); });
      var x0 = 40, y0 = 90;
      UJ.alfa(ctx, L.tramo(t, 0.06, 0.1), function () {
        for (var i = 0; i < 3; i++) casilla(x0 + i * cw, y0, i, nom[i], L.tramo(t, 0.1 + i * 0.05, 0.15 + i * 0.05));
        UJ.rotulo(ctx, lz, 'length = 3, para siempre', x0 + 1.5 * cw, y0 + ch + 34, { tam: 18, peso: 700, color: A, visible: 1 - L.tramo(t, 0.56, 0.58) });
      });
      // La cuarta
      var fx = L.claves(t, [[0.3, W + 10], [0.38, x0 + 3 * cw + 10, 'frena'], [0.42, x0 + 3 * cw + 30, 'atras'], [0.46, x0 + 3 * cw + 60]]);
      if (t >= 0.3 && t < 0.57) {
        L.rectRed(ctx, fx, y0 + 6, cw - 12, ch - 12, 6); L.rellena(ctx, L.tono(R, 0.8), R, 2);
        UJ.rotulo(ctx, lz, 'Firulais', fx + (cw - 12) / 2, y0 + 22, { tam: 20, peso: 700 });
      }
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.34), function () { UJ.codigo(ctx, lz, 520, 20, 256, t < 0.86 ? 'arr[3] = firulais;' : 'nuevo[3] = firulais;', 1, 18); });
      UJ.rayo(ctx, 712, 76, 60, R, L.tramo(t, 0.4, 0.44) * (1 - L.tramo(t, 0.56, 0.58)));
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5) * (1 - L.tramo(t, 0.56, 0.58)), function () {
        L.rectRed(ctx, 300, 230, 476, 48, 10); L.rellena(ctx, R);
        UJ.rotulo(ctx, lz, 'ArrayIndexOutOfBoundsException', 538, 242, { tam: 19, peso: 800, color: m.papel, letra: 'Consolas, monospace' });
      });
      // Crecer: crear otro y copiar
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.6), function () { UJ.codigo(ctx, lz, 24, 436, 400, 'Mascota[] nuevo = new Mascota[6];', L.tramo(t, 0.56, 0.62), 18); });
      var y1 = 330, cw2 = 120;
      UJ.alfa(ctx, L.tramo(t, 0.6, 0.64), function () {
        for (var k = 0; k < 6; k++) {
          var tx = null, a = 0, col = V;
          if (k < 3) { tx = nom[k]; a = L.tramo(t, 0.68 + k * 0.06, 0.72 + k * 0.06); }
          if (k === 3) { tx = 'Firulais'; a = L.tramo(t, 0.88, 0.92); col = C; }
          L.rectRed(ctx, x0 + k * cw2, y1, cw2, ch, 8); L.rellena(ctx, m.papel, A, 2);
          UJ.rotulo(ctx, lz, '[' + k + ']', x0 + k * cw2 + cw2 / 2, y1 + ch + 6, { tam: 16, color: m.gris, letra: 'Consolas, monospace' });
          if (tx) UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, x0 + k * cw2 + 6, y1 + 6, cw2 - 12, ch - 12, 6); L.rellena(ctx, L.tono(col, 0.82));
            UJ.rotulo(ctx, lz, tx, x0 + k * cw2 + cw2 / 2, y1 + 22, { tam: 19, peso: 700 });
          });
        }
      });
      for (var j = 0; j < 3; j++) {
        L.flecha(ctx, x0 + j * cw + cw / 2, y0 + ch + 30, x0 + j * cw2 + cw2 / 2, y1 - 4, C, 3, L.tramo(t, 0.64 + j * 0.06, 0.7 + j * 0.06, 'frena'));
      }
      UJ.rotulo(ctx, lz, 'nuevo[i] = arr[i]; una por una', 610, 444, { tam: 18, peso: 700, color: C, visible: L.tramo(t, 0.7, 0.8) });
      UJ.alfa(ctx, L.tramo(t, 0.9, 0.98), function () {
        L.rectRed(ctx, 24, 500, W - 48, 112, 14); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'Crecer = crear otro arreglo y copiar.', W / 2, 514, { tam: 23, peso: 800, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'Sirve si el tamaño se conoce: 7 días, 12 meses.', W / 2, 556, { tam: 19, ancho: W - 80 });
      });
    }
  });
})();
