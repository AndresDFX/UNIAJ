/* Causa proxima y causa raiz: el ultimo evento de la cadena (el disco falla) frente a la condicion
 * que le dio consecuencias (un respaldo que nadie habia restaurado ni vigilado). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('causa-raiz', {
    duracion: 5,
    pasos: [0.34, 0.74, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      // Lo que se ve
      UJ.caja(ctx, lz, 30, 40, 300, 100, 'El disco falla', 'un viernes', R, L.tramo(t, 0, 0.1));
      L.flecha(ctx, 334, 90, 450, 90, R, 4, L.tramo(t, 0.1, 0.18, 'frena'));
      UJ.caja(ctx, lz, 454, 40, 316, 100, 'Se pierden 3 semanas', 'de historias clínicas', R, L.tramo(t, 0.16, 0.26));
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.32), function () {
        L.rectRed(ctx, 60, 156, 240, 36, 18); L.rellena(ctx, L.tono(R, 0.75));
        UJ.rotulo(ctx, lz, 'causa próxima', 180, 163, { tam: 18, peso: 800 });
      });
      // ¿Por que?
      for (var k = 0; k < 3; k++)
        UJ.rotulo(ctx, lz, '¿por qué?', 180, 214 + k * 34, { tam: 19, peso: 700, color: L.tono(m.tinta, 0.2 + k * 0.1), visible: L.tramo(t, 0.36 + k * 0.06, 0.42 + k * 0.06) });
      L.flecha(ctx, 180, 200, 180, 330, C, 4, L.tramo(t, 0.36, 0.56));
      // Lo que lo permitio
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.66), function () {
        L.rectRed(ctx, 30, 340, 740, 130, 14); L.rellena(ctx, L.tono(C, 0.88), C, 3);
        UJ.rotulo(ctx, lz, 'Un respaldo que nadie había restaurado nunca', 400, 356, { tam: 22, peso: 800, color: L.tono(C, -0.35), ancho: 700 });
        UJ.rotulo(ctx, lz, 'y nadie vigilaba si el del día se ejecutó', 400, 400, { tam: 20, peso: 600, ancho: 700 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.74), function () {
        L.rectRed(ctx, 60, 482, 200, 36, 18); L.rellena(ctx, L.tono(C, 0.55));
        UJ.rotulo(ctx, lz, 'causa raíz', 160, 489, { tam: 18, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'Los discos fallan siempre; lo que se cambia es la raíz.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.8, 1) });
    }
  });
})();
