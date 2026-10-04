/* Ilustracion: la misma logica de facturacion en Oracle (PL/SQL) y en PostgreSQL (PL/pgSQL),
 * fila por fila. El contraste se queda como contraste: el motor del curso es PostgreSQL. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-oracle-pg', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'La misma lógica, dos motores', W / 2, 8, { tam: 24, peso: 800, color: A });
      L.rectRed(ctx, 16, 50, 376, 46, 10); L.rellena(ctx, L.tono(m.tinta, 0.85), L.tono(m.tinta, 0.5), 2);
      UJ.rotulo(ctx, lz, 'Oracle · PL/SQL', 204, 60, { tam: 19, peso: 800 });
      L.rectRed(ctx, 408, 50, 376, 46, 10); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'PostgreSQL · PL/pgSQL', 596, 60, { tam: 19, peso: 800, color: m.papel });
      var f = [
        ['tipos', 'NUMBER', 'INT · NUMERIC'],
        ['filas afectadas', 'SQL%ROWCOUNT', 'GET DIAGNOSTICS v = ROW_COUNT'],
        ['abortar', 'RAISE_APPLICATION_ERROR(-20001, …)', "RAISE EXCEPTION '… %', valor"],
        ['al fallar', 'WHEN OTHERS THEN ROLLBACK; RAISE;', 'nada: la excepción que sale deshace el CALL'],
        ['quién confirma', 'suele hacerlo el procedimiento', 'el llamador']
      ];
      for (var i = 0; i < f.length; i++) {
        var y = 110 + i * 86;
        UJ.rotulo(ctx, lz, f[i][0], W / 2, y - 2, { tam: 14, peso: 800, color: L.tono(m.tinta, 0.3) });
        L.rectRed(ctx, 16, y + 20, 376, 56, 10); L.rellena(ctx, L.tono(m.tinta, 0.94), L.tono(m.tinta, 0.6), 1);
        L.texto(ctx, f[i][1], 204, y + 36, { tam: 15, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace', ancho: 360 });
        L.rectRed(ctx, 408, y + 20, 376, 56, 10); L.rellena(ctx, L.tono(A, 0.92), A, 1);
        L.texto(ctx, f[i][2], 596, y + 36, { tam: 15, peso: 700, color: L.tono(A, -0.3), alinear: 'center', letra: 'Consolas, monospace', ancho: 360 });
      }
      L.rectRed(ctx, 16, 546, W - 32, 78, 12); L.rellena(ctx, L.tono(V, 0.88), V, 2);
      UJ.rotulo(ctx, lz, 'Por qué la base quedó intacta: el CALL es su propia transacción', W / 2, 556, { tam: 17, peso: 800, color: L.tono(V, -0.3), ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'y la excepción propagada la deshace entera; ningún ROLLBACK escrito lo hizo', W / 2, 588, { tam: 15, ancho: W - 60 });
    }
  });
})();
