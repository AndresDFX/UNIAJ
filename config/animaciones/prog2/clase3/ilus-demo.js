/* Ilustracion: que observar en la demo. Cuatro turnos entran a la cola; peek muestra el primero
 * sin cambiar size() y poll los saca en orden de llegada. Cada atendido entra a la pila del
 * historial con push; pop deshace el ultimo (Nieve) y arriba queda Rocky. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, Y = m.sello, W = lz.ancho;
      var nom = ['Firulais', 'Michi', 'Rocky', 'Nieve'];
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });

      // 1. La sala de espera: cola FIFO
      UJ.rotulo(ctx, lz, '1 · La sala de espera: una cola', W / 2, 54, { tam: 20, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'frente', 160, 90, { tam: 17, peso: 700, color: R });
      UJ.rotulo(ctx, lz, 'final', 610, 90, { tam: 17, peso: 700, color: V });
      for (var i = 0; i < 4; i++) {
        var x = 90 + i * 150, primero = i === 0;
        L.rectRed(ctx, x, 118, 140, 56, 12);
        L.rellena(ctx, L.tono(primero ? Y : A, 0.82), primero ? m.tinta : A, primero ? 3 : 2);
        UJ.rotulo(ctx, lz, nom[i], x + 70, 134, { tam: 20, peso: 700 });
      }
      L.flecha(ctx, 772, 146, 694, 146, V, 4, 1);
      UJ.rotulo(ctx, lz, 'offer ×4', 732, 112, { tam: 16, peso: 700, color: V });
      L.flecha(ctx, 84, 146, 20, 146, R, 4, 1);
      UJ.rotulo(ctx, lz, 'poll', 48, 112, { tam: 16, peso: 700, color: R });
      UJ.codigo(ctx, lz, 24, 194, 210, 'cola.peek();', 1, 16);
      UJ.rotulo(ctx, lz, 'Firulais · size() sigue en 4', 252, 199, { tam: 18, peso: 700, alinear: 'left' });
      UJ.codigo(ctx, lz, 24, 238, 210, 'cola.poll();  // ×4', 1, 16);
      UJ.rotulo(ctx, lz, 'pasan en orden de llegada: Firulais, Michi, Rocky, Nieve', 252, 243,
                { tam: 18, peso: 700, color: R, alinear: 'left', ancho: 524 });
      ctx.strokeStyle = L.tono(m.tinta, 0.75); ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(24, 290); ctx.lineTo(W - 24, 290); ctx.stroke();

      // 2. El historial: pila LIFO
      UJ.rotulo(ctx, lz, '2 · El historial: una pila', W / 2, 302, { tam: 20, peso: 800, color: C });
      UJ.codigo(ctx, lz, 40, 340, 280, 'pila.push(consulta);', 1, 16);
      L.flecha(ctx, 180, 374, 180, 402, C, 4, 1);
      UJ.rotulo(ctx, lz, 'cada atendido', 196, 378, { tam: 15, peso: 600, color: C, alinear: 'left' });
      ctx.strokeStyle = m.tinta; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(30, 612); ctx.lineTo(330, 612); ctx.stroke();
      for (var k = 0; k < 4; k++) {
        var y = 560 - k * 50, ultimo = k === 3, arriba = k === 2;
        UJ.alfa(ctx, ultimo ? 0.4 : 1, function () {
          L.rectRed(ctx, 40, y, 280, 46, 10);
          L.rellena(ctx, L.tono(arriba ? Y : A, 0.82), arriba ? m.tinta : A, arriba ? 3 : 2);
          UJ.rotulo(ctx, lz, 'Consulta de ' + nom[k], 180, y + 12, { tam: 18, peso: 700 });
        });
      }
      UJ.sello(ctx, lz, 320, 412, 16, false, 1);
      function fila(y, cod, res, c) {
        UJ.codigo(ctx, lz, 370, y, 170, cod, 1, 16);
        UJ.rotulo(ctx, lz, res, 556, y + 5, { tam: 18, peso: 700, color: c, alinear: 'left', ancho: 224 });
      }
      fila(350, 'pila.peek();', 'Nieve: la última', m.tinta);
      fila(404, 'pila.pop();', 'se deshace Nieve', R);
      fila(458, 'pila.peek();', 'ahora arriba: Rocky', m.tinta);
      UJ.rotulo(ctx, lz, 'La cola atiende por orden de llegada;', 573, 540, { tam: 18, peso: 600, ancho: 400 });
      UJ.rotulo(ctx, lz, 'la pila deshace lo último.', 573, 568, { tam: 18, peso: 600, ancho: 400 });
    }
  });
})();
