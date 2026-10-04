/* Precondicion, flujo y postcondicion: lo que se da por cierto antes, lo que queda garantizado
 * despues (y que se vuelve caso de prueba), y que el fracaso no deja nada a medias. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pre-post', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.42, 0.74, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Registrar mascota', W / 2, 20, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var y = 80, an = 232;
      UJ.tarjeta(ctx, lz, 24, y, an, 'Precondición', ['usuario autenticado', 'el dueño existe'], m.gris, L.tramo(t, 0.04, 0.12), undefined, { alto: 130 });
      UJ.flecha(ctx, lz, 258, y + 65, 282, y + 65, m.tinta, L.tramo(t, 0.12, 0.16), null, { grosor: 3 });
      UJ.tarjeta(ctx, lz, 284, y, an, 'Flujo', ['nadie vuelve a pedir', 'la contraseña'], A, L.tramo(t, 0.14, 0.22), undefined, { alto: 130 });
      UJ.flecha(ctx, lz, 518, y + 65, 542, y + 65, m.tinta, L.tramo(t, 0.22, 0.26), null, { grosor: 3 });
      UJ.tarjeta(ctx, lz, 544, y, an, 'Postcondición', ['ficha con código único', 'asociada a un propietario', 'bitácora: quién y cuándo'],
        m.verde, L.tramo(t, 0.24, 0.32), L.tramo(t, 0.26, 0.4) * 3, { alto: 130, tam: 17 });

      // La postcondicion se vuelve prueba
      UJ.flecha(ctx, lz, 660, 214, 660, 300, m.verde, L.tramo(t, 0.44, 0.54), null, { grosor: 3 });
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.6), function () {
        L.rectRed(ctx, 544, 304, an, 84, 12); L.rellena(ctx, L.tono(m.verde, 0.86), m.verde, 2.5);
        UJ.rotulo(ctx, lz, 'Caso de prueba', 660, 316, { tam: 20, peso: 800, color: L.tono(m.verde, -0.3) });
        UJ.rotulo(ctx, lz, 'cada garantía se comprueba', 660, 348, { tam: 17, peso: 600, ancho: an - 20 });
      });

      // Rama de fracaso
      UJ.flecha(ctx, lz, 400, 214, 400, 300, m.malva, L.tramo(t, 0.76, 0.84), 'si falla', { grosor: 3, dy: -12 });
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.9), function () {
        L.rectRed(ctx, 284, 304, an, 84, 12); L.rellena(ctx, L.tono(m.malva, 0.88), m.malva, 2.5);
        UJ.rotulo(ctx, lz, 'Ningún registro a medias', 400, 320, { tam: 19, peso: 800, color: m.malva, ancho: an - 20 });
      });

      UJ.rotulo(ctx, lz, 'Antes: se da por cierto. Después: queda garantizado.', W / 2, 560,
        { tam: 22, peso: 700, color: m.tinta, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
