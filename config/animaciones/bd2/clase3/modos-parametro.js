/* Modos de parametro: IN por omision; un codigo de retorno OUT se puede ignorar, RAISE EXCEPTION no. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('modos-parametro', {
    duracion: 4.8,
    pasos: [0.3, 0.65, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El modo es la dirección en que viaja el dato', W / 2, 16, { tam: 24, peso: 800, color: A, ancho: W - 40 });
      UJ.caja(ctx, lz, 330, 70, 200, 80, 'procedimiento', null, A, L.tramo(t, 0, 0.08));
      L.flecha(ctx, 40, 120, 326, 120, A, 4, L.tramo(t, 0.08, 0.2, 'frena'));
      UJ.rotulo(ctx, lz, 'p_id_mascota INT', 180, 84, { tam: 18, peso: 700, visible: L.tramo(t, 0.12, 0.2) });
      UJ.rotulo(ctx, lz, '= IN, no se escribe', 545, 98, { tam: 18, color: A, alinear: 'left', visible: L.tramo(t, 0.2, 0.28) });
      var y = 200;
      UJ.rotulo(ctx, lz, 'Código de retorno OUT', 200, y, { tam: 22, peso: 800, color: R, visible: L.tramo(t, 0.3, 0.36) });
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.42), function () {
        UJ.codigo(ctx, lz, 30, y + 44, 340, 'p_resultado := -1;', 1, 18);
      });
      L.flecha(ctx, 200, y + 88, 200, y + 140, R, 3, L.tramo(t, 0.42, 0.5));
      UJ.caja(ctx, lz, 50, y + 144, 300, 80, 'la app no lo mira', 'nada falla', R, L.tramo(t, 0.48, 0.56));
      UJ.rotulo(ctx, lz, 'la regla no se cumplió', 200, y + 240, { tam: 19, peso: 700, color: R, visible: L.tramo(t, 0.56, 0.64) });
      UJ.rotulo(ctx, lz, 'RAISE EXCEPTION', 600, y, { tam: 22, peso: 800, color: A, visible: L.tramo(t, 0.66, 0.7) });
      UJ.alfa(ctx, L.tramo(t, 0.68, 0.74), function () {
        UJ.codigo(ctx, lz, 430, y + 44, 340, "RAISE EXCEPTION '…';", 1, 18);
      });
      L.flecha(ctx, 600, y + 88, 600, y + 140, A, 3, L.tramo(t, 0.74, 0.8));
      UJ.caja(ctx, lz, 450, y + 144, 300, 80, 'el motor devuelve fallo', 'la app no puede ignorarlo', A, L.tramo(t, 0.78, 0.86));
      UJ.rotulo(ctx, lz, 'y nada quedó escrito', 600, y + 240, { tam: 19, peso: 700, color: A, visible: L.tramo(t, 0.86, 0.94) });
      UJ.rotulo(ctx, lz, 'El encabezado es un contrato: nombre, orden y tipos.', W / 2, 560, { tam: 20, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
