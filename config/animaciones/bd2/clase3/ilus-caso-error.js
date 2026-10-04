/* Ilustracion: anatomia del bloque DO de un caso de ERROR. Si el CALL termina sin excepcion, la
 * prueba FALLO; si cae en EXCEPTION, se registra SQLERRM. Debajo, los cuatro casos y el conteo
 * de cita antes y despues (10 -> 11) que prueba que el caso valido si escribio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-caso-error', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      var lin = [
        ['DO $$', 0], ['BEGIN', 0], ['CALL sp_agendar_cita(3, 2, ...);', 1],
        ["INSERT ... ('FALLO: no lanzó error', FALSE);", 1],
        ['EXCEPTION WHEN OTHERS THEN', 0],
        ['INSERT ... (SQLERRM, TRUE);', 1], ['END $$;', 0]
      ];
      L.rectRed(ctx, 20, 20, 520, 300, 12); L.rellena(ctx, L.tono(m.tinta, -0.55));
      ctx.font = '500 15px Consolas, monospace'; ctx.fillStyle = '#E8F4FA'; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      for (var i = 0; i < lin.length; i++) ctx.fillText(lin[i][0], 36 + lin[i][1] * 18, 38 + i * 40, 490);
      // Notas al margen
      function nota(y, txt, col) {
        L.flecha(ctx, 556, y + 12, 542, y + 12, col, 3, 1);
        L.rectRed(ctx, 560, y - 10, 222, 48, 10); L.rellena(ctx, L.tono(col, 0.9), col, 2);
        UJ.rotulo(ctx, lz, txt, 671, y - 2, { tam: 15, peso: 700, color: col, ancho: 210 });
      }
      nota(118, 'si llega aquí sin error, la prueba FALLÓ', R);
      nota(192, 'aquí cae el error esperado', V);
      nota(246, 'SQLERRM = el texto del error', A);
      // Cuatro casos
      UJ.rotulo(ctx, lz, 'Un bloque por caso', 30, 340, { tam: 20, peso: 800, color: A, alinear: 'left' });
      var casos = [['mascota activa', 'se crea la cita', V], ['inactiva (3)', 'error', R], ['no existe (99)', 'error', R], ['franja ocupada', 'error', R]];
      for (var k = 0; k < 4; k++) {
        var x = 20 + k * 192;
        L.rectRed(ctx, x, 376, 180, 70, 10); L.rellena(ctx, L.tono(casos[k][2], 0.9), casos[k][2], 2);
        UJ.rotulo(ctx, lz, casos[k][0], x + 90, 386, { tam: 16, peso: 700, ancho: 170 });
        UJ.rotulo(ctx, lz, casos[k][1], x + 90, 414, { tam: 15, color: casos[k][2] });
      }
      // Conteo
      L.rectRed(ctx, 20, 470, W - 40, 140, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'SELECT COUNT(*) FROM cita;', W / 2, 482, { tam: 18, peso: 700 });
      UJ.rotulo(ctx, lz, '10', 260, 516, { tam: 44, peso: 800, color: A });
      L.flecha(ctx, 310, 544, 470, 544, A, 4, 1);
      UJ.rotulo(ctx, lz, '11', 530, 516, { tam: 44, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'antes · después: el caso válido escribió y los tres errores no dejaron nada', W / 2, 582, { tam: 15, ancho: W - 60 });
    }
  });
})();
