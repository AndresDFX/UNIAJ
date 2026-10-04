/* El reparto de los 5 a 8 minutos (convencion, no regla dura): 45 s problema, 90 s modelo, 60 s
 * seguridad, 90 s automatizacion, 60 s optimizacion, 45 s integracion, 30 s cierre = 7 min. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('reparto-minutos', {
    duracion: 5,
    // Pasos LOGICOS: 1) lo que se cuenta (problema y modelo), 2) lo que se demuestra ejecutando
    // (seguridad, automatizacion, optimizacion), 3) integracion, cierre y el total.
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var tramos = [[45, 'Problema', 'en lenguaje de negocio, sin tablas'], [90, 'Modelo', 'el ER y dos decisiones'],
                    [60, 'Seguridad', 'la matriz de roles'], [90, 'Automatización', 'caso válido y caso inválido'],
                    [60, 'Optimización', 'plan antes y después'], [45, 'Integración', 'y su punto débil'], [30, 'Cierre', '']];
      var x = 30, esc = 740 / 420, t0 = [0.04, 0.14, 0.36, 0.46, 0.56, 0.74, 0.82];
      var grupos = [[0, 2, 'lo que se cuenta', 0.04], [2, 5, 'lo que se demuestra ejecutando', 0.36], [5, 7, 'cierre', 0.74]];
      var xs = [];
      for (var i = 0; i < 7; i++) {
        var an = tramos[i][0] * esc, a = L.tramo(t, t0[i], t0[i] + 0.08, 'suave'), col = i % 2 ? C : A;
        xs.push(x);
        if (a > 0) {
          L.rectRed(ctx, x, 50, an * a, 70, 6); L.rellena(ctx, L.tono(col, 0.2 + (i % 3) * 0.15), m.papel, 2);
          UJ.rotulo(ctx, lz, tramos[i][0] + ' s', x + an / 2, 74, { tam: 17, peso: 800, color: m.papel, visible: L.tramo(a, 0.8, 1) });
          var y = 170 + i * 50;
          UJ.alfa(ctx, L.tramo(a, 0.6, 1), function () {
            L.rectRed(ctx, 30, y, 14, 40, 4); L.rellena(ctx, L.tono(col, 0.2 + (i % 3) * 0.15));
            UJ.rotulo(ctx, lz, tramos[i][0] + ' s · ' + tramos[i][1], 56, y + 8, { tam: 20, peso: 800, alinear: 'left', color: L.tono(col, -0.2) });
            if (tramos[i][2]) UJ.rotulo(ctx, lz, tramos[i][2], 360, y + 10, { tam: 18, alinear: 'left', ancho: 410 });
          });
        }
        x += an;
      }
      xs.push(x);
      // Rotulo de cada grupo, bajo la barra
      for (var g = 0; g < 3; g++) {
        var gx0 = xs[grupos[g][0]], gx1 = xs[grupos[g][1]];
        UJ.alfa(ctx, L.tramo(t, grupos[g][3], grupos[g][3] + 0.04), function () {
          ctx.strokeStyle = L.tono(m.tinta, 0.4); ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(gx0 + 4, 128); ctx.lineTo(gx0 + 4, 136); ctx.lineTo(gx1 - 4, 136); ctx.lineTo(gx1 - 4, 128); ctx.stroke();
          UJ.rotulo(ctx, lz, grupos[g][2], (gx0 + gx1) / 2, 140, { tam: 15, peso: 700, color: L.tono(m.tinta, 0.2) });
        });
      }
      UJ.rotulo(ctx, lz, '≈ 7 minutos de un máximo de 8', W / 2, 14, { tam: 20, peso: 800, color: A, visible: L.tramo(t, 0.9, 0.94) });
      UJ.rotulo(ctx, lz, 'El límite obliga a elegir qué se deja fuera.', W / 2, 545, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
