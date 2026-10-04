/* La pila LIFO con Deque: push x3 encima; peek mira el de encima; pop lo saca (como Ctrl+Z). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pila-lifo', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'Deque<Historia> pila = new ArrayDeque<>();', L.tramo(t, 0, 0.06), 18);
      // base
      ctx.strokeStyle = m.tinta; ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(50, 450); ctx.lineTo(330, 450); ctx.stroke();
      var nombres = ['Historia de Luna', 'Historia de Michi', 'Historia de Rocky'];
      var sale = L.tramo(t, 0.6, 0.72, 'suave');
      for (var i = 0; i < 3; i++) {
        var cae = L.tramo(t, 0.07 + i * 0.06, 0.13 + i * 0.06, 'frena');
        if (cae <= 0) continue;
        var y = L.mezcla(90, 450 - (i + 1) * 66, cae), x = 60, a = 1;
        if (i === 2) { y -= 120 * sale; x += 300 * sale; a = 1 - sale; }
        UJ.alfa(ctx, a, function () {
          var mira = i === 2 && t > 0.34;
          L.rectRed(ctx, x, y, 260, 58, 10); L.rellena(ctx, L.tono(mira ? S : A, 0.82), mira ? m.tinta : A, mira ? 4 : 2);
          UJ.rotulo(ctx, lz, nombres[i], x + 130, y + 17, { tam: 19, peso: 700 });
        });
      }
      UJ.rotulo(ctx, lz, 'pila', 190, 462, { tam: 17, color: m.gris || m.tinta });
      function linea(y, cod, res, c, a0) {
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.01), function () { UJ.codigo(ctx, lz, 370, y, 410, cod, L.tramo(t, a0, a0 + 0.06), 17); });
        UJ.rotulo(ctx, lz, res, 380, y + 42, { tam: 18, peso: 700, color: c, alinear: 'left', ancho: 400, visible: L.tramo(t, a0 + 0.05, a0 + 0.1) });
      }
      linea(90, 'pila.push(h);  // ×3', 'cada una queda encima', V, 0.06);
      linea(180, 'pila.peek();', 'Rocky: mira la de encima, no la saca', m.tinta, 0.36);
      linea(270, 'pila.pop();', 'saca a Rocky: deshace lo último', R, 0.6);
      UJ.rotulo(ctx, lz, 'Es el Ctrl+Z: pop deshace la última atención registrada.', 380, 370, { tam: 18, alinear: 'left', ancho: 400, visible: L.tramo(t, 0.74, 0.8) });
      UJ.rotulo(ctx, lz, 'LIFO: siempre se toma el de encima.', W / 2, 510, { tam: 23, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.84, 0.92) });
      UJ.rotulo(ctx, lz, 'Stack es de 1995 (hereda de Vector): hoy se usa Deque con ArrayDeque.', W / 2, 560, { tam: 19, color: A, ancho: W - 40, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
