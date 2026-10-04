/* Fragmentos combinados de la secuencia: alt (caminos excluyentes), opt (solo si se cumple la
 * condicion) y loop (se repite por cada elemento). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('fragmentos', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, T = m.tinta, G = m.gris, V = m.verde, R = m.malva;
      var px = [110, 300, 490, 690], ns = [':PantallaAgenda', ':ControlAgenda', ':RepositorioCitas', ':Mensajería'];
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        for (var i = 0; i < 4; i++) {
          L.rectRed(ctx, px[i] - 86, 20, 172, 40, 8); L.rellena(ctx, L.tono(A, 0.88), A, 2);
          UJ.rotulo(ctx, lz, ns[i], px[i], 30, { tam: 16, peso: 700, color: A });
          UJ.linea(ctx, px[i], 60, px[i], 612, L.tono(G, 0.3), 2, 1, true);
        }
      });
      function marco(y, h, tag, nota, c, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 24, y, 752, h, 4); L.rellena(ctx, L.tono(c, 0.93, 0.55), c, 2.5);
          ctx.beginPath(); ctx.moveTo(24, y); ctx.lineTo(96, y); ctx.lineTo(96, y + 22); ctx.lineTo(86, y + 32); ctx.lineTo(24, y + 32); ctx.closePath();
          L.rellena(ctx, c);
          UJ.rotulo(ctx, lz, tag, 58, y + 6, { tam: 18, peso: 800, color: m.papel });
          UJ.rotulo(ctx, lz, nota, 764, y + 8, { tam: 16, peso: 700, color: L.tono(c, -0.3), alinear: 'right' });
        });
      }
      function guarda(x, y, txt, c, a) {
        UJ.alfa(ctx, a, function () {
          var w = UJ.medir(ctx, lz, txt, 17, 700) + 12;
          L.rectRed(ctx, x - 6, y - 2, w, 26, 5); L.rellena(ctx, m.papel);
          UJ.rotulo(ctx, lz, txt, x, y, { tam: 17, peso: 700, color: L.tono(c, -0.3), alinear: 'left' });
        });
      }
      function msg(i, j, y, txt, c, p) {
        var x1 = px[i] + (j > i ? 4 : -4), x2 = px[j] + (j > i ? -4 : 4);
        L.flecha(ctx, x1, y, x2, y, c, 2.5, p);
        if (p >= 0.95) {
          var w = UJ.medir(ctx, lz, txt, 16, 600) + 12, mx = (x1 + x2) / 2;
          L.rectRed(ctx, mx - w / 2, y - 27, w, 23, 5); L.rellena(ctx, m.papel);
          UJ.rotulo(ctx, lz, txt, mx, y - 25, { tam: 16, peso: 600, color: c });
        }
      }
      // alt
      marco(76, 228, 'alt', 'dos caminos excluyentes', A, L.tramo(t, 0.08, 0.14));
      guarda(110, 118, '[hay horario]', A, L.tramo(t, 0.14, 0.18));
      msg(1, 2, 174, 'guardarCita()', A, L.tramo(t, 0.18, 0.25));
      UJ.alfa(ctx, L.tramo(t, 0.25, 0.28), function () {
        ctx.save(); ctx.setLineDash([10, 7]); L.trazo(ctx, [[24, 196], [776, 196]], 1, A, 2); ctx.restore();
      });
      guarda(110, 208, '[no hay]', A, L.tramo(t, 0.28, 0.31));
      msg(1, 0, 272, 'ofrecerAlternativas()', A, L.tramo(t, 0.31, 0.38));
      // opt
      marco(326, 116, 'opt', 'solo si se cumple', V, L.tramo(t, 0.42, 0.48));
      guarda(110, 366, '[autorizó mensajería]', V, L.tramo(t, 0.48, 0.52));
      msg(1, 3, 422, 'enviarRecordatorio()', L.tono(V, -0.2), L.tramo(t, 0.52, 0.6));
      // loop
      marco(464, 132, 'loop', 'se repite', C, L.tramo(t, 0.72, 0.78));
      guarda(110, 504, '[por cada vacuna]', C, L.tramo(t, 0.78, 0.82));
      msg(1, 2, 568, 'agregarVacuna()', L.tono(C, -0.3), L.tramo(t, 0.82, 0.9));
    }
  });
})();
