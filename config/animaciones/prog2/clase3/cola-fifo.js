/* La cola FIFO con Queue: offer x3 entra por el final; peek mira el primero sin cambiar size;
 * poll lo saca; con la cola vacia poll y peek devuelven null. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cola-fifo', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'Queue<Turno> sala = new LinkedList<>();', L.tramo(t, 0, 0.06), 18);
      UJ.rotulo(ctx, lz, 'frente', 115, 92, { tam: 17, peso: 700, color: R, visible: L.tramo(t, 0.04, 0.08) });
      UJ.rotulo(ctx, lz, 'final', 690, 92, { tam: 17, peso: 700, color: V, visible: L.tramo(t, 0.04, 0.08) });
      var nombres = ['Luna', 'Michi', 'Rocky'];
      var sale = L.tramo(t, 0.6, 0.7, 'suave'), corre = L.tramo(t, 0.68, 0.76, 'suave');
      for (var i = 0; i < 3; i++) {
        var llega = L.tramo(t, 0.07 + i * 0.06, 0.13 + i * 0.06, 'frena');
        var x = L.mezcla(780, 50 + i * 150, llega);
        if (i > 0) x -= 150 * corre;
        var y = 120, a = llega > 0 ? 1 : 0;
        if (i === 0) { x -= 160 * sale; a *= 1 - sale; }
        UJ.alfa(ctx, a, function () {
          var mira = i === 0 && t > 0.34;
          L.rectRed(ctx, x, y, 130, 60, 12); L.rellena(ctx, L.tono(mira ? S : A, 0.82), mira ? m.tinta : A, mira ? 4 : 2);
          UJ.rotulo(ctx, lz, nombres[i], x + 65, y + 17, { tam: 21, peso: 700 });
        });
      }
      var n = t < 0.13 ? 0 : t < 0.19 ? 1 : t < 0.25 ? 2 : 3;
      if (t >= 0.68) n = 2;
      if (t > 0.1) UJ.rotulo(ctx, lz, 'size() = ' + n, W / 2, 200, { tam: 20, peso: 700, color: A });
      function linea(y, cod, res, c, a0) {
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.01), function () { UJ.codigo(ctx, lz, 20, y, 400, cod, L.tramo(t, a0, a0 + 0.06), 17); });
        UJ.rotulo(ctx, lz, res, 440, y + 6, { tam: 18, peso: 700, color: c, alinear: 'left', ancho: 340, visible: L.tramo(t, a0 + 0.05, a0 + 0.1) });
      }
      linea(250, 'sala.offer(x);  // ×3', 'entran por el final', V, 0.06);
      linea(310, 'sala.peek();', 'Luna: lo mira; size sigue en 3', m.tinta, 0.36);
      linea(370, 'sala.poll();', 'saca a Luna; size pasa a 2', R, 0.6);
      linea(430, 'sala.poll();  // cola vacía', 'null, sin excepción (peek igual)', A, 0.83);
      UJ.rotulo(ctx, lz, 'FIFO: el primero que entra es el primero que sale.', W / 2, 520, { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.88, 0.96) });
      UJ.rotulo(ctx, lz, 'Queue es interfaz: new Queue<>() no compila.', W / 2, 565, { tam: 19, color: R, ancho: W - 40, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
