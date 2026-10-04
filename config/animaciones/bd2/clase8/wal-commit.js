/* Durabilidad: el WAL. El motor escribe en un archivo secuencial lo que va a cambiar ANTES de
 * tocar las paginas de datos; el COMMIT solo espera a que ese registro quede grabado. Tras una
 * caida, el log se reproduce. Por eso agrupar COMMIT en cargas masivas es mucho mas rapido. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('wal-commit', {
    duracion: 5,
    // Pasos LOGICOS: 1) el cambio va primero al WAL y el COMMIT espera solo eso; 2) las paginas
    // de datos se escriben despues; 3) la caida y la recuperacion; 4) la consecuencia practica.
    pasos: [0.4, 0.62, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.caja(ctx, lz, 30, 40, 200, 90, 'Cambio', 'UPDATE ...', A, L.tramo(t, 0, 0.08));
      L.flecha(ctx, 235, 85, 320, 85, A, 4, L.tramo(t, 0.08, 0.16));
      // El log secuencial
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.18), function () {
        UJ.rotulo(ctx, lz, 'WAL · registro secuencial', 545, 20, { tam: 19, peso: 800, color: A });
        L.rectRed(ctx, 330, 50, 430, 70, 10); L.rellena(ctx, L.tono(A, 0.94), A, 2);
      });
      var n = Math.floor(L.mezcla(0, 6, L.tramo(t, 0.14, 0.32)));
      for (var i = 0; i < n; i++) { L.rectRed(ctx, 340 + i * 69, 60, 60, 50, 6); L.rellena(ctx, i === 5 ? L.tono(V, 0.5) : L.tono(A, 0.6)); }
      UJ.rotulo(ctx, lz, 'COMMIT = su registro grabado (verde): unos cientos de bytes', 545, 130, { tam: 18, ancho: 430, visible: L.tramo(t, 0.32, 0.4) });
      UJ.sello(ctx, lz, 760, 50, 22, true, L.tramo(t, 0.32, 0.38));
      // Paginas de datos, despues
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () {
        L.rectRed(ctx, 330, 210, 430, 120, 10); L.rellena(ctx, L.tono(m.tinta, 0.94), L.tono(m.tinta, 0.5), 2);
        UJ.rotulo(ctx, lz, 'Páginas de datos', 545, 220, { tam: 19, peso: 800 });
        for (var k = 0; k < 4; k++) { L.rectRed(ctx, 350 + k * 102, 256, 88, 58, 6); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.5), 2); }
        UJ.rotulo(ctx, lz, 'se escriben después, sin prisa', 545, 340, { tam: 18 });
      });
      L.flecha(ctx, 545, 176, 545, 206, L.tono(m.tinta, 0.4), 3, L.tramo(t, 0.5, 0.58));
      // Caida y recuperacion
      UJ.rayo(ctx, 100, 190, 80, R, L.tramo(t, 0.64, 0.7));
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.74), function () {
        UJ.rotulo(ctx, lz, 'se cae el servidor', 120, 280, { tam: 19, peso: 800, color: R, ancho: 200 });
        UJ.rotulo(ctx, lz, 'al volver, reproduce el WAL: lo confirmado sigue ahí', 150, 320, { tam: 18, ancho: 250 });
      });
      // Consecuencia
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 40, 440, 720, 140, 16); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Un COMMIT por fila en 100.000 filas:', 400, 460, { tam: 21, peso: 800, color: L.tono(C, -0.35), ancho: 680 });
        UJ.rotulo(ctx, lz, 'entre 5 y 20 veces más lento que agrupar (orden de magnitud: se mide)', 400, 504, { tam: 19, ancho: 680 });
        UJ.rotulo(ctx, lz, 'WAL en PostgreSQL · redo log en Oracle', 400, 548, { tam: 17, ancho: 680 });
      });
    }
  });
})();
