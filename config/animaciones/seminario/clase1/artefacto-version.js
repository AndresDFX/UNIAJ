/* Un artefacto vive con fecha, versión y registro del cambio: si la decisión cambia y nadie
 * versiona, circulan dos verdades; con v1.1 y su registro, circula una. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('artefacto-version', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.28, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un artefacto lleva versión', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });

      function hoja(x, y, an, al, color, l1, l2) {
        L.rectRed(ctx, x, y, an, al, 10); L.rellena(ctx, m.papel, color, 2.5);
        L.rectRed(ctx, x, y, 10, al, 4); L.rellena(ctx, color);
        UJ.rotulo(ctx, lz, l1, x + an / 2 + 5, y + 12, { tam: 19, peso: 800, color: L.tono(color, -0.2), ancho: an - 30 });
        if (l2) UJ.rotulo(ctx, lz, l2, x + an / 2 + 5, y + 42, { tam: 18, peso: 600, ancho: an - 30 });
      }
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.12), function () { hoja(250, 74, 300, 76, A, 'Diagrama de clases', 'v1.0 · 02/09'); });
      UJ.rayo(ctx, 575, 150, 56, m.sello, L.tramo(t, 0.14, 0.2));
      UJ.rotulo(ctx, lz, 'la decisión cambia', 610, 166, { tam: 19, peso: 700, color: L.tono(m.sello, -0.35), alinear: 'left', visible: L.tramo(t, 0.16, 0.24) });

      // Camino malo
      var pm = L.tramo(t, 0.3, 0.38);
      UJ.flecha(ctx, lz, 330, 156, 210, 236, R, pm, null, { grosor: 3 });
      UJ.rotulo(ctx, lz, 'Sin versionar', 205, 246, { tam: 20, peso: 800, color: R, visible: L.tramo(t, 0.34, 0.4) });
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.46), function () { hoja(40, 290, 220, 70, L.tono(m.tinta, 0.3), 'Diagrama', 'v1.0 · 02/09'); });
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () { hoja(150, 372, 220, 70, L.tono(m.tinta, 0.3), 'Diagrama', 'nueva decisión'); });
      UJ.sello(ctx, lz, 90, 478, 26, false, L.tramo(t, 0.5, 0.58));
      UJ.rotulo(ctx, lz, 'dos verdades circulando', 126, 466, { tam: 19, peso: 700, color: R, alinear: 'left', visible: L.tramo(t, 0.52, 0.6) });

      // Camino bueno
      var pb = L.tramo(t, 0.62, 0.7);
      UJ.flecha(ctx, lz, 470, 156, 590, 236, V, pb, null, { grosor: 3 });
      UJ.rotulo(ctx, lz, 'Versionado', 595, 246, { tam: 20, peso: 800, color: V, visible: L.tramo(t, 0.66, 0.72) });
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () { hoja(450, 290, 290, 76, V, 'Diagrama de clases', 'v1.1 · 09/09'); });
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.84), function () {
        L.rectRed(ctx, 450, 378, 290, 50, 8); L.rellena(ctx, L.tono(V, 0.9), V, 1.5);
        UJ.rotulo(ctx, lz, 'v1.1 · Mascota exige Dueño', 595, 380, { tam: 16, peso: 700, color: L.tono(V, -0.3) });
        UJ.rotulo(ctx, lz, 'motivo: entrevista', 595, 402, { tam: 16, peso: 600, color: L.tono(V, -0.3) });
      });
      UJ.sello(ctx, lz, 595, 466, 26, true, L.tramo(t, 0.82, 0.9));

      UJ.rotulo(ctx, lz, 'Fecha, versión y registro del cambio.', W / 2, 560,
                { tam: 24, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
