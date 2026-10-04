/* Procedimiento y funcion: CALL para que HAGA, SELECT para que DEVUELVA; solo el procedimiento puede
 * COMMIT/ROLLBACK, y SELECT sobre un procedimiento es error. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('procedimiento-funcion', {
    duracion: 4.8,
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      var X = W / 2 + 10;
      UJ.rotulo(ctx, lz, 'PROCEDIMIENTO · hace', 200, 16, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      UJ.alfa(ctx, L.tramo(t, 0.03, 0.1), function () { UJ.codigo(ctx, lz, 20, 64, 360, 'CALL sp_agendar_cita(…);', 1, 17); });
      UJ.caja(ctx, lz, 40, 130, 320, 80, 'cambia los datos', 'puede COMMIT / ROLLBACK', A, L.tramo(t, 0.1, 0.2));
      UJ.rotulo(ctx, lz, 'FUNCIÓN · devuelve', X + 190, 16, { tam: 26, peso: 800, color: C, visible: L.tramo(t, 0.2, 0.25) });
      UJ.alfa(ctx, L.tramo(t, 0.23, 0.3), function () { UJ.codigo(ctx, lz, X, 64, 380, 'SELECT fn_x(…);', 1, 17); });
      UJ.caja(ctx, lz, X + 30, 130, 320, 80, 'un valor para la consulta', 'no puede COMMIT / ROLLBACK', C, L.tramo(t, 0.3, 0.4));
      UJ.rotulo(ctx, lz, 'No son dos sabores del mismo objeto.', W / 2, 250, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.42, 0.52) });
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.82), function () {
        UJ.codigo(ctx, lz, 60, 320, W - 120, 'SELECT sp_agendar_cita(…);', 1, 19);
        UJ.sello(ctx, lz, W - 90, 339, 24, false, 1);
      });
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.92), function () {
        L.rectRed(ctx, 60, 400, W - 120, 80, 10); L.rellena(ctx, L.tono(R, 0.88), R, 2);
        UJ.rotulo(ctx, lz, 'ERROR: sp_agendar_cita(…) is a procedure', W / 2, 412, { tam: 19, peso: 700, color: R, ancho: W - 140 });
        UJ.rotulo(ctx, lz, 'HINT: To call a procedure, use CALL.', W / 2, 444, { tam: 17, color: R, ancho: W - 140 });
      });
      UJ.rotulo(ctx, lz, 'El motor no deja confundirlos.', W / 2, 520, { tam: 21, peso: 700, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
