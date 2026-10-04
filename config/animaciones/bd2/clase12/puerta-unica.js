/* Integrar no es conectarse: o la aplicacion arma texto SQL contra cada tabla, o entra por una
 * unica puerta (los procedimientos) descrita en un contrato que las dos partes respetan. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('puerta-unica', {
    duracion: 5,
    pasos: [0.42, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var tablas = ['dueno', 'mascota', 'cita', 'insumo'];
      function escena(y0, a, puerta, p) {
        UJ.alfa(ctx, a, function () {
          UJ.caja(ctx, lz, 20, y0 + 70, 150, 80, 'Aplicación', '', A, 1);
          for (var i = 0; i < 4; i++) {
            L.rectRed(ctx, 600, y0 + 20 + i * 46, 180, 38, 8); L.rellena(ctx, L.tono(A, 0.9), A, 2);
            UJ.rotulo(ctx, lz, tablas[i], 690, y0 + 27 + i * 46, { tam: 18, peso: 600 });
          }
          if (puerta) {
            L.rectRed(ctx, 330, y0 + 50, 150, 120, 12); L.rellena(ctx, L.tono(V, 0.85), V, 3);
            UJ.rotulo(ctx, lz, 'procedimientos', 405, y0 + 70, { tam: 18, peso: 800, color: L.tono(V, -0.3) });
            UJ.rotulo(ctx, lz, '+ contrato', 405, y0 + 120, { tam: 18, peso: 700, color: L.tono(V, -0.3) });
          }
        });
        if (!puerta) for (var k = 0; k < 4; k++)
          L.flecha(ctx, 174, y0 + 110, 596, y0 + 39 + k * 46, R, 3, L.tramo(p, k * 0.2, 0.3 + k * 0.2));
        else {
          L.flecha(ctx, 174, y0 + 110, 326, y0 + 110, V, 4, L.tramo(p, 0, 0.3));
          for (var j = 0; j < 4; j++) L.flecha(ctx, 484, y0 + 110, 596, y0 + 39 + j * 46, V, 3, L.tramo(p, 0.3 + j * 0.15, 0.5 + j * 0.15));
        }
      }
      UJ.rotulo(ctx, lz, 'Texto SQL contra las tablas', 20, 4, { tam: 21, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0, 0.06) });
      escena(20, L.tramo(t, 0, 0.08), false, L.tramo(t, 0.08, 0.38));
      UJ.rotulo(ctx, lz, 'Una sola puerta', 20, 270, { tam: 21, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0.44, 0.5) });
      escena(286, L.tramo(t, 0.44, 0.52), true, L.tramo(t, 0.52, 0.82));
      UJ.rotulo(ctx, lz, 'Conectarse son dos líneas; integrar es elegir la puerta.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
