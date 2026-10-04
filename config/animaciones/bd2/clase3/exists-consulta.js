/* Segundo procedimiento: el UNIQUE ya defiende el dato, pero el IF EXISTS da un mensaje que se
 * entiende y valida lo que la restriccion no ve (cita inexistente o CANCELADA). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('exists-consulta', {
    duracion: 5,
    pasos: [0.34, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Segunda consulta para la cita 7', W / 2, 14, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      // Solo la restriccion
      UJ.rotulo(ctx, lz, 'Solo UNIQUE (id_cita)', 200, 70, { tam: 21, peso: 800, color: R, visible: L.tramo(t, 0.05, 0.1) });
      UJ.alfa(ctx, L.tramo(t, 0.12, 0.22), function () {
        L.rectRed(ctx, 20, 112, 360, 120, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        L.texto(ctx, 'duplicate key value violates unique constraint "consulta_id_cita_key"', 36, 126,
                { tam: 16, color: R, letra: 'Consolas, monospace', ancho: 330 });
      });
      UJ.rotulo(ctx, lz, 'técnico: nombra el índice', 200, 248, { tam: 18, visible: L.tramo(t, 0.22, 0.3) });
      // IF EXISTS
      var X = W / 2 + 10;
      UJ.rotulo(ctx, lz, 'IF EXISTS … RAISE', X + 190, 70, { tam: 21, peso: 800, color: A, visible: L.tramo(t, 0.36, 0.4) });
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.5), function () {
        L.rectRed(ctx, X, 112, 370, 120, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'ERROR: la cita 7 ya tiene consulta registrada', X + 185, 140, { tam: 19, peso: 700, color: A, ancho: 340 });
      });
      UJ.rotulo(ctx, lz, 'lo entiende la recepcionista', X + 190, 248, { tam: 18, visible: L.tramo(t, 0.5, 0.58) });
      // lo que la restriccion no ve
      UJ.rotulo(ctx, lz, 'Lo que el UNIQUE no ve', W / 2, 310, { tam: 22, peso: 800, color: C, visible: L.tramo(t, 0.68, 0.72) });
      UJ.caja(ctx, lz, 40, 360, 340, 80, '¿la cita existe?', null, C, L.tramo(t, 0.72, 0.8));
      UJ.caja(ctx, lz, 420, 360, 340, 80, '¿no CANCELADA?', null, C, L.tramo(t, 0.78, 0.86));
      UJ.rotulo(ctx, lz, 'La restricción es la última línea de defensa; el procedimiento, la primera.', W / 2, 490,
                { tam: 20, ancho: W - 60, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
