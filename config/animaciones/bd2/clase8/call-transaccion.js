/* Un CALL fuera de BEGIN es su propia transaccion. Descuenta 2 del insumo 3 (40 -> 38), se
 * estrella en el insumo 2 (hay 3, pide 10), la excepcion se propaga y todo se deshace: el insumo
 * 3 vuelve a 40 y no queda factura. Quien decide el COMMIT es el llamador. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('call-transaccion', {
    duracion: 5,
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 16, W - 40, 'CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);', L.tramo(t, 0, 0.12), 18);
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.16), function () {
        ctx.save(); ctx.setLineDash([12, 8]);
        L.rectRed(ctx, 20, 80, W - 40, 330, 18); ctx.strokeStyle = A; ctx.lineWidth = 3; ctx.stroke(); ctx.restore();
        UJ.rotulo(ctx, lz, 'una sola transacción: la del CALL', W / 2, 92, { tam: 19, peso: 700, color: A });
      });
      // factura provisional
      var deshecho = L.tramo(t, 0.74, 0.86);
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.2) * (1 - deshecho), function () {
        UJ.caja(ctx, lz, 50, 140, 200, 90, 'factura', 'cabecera insertada', A, 1);
      });
      // insumo 3
      var s3 = t < 0.74 ? Math.round(L.mezcla(40, 38, L.tramo(t, 0.22, 0.32))) : Math.round(L.mezcla(38, 40, deshecho));
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.24), function () {
        L.rectRed(ctx, 300, 140, 200, 120, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'insumo 3 · pide 2', 400, 152, { tam: 18, peso: 700 });
        UJ.rotulo(ctx, lz, 'stock ' + s3, 400, 190, { tam: 34, peso: 800, color: V });
      });
      // insumo 2
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.4), function () {
        L.rectRed(ctx, 550, 140, 200, 120, 14); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'insumo 2 · pide 10', 650, 152, { tam: 18, peso: 700 });
        UJ.rotulo(ctx, lz, 'stock 3', 650, 190, { tam: 34, peso: 800, color: R });
      });
      UJ.sello(ctx, lz, 750, 256, 22, false, L.tramo(t, 0.4, 0.46));
      // Propagacion
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        UJ.codigo(ctx, lz, 300, 290, 450, 'RAISE EXCEPTION: stock insuficiente', 1, 17);
      });
      UJ.rotulo(ctx, lz, 'la excepción se propaga fuera del CALL', W / 2, 350, { tam: 20, peso: 800, color: R, visible: L.tramo(t, 0.56, 0.68) });
      // Resultado
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.9), function () {
        UJ.rotulo(ctx, lz, 'sin factura', 150, 175, { tam: 20, peso: 700, color: L.tono(m.tinta, 0.3) });
        UJ.rotulo(ctx, lz, 'volvió solo', 400, 234, { tam: 16, peso: 700, color: V });
      });
      UJ.alfa(ctx, L.tramo(t, 0.88, 0.98), function () {
        L.rectRed(ctx, 40, 450, 720, 130, 16); L.rellena(ctx, L.tono(A, 0.93), A, 2);
        UJ.rotulo(ctx, lz, 'Quien decide el COMMIT es uno solo: el llamador.', 400, 470, { tam: 22, peso: 800, color: A, ancho: 680 });
        UJ.rotulo(ctx, lz, 'Un procedimiento que confirma por su cuenta le quita la posibilidad de deshacer.', 400, 518, { tam: 18, ancho: 680 });
      });
    }
  });
})();
