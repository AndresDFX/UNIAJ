/* Diagrama de secuencia de «agendar cita»: cinco participantes con su linea de vida y los
 * mensajes en orden, con retornos punteados. El tiempo corre hacia abajo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('secuencia', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, T = m.tinta, G = m.gris, W = lz.ancho;
      var nombres = [['Recepcionista'], ['Pantalla', 'Agenda'], ['Control', 'Agenda'], ['Repositorio', 'Mascotas'], ['Repositorio', 'Citas']];
      var xs = [100, 250, 400, 550, 700], bw = 136, by = 64, bh = 60, fin = 500;
      UJ.rotulo(ctx, lz, 'Secuencia: agendar una cita', W / 2, 18, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 5; i++) {
        (function (i) {
          var a = L.tramo(t, 0.03 + i * 0.03, 0.09 + i * 0.03);
          UJ.alfa(ctx, a, function () {
            var c = i === 0 ? T : A;
            L.rectRed(ctx, xs[i] - bw / 2, by, bw, bh, 8); L.rellena(ctx, L.tono(c, 0.88), c, 2.5);
            var ls = nombres[i], y0 = by + bh / 2 - ls.length * 11;
            for (var k = 0; k < ls.length; k++) UJ.rotulo(ctx, lz, ls[k], xs[i], y0 + k * 22, { tam: 17, peso: 700, color: c });
          });
          UJ.linea(ctx, xs[i], by + bh, xs[i], fin, L.tono(G, 0.2), 2, L.tramo(t, 0.1 + i * 0.03, 0.24 + i * 0.03), true);
        })(i);
      }
      // El tiempo corre hacia abajo
      UJ.alfa(ctx, L.tramo(t, 0.2, 0.28), function () {
        L.flecha(ctx, 24, 150, 24, 480, L.tono(C, -0.2), 3, 1);
        UJ.rotulo(ctx, lz, 'el tiempo corre hacia abajo', 24, 515, { tam: 17, peso: 700, color: L.tono(C, -0.25), alinear: 'left' });
      });
      var msgs = [
        [0, 1, 165, 'solicitarAgendamiento()', false, 0.3, 0.38],
        [1, 2, 200, 'agendarCita()', false, 0.38, 0.45],
        [2, 3, 250, 'existePorCodigo()', false, 0.45, 0.53],
        [3, 2, 300, 'mascota', true, 0.55, 0.62],
        [2, 4, 345, 'consultarDisponibilidad()', false, 0.68, 0.76],
        [4, 2, 390, 'horariosLibres', true, 0.78, 0.85],
        [2, 1, 432, 'confirmacion(idCita)', true, 0.87, 0.95]
      ];
      for (var j = 0; j < msgs.length; j++) {
        var g = msgs[j], p = L.tramo(t, g[5], g[6], 'frena');
        var x1 = xs[g[0]] + (g[1] > g[0] ? 9 : -9), x2 = xs[g[1]] + (g[1] > g[0] ? -8 : 8);
        var col = g[4] ? L.tono(T, 0.25) : A;
        UJ.flecha(ctx, lz, x1, g[2], x2, g[2], col, p, null, { punteada: g[4], grosor: 2.5 });
        if (p >= 0.95) {
          var w = UJ.medir(ctx, lz, g[3], 16, 600) + 14, mx = (x1 + x2) / 2;
          var lo = Math.min(x1, x2) + 4, hi = Math.max(x1, x2) - 4;
          mx = x2 < x1 ? Math.min(hi - w / 2, Math.max(lo + w / 2, mx)) : Math.max(lo + w / 2, Math.min(hi - w / 2, mx));
          L.rectRed(ctx, mx - w / 2, g[2] - 28, w, 24, 6); L.rellena(ctx, m.papel);
          UJ.rotulo(ctx, lz, g[3], mx, g[2] - 25, { tam: 16, peso: 600, color: col });
        }
      }
      // Barra de activacion del control (encima de los rotulos)
      var act = L.tramo(t, 0.36, 0.95);
      if (act > 0) { L.rectRed(ctx, xs[2] - 7, 196, 14, (432 - 196) * act, 3); L.rellena(ctx, L.tono(A, 0.7), A, 1.5); }
      UJ.rotulo(ctx, lz, 'Mensajes en orden: quién le pide qué a quién.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.95, 1) });
    }
  });
})();
