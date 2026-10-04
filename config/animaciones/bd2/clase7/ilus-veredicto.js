/* Ilustracion: el veredicto de particionamiento con numeros. Volumen esperado de la clinica
 * (40 citas x 300 dias = 12.000 al ano; 60.000 en cinco anos) contra el umbral de oficio
 * (decenas de millones de filas). Escala logaritmica: cada marca es x10. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-veredicto', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, '¿Se particiona? Primero el número', W / 2, 8, { tam: 24, peso: 800, color: A });
      // la cuenta
      L.rectRed(ctx, 20, 52, W - 40, 112, 14); L.rellena(ctx, L.tono(A, 0.94), A, 2);
      UJ.rotulo(ctx, lz, '40 citas al día × 300 días = 12.000 al año', W / 2, 66, { tam: 21, peso: 700 });
      UJ.rotulo(ctx, lz, '× 5 años de historia = 60.000 citas', W / 2, 108, { tam: 21, peso: 800, color: A });
      // escala logaritmica
      var x0 = 70, x1 = 730, y = 300;
      function px(v) { return x0 + (Math.log(v) / Math.LN10 - 3) / 5 * (x1 - x0); }
      L.trazo(ctx, [[x0, y], [x1, y]], 1, m.tinta, 3);
      var marcas = [[1e3, '1 mil'], [1e4, '10 mil'], [1e5, '100 mil'], [1e6, '1 millón'], [1e7, '10 millones'], [1e8, '100 millones']];
      for (var i = 0; i < marcas.length; i++) {
        var x = px(marcas[i][0]);
        L.trazo(ctx, [[x, y - 8], [x, y + 8]], 1, m.tinta, 2);
        UJ.rotulo(ctx, lz, marcas[i][1], x, y + 14, { tam: 13, color: L.tono(m.tinta, 0.2) });
      }
      UJ.rotulo(ctx, lz, 'filas (cada marca es × 10)', W / 2, y + 40, { tam: 14, peso: 700, color: L.tono(m.tinta, 0.3) });
      // zona del umbral
      var u0 = px(1e7), u1 = px(1e8);
      L.rectRed(ctx, u0, y - 92, u1 - u0, 78, 10); L.rellena(ctx, L.tono(R, 0.88), R, 2);
      UJ.rotulo(ctx, lz, 'empieza a pagar:', (u0 + u1) / 2, y - 84, { tam: 14, peso: 700, color: R });
      UJ.rotulo(ctx, lz, 'decenas de millones', (u0 + u1) / 2, y - 60, { tam: 14, peso: 800, color: R, ancho: u1 - u0 - 6 });
      // puntos
      function punto(v, txt, col, arriba) {
        var x = px(v);
        L.circulo(ctx, x, y, 10); L.rellena(ctx, col);
        UJ.rotulo(ctx, lz, txt, x, arriba ? y - 64 : y + 62, { tam: 15, peso: 800, color: col, ancho: 170 });
      }
      punto(30010, 'base de hoy: 30.010', C, true);
      punto(60000, 'la clínica a 5 años: 60.000', A, false);
      // veredicto
      L.rectRed(ctx, 20, 432, W - 40, 186, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
      UJ.rotulo(ctx, lz, 'Veredicto: NO se particiona', W / 2, 446, { tam: 24, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'cientos de veces por debajo del umbral', W / 2, 490, { tam: 18, peso: 700 });
      UJ.rotulo(ctx, lz, 'con el volumen de la clase la ganancia de rendimiento no se aprecia, y se dice', W / 2, 528, { tam: 16, ancho: W - 80 });
      UJ.rotulo(ctx, lz, 'lo que sí quedó probado: la poda en el plan y el archivado con DROP', W / 2, 566, { tam: 16, peso: 700, ancho: W - 80 });
    }
  });
})();
