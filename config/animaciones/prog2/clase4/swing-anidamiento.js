/* Swing: el JFrame con BorderLayout (NORTH, CENTER, SOUTH); en NORTH un JPanel con FlowLayout
 * que contiene JLabel, JTextField y JButton. Abajo, el arbol de anidamiento. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('swing-anidamiento', {
    duracion: 4.8,
    pasos: [0.22, 0.45, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var T = t; t = Math.min(1, t / 0.75);
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, G = m.gris || m.tinta, W = lz.ancho;
      var wx = 140, wy = 20, ww = 640;
      // ventana
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, wx, wy, ww, 380, 10); L.rellena(ctx, m.papel, m.tinta, 3);
        L.rectRed(ctx, wx, wy, ww, 40, 10); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'JFrame · BorderLayout', wx + 16, wy + 9, { tam: 19, peso: 700, color: m.papel, alinear: 'left' });
      });
      var reg = [['NORTH', 60, 80], ['CENTER', 140, 180], ['SOUTH', 320, 80]];
      reg.forEach(function (r, i) {
        UJ.alfa(ctx, L.tramo(t, 0.08 + i * 0.05, 0.14 + i * 0.05), function () {
          ctx.save(); ctx.setLineDash([8, 6]);
          L.rectRed(ctx, wx + 8, r[1] + 4, ww - 16, r[2] - 8, 6); L.rellena(ctx, L.tono(G, 0.95), L.tono(G, 0.3), 2);
          ctx.restore();
          UJ.rotulo(ctx, lz, r[0], wx - 12, r[1] + r[2] / 2 - 10, { tam: 17, peso: 700, color: G, alinear: 'right' });
        });
      });
      // JPanel en NORTH
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.42), function () {
        L.rectRed(ctx, wx + 14, 70, ww - 28, 60, 6); L.rellena(ctx, L.tono(C, 0.88), C, 3);
        UJ.rotulo(ctx, lz, 'JPanel · FlowLayout', wx + ww - 26, 90, { tam: 16, peso: 700, color: C, alinear: 'right' });
      });
      // componentes
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.72), function () {
        UJ.rotulo(ctx, lz, 'Nombre:', wx + 30, 89, { tam: 18, peso: 700, alinear: 'left' });
      });
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.76), function () {
        L.rectRed(ctx, wx + 118, 82, 200, 36, 4); L.rellena(ctx, m.papel, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Luna', wx + 128, 89, { tam: 17, alinear: 'left', color: G });
      });
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.8), function () {
        L.rectRed(ctx, wx + 330, 82, 110, 36, 8); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'Buscar', wx + 385, 89, { tam: 17, peso: 700, color: m.papel });
      });
      UJ.rotulo(ctx, lz, 'JLabel', wx + 62, 154, { tam: 16, peso: 700, color: V, visible: L.tramo(t, 0.8, 0.84) });
      UJ.rotulo(ctx, lz, 'JTextField', wx + 218, 154, { tam: 16, peso: 700, color: V, visible: L.tramo(t, 0.8, 0.84) });
      UJ.rotulo(ctx, lz, 'JButton', wx + 385, 154, { tam: 16, peso: 700, color: V, visible: L.tramo(t, 0.8, 0.84) });
      // arbol
      UJ.rotulo(ctx, lz, 'JFrame (BorderLayout)', 40, 430, { tam: 20, peso: 700, color: A, alinear: 'left', visible: L.tramo(t, 0.16, 0.24) });
      UJ.rotulo(ctx, lz, '└ en NORTH: JPanel (FlowLayout)', 70, 468, { tam: 20, peso: 700, color: C, alinear: 'left', visible: L.tramo(t, 0.44, 0.54) });
      UJ.rotulo(ctx, lz, '└ JLabel · JTextField · JButton', 110, 506, { tam: 20, peso: 700, color: V, alinear: 'left', visible: L.tramo(t, 0.82, 0.9) });
      var f = L.tramo(T, 0.78, 0.86);
      UJ.alfa(ctx, f, function () {
        L.rectRed(ctx, 20, 412, W - 40, 220, 10); L.rellena(ctx, m.papel);
        UJ.rotulo(ctx, lz, 'Crearla en el hilo de Swing (EDT) y las tres líneas obligatorias:', 30, 418, { tam: 18, peso: 700, color: A, alinear: 'left' });
        UJ.codigo(ctx, lz, 30, 450, W - 60, 'SwingUtilities.invokeLater(() -> new Ventana().setVisible(true));', 1, 16);
        UJ.codigo(ctx, lz, 30, 490, W - 60, 'setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  // cerrar termina', 1, 16);
        UJ.codigo(ctx, lz, 30, 530, W - 60, 'setSize(600, 230);   // o pack()               // darle tamaño', 1, 16);
        UJ.codigo(ctx, lz, 30, 570, W - 60, 'setVisible(true);                              // que aparezca', 1, 16);
      });
      if (f < 1) UJ.rotulo(ctx, lz, 'El layout acomoda; el contenedor contiene.', W / 2, 570, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
