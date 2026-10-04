/* Como se lee un hito: una fecha suelta, y las cuatro preguntas que la vuelven herramienta.
 * La cuarta (que sigue vivo hoy) es la que se resalta. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('hito-cuatro-preguntas', {
    duracion: 5,
    // Pasos LOGICOS: 1) el hito contado como una fecha suelta, 2-4) una pregunta por clic,
    // 5) la cuarta pregunta, la que vuelve la fecha herramienta. Ningun paso adelanta el siguiente.
    pasos: [0.16, 0.36, 0.56, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, S = m.sello || m.acento;
      // La fecha suelta
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.circulo(ctx, 110, 90, 54); L.rellena(ctx, L.tono(A, 0.85), A, 3);
        UJ.rotulo(ctx, lz, 'un hito', 110, 74, { tam: 22, peso: 800, color: A });
        UJ.rotulo(ctx, lz, '= una fecha suelta', 185, 76, { tam: 24, peso: 600, alinear: 'left' });
      });
      var preg = [
        ['1 · ¿Qué dolía antes?', 'el problema y a quién le pasaba'],
        ['2 · ¿Qué propuso?', 'la idea, en una frase'],
        ['3 · ¿Qué resolvió de verdad?', 'qué parte sí, no todo'],
        ['4 · ¿Qué sigue vivo hoy?', 'lo que nadie ha cerrado']
      ];
      var desde = [0.18, 0.38, 0.58, 0.78];
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, desde[i], desde[i] + 0.1), y = 170 + i * 98;
        var c = i === 3 ? L.tono(S, -0.35) : A;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 60 + i * 30, y, 640 - i * 30, 82, 14);
          L.rellena(ctx, i === 3 ? L.tono(S, 0.55) : L.tono(A, 0.9), c, 3);
          UJ.rotulo(ctx, lz, preg[i][0], 84 + i * 30, y + 12, { tam: 25, peso: 800, color: i === 3 ? m.tinta : A, alinear: 'left', ancho: 600 - i * 30 });
          UJ.rotulo(ctx, lz, preg[i][1], 84 + i * 30, y + 48, { tam: 20, alinear: 'left', ancho: 600 - i * 30 });
        });
      }
      UJ.rotulo(ctx, lz, 'Con la cuarta pregunta, la fecha se vuelve herramienta.', W / 2, 580, { tam: 23, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 0.98) });
    }
  });
})();
