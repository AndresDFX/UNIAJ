/* Ilustracion: mapas y ventanas, un mismo objetivo. Una sola pregunta («el expediente de M-004»);
 * el bloque 1 la resuelve con el HashMap en consola, el bloque 2 le da una ventana Swing escrita a
 * mano, y al final la ventana solo lee el ID y le pregunta al mapa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-objetivo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, S = m.sello || C, W = lz.ancho;
      var MONO = 'Consolas, monospace';
      // La pregunta
      L.rectRed(ctx, 190, 14, 420, 60, 30); L.rellena(ctx, L.tono(S, 0.6), m.tinta, 2);
      UJ.rotulo(ctx, lz, '¿El expediente de M-004?', W / 2, 30, { tam: 24, peso: 800 });
      UJ.rotulo(ctx, lz, 'la pregunta más frecuente en recepción', W / 2, 82, { tam: 16, color: m.gris || m.tinta });
      L.flecha(ctx, 300, 108, 214, 144, m.tinta, 3, 1);
      L.flecha(ctx, 500, 108, 586, 144, m.tinta, 3, 1);

      // Bloque 1: mapas y conjuntos
      L.rectRed(ctx, 24, 150, 360, 250, 14); L.rellena(ctx, L.tono(A, 0.92), A, 2);
      UJ.rotulo(ctx, lz, '1 · Mapas y conjuntos', 204, 164, { tam: 22, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'demo en consola', 204, 196, { tam: 16 });
      var filas = [['"M-003"', 'Rocky'], ['"M-004"', 'Nieve'], ['"M-005"', 'Toby']];
      for (var i = 0; i < filas.length; i++) {
        var fy = 230 + i * 40;
        L.rectRed(ctx, 54, fy, 300, 38, 4);
        L.rellena(ctx, i === 1 ? L.tono(S, 0.55) : m.papel, L.tono(A, 0.5), 1);
        L.texto(ctx, filas[i][0], 70, fy + 9, { tam: 18, peso: 700, color: m.tinta, letra: MONO });
        L.texto(ctx, '→', 182, fy + 7, { tam: 20, peso: 700, color: A, letra: lz.letra });
        L.texto(ctx, filas[i][1], 220, fy + 9, { tam: 18, peso: 600, color: m.tinta, letra: lz.letra });
      }
      UJ.rotulo(ctx, lz, 'get(clave): directo, sin recorrer', 204, 360, { tam: 17, peso: 700, color: V });

      // Bloque 2: la ventana Swing
      L.rectRed(ctx, 416, 150, 360, 250, 14); L.rellena(ctx, L.tono(C, 0.92), C, 2);
      UJ.rotulo(ctx, lz, '2 · Ventana Swing', 596, 164, { tam: 22, peso: 800, color: C });
      UJ.rotulo(ctx, lz, 'escrita a mano', 596, 196, { tam: 16 });
      L.rectRed(ctx, 440, 228, 312, 150, 8); L.rellena(ctx, m.papel, m.tinta, 2);
      L.rectRed(ctx, 440, 228, 312, 34, 8); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'Buscar expediente', 456, 235, { tam: 16, peso: 700, color: m.papel, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'ID:', 456, 286, { tam: 17, peso: 700, alinear: 'left' });
      L.rectRed(ctx, 492, 278, 128, 38, 4); L.rellena(ctx, m.papel, m.tinta, 2);
      L.texto(ctx, 'M-004', 504, 288, { tam: 18, peso: 600, color: m.tinta, letra: MONO });
      L.rectRed(ctx, 632, 278, 104, 38, 8); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'Buscar', 684, 287, { tam: 17, peso: 700, color: m.papel });
      UJ.rotulo(ctx, lz, 'JFrame · JPanel · JTextField · JButton', 596, 336, { tam: 16, color: m.gris || m.tinta });

      // Al final se juntan
      UJ.rotulo(ctx, lz, 'Al cierre se juntan: la ventana pregunta, el mapa responde', W / 2, 424,
                { tam: 19, peso: 800, color: A, ancho: W - 40 });
      L.rectRed(ctx, 24, 466, 200, 64, 12); L.rellena(ctx, L.tono(C, 0.88), C, 2);
      UJ.rotulo(ctx, lz, 'la ventana lee', 124, 474, { tam: 17, peso: 700, color: C });
      UJ.rotulo(ctx, lz, '"M-004"', 124, 500, { tam: 17, peso: 700 });
      L.flecha(ctx, 228, 498, 262, 498, m.tinta, 3, 1);
      UJ.codigo(ctx, lz, 268, 478, 270, 'expedientes.get("M-004")', 1, 17);
      L.flecha(ctx, 542, 498, 576, 498, m.tinta, 3, 1);
      L.rectRed(ctx, 582, 466, 194, 64, 12); L.rellena(ctx, L.tono(V, 0.86), V, 2);
      UJ.rotulo(ctx, lz, 'Nieve (Persa)', 676, 487, { tam: 19, peso: 800, color: m.tinta });
      UJ.sello(ctx, lz, 760, 470, 16, true, 1);
      UJ.rotulo(ctx, lz, 'El mapa busca; la ventana solo pregunta y muestra.', W / 2, 568,
                { tam: 19, peso: 700, ancho: W - 40 });
    }
  });
})();
