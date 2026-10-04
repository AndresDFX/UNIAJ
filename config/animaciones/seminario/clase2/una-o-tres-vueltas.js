/* Una vuelta larga contra tres vueltas cortas: en una sola, el malentendido de la semana 2 se
 * descubre en la 15; en ciclos, la clinica opina al final de cada vuelta. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('una-o-tres-vueltas', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.42, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      var cols = [A, m.acento, L.tono(A, 0.35), m.verde], letras = ['R', 'D', 'C', 'P'];
      function xs(s) { return 60 + (s - 1) * 48; }       // inicio de la semana s
      function barra(xa, xb, y, h, p) {
        var w = (xb - xa) / 4;
        for (var k = 0; k < 4; k++) {
          var q = Math.max(0, Math.min(1, p * 4 - k));
          if (q <= 0) continue;
          L.rectRed(ctx, xa + k * w, y, w * q, h, 4); L.rellena(ctx, cols[k], m.papel, 2);
          if (q > 0.6) UJ.rotulo(ctx, lz, letras[k], xa + k * w + w / 2, y + h / 2 - 11, { tam: 18, peso: 800, color: m.papel });
        }
      }
      // Carril 1
      UJ.rotulo(ctx, lz, 'Una vuelta', 24, 24, { tam: 24, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0, 0.06) });
      barra(xs(1), xs(16), 130, 46, L.tramo(t, 0.04, 0.2));
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.1), function () {
        UJ.rotulo(ctx, lz, 'sem 1', xs(1) + 24, 184, { tam: 17, peso: 600, color: m.gris });
        UJ.rotulo(ctx, lz, 'sem 15', xs(15) + 24, 184, { tam: 17, peso: 600, color: m.gris });
      });
      UJ.alfa(ctx, L.tramo(t, 0.2, 0.27), function () {
        L.trazo(ctx, [[xs(2) + 24, 118], [xs(2) + 24, 186]], 1, R, 5);
        UJ.rotulo(ctx, lz, 'malentendido (sem 2)', xs(2) + 10, 84, { tam: 18, peso: 700, color: R, alinear: 'left' });
      });
      UJ.alfa(ctx, L.tramo(t, 0.28, 0.4), function () {
        ctx.save(); ctx.setLineDash([8, 7]);
        L.trazo(ctx, [[xs(2) + 24, 190], [xs(2) + 24, 236], [xs(15) + 24, 236], [xs(15) + 24, 212]], 1, R, 2.5);
        ctx.restore();
        UJ.sello(ctx, lz, xs(15) - 20, 92, 18, false, 1);
        UJ.rotulo(ctx, lz, 'el cliente ve algo solo en la 15', xs(9), 246, { tam: 17, peso: 700, color: R, ancho: 360 });
      });
      // Carril 2
      UJ.rotulo(ctx, lz, 'En ciclos', 24, 290, { tam: 24, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0.42, 0.47) });
      var nombres = ['ficha del paciente', 'historial', 'reportes'];
      for (var v = 0; v < 3; v++) {
        var xa = xs(1 + v * 5), xb = xs(6 + v * 5) - 10, a0 = 0.46 + v * 0.11;
        UJ.rotulo(ctx, lz, nombres[v], (xa + xb) / 2, 340, { tam: 18, peso: 700, visible: L.tramo(t, a0, a0 + 0.03) });
        barra(xa, xb, 372, 42, L.tramo(t, a0, a0 + 0.07));
        UJ.sello(ctx, lz, (xa + xb) / 2, 450, 18, true, L.tramo(t, a0 + 0.07, a0 + 0.1));
        UJ.rotulo(ctx, lz, 'la clínica opina', (xa + xb) / 2, 476, { tam: 17, peso: 700, color: V, visible: L.tramo(t, a0 + 0.08, a0 + 0.11) });
      }
      UJ.rotulo(ctx, lz, 'En ciclos el error se corrige cuando todavía es barato.', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
