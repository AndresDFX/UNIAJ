/* Causa proxima y causa raiz: el ultimo evento de la cadena (el disco falla) frente a la condicion
 * que le dio consecuencias (un respaldo que nadie habia restaurado ni vigilado), y cuando parar
 * de preguntar por que. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('causa-raiz', {
    duracion: 5,
    // Pasos LOGICOS: 1) lo que se ve: la causa proxima, 2) preguntar por que hasta la causa
    // raiz, 3) la regla para saber que ya se llego.
    pasos: [0.34, 0.74, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // 1. Lo que se ve
      UJ.caja(ctx, lz, 30, 30, 300, 100, 'El disco falla', 'un viernes', R, L.tramo(t, 0, 0.1));
      L.flecha(ctx, 334, 80, 450, 80, R, 4, L.tramo(t, 0.1, 0.18, 'frena'));
      UJ.caja(ctx, lz, 454, 30, 316, 100, 'Se pierden 3 semanas', 'de historias clínicas', R, L.tramo(t, 0.16, 0.26));
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.32), function () {
        L.rectRed(ctx, 60, 144, 240, 36, 18); L.rellena(ctx, L.tono(R, 0.75));
        UJ.rotulo(ctx, lz, 'causa próxima', 180, 151, { tam: 18, peso: 800 });
      });
      // 2. ¿Por que? hasta la raiz
      for (var k = 0; k < 3; k++)
        UJ.rotulo(ctx, lz, '¿por qué?', 198, 200 + k * 32, { tam: 19, peso: 700, alinear: 'left', color: L.tono(m.tinta, 0.2 + k * 0.1), visible: L.tramo(t, 0.36 + k * 0.06, 0.42 + k * 0.06) });
      L.flecha(ctx, 180, 188, 180, 302, C, 4, L.tramo(t, 0.36, 0.56));
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.66), function () {
        L.rectRed(ctx, 30, 310, 740, 116, 14); L.rellena(ctx, L.tono(C, 0.88), C, 3);
        UJ.rotulo(ctx, lz, 'Un respaldo que nadie había restaurado nunca', 400, 324, { tam: 22, peso: 800, color: L.tono(C, -0.35), ancho: 700 });
        UJ.rotulo(ctx, lz, 'y nadie vigilaba si el del día se ejecutó', 400, 366, { tam: 20, peso: 600, ancho: 700 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.72), function () {
        L.rectRed(ctx, 60, 436, 200, 36, 18); L.rellena(ctx, L.tono(C, 0.55));
        UJ.rotulo(ctx, lz, 'causa raíz', 160, 443, { tam: 18, peso: 800 });
      });
      // 3. Cuando parar
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.9), function () {
        L.rectRed(ctx, 30, 494, 360, 120, 12); L.rellena(ctx, L.tono(R, 0.92), R, 2);
        UJ.rotulo(ctx, lz, 'Nombra a una persona:', 210, 506, { tam: 19, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'todavía no es la raíz, sigue preguntando', 210, 540, { tam: 17, ancho: 330 });
        L.rectRed(ctx, 410, 494, 360, 120, 12); L.rellena(ctx, L.tono(V, 0.88), V, 2);
        UJ.rotulo(ctx, lz, 'Nombra algo que se cambia:', 590, 506, { tam: 19, peso: 800, color: L.tono(V, -0.3) });
        UJ.rotulo(ctx, lz, 'un permiso, una restricción, una alarma: llegaste', 590, 540, { tam: 17, ancho: 330 });
      });
    }
  });
})();
