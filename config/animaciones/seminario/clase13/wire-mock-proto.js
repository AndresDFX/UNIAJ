/* La misma pantalla «Registrar mascota» en tres fidelidades: wireframe (que va y en que orden),
 * mockup (como se ve) y prototipo (como se siente al hacer clic). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('wire-mock-proto', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, T = m.tinta, G = m.gris, V = m.verde, W = lz.ancho;
      var cols = [24, 285, 546], cw = 230, sy = 70, sh = 300;
      var titulos = ['Wireframe', 'Mockup', 'Prototipo'];
      var preg = ['¿qué va y en qué orden?', '¿cómo se ve?', '¿cómo se siente?'];
      var ini = [0, 0.32, 0.62];

      function pantalla(k, a) {
        var x = cols[k], gris = k === 0;
        UJ.alfa(ctx, a, function () {
          UJ.rotulo(ctx, lz, titulos[k], x + cw / 2, sy - 40, { tam: 22, peso: 800, color: gris ? L.tono(G, -0.3) : A });
          L.rectRed(ctx, x, sy, cw, sh, 12); L.rellena(ctx, m.papel, gris ? G : A, 2.5);
          // cabecera
          L.rectRed(ctx, x, sy, cw, 40, 12); L.rellena(ctx, gris ? L.tono(G, 0.6) : A);
          L.rectRed(ctx, x, sy + 28, cw, 12, 0); L.rellena(ctx, gris ? L.tono(G, 0.6) : A);
          UJ.rotulo(ctx, lz, gris ? '[título]' : 'Registrar mascota', x + cw / 2, sy + 9, { tam: 17, peso: 800, color: gris ? T : m.papel });
          if (gris) {
            var cajas = [['búsqueda del dueño', 50], ['datos de la mascota', 120]];
            L.rectRed(ctx, x + 16, sy + 56, cw - 32, 50, 4); L.rellena(ctx, L.tono(G, 0.8), G, 1.5);
            UJ.rotulo(ctx, lz, 'búsqueda del dueño', x + cw / 2, sy + 71, { tam: 17, peso: 600, color: T });
            L.rectRed(ctx, x + 16, sy + 120, cw - 32, 110, 4); L.rellena(ctx, L.tono(G, 0.8), G, 1.5);
            ctx.save(); ctx.strokeStyle = L.tono(G, 0.4); ctx.lineWidth = 1.5; ctx.beginPath();
            ctx.moveTo(x + 16, sy + 120); ctx.lineTo(x + cw - 16, sy + 230); ctx.moveTo(x + cw - 16, sy + 120); ctx.lineTo(x + 16, sy + 230); ctx.stroke(); ctx.restore();
            L.rectRed(ctx, x + 40, sy + 160, cw - 80, 30, 4); L.rellena(ctx, L.tono(G, 0.8));
            UJ.rotulo(ctx, lz, 'datos de la mascota', x + cw / 2, sy + 165, { tam: 17, peso: 600, color: T });
            L.rectRed(ctx, x + cw - 106, sy + 246, 90, 38, 4); L.rellena(ctx, L.tono(G, 0.6), G, 1.5);
            UJ.rotulo(ctx, lz, 'Guardar', x + cw - 61, sy + 255, { tam: 17, peso: 700, color: T });
          } else {
            UJ.rotulo(ctx, lz, 'Dueño', x + 16, sy + 50, { tam: 16, peso: 700, color: A, alinear: 'left' });
            L.rectRed(ctx, x + 16, sy + 72, cw - 32, 32, 6); L.rellena(ctx, L.tono(C, 0.9), C, 1.5);
            UJ.rotulo(ctx, lz, '🔍 CC 1.144.…', x + 26, sy + 78, { tam: 16, peso: 500, color: T, alinear: 'left' });
            UJ.rotulo(ctx, lz, 'Nombre', x + 16, sy + 114, { tam: 16, peso: 700, color: A, alinear: 'left' });
            L.rectRed(ctx, x + 16, sy + 136, cw - 32, 32, 6); L.rellena(ctx, m.papel, C, 1.5);
            UJ.rotulo(ctx, lz, 'Rocky', x + 26, sy + 142, { tam: 16, peso: 500, color: T, alinear: 'left' });
            UJ.rotulo(ctx, lz, 'Especie', x + 16, sy + 178, { tam: 16, peso: 700, color: A, alinear: 'left' });
            L.rectRed(ctx, x + 16, sy + 200, cw - 32, 32, 6); L.rellena(ctx, m.papel, C, 1.5);
            UJ.rotulo(ctx, lz, 'Canino  ▾', x + 26, sy + 206, { tam: 16, peso: 500, color: T, alinear: 'left' });
            L.rectRed(ctx, x + cw - 116, sy + 246, 100, 40, 8); L.rellena(ctx, V);
            UJ.rotulo(ctx, lz, 'Guardar', x + cw - 66, sy + 256, { tam: 18, peso: 800, color: m.papel });
          }
          UJ.rotulo(ctx, lz, preg[k], x + cw / 2, sy + sh + 16, { tam: 19, peso: 700, color: gris ? L.tono(G, -0.35) : L.tono(A, -0.2) });
        });
      }
      pantalla(0, L.tramo(t, ini[0], ini[0] + 0.12));
      pantalla(1, L.tramo(t, ini[1], ini[1] + 0.12));
      pantalla(2, L.tramo(t, ini[2], ini[2] + 0.1));

      // Cursor que hace clic en Guardar
      var bx = cols[2] + cw - 30, byy = sy + 278;
      var cm = L.tramo(t, 0.72, 0.8, 'suave');
      if (cm > 0) {
        var cx = bx + 60 * (1 - cm), cy = byy + 70 * (1 - cm);
        var clic = L.tramo(t, 0.8, 0.84);
        if (clic > 0 && clic < 1) { L.circulo(ctx, bx, byy, 8 + 18 * clic); L.rellena(ctx, null, L.tono(m.sello, -0.2), 3); }
        ctx.save(); ctx.beginPath();
        ctx.moveTo(cx, cy); ctx.lineTo(cx, cy + 26); ctx.lineTo(cx + 7, cy + 20); ctx.lineTo(cx + 12, cy + 30);
        ctx.lineTo(cx + 17, cy + 28); ctx.lineTo(cx + 12, cy + 18); ctx.lineTo(cx + 21, cy + 18); ctx.closePath();
        L.rellena(ctx, T, m.papel, 1.5); ctx.restore();
      }
      // Lleva a la ficha del paciente
      L.flecha(ctx, cols[2] + 40, sy + sh + 46, cols[2] + 40, 446, V, 3, L.tramo(t, 0.84, 0.88));
      UJ.alfa(ctx, L.tramo(t, 0.87, 0.92), function () {
        L.rectRed(ctx, cols[2], 450, cw, 52, 10); L.rellena(ctx, L.tono(V, 0.85), V, 2.5);
        UJ.rotulo(ctx, lz, 'Ficha del paciente', cols[2] + cw / 2, 465, { tam: 18, peso: 800, color: L.tono(V, -0.35) });
      });
      UJ.rotulo(ctx, lz, 'Diseñar es equivocarse barato.', W / 2, 560,
                { tam: 23, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
