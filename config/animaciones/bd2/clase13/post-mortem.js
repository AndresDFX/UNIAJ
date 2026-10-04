/* El post-mortem: el documento breve que se escribe despues de un incidente en produccion y que
 * responde cuatro preguntas. El analisis de casos es una practica profesional, no relleno. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('post-mortem', {
    duracion: 4.6,
    pasos: [0.3, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.caja(ctx, lz, 40, 30, 280, 90, 'Falla en producción', '', R, L.tramo(t, 0, 0.1));
      UJ.rayo(ctx, 340, 36, 76, R, L.tramo(t, 0.06, 0.14));
      L.flecha(ctx, 420, 75, 476, 75, m.tinta, 4, L.tramo(t, 0.14, 0.2, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.28), function () {
        L.rectRed(ctx, 480, 20, 290, 110, 10); L.rellena(ctx, m.papel, A, 3);
        UJ.rotulo(ctx, lz, 'Post-mortem', 625, 34, { tam: 26, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'documento breve', 625, 78, { tam: 18 });
      });
      var preg = [['¿Qué pasó?', ''], ['¿Cuándo, y con qué impacto?', 'medible'], ['¿Por qué fue posible?', 'la causa raíz'], ['¿Qué se cambia?', 'para que no vuelva a pasar igual']];
      for (var i = 0; i < 4; i++) {
        var y = 160 + i * 92, a = L.tramo(t, 0.32 + i * 0.11, 0.4 + i * 0.11);
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, 74, y + 38, 26); L.rellena(ctx, i === 2 ? C : A);
          UJ.rotulo(ctx, lz, String(i + 1), 74, y + 24, { tam: 24, peso: 800, color: m.papel });
          L.rectRed(ctx, 116, y, 650, 76, 12); L.rellena(ctx, L.tono(i === 2 ? C : A, 0.9), i === 2 ? C : A, 2);
          UJ.rotulo(ctx, lz, preg[i][0], 136, y + 10, { tam: 22, peso: 800, alinear: 'left', color: i === 2 ? L.tono(C, -0.3) : A });
          if (preg[i][1]) UJ.rotulo(ctx, lz, preg[i][1], 136, y + 44, { tam: 17, alinear: 'left' });
        });
      }
      UJ.rotulo(ctx, lz, 'Analizar casos reales es un oficio con nombre propio.', W / 2, 545,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
