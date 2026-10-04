/* Ilustracion: el cliente. Hoy todo vive en papel y duele en tres puntos; tres personas van a
 * usar la base y esperan cosas distintas, y sus intereses chocan (mas datos = mas clics). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-cliente', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      function persona(x, y, col) {
        L.circulo(ctx, x, y, 22); L.rellena(ctx, col);
        L.rectRed(ctx, x - 30, y + 28, 60, 44, 18); L.rellena(ctx, col);
      }
      // Hoy: papel
      UJ.rotulo(ctx, lz, 'Hoy: carpetas de papel', W / 2, 12, { tam: 24, peso: 800, color: R });
      var dolor = ['fichas que se extravían', 'filas en la sala de espera', 'cero métricas del mes'];
      for (var i = 0; i < 3; i++) {
        var x = 30 + i * 252;
        L.rectRed(ctx, x, 56, 236, 64, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, dolor[i], x + 118, 76, { tam: 18, peso: 700, color: R, ancho: 220 });
      }
      L.flecha(ctx, W / 2, 128, W / 2, 166, L.tono(m.tinta, 0.4), 4, 1);
      // Tres personas
      UJ.rotulo(ctx, lz, 'Tres personas van a usar la base', W / 2, 172, { tam: 24, peso: 800, color: A });
      var gente = [['El dueño', 'métricas del negocio', A], ['La recepcionista', 'agendar rápido', C], ['El veterinario', 'el historial a la mano', L.tono(A, 0.25)]];
      for (var k = 0; k < 3; k++) {
        var cx = 140 + k * 260;
        persona(cx, 252, gente[k][2]);
        UJ.rotulo(ctx, lz, gente[k][0], cx, 340, { tam: 21, peso: 800, color: gente[k][2] });
        UJ.rotulo(ctx, lz, 'quiere ' + gente[k][1], cx, 372, { tam: 18, ancho: 230 });
      }
      // El conflicto
      L.flecha(ctx, 270, 428, 160, 428, R, 4, 1);
      L.flecha(ctx, 270, 428, 380, 428, R, 4, 1);
      L.rectRed(ctx, 40, 470, W - 80, 128, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Sus intereses chocan', W / 2, 486, { tam: 24, peso: 800 });
      UJ.rotulo(ctx, lz, 'un campo más en la cita le da métricas al dueño y le suma clics a la recepcionista', W / 2, 526, { tam: 18, ancho: W - 140 });
    }
  });
})();
