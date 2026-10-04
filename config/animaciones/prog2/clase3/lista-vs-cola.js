/* Cuando la lista permite demasiado. Con un ArrayList, add(0, x) cuela a alguien y compila;
 * con Queue ese metodo no existe: solo offer (al final) y poll (el primero). */
(function () {
  var L = FP_LIENZO;
  function ficha(ctx, lz, x, y, txt, c, a) {
    UJ.alfa(ctx, a, function () {
      L.rectRed(ctx, x, y, 110, 50, 10); L.rellena(ctx, L.tono(c, 0.86), c, 2);
      UJ.rotulo(ctx, lz, txt, x + 55, y + 13, { tam: 19, peso: 700, color: lz.marca.tinta });
    });
  }
  FP_ANIMADOR.registrar('lista-vs-cola', {
    duracion: 4.8,
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      // --- ArrayList
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'List<Turno> sala = new ArrayList<>();', L.tramo(t, 0, 0.08), 18);
      var nombres = ['Luna', 'Michi', 'Rocky'];
      var corre = L.tramo(t, 0.2, 0.3, 'suave');
      for (var i = 0; i < 3; i++) ficha(ctx, lz, 40 + (i + corre) * 130, 80, nombres[i], A, L.tramo(t, 0.04 + i * 0.03, 0.1 + i * 0.03));
      UJ.alfa(ctx, L.tramo(t, 0.12, 0.12 + 0.01), function () { UJ.codigo(ctx, lz, 20, 150, 420, 'sala.add(0, firulais);', L.tramo(t, 0.12, 0.2), 18); });
      var fy = L.claves(t, [[0.2, 10], [0.3, 80, 'frena']]);
      ficha(ctx, lz, 40, fy, 'Firulais', R, L.tramo(t, 0.2, 0.24));
      UJ.sello(ctx, lz, 600, 105, 24, false, L.tramo(t, 0.28, 0.34));
      UJ.rotulo(ctx, lz, 'compila y se coló', 635, 92, { tam: 19, peso: 700, color: R, alinear: 'left', ancho: 150, visible: L.tramo(t, 0.28, 0.34) });
      UJ.rotulo(ctx, lz, 'La regla «el primero que llega pasa primero» quedó rota.', 460, 160, { tam: 16, alinear: 'left', ancho: 320, visible: L.tramo(t, 0.28, 0.34) });
      // --- Queue
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.42), function () {
        ctx.strokeStyle = L.tono(m.tinta, 0.75); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(20, 232); ctx.lineTo(W - 20, 232); ctx.stroke();
      });
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.38 + 0.01), function () { UJ.codigo(ctx, lz, 20, 250, W - 40, 'Queue<Turno> sala = new ArrayDeque<>();', L.tramo(t, 0.38, 0.46), 18); });
      for (var k = 0; k < 3; k++) ficha(ctx, lz, 170 + k * 130, 320, nombres[k], A, L.tramo(t, 0.42 + k * 0.02, 0.48 + k * 0.02));
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.58), function () {
        UJ.codigo(ctx, lz, 20, 470, 420, 'sala.add(0, firulais);', 1, 18);
        ctx.strokeStyle = R; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(30, 490); ctx.lineTo(430, 488); ctx.stroke();
      });
      UJ.sello(ctx, lz, 480, 488, 24, false, L.tramo(t, 0.58, 0.64));
      UJ.rotulo(ctx, lz, 'add(int, E) no existe en Queue: no compila', 520, 470, { tam: 18, peso: 700, color: R, alinear: 'left', ancho: 260, visible: L.tramo(t, 0.6, 0.68) });
      // offer / poll
      var p = L.tramo(t, 0.72, 0.84);
      L.flecha(ctx, 170, 345, 40, 345, R, 4, p);
      L.flecha(ctx, 760, 345, 570, 345, V, 4, p);
      UJ.rotulo(ctx, lz, 'poll(): saca el primero', 110, 390, { tam: 17, peso: 700, color: R, visible: L.tramo(t, 0.78, 0.86) });
      UJ.rotulo(ctx, lz, 'offer(x): entra al final', 650, 390, { tam: 17, peso: 700, color: V, visible: L.tramo(t, 0.78, 0.86) });
      UJ.rotulo(ctx, lz, 'La estructura más limitada blinda la regla del negocio.', W / 2, 570, { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.86, 0.96) });
    }
  });
})();
