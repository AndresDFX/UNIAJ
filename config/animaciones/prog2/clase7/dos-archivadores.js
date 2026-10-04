/* El problema: un solo archivador. Cada ventana hace su propio new RepositorioMascotas() y quedan
 * dos listas distintas en memoria; la de citas no ve a Luna. La salida: una sola instancia que
 * las dos ventanas alcanzan. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dos-archivadores', {
    duracion: 4.8,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, W = lz.ancho;
      // Paso 1: dos ventanas, dos new, dos listas
      UJ.caja(ctx, lz, 40, 20, 320, 80, 'Ventana de registro', null, A, L.tramo(t, 0, 0.06));
      UJ.caja(ctx, lz, 440, 20, 320, 80, 'Ventana de citas', null, C, L.tramo(t, 0.03, 0.09));
      var nuevo = 1 - L.tramo(t, 0.68, 0.74), uno = L.tramo(t, 0.72, 0.78);
      UJ.alfa(ctx, nuevo, function () {
        UJ.codigo(ctx, lz, 40, 116, 320, 'new RepositorioMascotas()', L.tramo(t, 0.08, 0.16), 16);
        UJ.codigo(ctx, lz, 440, 116, 320, 'new RepositorioMascotas()', L.tramo(t, 0.12, 0.2), 16);
      });
      UJ.alfa(ctx, uno, function () {
        UJ.codigo(ctx, lz, 40, 116, 320, 'RepositorioClinica.getInstancia()', 1, 15);
        UJ.codigo(ctx, lz, 440, 116, 320, 'RepositorioClinica.getInstancia()', 1, 15);
      });
      // Las dos listas (desaparecen en el paso 3)
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.24) * nuevo, function () {
        L.flecha(ctx, 200, 152, 200, 196, A, 3);
        L.flecha(ctx, 600, 152, 600, 196, C, 3);
        UJ.tabla(ctx, lz, 40, 200, 320, 'lista n.º 1', ['Luna', 'Michi', 'Rocky'], L.tramo(t, 0.2, 0.3) * 3, A);
        UJ.tabla(ctx, lz, 440, 200, 320, 'lista n.º 2', [], 0, C);
        UJ.rotulo(ctx, lz, '(vacía)', 600, 262, { tam: 20, peso: 500, color: L.tono(m.tinta, 0.4) });
        UJ.rotulo(ctx, lz, 'Dos new → dos listas distintas en memoria', W / 2, 390, { tam: 24, peso: 700, ancho: W - 40 });
      });
      // Paso 2: la de citas no ve a Luna
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.46) * nuevo, function () {
        UJ.codigo(ctx, lz, 440, 300, 320, 'buscar("Luna") → null', 1, 16);
        UJ.sello(ctx, lz, 720, 270, 26, false, L.tramo(t, 0.46, 0.54));
        UJ.rotulo(ctx, lz, 'La ventana de citas no ve las mascotas', W / 2, 450, { tam: 23, color: R, ancho: W - 40 });
        UJ.rotulo(ctx, lz, 'que registró la ventana de registro.', W / 2, 482, { tam: 23, color: R, ancho: W - 40 });
      });
      // Paso 3: una sola instancia compartida
      UJ.alfa(ctx, uno, function () {
        L.flecha(ctx, 200, 152, 300, 222, A, 3, L.tramo(t, 0.74, 0.82));
        L.flecha(ctx, 600, 152, 500, 222, C, 3, L.tramo(t, 0.74, 0.82));
        UJ.tabla(ctx, lz, 240, 226, 320, 'una sola instancia', ['Luna', 'Michi', 'Rocky'], 3, V);
        UJ.sello(ctx, lz, 600, 290, 26, true, L.tramo(t, 0.82, 0.9));
        UJ.rotulo(ctx, lz, 'Las dos ventanas ven a Luna', W / 2, 430, { tam: 24, peso: 700, color: V });
        UJ.rotulo(ctx, lz, 'Una y solo una instancia,', W / 2, 480, { tam: 22, peso: 600, visible: L.tramo(t, 0.86, 0.94) });
        UJ.rotulo(ctx, lz, 'alcanzable desde cualquier parte del programa.', W / 2, 512, { tam: 22, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.88, 0.97) });
      });
    }
  });
})();
