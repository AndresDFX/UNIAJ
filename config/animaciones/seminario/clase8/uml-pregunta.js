/* Una frase en lenguaje natural deja preguntas abiertas; el diagrama UML Dueño 1 — 0..* Mascota
 * las contesta con dos números y una línea. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('uml-pregunta', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.14, 0.46, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.rectRed(ctx, 90, 30, 620, 60, 14); L.rellena(ctx, L.tono(m.sello, 0.85), L.tono(m.sello, -0.25), 2);
        UJ.rotulo(ctx, lz, '«Un dueño puede tener varias mascotas»', W / 2, 47, { tam: 24, peso: 700 });
      });
      var preguntas = ['¿Una mascota puede tener dos dueños?', '¿Existe el dueño antes de su primera mascota?', '¿Qué pasa con sus mascotas al borrar el dueño?'];
      var resp = L.tramo(t, 0.8, 0.9);
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, 0.16 + i * 0.09, 0.24 + i * 0.09), y = 116 + i * 52;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 120, y, 560, 40, 20); L.rellena(ctx, L.mezclaColor(L.tono(R, 0.88), L.tono(V, 0.86), resp), L.mezclaColor(R, V, resp), 2);
          UJ.rotulo(ctx, lz, preguntas[i], 400, y + 9, { tam: 19, peso: 700, color: L.tono(L.mezclaColor(R, V, resp), -0.2) });
        });
      }
      // El diagrama
      var d = L.tramo(t, 0.5, 0.62);
      UJ.caja(ctx, lz, 90, 312, 190, 70, 'Dueño', null, A, d);
      UJ.caja(ctx, lz, 520, 312, 190, 70, 'Mascota', null, A, d);
      UJ.linea(ctx, 280, 347, 520, 347, m.tinta, 3, L.tramo(t, 0.6, 0.68));
      UJ.alfa(ctx, L.tramo(t, 0.68, 0.74), function () {
        UJ.rotulo(ctx, lz, '1', 300, 312, { tam: 26, peso: 800, color: R });
        UJ.rotulo(ctx, lz, '0..*', 482, 312, { tam: 26, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'tiene', 400, 356, { tam: 18, peso: 600, color: m.gris });
      });
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.84), function () {
        L.texto(ctx, '1: cada mascota tiene exactamente un dueño; no puede quedar sin él', 70, 420, { tam: 19, peso: 600, color: m.tinta, ancho: 660, letra: lz.letra });
        L.texto(ctx, '0..*: el dueño puede existir con cero mascotas', 70, 460, { tam: 19, peso: 600, color: m.tinta, ancho: 660, letra: lz.letra });
      });
      UJ.rotulo(ctx, lz, 'Dos números y una línea contestan lo que la frase deja abierto', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
