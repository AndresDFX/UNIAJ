/* Proyecto frente a producto: el proyecto (el semestre) tiene inicio y fin; el producto (el
 * sistema) sigue vivo con versiones durante años. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('proyecto-producto', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Proyecto y producto no son lo mismo', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.08) });

      // Proyecto: barra con inicio y fin
      var px = 60, pw = 280, py = 150;
      UJ.rotulo(ctx, lz, 'Proyecto: el semestre', px, py - 46, { tam: 22, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0.06, 0.14) });
      var pb = L.tramo(t, 0.1, 0.26, 'frena');
      if (pb > 0) { L.rectRed(ctx, px, py, pw * pb, 40, 10); L.rellena(ctx, L.tono(A, 0.75), A, 2.5); }
      UJ.alfa(ctx, L.tramo(t, 0.12, 0.18), function () {
        UJ.linea(ctx, px, py - 8, px, py + 60, A, 3);
        UJ.rotulo(ctx, lz, 'inicio', px, py + 66, { tam: 18, peso: 700, color: A });
      });
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.32), function () {
        UJ.linea(ctx, px + pw, py - 8, px + pw, py + 60, m.malva, 4);
        UJ.rotulo(ctx, lz, 'fin: se cierra', px + pw, py + 66, { tam: 18, peso: 700, color: m.malva });
      });

      // Producto: linea larga con versiones
      var ly = 360, lx0 = 60, lx1 = W - 50;
      UJ.rotulo(ctx, lz, 'Producto: el sistema', lx0, ly - 70, { tam: 22, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0.38, 0.44) });
      var pl = L.tramo(t, 0.4, 0.72, 'suave');
      if (pl > 0) L.flecha(ctx, lx0, ly, lx0 + (lx1 - lx0) * pl, ly, V, 5, 1);
      var hitos = [['v1.0', 340], ['v1.1', 480], ['v2.0', 620]];
      for (var i = 0; i < hitos.length; i++) {
        var hx = hitos[i][1], a = L.tramo(t, 0.46 + i * 0.07, 0.52 + i * 0.07);
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, hx, ly, 11); L.rellena(ctx, m.papel, V, 4);
          UJ.rotulo(ctx, lz, hitos[i][0], hx, ly + 22, { tam: 19, peso: 800, color: V });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.52), function () {
        UJ.linea(ctx, 340, py + 100, 340, ly - 16, L.tono(m.tinta, 0.5), 2, 1, true);
        UJ.rotulo(ctx, lz, 'la entrega', 350, py + 128, { tam: 17, peso: 600, color: L.tono(m.tinta, 0.3), alinear: 'left' });
      });
      UJ.rotulo(ctx, lz, 'puede seguir vivo diez años', lx1 - 10, ly + 66, { tam: 20, peso: 700, color: V, alinear: 'right', visible: L.tramo(t, 0.66, 0.76) });

      UJ.rotulo(ctx, lz, 'Un proyecto termina; un producto sigue vivo.', W / 2, 555,
                { tam: 24, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.82, 0.98) });
    }
  });
})();
