/* La pantalla «ver mi turno» se arma en cinco pasos: para que existe, el numero grande, textos
 * reales, el estado vacio o de error, y que pasa al tocar Cancelar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pantalla-turno', {
    duracion: 5,
    // Pasos LOGICOS: uno por paso del ejemplo; cada nota llega con lo que se dibuja en el telefono.
    pasos: [0.16, 0.36, 0.56, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030';
      function telefono(x, y, a, fn) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, 250, 470, 30); L.rellena(ctx, L.tono(m.tinta, -0.2));
          L.rectRed(ctx, x + 12, y + 30, 226, 410, 12); L.rellena(ctx, m.papel);
          fn(x + 12, y + 30);
        });
      }
      function nota(txt, y, a) {
        UJ.rotulo(ctx, lz, txt, 300, y, { tam: 20, peso: 700, alinear: 'left', ancho: 200, visible: a });
      }
      // 1 · Para que existe (el telefono y su titulo)
      telefono(30, 60, L.tramo(t, 0, 0.08), function (x, y) {
        UJ.rotulo(ctx, lz, 'Mi turno', x + 113, y + 18, { tam: 24, peso: 800, color: A });
        // 2 · El numero grande al centro
        UJ.rotulo(ctx, lz, 'Van 4 antes que usted', x + 113, y + 90, { tam: 30, peso: 800, color: m.tinta, ancho: 200, visible: L.tramo(t, 0.2, 0.3) });
        // 3 · Textos reales
        UJ.rotulo(ctx, lz, 'Su turno: 27', x + 113, y + 210, { tam: 24, peso: 600, visible: L.tramo(t, 0.4, 0.5) });
        // 5 · El boton que se toca
        UJ.alfa(ctx, L.tramo(t, 0.8, 0.86), function () {
          L.rectRed(ctx, x + 23, y + 330, 180, 50, 25); L.rellena(ctx, L.tono(R, 0.85), R, 2);
          UJ.rotulo(ctx, lz, 'Cancelar turno', x + 113, y + 343, { tam: 19, peso: 700, color: R });
        });
      });
      nota('1 · Para qué existe: saber cuántos van antes', 70, L.tramo(t, 0.03, 0.12));
      nota('2 · Un número grande al centro', 160, L.tramo(t, 0.22, 0.32));
      nota('3 · Textos reales, no «texto aquí»', 250, L.tramo(t, 0.42, 0.52));
      // 4 · Vacio y error
      UJ.alfa(ctx, L.tramo(t, 0.6, 0.7), function () {
        L.rectRed(ctx, 520, 60, 250, 120, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'Aún no tiene turno → Pedir turno', 645, 82, { tam: 18, peso: 700, ancho: 220 });
        L.rectRed(ctx, 520, 200, 250, 120, 14); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'Sin conexión: intente de nuevo', 645, 222, { tam: 18, peso: 700, ancho: 220 });
      });
      nota('4 · Estados vacío y error', 340, L.tramo(t, 0.62, 0.72));
      // 5 · Que pasa al tocar
      L.flecha(ctx, 245, 445, 515, 470, R, 3, L.tramo(t, 0.86, 0.92));
      UJ.alfa(ctx, L.tramo(t, 0.88, 0.96), function () {
        L.rectRed(ctx, 520, 430, 250, 120, 14); L.rellena(ctx, m.papel, R, 3);
        UJ.rotulo(ctx, lz, '¿Seguro que cancela su turno?', 645, 452, { tam: 18, peso: 700, ancho: 220 });
      });
      nota('5 · Qué pasa al tocar', 560, L.tramo(t, 0.84, 0.94));
    }
  });
})();
