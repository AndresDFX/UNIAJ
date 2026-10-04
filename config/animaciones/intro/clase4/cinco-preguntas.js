/* Cinco preguntas como cinco filtros por los que pasa una idea. La 3 es la que mas rapido
 * descarta; la 5 busca el momento mas barato para parar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cinco-preguntas', {
    duracion: 5,
    pasos: [0.34, 0.6, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, S = m.sello || m.acento, W = lz.ancho;
      var q = ['¿Quién se puede dañar?', '¿Lo sabe y lo aceptó?', '¿Aguanta que se sepa?', '¿Qué dice el código de ética?', '¿Cuándo se puede parar?'];
      var t0 = [0.02, 0.16, 0.36, 0.62, 0.72];
      for (var i = 0; i < 5; i++) {
        var a = L.tramo(t, t0[i], t0[i] + 0.1), y = 24 + i * 100, dest = i === 2;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 150, y, 620, 80, 14);
          L.rellena(ctx, dest ? L.tono(S, 0.55) : L.tono(A, 0.9), dest ? L.tono(S, -0.35) : A, 3);
          L.circulo(ctx, 100, y + 40, 34); L.rellena(ctx, dest ? L.tono(S, -0.3) : A);
          UJ.rotulo(ctx, lz, String(i + 1), 100, y + 22, { tam: 30, peso: 800, color: m.papel });
          UJ.rotulo(ctx, lz, q[i], 176, y + 22, { tam: 27, peso: 700, alinear: 'left', ancho: 580 });
        });
      }
      UJ.rotulo(ctx, lz, 'la más rápida para descartar', 600, 280, { tam: 17, peso: 700, color: L.tono(S, -0.45), visible: L.tramo(t, 0.46, 0.56) });
      UJ.rotulo(ctx, lz, 'Parar temprano es barato; después de entregar cuesta mucho más.', W / 2, 540, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
