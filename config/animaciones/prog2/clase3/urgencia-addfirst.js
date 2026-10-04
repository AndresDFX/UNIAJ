/* Una cola no se recorre para buscar: la urgencia se modela con Deque. addLast para los que
 * llegan, addFirst para el caso critico; pollFirst los saca en ese orden. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('urgencia-addfirst', {
    duracion: 4.8,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'Deque<Turno> sala = new ArrayDeque<>();', L.tramo(t, 0, 0.06), 18);
      UJ.rotulo(ctx, lz, 'frente', 95, 96, { tam: 17, peso: 700, color: R, visible: L.tramo(t, 0.04, 0.08) });
      var corre = L.tramo(t, 0.4, 0.5, 'suave');
      var nombres = ['Luna', 'Michi', 'Rocky'];
      function ficha(x, txt, c, borde) {
        L.rectRed(ctx, x, 124, 140, 62, 12); L.rellena(ctx, L.tono(c, 0.84), c, borde || 2);
        UJ.rotulo(ctx, lz, txt, x + 70, 142, { tam: 21, peso: 700 });
      }
      for (var i = 0; i < 3; i++) {
        var llega = L.tramo(t, 0.08 + i * 0.06, 0.14 + i * 0.06, 'frena');
        if (llega <= 0) continue;
        ficha(L.mezcla(800, 30 + (i + corre) * 160, llega), nombres[i], A);
      }
      var u = L.tramo(t, 0.46, 0.56, 'frena');
      if (u > 0) ficha(L.mezcla(-160, 30, u), 'Firulais', R, 4);
      UJ.rotulo(ctx, lz, 'urgencia', 100, 194, { tam: 16, peso: 700, color: R, visible: L.tramo(t, 0.54, 0.58) });
      // orden de salida
      for (var k = 0; k < 4; k++) {
        var a = L.tramo(t, 0.72 + k * 0.05, 0.76 + k * 0.05);
        if (a <= 0) continue;
        var cx = 100 + k * 160;
        L.circulo(ctx, cx, 222 + 10, 17 * a); L.rellena(ctx, m.tinta);
        UJ.rotulo(ctx, lz, String(k + 1), cx, 221, { tam: 18, peso: 800, color: m.papel });
      }
      function linea(y, cod, res, c, a0) {
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.01), function () { UJ.codigo(ctx, lz, 20, y, 420, cod, L.tramo(t, a0, a0 + 0.06), 17); });
        UJ.rotulo(ctx, lz, res, 460, y + 6, { tam: 18, peso: 700, color: c, alinear: 'left', ancho: 320, visible: L.tramo(t, a0 + 0.05, a0 + 0.1) });
      }
      linea(290, 'sala.addLast(t);  // ×3', 'los que llegan: al final', V, 0.08);
      linea(350, 'sala.addFirst(firulais);', 'el caso crítico pasa adelante', R, 0.4);
      linea(410, 'sala.pollFirst();  // ×4', 'Firulais, Luna, Michi, Rocky', A, 0.7);
      UJ.rotulo(ctx, lz, 'Buscar a alguien dentro de la cola para sacarlo: ya no es una cola pura.', W / 2, 500, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.88, 0.94) });
      UJ.rotulo(ctx, lz, 'Consumir es poll; mirar es peek o for-each (size() sigue igual).', W / 2, 560, { tam: 19, color: A, ancho: W - 40, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
