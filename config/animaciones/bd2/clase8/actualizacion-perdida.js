/* Aislamiento: la actualizacion perdida. Quedan 3 vacunas; dos recepcionistas facturan 3 cada
 * una al mismo tiempo: ambas leen 3, ambas calculan 0, ambas escriben 0. Seis vendidas, tres de
 * aire. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('actualizacion-perdida', {
    duracion: 5,
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      // Las dos sesiones y la fila compartida
      UJ.caja(ctx, lz, 30, 30, 220, 80, 'Recepción 1', 'factura 3', A, L.tramo(t, 0, 0.08));
      UJ.caja(ctx, lz, 550, 30, 220, 80, 'Recepción 2', 'factura 3', C, L.tramo(t, 0, 0.08));
      var stock = t < 0.6 ? 3 : 0;
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.12), function () {
        L.rectRed(ctx, 300, 30, 200, 120, 16); L.rellena(ctx, L.tono(m.tinta, 0.92), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'insumo · vacuna', 400, 42, { tam: 17 });
        UJ.rotulo(ctx, lz, 'stock ' + stock, 400, 76, { tam: 40, peso: 800, color: stock === 0 && t > 0.6 ? R : A });
      });
      function fila(y, txt1, txt2, a, color) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 30, y, 220, 44, 8); L.rellena(ctx, m.papel, A, 2);
          L.texto(ctx, txt1, 140, y + 11, { tam: 18, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
          L.rectRed(ctx, 550, y, 220, 44, 8); L.rellena(ctx, m.papel, C, 2);
          L.texto(ctx, txt2, 660, y + 11, { tam: 18, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, color, 400, y + 10, { tam: 17, peso: 700, color: L.tono(m.tinta, 0.3) });
        });
      }
      fila(190, 'lee stock = 3', 'lee stock = 3', L.tramo(t, 0.14, 0.24), 'a la vez');
      L.flecha(ctx, 320, 150, 250, 205, A, 3, L.tramo(t, 0.16, 0.26));
      L.flecha(ctx, 480, 150, 550, 205, C, 3, L.tramo(t, 0.16, 0.26));
      fila(260, '3 - 3 = 0', '3 - 3 = 0', L.tramo(t, 0.38, 0.46), 'calcula');
      fila(330, 'escribe 0', 'escribe 0', L.tramo(t, 0.5, 0.58), 'confirma');
      L.flecha(ctx, 250, 350, 320, 150, A, 3, L.tramo(t, 0.56, 0.64));
      L.flecha(ctx, 550, 350, 480, 150, C, 3, L.tramo(t, 0.56, 0.64));
      // Resultado
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.82), function () {
        L.rectRed(ctx, 40, 410, 720, 90, 16); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'stock 0 · seis vendidas · tres entregadas de aire', 400, 424, { tam: 22, peso: 800, color: R, ancho: 680 });
        UJ.rotulo(ctx, lz, 'actualización perdida (lost update)', 400, 462, { tam: 18, ancho: 680 });
      });
      UJ.rotulo(ctx, lz, 'Aislamiento: el resultado debe ser el de ejecutarlas una después de la otra.', W / 2, 530, { tam: 20, peso: 700, color: A, ancho: W - 60, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
