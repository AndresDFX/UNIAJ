/* La cola FIFO con Queue: offer x3 entra por el final; peek mira el primero sin cambiar size;
 * poll lo saca; con la cola vacia poll y peek devuelven null. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cola-fifo', {
    duracion: 5,
    // Pasos LOGICOS: 1) offer x3: entran por el final, 2) peek mira a Luna sin sacarla,
    // 3) poll saca a Luna, 4) la cola se vacia y el siguiente poll da null, 5) la conclusion.
    // La linea «cola vacia» llega cuando la cola de verdad esta vacia (antes la decia con dos
    // turnos todavia en pantalla).
    pasos: [0.25, 0.42, 0.62, 0.87, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'Queue<Turno> sala = new LinkedList<>();', L.tramo(t, 0, 0.05), 18);
      UJ.rotulo(ctx, lz, 'frente', 115, 92, { tam: 17, peso: 700, color: R, visible: L.tramo(t, 0.03, 0.07) });
      UJ.rotulo(ctx, lz, 'final', 690, 92, { tam: 17, peso: 700, color: V, visible: L.tramo(t, 0.03, 0.07) });
      var nombres = ['Luna', 'Michi', 'Rocky'];
      var sale = L.tramo(t, 0.45, 0.53, 'suave'), corre = L.tramo(t, 0.51, 0.59, 'suave');
      var vacia = L.tramo(t, 0.65, 0.73, 'suave');
      for (var i = 0; i < 3; i++) {
        var llega = L.tramo(t, 0.06 + i * 0.05, 0.11 + i * 0.05, 'frena');
        var x = L.mezcla(780, 50 + i * 150, llega);
        var y = 120, a = llega > 0 ? 1 : 0;
        if (i === 0) { x -= 160 * sale; a *= 1 - sale; }
        else { x -= 150 * corre + 160 * vacia; a *= 1 - vacia; }
        UJ.alfa(ctx, a, function () {
          var mira = i === 0 && t > 0.27;
          L.rectRed(ctx, x, y, 130, 60, 12); L.rellena(ctx, L.tono(mira ? S : A, 0.82), mira ? m.tinta : A, mira ? 4 : 2);
          UJ.rotulo(ctx, lz, nombres[i], x + 65, y + 17, { tam: 21, peso: 700 });
        });
      }
      var n = t < 0.11 ? 0 : t < 0.16 ? 1 : t < 0.21 ? 2 : 3;
      if (t >= 0.53) n = 2;
      if (t >= 0.71) n = 0;
      if (t > 0.08) UJ.rotulo(ctx, lz, 'size() = ' + n, W / 2, 200, { tam: 20, peso: 700, color: A });
      function linea(y, cod, res, c, a0) {
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.01), function () { UJ.codigo(ctx, lz, 20, y, 400, cod, L.tramo(t, a0, a0 + 0.06), 17); });
        UJ.rotulo(ctx, lz, res, 440, y + 6, { tam: 18, peso: 700, color: c, alinear: 'left', ancho: 340, visible: L.tramo(t, a0 + 0.05, a0 + 0.1) });
      }
      linea(250, 'sala.offer(x);  // ×3', 'entran por el final', V, 0.05);
      linea(300, 'sala.peek();', 'Luna: lo mira; size sigue en 3', m.tinta, 0.28);
      linea(350, 'sala.poll();', 'saca a Luna; size pasa a 2', R, 0.45);
      linea(400, 'sala.poll();  // ×2', 'salen Michi y Rocky: cola vacía', R, 0.64);
      linea(450, 'sala.poll();  // cola vacía', 'null, sin excepción (peek igual)', A, 0.76);
      UJ.rotulo(ctx, lz, 'FIFO: el primero que entra es el primero que sale.', W / 2, 528, { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.89, 0.95) });
      UJ.rotulo(ctx, lz, 'Queue es interfaz: new Queue<>() no compila.', W / 2, 572, { tam: 19, color: R, ancho: W - 40, visible: L.tramo(t, 0.91, 0.98) });
    }
  });
})();
