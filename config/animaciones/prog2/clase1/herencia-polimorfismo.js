/* Herencia y polimorfismo: Perro y Gato extienden Mascota; se recorre una lista de Mascota
 * llamando hacerSonido() y responde Guau o Miau segun el objeto real. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('herencia-polimorfismo', {
    duracion: 4.8,
    pasos: [0.32, 0.58, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, W = lz.ancho;
      function clase(x, y, w, nombre, lineas, color, a) {
        UJ.alfa(ctx, a, function () {
          var h = 44 + lineas.length * 28 + 8;
          L.rectRed(ctx, x, y, w, h, 12); L.rellena(ctx, L.tono(color, 0.9), color, 3);
          L.rectRed(ctx, x, y, w, 40, 12); L.rellena(ctx, color);
          UJ.rotulo(ctx, lz, nombre, x + w / 2, y + 8, { tam: 20, peso: 800, color: m.papel, letra: 'Consolas, monospace' });
          for (var i = 0; i < lineas.length; i++) UJ.rotulo(ctx, lz, lineas[i], x + 14, y + 48 + i * 28, { tam: 17, alinear: 'left', letra: 'Consolas, monospace' });
        });
      }
      clase(270, 16, 260, 'Mascota', ['nombre, edad', 'hacerSonido()'], A, L.tramo(t, 0, 0.1));
      clase(60, 190, 260, 'Perro extends Mascota', ['raza', 'hacerSonido(): Guau'], C, L.tramo(t, 0.1, 0.2));
      clase(480, 190, 260, 'Gato extends Mascota', ['interior', 'hacerSonido(): Miau'], C, L.tramo(t, 0.14, 0.24));
      // Flechas de herencia (triangulo hueco hacia la superclase)
      function hereda(x1, y1, x2, y2, a) {
        if (a <= 0) return;
        L.trazo(ctx, [[x1, y1], [x2, y2]], a, A, 3);
        if (a < 1) return;
        var ang = Math.atan2(y2 - y1, x2 - x1), p = 18;
        ctx.beginPath(); ctx.moveTo(x2, y2);
        ctx.lineTo(x2 - p * Math.cos(ang - 0.45), y2 - p * Math.sin(ang - 0.45));
        ctx.lineTo(x2 - p * Math.cos(ang + 0.45), y2 - p * Math.sin(ang + 0.45));
        ctx.closePath(); ctx.fillStyle = m.papel; ctx.fill(); ctx.strokeStyle = A; ctx.lineWidth = 3; ctx.stroke();
      }
      hereda(190, 188, 330, 120, L.tramo(t, 0.18, 0.26));
      hereda(610, 188, 470, 120, L.tramo(t, 0.2, 0.28));
      UJ.rotulo(ctx, lz, '«tiene un» sería composición', 400, 166, { tam: 15, color: m.gris, visible: L.tramo(t, 0.26, 0.3) });
      UJ.rotulo(ctx, lz, '«es un»', 400, 140, { tam: 18, peso: 700, color: A, visible: L.tramo(t, 0.26, 0.3) });
      // La lista y el recorrido
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.4), function () {
        UJ.codigo(ctx, lz, 30, 316, W - 60, 'for (Mascota m : mascotas) m.hacerSonido();', L.tramo(t, 0.34, 0.46), 18);
      });
      var items = [['Perro', 'Firulais', 'Guau'], ['Gato', 'Michi', 'Miau'], ['Perro', 'Rocky', 'Guau']];
      for (var i = 0; i < 3; i++) {
        var x = 40 + i * 250, a = L.tramo(t, 0.4 + i * 0.04, 0.46 + i * 0.04);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, 380, 220, 70, 12); L.rellena(ctx, L.tono(V, 0.88), V, 3);
          UJ.rotulo(ctx, lz, items[i][1], x + 110, 388, { tam: 21, peso: 800 });
          UJ.rotulo(ctx, lz, 'objeto real: ' + items[i][0], x + 110, 418, { tam: 16, color: V, peso: 700 });
        });
        // Globo con el sonido
        var g = L.tramo(t, 0.62 + i * 0.08, 0.7 + i * 0.08, 'atras');
        if (g > 0) {
          var cx = x + 110, cy = 500;
          ctx.save(); ctx.translate(cx, cy); ctx.scale(g, g);
          L.rectRed(ctx, -70, -22, 140, 48, 24); L.rellena(ctx, m.sello, L.tono(m.sello, -0.4), 2);
          ctx.beginPath(); ctx.moveTo(-10, -22); ctx.lineTo(0, -36); ctx.lineTo(10, -22); ctx.closePath(); ctx.fillStyle = m.sello; ctx.fill();
          UJ.rotulo(ctx, lz, '¡' + items[i][2] + '!', 0, -12, { tam: 24, peso: 800 });
          ctx.restore();
        }
      }
      UJ.rotulo(ctx, lz, 'El mismo mensaje; responde el objeto real.', W / 2, 570, { tam: 23, peso: 800, color: A, ancho: W - 40, visible: L.tramo(t, 0.88, 0.97) });
    }
  });
})();
