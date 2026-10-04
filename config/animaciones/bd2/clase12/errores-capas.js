/* Las tres reglas del manejo de errores entre capas. 1) Un fallo nunca se esconde en un -1
 * suelto: el rechazo de negocio esperado va en la fila del contrato (ok, mensaje) y el error que
 * debe abortar se lanza con RAISE y un codigo propio. 2) La aplicacion traduce y registra el
 * tecnico en el log. 3) La operacion completa vive en un procedimiento y nadie confirma a medias. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('errores-capas', {
    duracion: 5,
    // Pasos LOGICOS: una regla por paso.
    pasos: [0.33, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // Regla 1
      UJ.rotulo(ctx, lz, '1 · un fallo nunca se esconde en un -1', 30, 8, { tam: 21, peso: 800, color: A, alinear: 'left' });
      UJ.alfa(ctx, L.tramo(t, 0.03, 0.09), function () {
        L.rectRed(ctx, 30, 48, 220, 50, 10); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'p_resultado := -1', 140, 61, { tam: 18, color: R });
      });
      UJ.sello(ctx, lz, 268, 73, 16, false, L.tramo(t, 0.09, 0.13));
      UJ.rotulo(ctx, lz, 'nadie está obligado a revisarlo', 140, 106, { tam: 14, peso: 700, color: R, ancho: 230, visible: L.tramo(t, 0.11, 0.15) });
      UJ.codigo(ctx, lz, 300, 44, 480, "RETURN QUERY SELECT FALSE, 'Franja ocupada', NULL;", L.tramo(t, 0.15, 0.22), 14);
      UJ.rotulo(ctx, lz, 'rechazo de negocio esperado: va en la fila del contrato', 540, 76, { tam: 14, peso: 700, color: L.tono(V, -0.2), ancho: 480, visible: L.tramo(t, 0.21, 0.25) });
      UJ.codigo(ctx, lz, 300, 102, 480, "RAISE EXCEPTION '…' USING ERRCODE = 'MA001';", L.tramo(t, 0.24, 0.29), 14);
      UJ.rotulo(ctx, lz, 'error que debe abortar: se lanza, con código propio', 540, 134, { tam: 14, peso: 700, color: A, ancho: 480, visible: L.tramo(t, 0.28, 0.32) });
      // Regla 2
      UJ.rotulo(ctx, lz, '2 · la aplicación traduce', 30, 184, { tam: 21, peso: 800, color: C, alinear: 'left', visible: L.tramo(t, 0.34, 0.4) });
      UJ.caja(ctx, lz, 30, 224, 200, 70, 'MA001', 'SQLSTATE', C, L.tramo(t, 0.38, 0.44));
      L.flecha(ctx, 234, 244, 380, 244, C, 4, L.tramo(t, 0.44, 0.5, 'frena'));
      UJ.caja(ctx, lz, 384, 210, 386, 64, 'Pantalla', '«La mascota está inactiva»', V, L.tramo(t, 0.48, 0.54));
      L.flecha(ctx, 234, 276, 380, 314, L.tono(m.tinta, 0.3), 3, L.tramo(t, 0.52, 0.58, 'frena'));
      UJ.caja(ctx, lz, 384, 290, 386, 64, 'Log del servidor', 'error técnico + id de correlación', L.tono(m.tinta, 0.2), L.tramo(t, 0.56, 0.62));
      // Regla 3
      UJ.rotulo(ctx, lz, '3 · quien decide COMMIT', 30, 384, { tam: 21, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0.68, 0.72) });
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        L.rectRed(ctx, 30, 424, 740, 110, 12); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'un procedimiento = la operación de negocio completa', 400, 436, { tam: 19, peso: 700, ancho: 700 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.86), function () {
        L.rectRed(ctx, 80, 476, 280, 44, 22); L.rellena(ctx, L.tono(V, 0.75));
        UJ.rotulo(ctx, lz, 'todo bien → se confirma', 220, 486, { tam: 18, peso: 800 });
        L.rectRed(ctx, 440, 476, 280, 44, 22); L.rellena(ctx, L.tono(R, 0.75));
        UJ.rotulo(ctx, lz, 'falla → el error deshace el CALL', 580, 486, { tam: 18, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'La aplicación no confirma a la mitad.', W / 2, 572,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
