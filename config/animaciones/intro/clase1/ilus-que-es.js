/* Ilustracion: que es la ingenieria. Un problema y una restriccion llegan a una DECISION, y la
 * decision tiene una consecuencia de la que se responde. La de Sistemas aplica eso a software,
 * datos, redes y personas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-que-es', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', S = m.sello || C, W = lz.ancho;
      var gris = L.tono(m.tinta, 0.4);
      UJ.rotulo(ctx, lz, 'Ingeniería = decidir con recursos limitados', W / 2, 14, { tam: 27, peso: 800, color: A, ancho: W - 40 });
      UJ.caja(ctx, lz, 20, 90, 250, 120, 'PROBLEMA', 'algo le duele a alguien concreto', C);
      UJ.caja(ctx, lz, 530, 90, 250, 120, 'RESTRICCIÓN', 'tiempo · dinero · energía · personas · ley', R);
      UJ.rotulo(ctx, lz, 'sin ella hay un deseo, no ingeniería', 655, 220, { tam: 17, peso: 700, color: R, ancho: 240 });
      L.flecha(ctx, 272, 196, 330, 246, gris, 4, 1);
      L.flecha(ctx, 528, 196, 470, 246, gris, 4, 1);
      // La decision, al centro
      L.circulo(ctx, 400, 300, 88); L.rellena(ctx, A, L.tono(A, -0.3), 3);
      UJ.rotulo(ctx, lz, 'DECIDIR', 400, 282, { tam: 32, peso: 800, color: m.papel });
      L.flecha(ctx, 400, 390, 400, 428, gris, 4, 1);
      UJ.caja(ctx, lz, 250, 432, 300, 100, 'CONSECUENCIA', 'a quién afecta · se responde por ella', L.tono(S, -0.45));
      // La de Sistemas
      L.rectRed(ctx, 20, 556, W - 40, 66, 33); L.rellena(ctx, L.tono(A, 0.9), A, 2);
      UJ.rotulo(ctx, lz, 'De Sistemas: aplicada a software · datos · redes · personas', W / 2, 576, { tam: 21, peso: 800, color: A, ancho: W - 80 });
    }
  });
})();
