/* Del programa estructurado al objeto: tres arreglos paralelos; se ordena solo nombres[] y Luna
 * queda con la edad de otra mascota. Despues: la mascota como un objeto con sus tres datos juntos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('estructurado-vs-objeto', {
    duracion: 4.8,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, W = lz.ancho;
      var cols = [['nombres[]', ['Rocky', 'Luna', 'Michi']], ['especies[]', ['Canino', 'Canino', 'Felino']], ['edades[]', ['8', '3', '5']]];
      var x0 = 90, cw = 200, gap = 20, y0 = 30, cab = 44, fh = 48;
      // Orden de nombres: Rocky,Luna,Michi -> Luna,Michi,Rocky (posicion destino de cada uno)
      var dest = [2, 0, 1], s = L.tramo(t, 0.36, 0.5, 'suave');
      for (var i = 0; i < 3; i++) {
        UJ.rotulo(ctx, lz, String(i), 60, y0 + cab + i * fh + 12, { tam: 18, peso: 700, color: m.gris, visible: L.tramo(t, 0, 0.1) });
      }
      for (var c = 0; c < 3; c++) {
        var x = x0 + c * (cw + gap), a = L.tramo(t, 0.02 + c * 0.05, 0.1 + c * 0.05);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y0, cw, cab, 10); L.rellena(ctx, c === 0 && s > 0 ? R : A);
          UJ.rotulo(ctx, lz, cols[c][0], x + cw / 2, y0 + 10, { tam: 20, peso: 700, color: m.papel, letra: 'Consolas, monospace' });
          for (var k = 0; k < 3; k++) {
            L.rectRed(ctx, x, y0 + cab + k * fh, cw, fh, 0); L.rellena(ctx, k % 2 ? L.tono(A, 0.94) : m.papel, L.tono(A, 0.6), 1);
          }
          for (var j = 0; j < 3; j++) {
            var fila = c === 0 ? L.mezcla(j, dest[j], s) : j;
            var bad = c === 0 && s >= 1 && dest[j] === 0;
            UJ.rotulo(ctx, lz, cols[c][1][j], x + cw / 2, y0 + cab + fila * fh + 12, { tam: 20, peso: bad ? 800 : 500, color: bad ? R : m.tinta });
          }
        });
      }
      // Paso 1: la mascota 1 es la casilla 1 de los tres
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.26) * (1 - L.tramo(t, 0.33, 0.36)), function () {
        L.rectRed(ctx, x0 - 6, y0 + cab + fh - 4, 3 * cw + 2 * gap + 12, fh + 8, 10); ctx.lineWidth = 4; ctx.strokeStyle = C; ctx.stroke();
      });
      UJ.rotulo(ctx, lz, 'La mascota 1 es la casilla 1 de los tres arreglos', W / 2, 228, { tam: 20, peso: 600, color: C, visible: L.tramo(t, 0.18, 0.27) * (1 - L.tramo(t, 0.33, 0.36)) });
      // Paso 2: se ordena solo nombres[]
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.56), function () {
        L.rectRed(ctx, x0 - 6, y0 + cab - 4, 3 * cw + 2 * gap + 12, fh + 8, 10); ctx.lineWidth = 4; ctx.strokeStyle = R; ctx.stroke();
      });
      UJ.rotulo(ctx, lz, 'Arrays.sort(nombres): Luna queda con 8 años, que eran de Rocky', W / 2, 228, { tam: 20, peso: 700, color: R, ancho: W - 60, visible: L.tramo(t, 0.52, 0.6) });
      UJ.sello(ctx, lz, 764, y0 + cab + fh / 2, 22, false, L.tramo(t, 0.5, 0.56));
      // Paso 3: el objeto junta los tres datos
      var nom = [['Luna', 'Canino', '3'], ['Michi', 'Felino', '5'], ['Rocky', 'Canino', '8']];
      for (var q = 0; q < 3; q++) {
        var cx = 30 + q * 255, cy = 300, b = L.tramo(t, 0.66 + q * 0.07, 0.76 + q * 0.07, 'frena');
        UJ.alfa(ctx, b, function () {
          var yy = cy + (1 - b) * 30;
          L.rectRed(ctx, cx, yy, 230, 180, 14); L.rellena(ctx, L.tono(m.verde, 0.88), m.verde, 3);
          L.rectRed(ctx, cx, yy, 230, 42, 14); L.rellena(ctx, m.verde);
          UJ.rotulo(ctx, lz, 'Mascota', cx + 115, yy + 9, { tam: 21, peso: 800, color: m.papel });
          UJ.rotulo(ctx, lz, 'nombre: ' + nom[q][0], cx + 18, yy + 56, { tam: 18, alinear: 'left', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, 'especie: ' + nom[q][1], cx + 18, yy + 86, { tam: 18, alinear: 'left' });
          UJ.rotulo(ctx, lz, 'edad: ' + nom[q][2], cx + 18, yy + 116, { tam: 18, alinear: 'left' });
          UJ.rotulo(ctx, lz, 'getEdad() · cumplirAños()', cx + 18, yy + 148, { tam: 15, alinear: 'left', color: m.verde, peso: 700 });
        });
      }
      UJ.rotulo(ctx, lz, 'Estado y comportamiento en un solo tipo:', W / 2, 510, { tam: 22, peso: 800, color: m.verde, visible: L.tramo(t, 0.88, 0.94) });
      UJ.rotulo(ctx, lz, 'ordenar mueve la mascota entera, nunca un dato suelto.', W / 2, 546, { tam: 21, peso: 600, ancho: W - 60, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
