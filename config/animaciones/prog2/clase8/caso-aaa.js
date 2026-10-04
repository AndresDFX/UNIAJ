/* Un caso de prueba AAA: Arrange (Kira activa, Rocky inactiva, y el resultado esperado escrito
 * antes), Act (agendar a Rocky) y Assert (lo obtenido contra lo esperado). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('caso-aaa', {
    duracion: 4.8,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      function titulo(letra, frase, y, color, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 20, y, 40, 34, 8); L.rellena(ctx, color);
          UJ.rotulo(ctx, lz, letra, 40, y + 5, { tam: 20, peso: 800, color: m.papel });
          UJ.rotulo(ctx, lz, frase, 72, y + 4, { tam: 22, peso: 800, alinear: 'left', color: color });
        });
      }
      UJ.codigo(ctx, lz, 20, 16, W - 40, '@Test void agendarMascotaInactivaLanzaExcepcion()', L.tramo(t, 0, 0.08), 16);
      // Arrange
      titulo('A', 'Arrange · preparar', 70, A, L.tramo(t, 0.06, 0.1));
      UJ.caja(ctx, lz, 20, 114, 210, 80, 'Kira', 'activa', V, L.tramo(t, 0.1, 0.16));
      UJ.caja(ctx, lz, 245, 114, 210, 80, 'Rocky', 'inactiva', R, L.tramo(t, 0.13, 0.19));
      UJ.alfa(ctx, L.tramo(t, 0.2, 0.27), function () {
        L.rectRed(ctx, 480, 100, 300, 104, 12); L.rellena(ctx, L.tono(S, 0.75), L.tono(S, -0.35), 3);
        UJ.rotulo(ctx, lz, 'Esperado, escrito ANTES:', 496, 112, { tam: 17, peso: 800, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'agendar a Rocky lanza', 496, 140, { tam: 17, peso: 500, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'IllegalStateException', 496, 166, { tam: 18, peso: 800, alinear: 'left', color: R });
      });
      // Act
      titulo('A', 'Act · ejecutar', 230, C, L.tramo(t, 0.38, 0.42));
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.43), function () { UJ.codigo(ctx, lz, 20, 278, 440, 'servicio.agendar("Rocky", fecha);', L.tramo(t, 0.42, 0.52), 16); });
      UJ.rayo(ctx, 470, 270, 50, S, L.tramo(t, 0.5, 0.54));
      L.flecha(ctx, 500, 295, 528, 295, C, 3, L.tramo(t, 0.52, 0.56));
      UJ.alfa(ctx, L.tramo(t, 0.54, 0.6), function () {
        L.rectRed(ctx, 532, 260, 248, 74, 12); L.rellena(ctx, L.tono(C, 0.88), C, 3);
        UJ.rotulo(ctx, lz, 'Obtenido:', 548, 270, { tam: 17, peso: 800, alinear: 'left', color: C });
        UJ.rotulo(ctx, lz, 'IllegalStateException', 548, 298, { tam: 18, peso: 800, alinear: 'left', color: R });
      });
      // Assert
      titulo('A', 'Assert · comprobar', 370, V, L.tramo(t, 0.7, 0.74));
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.75), function () { UJ.codigo(ctx, lz, 20, 418, W - 40, 'assertThrows(IllegalStateException.class, () -> servicio.agendar("Rocky", fecha));', L.tramo(t, 0.74, 0.84), 14); });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.9), function () {
        UJ.rotulo(ctx, lz, 'esperado', 200, 486, { tam: 22, peso: 700, color: L.tono(S, -0.45) });
        UJ.rotulo(ctx, lz, '=', 300, 482, { tam: 30, peso: 800 });
        UJ.rotulo(ctx, lz, 'obtenido', 400, 486, { tam: 22, peso: 700, color: C });
      });
      UJ.sello(ctx, lz, 520, 500, 30, true, L.tramo(t, 0.86, 0.94));
      UJ.rotulo(ctx, lz, 'La prueba pasa: el caso negativo se comporta como se escribió.', W / 2, 560, { tam: 19, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.9, 0.99) });
    }
  });
})();
