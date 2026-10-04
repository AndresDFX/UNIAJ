/* Control pesimista: SELECT ... FOR UPDATE bloquea la fila leida. T1 toma el insumo 2 (stock 3);
 * T2 pide la misma fila con la misma clausula y espera. T1 descuenta 3 y confirma: stock 0 y el
 * bloqueo se libera. T2 entra, lee 0 y rechaza la venta: decidio con el dato verdadero. El costo
 * es la espera: transacciones cortas, o NOWAIT / SKIP LOCKED para no esperar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('for-update', {
    duracion: 5,
    // Pasos LOGICOS: 1) T1 bloquea y T2 espera; 2) T1 descuenta y confirma (se libera);
    // 3) T2 entra y lee el dato verdadero; 4) el costo y las variantes.
    pasos: [0.24, 0.48, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 14, W - 40, 'SELECT stock FROM insumo WHERE id_insumo = 2 FOR UPDATE;', L.tramo(t, 0, 0.08), 17);
      // La fila
      var stock = t < 0.4 ? 3 : 0;
      var bloqueada = t >= 0.1 && t < 0.42;
      UJ.alfa(ctx, L.tramo(t, 0.05, 0.1), function () {
        L.rectRed(ctx, 290, 92, 220, 130, 16); L.rellena(ctx, bloqueada ? L.tono(R, 0.88) : L.tono(A, 0.92), bloqueada ? R : A, 3);
        UJ.rotulo(ctx, lz, 'insumo 2', 400, 104, { tam: 19, peso: 700 });
        UJ.rotulo(ctx, lz, 'stock ' + stock, 400, 136, { tam: 36, peso: 800, color: bloqueada ? R : A });
        if (bloqueada) UJ.rotulo(ctx, lz, 'bloqueo exclusivo', 400, 188, { tam: 16, peso: 800, color: R });
      });
      // 1 · T1 obtiene la fila; T2 espera
      UJ.caja(ctx, lz, 20, 92, 230, 80, 'T1', 'obtiene y bloquea la fila', A, L.tramo(t, 0.06, 0.11));
      L.flecha(ctx, 252, 132, 288, 150, A, 3, L.tramo(t, 0.08, 0.12));
      UJ.caja(ctx, lz, 550, 92, 230, 80, 'T2', 'pide la fila: espera', C, L.tramo(t, 0.13, 0.18));
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.22) * (t < 0.5 ? 1 : 0), function () {
        L.circulo(ctx, 665, 210, 24); L.rellena(ctx, m.papel, C, 3);
        var ang = -Math.PI / 2 + t * 18;
        L.trazo(ctx, [[665, 210], [665 + 16 * Math.cos(ang), 210 + 16 * Math.sin(ang)]], 1, C, 3);
        L.trazo(ctx, [[665, 210], [665, 197]], 1, C, 3);
      });
      // 2 · T1 descuenta y confirma
      UJ.codigo(ctx, lz, 20, 250, 470, 'T1: UPDATE insumo SET stock = stock - 3; COMMIT;', L.tramo(t, 0.27, 0.36), 15);
      UJ.sello(ctx, lz, 512, 266, 18, true, L.tramo(t, 0.37, 0.43));
      UJ.rotulo(ctx, lz, 'el COMMIT libera la fila', 650, 258, { tam: 17, peso: 700, color: A, visible: L.tramo(t, 0.42, 0.47) });
      // 3 · T2 entra y lee el dato verdadero
      L.flecha(ctx, 548, 140, 512, 160, C, 3, L.tramo(t, 0.5, 0.56));
      UJ.codigo(ctx, lz, 20, 312, 470, 'T2 entra y lee stock = 0', L.tramo(t, 0.55, 0.62), 15);
      UJ.rotulo(ctx, lz, 'no alcanza: rechaza la venta', 640, 308, { tam: 18, peso: 800, color: V, ancho: 290, visible: L.tramo(t, 0.62, 0.67) });
      UJ.rotulo(ctx, lz, 'decidió con el dato verdadero', 640, 340, { tam: 16, ancho: 290, visible: L.tramo(t, 0.66, 0.71) });
      // 4 · El costo
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.86), function () {
        L.rectRed(ctx, 30, 410, 740, 200, 16); L.rellena(ctx, L.tono(m.tinta, 0.93), L.tono(m.tinta, 0.5), 2);
        UJ.rotulo(ctx, lz, 'El costo es la espera: transacciones cortas.', 400, 426, { tam: 21, peso: 800, color: A, ancho: 700 });
        UJ.rotulo(ctx, lz, 'Nada externo ni ninguna pantalla entre el bloqueo y el COMMIT.', 400, 470, { tam: 18, ancho: 700 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.88, 0.96), function () {
        UJ.codigo(ctx, lz, 60, 516, 680, 'FOR UPDATE NOWAIT       -> falla de inmediato', 1, 16);
        UJ.codigo(ctx, lz, 60, 556, 680, 'FOR UPDATE SKIP LOCKED  -> salta la fila tomada', 1, 16);
      });
    }
  });
})();
