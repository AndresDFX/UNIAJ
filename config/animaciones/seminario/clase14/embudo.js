/* El embudo de la sustentacion: de lo general (problema y alcance) a lo particular
 * (decisiones), con sus minutos; y por que empezar por las pantallas no funciona. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('embudo', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.45, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, G = m.gris, T = m.tinta, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El embudo: 12 minutos', W / 2, 16, { tam: 25, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      var niveles = [['Problema y alcance', 3], ['Requisitos', 2], ['Modelo', 2], ['Interfaz', 2], ['Decisiones', 2]];
      var y0 = 62, h = 60, gap = 6, wTop = 700, wBot = 300, cx = W / 2;
      var ancho = function (y) { return wTop - (wTop - wBot) * (y - y0) / (5 * (h + gap)); };
      for (var i = 0; i < 5; i++) {
        (function (i) {
          var a = L.tramo(t, 0.05 + i * 0.07, 0.11 + i * 0.07);
          UJ.alfa(ctx, a, function () {
            var ya = y0 + i * (h + gap), yb = ya + h, wa = ancho(ya), wb = ancho(yb + gap);
            var c = L.mezclaColor(A, C, i / 4);
            ctx.beginPath(); ctx.moveTo(cx - wa / 2, ya); ctx.lineTo(cx + wa / 2, ya); ctx.lineTo(cx + wb / 2, yb); ctx.lineTo(cx - wb / 2, yb); ctx.closePath();
            L.rellena(ctx, L.tono(c, 0.82), c, 2.5);
            UJ.rotulo(ctx, lz, niveles[i][0] + ' · ' + niveles[i][1] + ' min', cx, ya + 17, { tam: 20, peso: 800, color: L.tono(c, -0.35) });
          });
        })(i);
      }
      var yr = y0 + 5 * (h + gap) + 6;
      UJ.alfa(ctx, L.tramo(t, 0.48, 0.55), function () {
        L.rectRed(ctx, cx - 150, yr, 300, 44, 10); L.rellena(ctx, L.tono(G, 0.8), L.tono(G, -0.1), 2);
        UJ.rotulo(ctx, lz, 'Riesgos y cierre · 1 min', cx, yr + 11, { tam: 19, peso: 700, color: T });
      });
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.64), function () {
        UJ.pildora(ctx, lz, cx, yr + 58, '3 + 2 + 2 + 2 + 2 + 1 = 12 min', A, 1, { tam: 19, lleno: true, centrar: true });
      });
      // Orden invertido
      var yi = 532;
      var inv = ['Interfaz', 'Modelo', 'Requisitos', 'Problema'];
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.76), function () {
        UJ.rotulo(ctx, lz, 'Empezar por las pantallas:', 24, yi - 30, { tam: 19, peso: 800, color: R, alinear: 'left' });
      });
      var x = 24;
      for (var k = 0; k < 4; k++) {
        var a = L.tramo(t, 0.74 + k * 0.04, 0.78 + k * 0.04);
        var w = UJ.pildora(ctx, lz, x, yi, inv[k], R, a, { tam: 17 });
        if (k < 3) UJ.alfa(ctx, a, function () { L.flecha(ctx, x + w + 4, yi + 16, x + w + 18, yi + 16, R, 2.5, 1); });
        x += w + 22;
      }
      UJ.sello(ctx, lz, x + 14, yi + 16, 20, false, L.tramo(t, 0.9, 0.95));
      UJ.rotulo(ctx, lz, 'el jurado ve pantallas sin saber qué problema resuelven', W / 2, 590,
                { tam: 19, peso: 600, color: T, ancho: W - 40, visible: L.tramo(t, 0.93, 1) });
    }
  });
})();
