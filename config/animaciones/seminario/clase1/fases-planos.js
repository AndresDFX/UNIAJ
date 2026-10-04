/* Las cinco fases del desarrollo: requisitos y diseño son los planos (esta asignatura),
 * construcción y pruebas son la obra. Las metodologías cambian cómo se recorren. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('fases-planos', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.32, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Las fases de construir software', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var fases = ['Requisitos', 'Diseño', 'Construcción', 'Pruebas', 'Mantenimiento'];
      var x0 = 18, an = 136, gap = 22, y = 250, al = 76;
      var col = [A, A, m.acento, m.acento, m.gris];
      for (var i = 0; i < 5; i++) {
        var x = x0 + i * (an + gap), a = L.tramo(t, 0.05 + i * 0.045, 0.1 + i * 0.045);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, an, al, 12); L.rellena(ctx, L.tono(col[i], 0.88), col[i], 2.5);
          UJ.rotulo(ctx, lz, fases[i], x + an / 2, y + al / 2 - 10, { tam: 16, peso: 800, color: L.tono(col[i], -0.3) });
        });
        if (i < 4) L.flecha(ctx, x + an + 2, y + al / 2, x + an + gap - 2, y + al / 2, L.tono(m.tinta, 0.4), 2.5, L.tramo(t, 0.1 + i * 0.045, 0.14 + i * 0.045));
      }
      // Llaves
      function llave(xa, xb, yy, color, p) {
        if (p <= 0) return;
        var mid = (xa + xb) / 2;
        L.trazo(ctx, [[xa, yy + 18], [xa, yy + 6], [mid - 10, yy + 6], [mid, yy - 6], [mid + 10, yy + 6], [xb, yy + 6], [xb, yy + 18]], p, color, 3.5);
      }
      var xa0 = x0, xa1 = x0 + 2 * an + gap, xb0 = x0 + 2 * (an + gap), xb1 = xb0 + 2 * an + gap;
      llave(xa0, xa1, 214, A, L.tramo(t, 0.36, 0.46));
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        UJ.rotulo(ctx, lz, 'los planos', (xa0 + xa1) / 2, 140, { tam: 22, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'esta asignatura', (xa0 + xa1) / 2, 172, { tam: 18, peso: 700, color: L.tono(A, 0.2) });
      });
      llave(xb0, xb1, 214, L.tono(m.acento, -0.2), L.tramo(t, 0.52, 0.6));
      UJ.rotulo(ctx, lz, 'la obra', (xb0 + xb1) / 2, 172, { tam: 22, peso: 800, color: L.tono(m.acento, -0.25), visible: L.tramo(t, 0.58, 0.66) });

      // En ciclos: vuelta de Pruebas a Requisitos
      var pc = L.tramo(t, 0.72, 0.86, 'suave');
      if (pc > 0) {
        var xs = xb0 + an + gap + an / 2, xr = x0 + an / 2, yb = y + al;
        ctx.save(); ctx.setLineDash([10, 8]);
        L.trazo(ctx, [[xs, yb + 4], [xs, yb + 60], [xr, yb + 60], [xr, yb + 10]], pc, m.verde, 3);
        ctx.restore();
        if (pc >= 1) L.flecha(ctx, xr, yb + 30, xr, yb + 6, m.verde, 3, 1);
      }
      UJ.pildora(ctx, lz, W / 2 - 60, y + al + 42, 'una vez, o en ciclos', m.verde, L.tramo(t, 0.84, 0.9), { centrar: true, tam: 18 });

      UJ.rotulo(ctx, lz, 'Lo que cambia entre metodologías es cómo se recorren: una vez o en ciclos.', W / 2, 520,
                { tam: 22, peso: 700, ancho: W - 80, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
