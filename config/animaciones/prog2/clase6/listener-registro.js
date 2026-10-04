/* ActionListener, el contrato del clic: addActionListener(escucha) guarda la referencia en el
 * boton; al clic, Swing invoca actionPerformed(e). Tres formas de escribir el escucha. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('listener-registro', {
    duracion: 4.8,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'btn.addActionListener(escucha);', L.tramo(t, 0, 0.08), 20);
      // boton
      var pulsa = L.tramo(t, 0.36, 0.4) * (1 - L.tramo(t, 0.42, 0.46));
      L.rectRed(ctx, 40, 120 + pulsa * 4, 220, 80, 14); L.rellena(ctx, pulsa > 0 ? L.tono(A, -0.2) : A);
      UJ.rotulo(ctx, lz, 'Registrar', 150, 138 + pulsa * 4, { tam: 22, peso: 700, color: m.papel });
      UJ.rotulo(ctx, lz, 'JButton btn', 150, 172 + pulsa * 4, { tam: 15, color: m.papel });
      // lista de escuchas dentro del boton
      UJ.alfa(ctx, L.tramo(t, 0.08, 0.14), function () {
        L.rectRed(ctx, 40, 214, 220, 54, 8); L.rellena(ctx, m.papel, A, 2);
        UJ.rotulo(ctx, lz, 'sus escuchas:', 52, 220, { tam: 15, alinear: 'left', color: m.gris || m.tinta });
      });
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.2), function () {
        L.rectRed(ctx, 54, 240, 110, 24, 6); L.rellena(ctx, L.tono(S, 0.7));
        UJ.rotulo(ctx, lz, '→ escucha', 109, 242, { tam: 15, peso: 700 });
      });
      // objeto escucha
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.16), function () {
        L.rectRed(ctx, 470, 120, 290, 120, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'escucha', 615, 136, { tam: 22, peso: 700, color: V });
        UJ.rotulo(ctx, lz, 'implements ActionListener', 615, 170, { tam: 16 });
        UJ.rotulo(ctx, lz, 'actionPerformed(ActionEvent e)', 615, 198, { tam: 16, peso: 700 });
      });
      L.flecha(ctx, 166, 252, 464, 200, m.tinta, 3, L.tramo(t, 0.18, 0.26));
      UJ.rotulo(ctx, lz, 'el botón guarda la referencia', 330, 250, { tam: 16, alinear: 'left', visible: L.tramo(t, 0.22, 0.28) });
      // clic
      UJ.rayo(ctx, 270, 100, 46, S, L.tramo(t, 0.34, 0.38));
      UJ.rotulo(ctx, lz, 'clic', 300, 110, { tam: 18, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0.34, 0.38) });
      var pulso = L.tramo(t, 0.42, 0.52);
      if (pulso > 0 && pulso < 1) { L.circulo(ctx, L.mezcla(166, 464, pulso), L.mezcla(252, 200, pulso), 9); L.rellena(ctx, R); }
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.56), function () {
        L.rectRed(ctx, 466, 116, 298, 128, 16); ctx.strokeStyle = R; ctx.lineWidth = 4; ctx.stroke();
      });
      UJ.rotulo(ctx, lz, 'Swing invoca escucha.actionPerformed(e): una interfaz con un solo método.', W / 2, 300, { tam: 18, peso: 700, color: R, ancho: W - 40, visible: L.tramo(t, 0.5, 0.58) });
      // tres formas
      var formas = [['class Escucha implements ActionListener {…}', '1 · clase que implementa'],
                    ['btn.addActionListener(new ActionListener() {…});', '2 · clase anónima'],
                    ['btn.addActionListener(e -> registrar());', '3 · lambda']];
      for (var i = 0; i < 3; i++) {
        var a0 = 0.64 + i * 0.09, y = 360 + i * 62;
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.01), function () { UJ.codigo(ctx, lz, 20, y, 520, formas[i][0], L.tramo(t, a0, a0 + 0.07), 15); });
        UJ.rotulo(ctx, lz, formas[i][1], 556, y + 4, { tam: 18, peso: 700, color: A, alinear: 'left', visible: L.tramo(t, a0 + 0.05, a0 + 0.09) });
      }
      UJ.rotulo(ctx, lz, 'La lambda solo sirve con interfaces de un único método abstracto, como esta.', W / 2, 570, { tam: 18, ancho: W - 40, visible: L.tramo(t, 0.92, 0.99) });
    }
  });
})();
