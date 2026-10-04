/* Recorrer y borrar: el for-each que borra lanza ConcurrentModificationException; el Iterator
 * con it.remove() saca las de edad >= 9 sin error (o removeIf). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('recorrer-iterator', {
    duracion: 5,
    pasos: [0.36, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      var lista = [['Luna', 3], ['Rocky', 10], ['Michi', 5], ['Firulais', 9]];
      var cw = 170, ch = 70, x0 = 50;
      function fila(y, cursor, quitar, cierra, colCursor) {
        var vis = [], k;
        for (k = 0; k < 4; k++) vis.push(1 - (quitar[k] || 0));
        // posiciones compactadas
        var pos = 0;
        for (k = 0; k < 4; k++) {
          var x = x0 + pos * cw + (1 - cierra) * 0;
          var viejo = x0 + k * cw;
          var xx = L.mezcla(viejo, x, cierra);
          UJ.alfa(ctx, Math.max(0.0, vis[k]), function () {
            var mala = lista[k][1] >= 9;
            L.rectRed(ctx, xx + 6, y, cw - 12, ch, 10); L.rellena(ctx, L.tono(mala ? R : V, 0.85), mala ? R : V, 2);
            UJ.rotulo(ctx, lz, lista[k][0], xx + cw / 2, y + 10, { tam: 20, peso: 800 });
            UJ.rotulo(ctx, lz, 'edad ' + lista[k][1], xx + cw / 2, y + 40, { tam: 16 });
          });
          if (vis[k] > 0.25) pos++;
        }
        if (cursor >= 0) {
          var cx = x0 + cursor * cw + cw / 2;
          ctx.beginPath(); ctx.moveTo(cx, y - 6); ctx.lineTo(cx - 12, y - 26); ctx.lineTo(cx + 12, y - 26); ctx.closePath();
          ctx.fillStyle = colCursor; ctx.fill();
        }
      }
      // 1. for-each que borra
      UJ.alfa(ctx, L.tramo(t, 0, 0.04), function () {
        UJ.codigo(ctx, lz, 24, 14, W - 48, 'for (Mascota m : mascotas) if (m.getEdad() >= 9) mascotas.remove(m);', L.tramo(t, 0, 0.1), 15);
      });
      var c1 = t < 0.1 ? -1 : (t < 0.16 ? 0 : 1);
      var q1 = [0, 0.7 * L.tramo(t, 0.2, 0.24), 0, 0];
      fila(90, c1, q1, 0, A);
      UJ.rayo(ctx, 752, 84, 70, R, L.tramo(t, 0.26, 0.3));
      UJ.alfa(ctx, L.tramo(t, 0.27, 0.33), function () {
        L.rectRed(ctx, 24, 186, W - 48, 48, 10); L.rellena(ctx, R);
        UJ.rotulo(ctx, lz, 'ConcurrentModificationException', W / 2, 197, { tam: 22, peso: 800, color: m.papel, letra: 'Consolas, monospace' });
      });
      // 2. Iterator
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.42), function () {
        L.trazo(ctx, [[24, 256], [W - 24, 256]], 1, L.tono(m.gris, 0.5), 2);
        UJ.codigo(ctx, lz, 24, 270, W - 48, 'Iterator<Mascota> it = mascotas.iterator();', L.tramo(t, 0.38, 0.44), 16);
        UJ.codigo(ctx, lz, 24, 306, W - 48, 'while (it.hasNext()) if (it.next().getEdad() >= 9) it.remove();', L.tramo(t, 0.42, 0.5), 16);
      });
      var c2 = -1;
      if (t >= 0.5 && t < 0.72) c2 = Math.min(3, Math.floor((t - 0.5) / 0.05));
      var q2 = [0, L.tramo(t, 0.56, 0.6), 0, L.tramo(t, 0.66, 0.7)];
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.5), function () { fila(380, c2, q2, L.tramo(t, 0.72, 0.76, 'suave'), V); });
      UJ.sello(ctx, lz, 470, 415, 28, true, L.tramo(t, 0.72, 0.76));
      UJ.rotulo(ctx, lz, 'sin error', 516, 386, { tam: 22, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0.72, 0.76) });
      UJ.rotulo(ctx, lz, 'salen Rocky (10) y Firulais (9)', 516, 418, { tam: 17, peso: 600, alinear: 'left', ancho: 260, visible: L.tramo(t, 0.72, 0.76) });
      // 3. Regla
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.9), function () {
        L.rectRed(ctx, 24, 476, W - 48, 140, 14); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'índice: la posición · for-each: solo leer', W / 2, 490, { tam: 21, peso: 800, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'Borrar al recorrer: Iterator con it.remove(), o', W / 2, 530, { tam: 19, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'mascotas.removeIf(m -> m.getEdad() >= 9);', W / 2, 566, { tam: 18, peso: 700, letra: 'Consolas, monospace', ancho: W - 60 });
      });
    }
  });
})();
