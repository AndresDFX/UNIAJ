/* Control pesimista: SELECT ... FOR UPDATE bloquea la fila. T2 pide la misma fila con la misma
 * clausula y espera; T1 descuenta 3 (5 -> 2) y confirma; T2 entra y lee 2, no 5. El costo es la
 * espera: transacciones cortas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('for-update', {
    duracion: 5,
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 16, W - 40, 'SELECT stock FROM insumo WHERE id_insumo = 40 FOR UPDATE;', L.tramo(t, 0, 0.12), 17);
      // La fila
      var stock = t < 0.5 ? 5 : 2;
      var bloqueada = t >= 0.14 && t < 0.62;
      UJ.alfa(ctx, L.tramo(t, 0.08, 0.14), function () {
        L.rectRed(ctx, 290, 100, 220, 130, 16); L.rellena(ctx, bloqueada ? L.tono(R, 0.88) : L.tono(A, 0.92), bloqueada ? R : A, 3);
        UJ.rotulo(ctx, lz, 'insumo 40', 400, 112, { tam: 19, peso: 700 });
        UJ.rotulo(ctx, lz, 'stock ' + stock, 400, 146, { tam: 36, peso: 800, color: bloqueada ? R : A });
        if (bloqueada) UJ.rotulo(ctx, lz, 'bloqueo exclusivo', 400, 196, { tam: 16, peso: 800, color: R });
      });
      // T1
      UJ.caja(ctx, lz, 20, 100, 230, 80, 'T1', 'obtiene la fila', A, L.tramo(t, 0.12, 0.18));
      L.flecha(ctx, 252, 140, 288, 160, A, 3, L.tramo(t, 0.14, 0.2));
      // T2 espera
      UJ.caja(ctx, lz, 550, 100, 230, 80, 'T2', 'pide la fila: espera', C, L.tramo(t, 0.22, 0.28));
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.32) * (t < 0.62 ? 1 : 0), function () {
        L.circulo(ctx, 665, 230, 26); L.rellena(ctx, m.papel, C, 3);
        var ang = -Math.PI / 2 + t * 18;
        L.trazo(ctx, [[665, 230], [665 + 18 * Math.cos(ang), 230 + 18 * Math.sin(ang)]], 1, C, 3);
        L.trazo(ctx, [[665, 230], [665, 216]], 1, C, 3);
      });
      // T1 escribe y confirma
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.46), function () {
        UJ.codigo(ctx, lz, 20, 290, 370, 'T1: UPDATE stock = 5 - 3; COMMIT;', 1, 16);
      });
      UJ.sello(ctx, lz, 375, 284, 18, true, L.tramo(t, 0.5, 0.56));
      // T2 entra
      L.flecha(ctx, 548, 160, 512, 175, C, 3, L.tramo(t, 0.62, 0.68));
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.8), function () {
        UJ.codigo(ctx, lz, 410, 290, 370, 'T2 entra y lee stock = 2', 1, 16);
        UJ.rotulo(ctx, lz, 'valida sobre el dato verdadero', 595, 344, { tam: 18, peso: 700, color: V, ancho: 360 });
      });
      // Costo
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 30, 420, 740, 170, 16); L.rellena(ctx, L.tono(m.tinta, 0.93), L.tono(m.tinta, 0.5), 2);
        UJ.rotulo(ctx, lz, 'Resuelve el doble descuento de stock.', 400, 438, { tam: 21, peso: 800, color: A, ancho: 700 });
        UJ.rotulo(ctx, lz, 'Su costo es la espera: transacciones cortas,', 400, 488, { tam: 19, ancho: 700 });
        UJ.rotulo(ctx, lz, 'nada externo ni ninguna pantalla entre el bloqueo y el COMMIT.', 400, 524, { tam: 19, ancho: 700 });
      });
    }
  });
})();
