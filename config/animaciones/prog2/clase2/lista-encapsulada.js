/* La lista encapsulada: main no toca la List private; pasa por agregar, buscarPorId y
 * eliminarPorId. agregar rechaza un id repetido; buscarPorId devuelve null si no esta. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('lista-encapsulada', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      // La clase y su lista privada
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, 330, 30, 446, 400, 16); L.rellena(ctx, L.tono(A, 0.93), A, 3);
        UJ.rotulo(ctx, lz, 'RegistroMascotas', 553, 42, { tam: 22, peso: 800, color: A, letra: 'Consolas, monospace' });
        L.rectRed(ctx, 500, 90, 256, 320, 12); L.rellena(ctx, m.papel, A, 2);
        UJ.rotulo(ctx, lz, 'private List<Mascota>', 628, 100, { tam: 16, peso: 700, letra: 'Consolas, monospace' });
      });
      var items = ['M-001 · Luna', 'M-002 · Michi', 'M-003 · Rocky'];
      var n = 2 + (t >= 0.5 ? 1 : 0);
      for (var i = 0; i < 3; i++) {
        var a = i < 2 ? L.tramo(t, 0.04, 0.1) : L.tramo(t, 0.48, 0.54);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 516, 136 + i * 56, 224, 44, 8); L.rellena(ctx, L.tono(V, 0.85), V, 2);
          UJ.rotulo(ctx, lz, items[i], 628, 146 + i * 56, { tam: 17, peso: 700 });
        });
      }
      // main afuera
      UJ.alfa(ctx, L.tramo(t, 0.02, 0.1), function () {
        L.rectRed(ctx, 24, 170, 150, 80, 12); L.rellena(ctx, L.tono(m.gris, 0.85), m.gris, 2);
        UJ.rotulo(ctx, lz, 'main', 99, 192, { tam: 24, peso: 800, letra: 'Consolas, monospace' });
      });
      // 1. Intento directo
      var fuera = 1 - L.tramo(t, 0.32, 0.36);
      UJ.alfa(ctx, fuera, function () {
        L.flecha(ctx, 178, 120, 494, 120, R, 3, L.tramo(t, 0.1, 0.18, 'frena'));
        UJ.rotulo(ctx, lz, 'registro.mascotas.add(…)', 178, 84, { tam: 15, alinear: 'left', color: R, visible: L.tramo(t, 0.1, 0.16) });
        UJ.sello(ctx, lz, 420, 120, 22, false, L.tramo(t, 0.18, 0.24));
        UJ.rotulo(ctx, lz, 'no compila: es private', 160, 280, { tam: 19, peso: 800, color: R, visible: L.tramo(t, 0.2, 0.28) });
      });
      // 2. Las puertas
      var puertas = ['agregar(m)', 'buscarPorId(id)', 'eliminarPorId(id)'];
      for (var p = 0; p < 3; p++) {
        UJ.alfa(ctx, L.tramo(t, 0.34 + p * 0.03, 0.4 + p * 0.03), function () {
          L.rectRed(ctx, 310, 180 + p * 76, 176, 56, 10); L.rellena(ctx, A);
          UJ.rotulo(ctx, lz, puertas[p], 398, 196 + p * 76, { tam: 16, peso: 800, color: m.papel, letra: 'Consolas, monospace' });
        });
      }
      L.flecha(ctx, 178, 210, 304, 208, V, 4, L.tramo(t, 0.42, 0.46, 'frena') * (1 - L.tramo(t, 0.64, 0.66)));
      L.flecha(ctx, 488, 208, 512, 248, V, 3, L.tramo(t, 0.46, 0.5, 'frena'));
      UJ.rotulo(ctx, lz, 'agregar(M-003 Rocky) → entra', 24, 300, { tam: 18, peso: 700, color: V, alinear: 'left', visible: L.tramo(t, 0.52, 0.58) * (1 - L.tramo(t, 0.64, 0.66)) });
      // 3. Reglas de las puertas
      L.flecha(ctx, 178, 226, 304, 214, R, 3, L.tramo(t, 0.66, 0.7, 'frena'));
      UJ.sello(ctx, lz, 470, 168, 18, false, L.tramo(t, 0.7, 0.74));
      UJ.rotulo(ctx, lz, 'agregar(M-001) → id repetido, rechazado', 24, 300, { tam: 18, peso: 700, color: R, alinear: 'left', ancho: 280, visible: L.tramo(t, 0.7, 0.76) });
      UJ.rotulo(ctx, lz, 'buscarPorId("M-999") → null', 24, 360, { tam: 18, peso: 700, color: m.tinta, alinear: 'left', ancho: 280, visible: L.tramo(t, 0.76, 0.82) });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 24, 460, W - 48, 150, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Afuera solo hay métodos con reglas.', W / 2, 474, { tam: 22, peso: 800, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'Se programa contra la interfaz: List, no ArrayList.', W / 2, 516, { tam: 19, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'toString() en Mascota: nada de Mascota@6d06d69c.', W / 2, 552, { tam: 19, ancho: W - 80 });
      });
    }
  });
})();
