/* La lista negra de adjetivos que nadie puede comprobar, tachada; y cómo «que sea rápido» se
 * vuelve un RNF con número que se mide con cronómetro: pasa o no pasa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('lista-negra', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.24, 0.46, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'La lista negra: palabras que no se pueden verificar', W / 2, 22,
        { tam: 23, peso: 800, color: R, ancho: W - 40, visible: L.tramo(t, 0, 0.06) });
      var filas = [['rápido', 'amigable', 'fácil', 'intuitivo', 'robusto'], ['moderno', 'óptimo', 'eficiente', 'seguro']];
      var k = 0;
      for (var f = 0; f < 2; f++) {
        var ws = filas[f].map(function (p) { return UJ.medir(ctx, lz, p, 20, 700) + 28; });
        var total = ws.reduce(function (s, w) { return s + w; }, 0) + (ws.length - 1) * 16;
        var x = (W - total) / 2, y = 76 + f * 58;
        for (var i = 0; i < ws.length; i++) {
          var a = L.tramo(t, 0.06 + k * 0.016, 0.1 + k * 0.016);
          UJ.pildora(ctx, lz, x, y, filas[f][i], m.gris, a, { tam: 20 });
          UJ.rayar(ctx, x + 6, y + 18, ws[i] - 12, R, L.tramo(t, 0.26 + k * 0.02, 0.3 + k * 0.02));
          x += ws[i] + 16; k++;
        }
      }
      // De deseo a requisito
      UJ.alfa(ctx, L.tramo(t, 0.48, 0.54), function () {
        L.rectRed(ctx, 26, 236, 220, 110, 14); L.rellena(ctx, L.tono(m.gris, 0.9), m.gris, 2);
        UJ.rotulo(ctx, lz, 'Lo que dijo', 136, 252, { tam: 17, peso: 700, color: m.gris });
        UJ.rotulo(ctx, lz, '«que sea rápido»', 136, 284, { tam: 21, peso: 700, color: m.tinta });
      });
      UJ.flecha(ctx, lz, 250, 291, 300, 291, A, L.tramo(t, 0.54, 0.58));
      UJ.alfa(ctx, L.tramo(t, 0.58, 0.68), function () {
        L.rectRed(ctx, 304, 220, 470, 142, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
        UJ.pildora(ctx, lz, 322, 234, 'RNF-01', A, 1, { tam: 18, lleno: true });
        UJ.rotulo(ctx, lz, 'Búsqueda en máximo 3 s', 330, 282, { tam: 21, peso: 800, color: L.tono(A, -0.3), alinear: 'left' });
        UJ.rotulo(ctx, lz, 'con 5.000 fichas · 10 usuarios a la vez', 330, 318, { tam: 19, peso: 600, color: m.tinta, alinear: 'left', ancho: 430 });
      });
      // Se mide
      var c = L.tramo(t, 0.78, 0.92);
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.8), function () {
        var cx = 300, cy = 460;
        L.rectRed(ctx, cx - 10, cy - 70, 20, 12, 3); L.rellena(ctx, m.tinta);
        L.circulo(ctx, cx, cy, 56); L.rellena(ctx, m.papel, m.tinta, 4);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, 48, -Math.PI / 2, -Math.PI / 2 + c * Math.PI * 2 * 0.8); ctx.closePath();
        ctx.fillStyle = L.tono(V, 0.6); ctx.fill();
        var ang = -Math.PI / 2 + c * Math.PI * 2 * 0.8;
        L.trazo(ctx, [[cx, cy], [cx + Math.cos(ang) * 44, cy + Math.sin(ang) * 44]], 1, m.tinta, 4);
        UJ.rotulo(ctx, lz, 'se mide delante del cliente', cx, cy + 66, { tam: 17, peso: 600, color: m.tinta });
      });
      UJ.alfa(ctx, L.tramo(t, 0.9, 0.96), function () {
        UJ.sello(ctx, lz, 470, 460, 34, true, 1);
        UJ.rotulo(ctx, lz, 'pasa o no pasa', 520, 446, { tam: 24, peso: 800, color: V, alinear: 'left' });
      });
    }
  });
})();
