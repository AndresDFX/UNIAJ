/* Ilustracion: el contrato de sp_agendar_cita lleno, bloque por bloque, como lo lee quien lo llama
 * sin abrir el codigo: firma, llamada, pre y postcondiciones, tabla de errores y decision. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-contrato', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      L.rectRed(ctx, 14, 10, W - 28, 620, 16); L.rellena(ctx, m.papel, A, 3);
      UJ.rotulo(ctx, lz, 'Contrato · sp_agendar_cita', W / 2, 22, { tam: 23, peso: 800, color: A });
      function bloque(y, n, titulo, col) {
        L.rectRed(ctx, 30, y, 34, 34, 17); L.rellena(ctx, col);
        UJ.rotulo(ctx, lz, n, 47, y + 6, { tam: 17, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, titulo, 76, y + 6, { tam: 17, peso: 800, color: col, alinear: 'left' });
      }
      function linea(y, txt, mono) {
        L.texto(ctx, txt, 76, y, { tam: mono ? 14 : 15, color: m.tinta, letra: mono ? 'Consolas, monospace' : lz.letra, ancho: W - 110 });
      }
      bloque(62, '1', 'Firma', A);
      linea(98, 'sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT, p_fecha_hora TIMESTAMP)', true);
      bloque(124, '2', 'Cómo se llama', A);
      linea(160, "CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');", true);
      bloque(186, '3', 'Precondiciones', C);
      linea(222, 'la mascota existe y está activa · la franja del veterinario está libre');
      bloque(248, '4', 'Postcondiciones', C);
      linea(284, "bien: una fila nueva en cita con estado 'PROGRAMADA' · mal: NADA cambia");
      bloque(310, '5', 'Errores: mensaje literal → qué hace la app', R);
      var err = [["'ERROR: la mascota 99 no existe'", 'avisar y pedir otra mascota'],
                 ["'ERROR: la mascota 3 esta inactiva'", 'avisar: reactivar primero'],
                 ["'ERROR: el veterinario 1 ya tiene cita'", 'ofrecer otra hora']];
      for (var i = 0; i < 3; i++) {
        var y = 348 + i * 34;
        L.rectRed(ctx, 76, y, 360, 30, 0); L.rellena(ctx, i % 2 ? L.tono(R, 0.94) : m.papel, L.tono(R, 0.6), 1);
        L.rectRed(ctx, 436, y, 330, 30, 0); L.rellena(ctx, i % 2 ? L.tono(R, 0.94) : m.papel, L.tono(R, 0.6), 1);
        L.texto(ctx, err[i][0], 86, y + 7, { tam: 13, color: m.tinta, letra: 'Consolas, monospace', ancho: 344 });
        L.texto(ctx, err[i][1], 446, y + 6, { tam: 15, color: m.tinta, letra: lz.letra, ancho: 314 });
      }
      bloque(462, '6', 'Decisión de diseño', V);
      linea(498, 'aborta con RAISE EXCEPTION en vez de devolver un código en un OUT:');
      linea(522, 'abortar deshace lo hecho; un código que nadie revisa deja la cita creada.');
      L.rectRed(ctx, 30, 558, W - 60, 56, 10); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Los mensajes del contrato y los de la batería: el mismo texto', W / 2, 574, { tam: 17, peso: 700, ancho: W - 80 });
    }
  });
})();
