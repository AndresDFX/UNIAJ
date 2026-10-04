/* La sustentacion como coreografia: cinco bloques 1-1-2-2-1 minutos = 7; los dos de demo resaltados. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('guion-bloques', {
    duracion: 4.5,
    pasos: [0.4, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, S = m.sello, W = lz.ancho;
      var bl = [['Problema y solución', 1, 0], ['Arquitectura', 1, 0], ['Demo: registrar dueño y mascota', 2, 1], ['Demo: cita, búsqueda y guardado', 2, 1], ['Cierre y límites', 1, 0]];
      var x0 = 40, esc = (W - 80) / 7, y = 200, h = 130, x = x0;
      UJ.rotulo(ctx, lz, '7 minutos, cada bloque con su tiempo', W / 2, 40, { tam: 24, peso: 800, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 5; i++) {
        var an = bl[i][1] * esc, a = L.tramo(t, 0.04 + i * 0.07, 0.1 + i * 0.07, 'frena');
        var demo = bl[i][2] && t >= 0.42;
        var c = demo ? S : A;
        if (a > 0) {
          L.rectRed(ctx, x + 3, y, (an - 6) * a, h, 12); L.rellena(ctx, L.tono(c, demo ? 0.6 : 0.85), demo ? L.tono(S, -0.3) : A, demo ? 4 : 2);
          UJ.alfa(ctx, L.tramo(t, 0.08 + i * 0.07, 0.12 + i * 0.07), function () {
            UJ.rotulo(ctx, lz, bl[i][0], x + an / 2, y + 22, { tam: bl[i][1] === 1 ? 16 : 18, peso: 700, ancho: an - 8 });
            UJ.rotulo(ctx, lz, bl[i][1] + ' min', x + an / 2, y + h - 38, { tam: 20, peso: 800, color: L.tono(c, -0.35) });
          });
        }
        x += an;
      }
      // Regla de tiempo
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.38), function () {
        for (var k = 0; k <= 7; k++) {
          var xx = x0 + k * esc;
          ctx.strokeStyle = L.tono(m.tinta, 0.4); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(xx, y + h + 10); ctx.lineTo(xx, y + h + 22); ctx.stroke();
          UJ.rotulo(ctx, lz, String(k), xx, y + h + 26, { tam: 16 });
        }
        UJ.rotulo(ctx, lz, '1 + 1 + 2 + 2 + 1 = 7 min', W / 2, 400, { tam: 22, peso: 700 });
      });
      // Demo resaltada
      var xd = x0 + 2 * esc;
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.56), function () {
        L.trazo(ctx, [[xd + 4, y - 20], [xd + 4, y - 34], [xd + 4 * esc - 4, y - 34], [xd + 4 * esc - 4, y - 20]], 1, L.tono(S, -0.35), 4);
        UJ.rotulo(ctx, lz, '4 de 7 minutos: la demo', xd + 2 * esc, y - 74, { tam: 22, peso: 800, color: L.tono(S, -0.45) });
      });
      UJ.rotulo(ctx, lz, 'Más de la mitad del tiempo es mostrar que funciona.', W / 2, 470, { tam: 21, ancho: W - 40, visible: L.tramo(t, 0.74, 0.88) });
    }
  });
})();
