/* Clave primaria: no se repite y no admite nulos. La pregunta es cual: natural (cedula,
 * microchip: la controla un tercero y falla en la clinica) o sustituta (id que genera la base). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pk-natural-sustituta', {
    duracion: 5,
    pasos: [0.24, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.alfa(ctx, L.tramo(t, 0, 0.12), function () {
        L.rectRed(ctx, 120, 24, W - 240, 80, 14); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'Clave primaria', W / 2, 34, { tam: 26, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, 'no se repite · no admite nulos', W / 2, 70, { tam: 19, color: m.papel });
      });
      UJ.rotulo(ctx, lz, '¿Cuál columna?', W / 2, 124, { tam: 22, peso: 700, visible: L.tramo(t, 0.14, 0.22) });
      // Natural
      UJ.caja(ctx, lz, 30, 170, 350, 110, 'Natural', 'cédula · microchip', C, L.tramo(t, 0.26, 0.34));
      var fallos = ['el dueño llega sin cédula', 'el microchip se digita mal', 'la mascota rescatada no tiene'];
      for (var i = 0; i < 3; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.36 + i * 0.08, 0.42 + i * 0.08), function () {
          L.rectRed(ctx, 30, 300 + i * 60, 350, 48, 10); L.rellena(ctx, L.tono(R, 0.88), R, 2);
          UJ.rotulo(ctx, lz, fallos[i], 220, 312 + i * 60, { tam: 17, peso: 600, ancho: 280 });
        });
        UJ.sello(ctx, lz, 58, 324 + i * 60, 16, false, L.tramo(t, 0.38 + i * 0.08, 0.46 + i * 0.08));
      }
      // Sustituta
      UJ.caja(ctx, lz, 420, 170, 350, 110, 'Sustituta', 'id_dueno 1, 2, 3', A, L.tramo(t, 0.68, 0.76));
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.84), function () {
        L.rectRed(ctx, 420, 300, 350, 168, 10); L.rellena(ctx, L.tono(V, 0.88), V, 2);
        UJ.rotulo(ctx, lz, 'la genera la base', 595, 318, { tam: 19, peso: 700, color: V });
        UJ.rotulo(ctx, lz, 'sin significado de negocio', 595, 354, { tam: 17 });
        UJ.rotulo(ctx, lz, 'nunca hay que corregirla', 595, 390, { tam: 17 });
      });
      UJ.sello(ctx, lz, 740, 330, 20, true, L.tramo(t, 0.8, 0.88));
      UJ.rotulo(ctx, lz, 'Si el valor lo controla un tercero, no es la PK.', W / 2, 520,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
      UJ.rotulo(ctx, lz, '(convención de oficio, no regla del motor)', W / 2, 556, { tam: 16, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
