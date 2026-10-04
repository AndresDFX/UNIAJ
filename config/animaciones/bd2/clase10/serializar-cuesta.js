/* Serializar de verdad cuesta: ocho recepcionistas en paralelo terminan casi a la vez; en fila,
 * cada una espera a la anterior y el tiempo percibido se multiplica. Aislamiento es la pregunta de
 * que ve mi transaccion de las otras; es la I de ACID y la unica que se configura. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('serializar-cuesta', {
    duracion: 5,
    pasos: [0.34, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      var u = 72; // ancho de una operacion
      // En paralelo
      UJ.rotulo(ctx, lz, 'Ocho a la vez', 30, 16, { tam: 21, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0, 0.05) });
      var p = L.tramo(t, 0.06, 0.26);
      for (var i = 0; i < 8; i++) {
        if (p > 0) { L.rectRed(ctx, 30, 52 + i * 18, u * p, 13, 4); L.rellena(ctx, L.tono(A, 0.4)); }
      }
      UJ.rotulo(ctx, lz, '1 unidad de tiempo', 120, 106, { tam: 17, peso: 700, color: A, alinear: 'left', visible: L.tramo(t, 0.24, 0.3) });
      // En fila
      UJ.rotulo(ctx, lz, 'Una después de otra', 30, 220, { tam: 21, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0.36, 0.4) });
      for (var k = 0; k < 8; k++) {
        var q = L.tramo(t, 0.4 + k * 0.03, 0.43 + k * 0.03);
        if (q > 0) { L.rectRed(ctx, 30 + k * u, 256 + k * 18, u * q, 13, 4); L.rellena(ctx, L.tono(R, 0.4)); }
        if (t > 0.4 && q < 1) { L.rectRed(ctx, 30, 256 + k * 18, k * u, 13, 4); ctx.strokeStyle = L.tono(R, 0.7); ctx.lineWidth = 1; ctx.stroke(); }
      }
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.7), function () {
        UJ.rotulo(ctx, lz, '8 unidades de tiempo: cada una espera a la anterior', 400, 404, { tam: 18, peso: 700, color: R, ancho: 700 });
      });
      // La pregunta del aislamiento
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.84), function () {
        L.rectRed(ctx, 30, 440, 740, 160, 16); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Aislamiento: ¿qué ve mi transacción de las otras que todavía no terminan?', 400, 458, { tam: 20, peso: 800, color: L.tono(C, -0.4), ancho: 700 });
        UJ.rotulo(ctx, lz, 'La I de ACID: la única de las cuatro que el desarrollador configura.', 400, 530, { tam: 19, ancho: 700 });
      });
    }
  });
})();
