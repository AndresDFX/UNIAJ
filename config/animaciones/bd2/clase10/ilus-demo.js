/* Ilustracion: que observar en la demo de concurrencia. 1) Sin restriccion la base acepta dos
 * citas en la misma franja y la consulta de deteccion la encuentra. 2) Con la restriccion, el
 * segundo INSERT falla con 23505. 3) FOR UPDATE corre sin error en una sola sesion: la espera de
 * T2 no se puede ver aqui, se documenta en una linea de tiempo T1/T2. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 8, { tam: 26, peso: 800, color: A });
      function banda(y, n, titulo, color) {
        L.rectRed(ctx, 20, y, 760, 176, 16); L.rellena(ctx, L.tono(color, 0.93), color, 2);
        L.circulo(ctx, 52, y + 30, 18); L.rellena(ctx, color);
        UJ.rotulo(ctx, lz, String(n), 52, y + 18, { tam: 20, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, titulo, 82, y + 16, { tam: 21, peso: 800, color: color, alinear: 'left', ancho: 680 });
      }
      // 1 · Sin restriccion
      banda(52, 1, 'Sin restricción: la base acepta la doble reserva', R);
      UJ.codigo(ctx, lz, 40, 100, 380, 'INSERT … vet. 2 · 10:00 · Mishi', 1, 15);
      UJ.codigo(ctx, lz, 40, 138, 380, 'INSERT … vet. 2 · 10:00 · Bobby', 1, 15);
      L.flecha(ctx, 428, 134, 470, 134, R, 4, 1);
      UJ.tabla(ctx, lz, 476, 96, 284, 'HAVING COUNT(*) > 1', ['vet. 2 · 10:00 · 2 citas'], 1, R, -1);
      // 2 · Con la restriccion
      banda(240, 2, 'Con la restricción: el segundo INSERT falla', A);
      UJ.codigo(ctx, lz, 40, 288, 720, 'DELETE el duplicado  →  ALTER TABLE … UNIQUE (id_veterinario, fecha_hora)', 1, 15);
      UJ.codigo(ctx, lz, 40, 326, 380, 'INSERT … vet. 1 · 2026-09-01 08:00', 1, 15);
      L.flecha(ctx, 428, 342, 470, 342, A, 4, 1);
      L.rectRed(ctx, 476, 324, 284, 74, 10); L.rellena(ctx, L.tono(R, 0.9), R, 2);
      UJ.rotulo(ctx, lz, 'ERROR 23505', 618, 332, { tam: 18, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'duplicate key value violates unique constraint', 618, 358, { tam: 13, ancho: 270 });
      // 3 · FOR UPDATE en una sola sesion
      banda(428, 3, 'FOR UPDATE: corre sin error; la espera se documenta', C);
      UJ.codigo(ctx, lz, 40, 476, 380, 'SELECT … WHERE id_insumo = 2 FOR UPDATE;', 1, 15);
      UJ.rotulo(ctx, lz, 'una sola sesión: nadie más tiene la fila,', 210, 520, { tam: 15, ancho: 360 });
      UJ.rotulo(ctx, lz, 'así que nunca hay espera visible', 210, 542, { tam: 15, ancho: 360 });
      var cols = ['paso', 'T1', 'T2'];
      for (var k = 0; k < 3; k++) {
        L.rectRed(ctx, 476 + k * 96, 474, 90, 30, 6); L.rellena(ctx, C);
        UJ.rotulo(ctx, lz, cols[k], 521 + k * 96, 479, { tam: 15, peso: 800, color: m.papel });
        for (var f = 0; f < 3; f++) {
          L.rectRed(ctx, 476 + k * 96, 508 + f * 28, 90, 24, 4); L.rellena(ctx, m.papel, L.tono(C, 0.5), 1);
        }
      }
      var celdas = [['1', 'bloquea', '—'], ['2', '—', 'espera'], ['3', 'COMMIT', 'entra']];
      for (var r = 0; r < 3; r++) for (var c2 = 0; c2 < 3; c2++)
        UJ.rotulo(ctx, lz, celdas[r][c2], 521 + c2 * 96, 511 + r * 28, { tam: 13, peso: 600 });
    }
  });
})();
