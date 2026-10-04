/* == compara referencias; equals, contenido: dos objetos con los mismos datos. a == b da false
 * (son dos flechas a sitios distintos); a.equals(b), sobrescrito por id, da true. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('igual-equals', {
    duracion: 4.6,
    pasos: [0.3, 0.55, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      var vars = [['a', 70], ['b', 190]];
      for (var i = 0; i < 2; i++) {
        var y = vars[i][1], a = L.tramo(t, 0.02 + i * 0.08, 0.1 + i * 0.08);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 40, y, 120, 60, 10); L.rellena(ctx, m.papel, A, 2);
          UJ.rotulo(ctx, lz, vars[i][0], 70, y + 15, { tam: 26, peso: 800, letra: 'Consolas, monospace' });
          L.circulo(ctx, 132, y + 30, 8); L.rellena(ctx, A);
          L.rectRed(ctx, 420, y - 20, 330, 100, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
          UJ.rotulo(ctx, lz, 'Mascota', 585, y - 10, { tam: 18, peso: 800, color: V });
          UJ.rotulo(ctx, lz, 'id = "M-001"', 440, y + 18, { tam: 19, alinear: 'left', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, 'nombre = "Luna"', 440, y + 46, { tam: 19, alinear: 'left', letra: 'Consolas, monospace' });
        });
        L.flecha(ctx, 140, y + 30, 414, y + 30, A, 4, L.tramo(t, 0.08 + i * 0.08, 0.16 + i * 0.08, 'frena'));
      }
      UJ.rotulo(ctx, lz, 'Mismos datos, dos objetos distintos', W / 2, 20, { tam: 19, peso: 700, color: V, visible: L.tramo(t, 0.2, 0.28) });
      // a == b
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.4), function () {
        UJ.codigo(ctx, lz, 40, 310, 260, 'a == b', 1, 22);
        UJ.rotulo(ctx, lz, '¿la misma flecha?', 330, 302, { tam: 18, alinear: 'left', color: m.tinta });
        UJ.rotulo(ctx, lz, 'false', 330, 328, { tam: 26, peso: 800, alinear: 'left', color: R });
      });
      UJ.sello(ctx, lz, 520, 332, 24, false, L.tramo(t, 0.44, 0.52));
      // equals heredado de Object
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.52), function () {
        UJ.codigo(ctx, lz, 40, 372, 260, 'a.equals(b)', 1, 22);
        UJ.rotulo(ctx, lz, 'heredado de Object: hace ==', 330, 364, { tam: 18, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'false', 330, 390, { tam: 26, peso: 800, alinear: 'left', color: R });
      });
      UJ.sello(ctx, lz, 600, 394, 24, false, L.tramo(t, 0.52, 0.56));
      // equals sobrescrito
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.72), function () {
        UJ.codigo(ctx, lz, 40, 432, 260, 'a.equals(b)', 1, 22);
        UJ.rotulo(ctx, lz, 'sobrescrito: compara id', 330, 424, { tam: 18, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'true', 330, 450, { tam: 26, peso: 800, alinear: 'left', color: V });
      });
      UJ.sello(ctx, lz, 600, 454, 24, true, L.tramo(t, 0.74, 0.78));
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 30, 500, W - 60, 130, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Con objetos, equals; == solo para primitivos y null', W / 2, 512, { tam: 22, peso: 800, ancho: W - 100 });
        UJ.rotulo(ctx, lz, 'Sobrescribir equals obliga a sobrescribir hashCode:', W / 2, 556, { tam: 19, ancho: W - 100 });
        UJ.rotulo(ctx, lz, 'HashMap y HashSet usan los dos.', W / 2, 586, { tam: 19, ancho: W - 100 });
      });
    }
  });
})();
