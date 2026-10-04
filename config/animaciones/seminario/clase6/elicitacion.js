/* Tres técnicas de elicitación vierten, por un embudo, las frases crudas de la clínica:
 * son necesidades, todavía no requisitos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('elicitacion', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.34, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var tecnicas = [
        ['Entrevista', 'abiertas primero, cerradas al final'],
        ['Observación', 'media hora en recepción, con cronómetro'],
        ['Prototipo desechable', 'la gente sabe decir lo que NO quiere']
      ];
      for (var i = 0; i < 3; i++) {
        (function (i) {
          var x = 26 + i * 254, a = L.tramo(t, 0.02 + i * 0.09, 0.1 + i * 0.09);
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, x, 20, 240, 150, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2.5);
            L.rectRed(ctx, x, 20, 240, 46, 12); L.rellena(ctx, A);
            L.rectRed(ctx, x, 54, 240, 12, 0); L.rellena(ctx, A);
            UJ.rotulo(ctx, lz, tecnicas[i][0], x + 120, 31, { tam: 19, peso: 800, color: m.papel, ancho: 224 });
            UJ.rotulo(ctx, lz, tecnicas[i][1], x + 120, 84, { tam: 18, peso: 500, color: m.tinta, ancho: 210 });
          });
        })(i);
      }
      // Embudo
      var e = L.tramo(t, 0.34, 0.42);
      UJ.alfa(ctx, e, function () {
        ctx.beginPath(); ctx.moveTo(130, 186); ctx.lineTo(670, 186); ctx.lineTo(450, 250); ctx.lineTo(350, 250); ctx.closePath();
        L.rellena(ctx, L.tono(C, 0.8), C, 2.5);
        L.rectRed(ctx, 370, 250, 60, 22, 0); L.rellena(ctx, L.tono(C, 0.8), C, 2.5);
      });
      var frases = ['«que las fichas no se pierdan»', '«ver lo que le han hecho antes»',
        '«que la auxiliar agende sin llamarme»', '«que sea rápido»', '«cuántas consultas al mes»'];
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.46), function () {
        L.rectRed(ctx, 170, 282, 460, 214, 12); L.rellena(ctx, m.papel, L.tono(m.gris, 0.4), 2);
      });
      for (var k = 0; k < 5; k++) {
        var p = L.tramo(t, 0.44 + k * 0.07, 0.5 + k * 0.07, 'frena');
        if (p <= 0) continue;
        (function (k, p) {
          UJ.alfa(ctx, p, function () {
            UJ.rotulo(ctx, lz, frases[k], 400, 260 + (36 + k * 40) * p, { tam: 19, peso: 600, color: m.tinta });
          });
        })(k, p);
      }
      UJ.pildora(ctx, lz, W / 2, 530, 'necesidades, todavía no requisitos', m.malva, L.tramo(t, 0.86, 0.96), { tam: 20, centrar: true });
    }
  });
})();
