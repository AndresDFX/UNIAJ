/* El post-mortem: el documento breve que se escribe despues de un incidente en produccion y que
 * responde cuatro preguntas, sin buscar culpables (blameless). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('post-mortem', {
    duracion: 4.6,
    // Pasos LOGICOS: 1) la falla y el documento que se escribe despues, 2) las cuatro preguntas
    // que responde, 3) la regla del oficio: sin culpables. Ningun paso deja una idea a medias.
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // 1. La falla y el documento
      UJ.caja(ctx, lz, 40, 30, 280, 90, 'Falla en producción', '', R, L.tramo(t, 0, 0.1));
      UJ.rayo(ctx, 340, 36, 76, R, L.tramo(t, 0.06, 0.14));
      L.flecha(ctx, 420, 75, 476, 75, m.tinta, 4, L.tramo(t, 0.14, 0.2, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.28), function () {
        L.rectRed(ctx, 480, 20, 290, 110, 10); L.rellena(ctx, m.papel, A, 3);
        UJ.rotulo(ctx, lz, 'Post-mortem', 625, 34, { tam: 26, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'documento breve, después', 625, 78, { tam: 18 });
      });
      // 2. Las cuatro preguntas
      var preg = [['¿Qué pasó?', 'la secuencia de hechos, en orden'], ['¿Cuándo, y con qué impacto?', 'medible: datos, horas, dinero'],
                  ['¿Por qué fue posible?', 'la causa raíz'], ['¿Qué se cambia?', 'para que no vuelva a pasar igual']];
      for (var i = 0; i < 4; i++) {
        var y = 150 + i * 82, a = L.tramo(t, 0.32 + i * 0.09, 0.38 + i * 0.09);
        UJ.alfa(ctx, a, function () {
          var col = i === 2 ? C : A;
          L.circulo(ctx, 74, y + 34, 26); L.rellena(ctx, col);
          UJ.rotulo(ctx, lz, String(i + 1), 74, y + 20, { tam: 24, peso: 800, color: m.papel });
          L.rectRed(ctx, 116, y, 654, 70, 12); L.rellena(ctx, L.tono(col, 0.9), col, 2);
          UJ.rotulo(ctx, lz, preg[i][0], 136, y + 8, { tam: 22, peso: 800, alinear: 'left', color: i === 2 ? L.tono(C, -0.3) : A });
          UJ.rotulo(ctx, lz, preg[i][1], 136, y + 40, { tam: 17, alinear: 'left' });
        });
      }
      // 3. Sin culpables
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.86), function () {
        L.rectRed(ctx, 40, 492, 730, 118, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'Sin culpables (blameless): se analiza el sistema, no la persona', 405, 506,
                  { tam: 21, peso: 800, color: L.tono(V, -0.3), ancho: 690 });
        UJ.rotulo(ctx, lz, 'Si el informe castiga, nadie vuelve a reportar los errores pequeños', 405, 566,
                  { tam: 18, peso: 600, ancho: 690 });
      });
    }
  });
})();
