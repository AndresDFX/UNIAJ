/* La trampa del WHEN OTHERS: un procedimiento roto tambien lanza excepcion. paso = TRUE "porque
 * fallo" lo da por bueno; SQLERRM ILIKE '%inactiva%' exige que falle POR lo esperado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('trampa-when-others', {
    duracion: 5,
    pasos: [0.3, 0.62, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Caso negativo: mascota inactiva', W / 2, 14, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      UJ.caja(ctx, lz, 200, 60, 400, 70, 'procedimiento ROTO', 'una columna mal escrita', R, L.tramo(t, 0.05, 0.12));
      L.flecha(ctx, 400, 134, 400, 176, R, 3, L.tramo(t, 0.12, 0.18));
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.24), function () {
        L.rectRed(ctx, 110, 180, 580, 48, 10); L.rellena(ctx, L.tono(R, 0.88), R, 2);
        UJ.rotulo(ctx, lz, 'ERROR: column "activ" does not exist', 400, 192, { tam: 19, peso: 700, color: R, ancho: 560 });
      });
      UJ.rotulo(ctx, lz, 'También es una excepción.', W / 2, 244, { tam: 19, visible: L.tramo(t, 0.24, 0.3) });
      // WHEN OTHERS
      UJ.alfa(ctx, L.tramo(t, 0.32, 0.4), function () {
        UJ.codigo(ctx, lz, 20, 300, 370, 'WHEN OTHERS THEN paso := TRUE;', 1, 15);
      });
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () {
        L.rectRed(ctx, 60, 360, 290, 70, 12); L.rellena(ctx, L.tono(C, 0.85), C, 2);
        UJ.rotulo(ctx, lz, 'paso = t', 205, 382, { tam: 24, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'falso positivo', 205, 444, { tam: 21, peso: 800, color: R, visible: L.tramo(t, 0.52, 0.6) });
      // ILIKE
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.72), function () {
        UJ.codigo(ctx, lz, 410, 300, 370, "paso := SQLERRM ILIKE '%inactiva%';", 1, 15);
      });
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.8), function () {
        L.rectRed(ctx, 450, 360, 290, 70, 12); L.rellena(ctx, L.tono(A, 0.88), A, 2);
        UJ.rotulo(ctx, lz, 'paso = f', 595, 382, { tam: 24, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'el error queda a la vista', 595, 444, { tam: 21, peso: 800, color: A, visible: L.tramo(t, 0.78, 0.86) });
      UJ.rotulo(ctx, lz, 'Se afirma que falló Y que falló por lo esperado.', W / 2, 510, { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 0.93) });
      UJ.rotulo(ctx, lz, 'Una sola lectura de «paso» para las cuatro filas, y se declara.', W / 2, 556, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.93, 1) });
    }
  });
})();
