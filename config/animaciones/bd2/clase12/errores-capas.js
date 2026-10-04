/* Las tres reglas del manejo de errores entre capas: el procedimiento lanza el error (no devuelve
 * 0 o -1); la aplicacion lo traduce y registra el tecnico en el log; el procedimiento decide COMMIT. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('errores-capas', {
    duracion: 5,
    pasos: [0.33, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // Regla 1
      UJ.rotulo(ctx, lz, '1 · el procedimiento lanza el error', 30, 14, { tam: 21, peso: 800, color: A, alinear: 'left' });
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.12), function () {
        L.rectRed(ctx, 30, 52, 300, 56, 10); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'p_resultado := -1', 180, 66, { tam: 19, color: R });
      });
      UJ.sello(ctx, lz, 350, 80, 20, false, L.tramo(t, 0.1, 0.16));
      UJ.rotulo(ctx, lz, 'se puede ignorar', 180, 114, { tam: 16, peso: 700, color: R, visible: L.tramo(t, 0.12, 0.18) });
      UJ.codigo(ctx, lz, 390, 56, 380, "RAISE EXCEPTION '…' USING ERRCODE = 'MA001'", L.tramo(t, 0.18, 0.3), 15);
      UJ.rotulo(ctx, lz, 'código propio: SQLSTATE de 5 caracteres', 580, 104, { tam: 16, peso: 700, color: A, visible: L.tramo(t, 0.26, 0.32) });
      // Regla 2
      UJ.rotulo(ctx, lz, '2 · la aplicación traduce', 30, 170, { tam: 21, peso: 800, color: C, alinear: 'left', visible: L.tramo(t, 0.34, 0.4) });
      UJ.caja(ctx, lz, 30, 210, 200, 70, 'MA001', 'SQLSTATE', C, L.tramo(t, 0.38, 0.44));
      L.flecha(ctx, 234, 230, 380, 230, C, 4, L.tramo(t, 0.44, 0.5, 'frena'));
      UJ.caja(ctx, lz, 384, 196, 386, 64, 'Pantalla', '«La mascota está inactiva»', V, L.tramo(t, 0.48, 0.54));
      L.flecha(ctx, 234, 262, 380, 300, L.tono(m.tinta, 0.3), 3, L.tramo(t, 0.52, 0.58, 'frena'));
      UJ.caja(ctx, lz, 384, 276, 386, 64, 'Log del servidor', 'error técnico + id de correlación', L.tono(m.tinta, 0.2), L.tramo(t, 0.56, 0.62));
      // Regla 3
      UJ.rotulo(ctx, lz, '3 · quien decide COMMIT', 30, 370, { tam: 21, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0.68, 0.72) });
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        L.rectRed(ctx, 30, 410, 740, 110, 12); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'un procedimiento = la operación de negocio completa', 400, 422, { tam: 19, peso: 700, ancho: 700 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.86), function () {
        L.rectRed(ctx, 80, 462, 280, 44, 22); L.rellena(ctx, L.tono(V, 0.75));
        UJ.rotulo(ctx, lz, 'todo bien → se confirma', 220, 472, { tam: 18, peso: 800 });
        L.rectRed(ctx, 440, 462, 280, 44, 22); L.rellena(ctx, L.tono(R, 0.75));
        UJ.rotulo(ctx, lz, 'falla → el error deshace el CALL', 580, 472, { tam: 18, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'La aplicación no confirma a la mitad.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
