/* Caso cuatro, concurrencia: la actualizacion perdida. Dos procesos leen stock 5, cada uno resta 3
 * y ambos escriben 2: salieron 6 unidades y el sistema dice 2. Ningun mensaje de error. La defensa
 * vive en la base. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('actualizacion-perdida', {
    duracion: 5,
    // Pasos LOGICOS: 1) los dos leen el mismo 5, 2) los dos restan y escriben 2, 3) el
    // resultado sin error, 4) donde se defiende.
    pasos: [0.3, 0.62, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // El stock en el centro
      var valor = t < 0.5 ? '5' : '2';
      L.rectRed(ctx, 300, 30, 200, 110, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
      UJ.rotulo(ctx, lz, 'insumo.stock', 400, 42, { tam: 19, peso: 700, color: A });
      UJ.rotulo(ctx, lz, valor, 400, 72, { tam: 46, peso: 800, color: t < 0.5 ? m.tinta : R });
      function proceso(x, nombre, col, k) {
        UJ.caja(ctx, lz, x, 190, 240, 64, nombre, '', col, 1);
        UJ.alfa(ctx, L.tramo(t, 0.06 + k * 0.06, 0.16 + k * 0.06), function () { UJ.rotulo(ctx, lz, 'lee 5', x + 120, 270, { tam: 21, peso: 700, color: col }); });
        UJ.alfa(ctx, L.tramo(t, 0.34 + k * 0.04, 0.42 + k * 0.04), function () { UJ.rotulo(ctx, lz, '5 − 3 = 2', x + 120, 306, { tam: 21, peso: 700, color: col }); });
        UJ.alfa(ctx, L.tramo(t, 0.46 + k * 0.06, 0.54 + k * 0.06), function () { UJ.rotulo(ctx, lz, 'escribe 2', x + 120, 342, { tam: 21, peso: 800, color: col }); });
        L.flecha(ctx, x + 120, 186, k ? 470 : 330, 144, col, 3, L.tramo(t, 0.46 + k * 0.06, 0.54 + k * 0.06));
      }
      proceso(30, 'Proceso 1', A, 0);
      proceso(530, 'Proceso 2', C, 1);
      // 3. El resultado, sin error
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.76), function () {
        L.rectRed(ctx, 60, 392, 300, 70, 12); L.rellena(ctx, L.tono(m.tinta, 0.9), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'salieron 6 unidades', 210, 414, { tam: 21, peso: 800 });
        L.rectRed(ctx, 440, 392, 300, 70, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'el sistema dice 2', 590, 414, { tam: 21, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'Sin mensaje de error: se descubre semanas después.', W / 2, 476, { tam: 19, peso: 700, ancho: W - 40 });
      });
      // 4. Donde se defiende
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 40, 522, 720, 96, 12); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'La defensa vive en la base, no en la aplicación:', 400, 534, { tam: 20, peso: 800, color: L.tono(V, -0.3), ancho: 690 });
        UJ.rotulo(ctx, lz, 'UPDATE condicional o FOR UPDATE · UNIQUE para la doble reserva', 400, 574, { tam: 18, peso: 600, ancho: 690 });
      });
    }
  });
})();
