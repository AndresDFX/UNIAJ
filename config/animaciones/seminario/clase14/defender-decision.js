/* Como se defiende una decision de diseño: decision, alternativa descartada, criterio y
 * consecuencia, en cadena. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('defender-decision', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.25, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, G = m.gris, T = m.tinta, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Defender una decisión', W / 2, 16, { tam: 25, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      var items = [
        ['Decisión', 'Separar Historia_Clinica de Mascota', A],
        ['Alternativa', 'Los campos clínicos dentro de Mascota', L.tono(G, -0.15)],
        ['Criterio', 'Una mascota acumula muchas consultas en su vida: relación 1 a muchos', C],
        ['Consecuencia', 'Cuesta una entidad más; el RNF de 3 s se sostiene con un índice', V]
      ];
      var x = 60, w = W - 120, h = 96, gap = 34, y0 = 62, tw = 170;
      for (var i = 0; i < 4; i++) {
        (function (i) {
          var s = 0.04 + i * 0.25, y = y0 + i * (h + gap), c = items[i][2];
          if (i > 0) L.flecha(ctx, W / 2, y - gap + 2, W / 2, y - 3, L.tono(T, 0.3), 3, L.tramo(t, s - 0.03, s + 0.02));
          UJ.alfa(ctx, L.tramo(t, s, s + 0.08), function () {
            L.rectRed(ctx, x, y, w, h, 12); L.rellena(ctx, L.tono(c, 0.92), c, 2.5);
            L.rectRed(ctx, x, y, tw, h, 12); L.rellena(ctx, c);
            L.rectRed(ctx, x + tw - 12, y, 12, h, 0); L.rellena(ctx, c);
            UJ.rotulo(ctx, lz, items[i][0], x + tw / 2, y + h / 2 - 12, { tam: 20, peso: 800, color: m.papel });
            var hh = L.texto(ctx, items[i][1], -9999, -9999, { tam: 19, peso: 600, letra: lz.letra, ancho: w - tw - 36 });
            UJ.rotulo(ctx, lz, items[i][1], x + tw + 18, y + h / 2 - hh / 2, { tam: 19, peso: 600, color: T, alinear: 'left', ancho: w - tw - 36 });
          });
        })(i);
      }
      UJ.rotulo(ctx, lz, 'Sin alternativa ni criterio, una decisión es solo un gusto.', W / 2, 588,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
