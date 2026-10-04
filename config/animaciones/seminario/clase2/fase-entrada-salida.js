/* Una fase del ciclo de vida: entra el problema, sale un artefacto verificable y un criterio
 * dice cuando esta terminada. Sin artefacto, la fase fue solo una conversacion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('fase-entrada-salida', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué entra, qué sale y cuándo termina', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.08) });

      // Entrada
      UJ.alfa(ctx, L.tramo(t, 0.06, 0.16), function () {
        L.rectRed(ctx, 24, 200, 210, 120, 12); L.rellena(ctx, L.tono(m.gris, 0.85), m.gris, 2);
        UJ.rotulo(ctx, lz, 'entrada', 129, 216, { tam: 18, peso: 800, color: L.tono(m.gris, -0.4) });
        UJ.rotulo(ctx, lz, 'el problema de la clínica', 129, 248, { tam: 18, peso: 600, ancho: 180 });
      });
      UJ.flecha(ctx, lz, 236, 260, 282, 260, m.gris, L.tramo(t, 0.14, 0.22));
      // Fase
      UJ.caja(ctx, lz, 290, 200, 220, 120, 'Fase', 'Requisitos', A, L.tramo(t, 0.16, 0.28));

      // Salida: el artefacto
      UJ.flecha(ctx, lz, 512, 260, 558, 260, A, L.tramo(t, 0.36, 0.44));
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.56), function () {
        var x = 566, y = 150, an = 210, al = 230;
        ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + an - 30, y); ctx.lineTo(x + an, y + 30); ctx.lineTo(x + an, y + al); ctx.lineTo(x, y + al); ctx.closePath();
        L.rellena(ctx, m.papel, A, 2.5);
        UJ.rotulo(ctx, lz, 'artefacto', x + an / 2, y + 14, { tam: 18, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'lista numerada de RF y RNF', x + an / 2, y + 42, { tam: 17, peso: 600, ancho: an - 24 });
        var l = ['RF-01 …', 'RF-02 …', 'RNF-01 …'];
        for (var i = 0; i < 3; i++) L.texto(ctx, l[i], x + 20, y + 110 + i * 34, { tam: 17, peso: 600, color: L.tono(m.tinta, 0.3), letra: 'Consolas, monospace' });
      });

      // Criterio
      UJ.sello(ctx, lz, 600, 432, 22, true, L.tramo(t, 0.72, 0.82));
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.86), function () {
        UJ.rotulo(ctx, lz, 'criterio: la clínica la leyó y aprobó', 634, 410, { tam: 18, peso: 700, color: V, alinear: 'left', ancho: 150 });
      });
      UJ.rotulo(ctx, lz, 'Sin artefacto verificable la fase no existe: existe una conversación.', W / 2, 550,
                { tam: 21, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
