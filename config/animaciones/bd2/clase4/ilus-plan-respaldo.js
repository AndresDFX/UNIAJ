/* Ilustracion: las 6 secciones de un plan de respaldo, como tarjetas numeradas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-plan-respaldo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Plan de respaldo en 6 secciones', W / 2, 12, { tam: 26, peso: 800, color: A });
      var s = [
        ['Qué y con qué', 'pg_dump -Fc · pg_dumpall --globals-only'],
        ['Frecuencia', '20:30, después del cierre de las 20:00'],
        ['Retención', '7 diarias · 4 semanales · 12 mensuales · una fuera'],
        ['RPO y RTO', 'en números: cuánto se pierde, cuánto dura'],
        ['Restore de prueba', 'pg_restore en una base vacía, medido'],
        ['Qué NO cubre', 'el riesgo residual, dicho']
      ];
      for (var i = 0; i < 6; i++) {
        var col = i % 2, fila = Math.floor(i / 2);
        var x = 24 + col * 384, y = 64 + fila * 180;
        L.rectRed(ctx, x, y, 368, 160, 16); L.rellena(ctx, L.tono(i === 4 ? (m.verde || A) : A, 0.9), i === 4 ? (m.verde || A) : A, 2);
        L.circulo(ctx, x + 40, y + 40, 24); L.rellena(ctx, i === 4 ? (m.verde || A) : A);
        UJ.rotulo(ctx, lz, String(i + 1), x + 40, y + 26, { tam: 24, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, s[i][0], x + 78, y + 26, { tam: 21, peso: 800, alinear: 'left', color: L.tono(A, -0.2) });
        UJ.rotulo(ctx, lz, s[i][1], x + 24, y + 84, { tam: 16, alinear: 'left', ancho: 320 });
      }
      UJ.rotulo(ctx, lz, 'Un respaldo que nunca se restauró es solo un archivo.', W / 2, 604,
                { tam: 18, peso: 700, color: m.verde || A, ancho: W - 40 });
    }
  });
})();
