/* El savepoint implicito: un bloque BEGIN ... EXCEPTION marca un savepoint al entrar. Si algo
 * falla dentro, se deshace lo escrito en ese bloque y corre el manejador; lo escrito antes del
 * bloque se conserva. Cuesta: un savepoint por vuelta si va dentro de un bucle. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('savepoint-exception', {
    duracion: 5,
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      // Transaccion externa
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, 20, 20, W - 40, 420, 18); L.rellena(ctx, L.tono(A, 0.95), A, 3);
        UJ.rotulo(ctx, lz, 'Transacción', 120, 32, { tam: 20, peso: 800, color: A });
      });
      UJ.alfa(ctx, L.tramo(t, 0.06, 0.14), function () {
        L.rectRed(ctx, 50, 70, 300, 46, 8); L.rellena(ctx, L.tono(V, 0.88), V, 2);
        UJ.rotulo(ctx, lz, 'escritura A', 200, 81, { tam: 19, peso: 700, color: V });
      });
      // Bloque con EXCEPTION
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.22), function () {
        L.rectRed(ctx, 50, 140, W - 100, 270, 14); L.rellena(ctx, L.tono(C, 0.92), C, 2);
        UJ.codigo(ctx, lz, 70, 156, 160, 'BEGIN', 1, 17);
        UJ.codigo(ctx, lz, 70, 352, 560, 'EXCEPTION WHEN OTHERS THEN RAISE NOTICE ...', 1, 17);
      });
      // Bandera del savepoint
      UJ.alfa(ctx, L.tramo(t, 0.22, 0.3), function () {
        L.trazo(ctx, [[260, 150], [260, 196]], 1, R, 4);
        ctx.beginPath(); ctx.moveTo(262, 150); ctx.lineTo(296, 160); ctx.lineTo(262, 172); ctx.closePath(); ctx.fillStyle = R; ctx.fill();
        UJ.rotulo(ctx, lz, 'savepoint implícito', 310, 160, { tam: 18, peso: 800, color: R, alinear: 'left' });
      });
      var deshace = L.tramo(t, 0.6, 0.7);
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.36) * (1 - 0.5 * deshace), function () {
        L.rectRed(ctx, 90, 220, 280, 46, 8); L.rellena(ctx, L.tono(C, 0.7), L.tono(C, -0.3), 2);
        UJ.rotulo(ctx, lz, 'escritura B', 230, 231, { tam: 19, peso: 700 });
      });
      UJ.alfa(ctx, deshace, function () { L.trazo(ctx, [[90, 243], [370, 243]], 1, R, 4); });
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.44), function () {
        L.rectRed(ctx, 420, 220, 300, 46, 8); L.rellena(ctx, L.tono(R, 0.85), R, 2);
        UJ.rotulo(ctx, lz, 'falla', 570, 231, { tam: 19, peso: 800, color: R });
      });
      UJ.rayo(ctx, 690, 200, 50, R, L.tramo(t, 0.4, 0.46));
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.7), function () {
        UJ.rotulo(ctx, lz, 'vuelve al savepoint: B se deshace', 520, 296, { tam: 18, peso: 700, color: R, ancho: 340 });
      });
      UJ.rotulo(ctx, lz, '← A se conserva', 360, 82, { tam: 18, peso: 700, color: V, alinear: 'left', visible: L.tramo(t, 0.66, 0.72) });
      // Costo
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.86), function () {
        L.rectRed(ctx, 20, 470, W - 40, 130, 16); L.rellena(ctx, L.tono(m.tinta, 0.93), L.tono(m.tinta, 0.5), 2);
        UJ.rotulo(ctx, lz, 'Capturar no es lo mismo que dejar propagar.', W / 2, 488, { tam: 21, peso: 800, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'Dentro de un bucle: un savepoint por vuelta, y se paga.', W / 2, 530, { tam: 19, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'Manejadores solo donde hay una decisión que tomar.', W / 2, 562, { tam: 19, ancho: W - 80 });
      });
    }
  });
})();
