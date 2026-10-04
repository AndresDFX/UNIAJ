/* Inyeccion de SQL: concatenar mete el texto en la sentencia; el parametro viaja como dato despues
 * de que la sentencia ya se analizo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('inyeccion-sql', {
    duracion: 5,
    pasos: [0.25, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El usuario escribe:', 30, 20, { tam: 20, alinear: 'left', visible: L.tramo(t, 0, 0.04) });
      UJ.alfa(ctx, L.tramo(t, 0.02, 0.08), function () {
        L.rectRed(ctx, 230, 12, 400, 44, 8); L.rellena(ctx, m.papel, m.tinta, 2);
      });
      var luna = L.tramo(t, 0.04, 0.12), mala = L.tramo(t, 0.26, 0.36);
      var entrada = mala > 0 ? "Luna' OR '1'='1" : 'Luna';
      L.texto(ctx, entrada, 244, 22, { tam: 20, peso: 700, color: mala > 0 ? R : m.tinta, letra: 'Consolas, monospace', visible: mala > 0 ? mala : luna });
      // Concatenado
      UJ.rotulo(ctx, lz, 'Texto pegado a la sentencia', 30, 90, { tam: 22, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0.12, 0.16) });
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.2), function () {
        var s = mala > 0.5 ? "… WHERE nombre = 'Luna' OR '1'='1'" : "… WHERE nombre = 'Luna'";
        UJ.codigo(ctx, lz, 30, 130, W - 60, s, 1, 18);
      });
      UJ.rotulo(ctx, lz, mala > 0.5 ? 'condición siempre verdadera → todas las mascotas' : 'devuelve a Luna', W / 2, 182,
                { tam: 20, peso: 700, color: mala > 0.5 ? R : A, visible: L.tramo(t, 0.18, 0.24) + (mala > 0.5 ? 1 : 0) });
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.5), function () {
        UJ.tabla(ctx, lz, 30, 220, 330, 'mascota', ['Luna', 'Firulais', 'Michi', 'Rocky', '…'], 5, R, -1);
        UJ.sello(ctx, lz, 340, 222, 22, false, 1);
      });
      // Parametro
      UJ.rotulo(ctx, lz, 'Valor como parámetro', 590, 230, { tam: 22, peso: 800, color: A, visible: L.tramo(t, 0.6, 0.64) });
      var pas = ['1 · el motor analiza la sentencia', '2 · después llega el valor', '3 · se compara como dato'];
      for (var i = 0; i < 3; i++) {
        UJ.caja(ctx, lz, 410, 274 + i * 72, 360, 58, pas[i], null, A, L.tramo(t, 0.64 + i * 0.06, 0.7 + i * 0.06));
      }
      UJ.rotulo(ctx, lz, "ninguna mascota se llama  Luna' OR '1'='1", 590, 498, { tam: 17, peso: 600, ancho: 360, visible: L.tramo(t, 0.84, 0.9) });
      UJ.sello(ctx, lz, 590, 540, 18, true, L.tramo(t, 0.84, 0.9));
      UJ.rotulo(ctx, lz, 'Ojo: un EXECUTE que concatena dentro del procedimiento vuelve a abrir el agujero.', W / 2, 580,
                { tam: 18, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
