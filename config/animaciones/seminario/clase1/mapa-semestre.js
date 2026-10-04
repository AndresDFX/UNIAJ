/* El semestre en tres tramos: cada uno aporta su parte a un mismo paquete de diseño, que se
 * va llenando clase a clase. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('mapa-semestre', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.56, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un semestre, un paquete de diseño', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var tramos = [
        ['Clases 1-4', 'cómo se organiza el trabajo', A, 'organización'],
        ['Clases 6-9', 'qué debe hacer el sistema', m.acento, 'requisitos y modelos'],
        ['Clases 11-14', 'cómo se ve y cómo se sustenta', m.verde, 'interfaz y sustento']
      ];
      var bx = 520, by = 110, bw = 250, bh = 360, nivel = (bh - 54) / 3;
      // Caja del paquete
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.1), function () {
        L.rectRed(ctx, bx, by, bw, bh, 14); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.2), 3);
        UJ.rotulo(ctx, lz, 'Paquete de diseño', bx + bw / 2, by + 14, { tam: 21, peso: 800, color: m.tinta });
      });
      var inicios = [0.08, 0.34, 0.6];
      for (var i = 0; i < 3; i++) {
        var s = inicios[i], y = 110 + i * 125, c = tramos[i][2];
        var a = L.tramo(t, s, s + 0.07);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 30, y, 400, 96, 12); L.rellena(ctx, L.tono(c, 0.88), c, 2.5);
          UJ.rotulo(ctx, lz, tramos[i][0], 50, y + 16, { tam: 22, peso: 800, color: L.tono(c, -0.3), alinear: 'left' });
          UJ.rotulo(ctx, lz, tramos[i][1], 50, y + 54, { tam: 19, peso: 600, alinear: 'left', ancho: 370 });
        });
        // Flecha hacia el nivel del paquete
        var ny = by + 44 + i * nivel;
        UJ.flecha(ctx, lz, 436, y + 48, bx - 6, ny + nivel / 2, c, L.tramo(t, s + 0.08, s + 0.15, 'frena'), null, { grosor: 3.5 });
        var f = L.tramo(t, s + 0.12, s + 0.18, 'frena');
        if (f > 0) {
          L.rectRed(ctx, bx + 12, ny + nivel * (1 - f) + 4, bw - 24, nivel * f - 8, 8); L.rellena(ctx, L.tono(c, 0.7), c, 2);
          UJ.rotulo(ctx, lz, tramos[i][3], bx + bw / 2, ny + nivel / 2 - 11, { tam: 18, peso: 700, color: L.tono(c, -0.4), ancho: bw - 40, visible: L.tramo(t, s + 0.15, s + 0.19) });
        }
      }
      UJ.rotulo(ctx, lz, 'Nada se bota al terminar la clase.', W / 2, 560,
                { tam: 24, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.86, 0.98) });
    }
  });
})();
