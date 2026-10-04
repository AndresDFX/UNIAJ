/* Ilustracion: la linea base es la cifra de HOY; sin ella no hay con que comparar al final. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-linea-base', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', V = m.verde || A, S = m.sello || m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'La cifra de HOY, antes de tocar nada', W / 2, 14, { tam: 26, peso: 800, color: A });
      L.rectRed(ctx, 30, 70, 260, 150, 16); L.rellena(ctx, L.tono(A, 0.88), A, 3);
      UJ.rotulo(ctx, lz, 'HOY · línea base', 160, 84, { tam: 20, peso: 800, color: A });
      UJ.rotulo(ctx, lz, '2 h diarias', 160, 120, { tam: 34, peso: 800 });
      UJ.rotulo(ctx, lz, 'confirmando citas', 160, 172, { tam: 18 });
      L.flecha(ctx, 300, 145, 496, 145, L.tono(m.tinta, 0.4), 5, 1);
      UJ.rotulo(ctx, lz, 'el proyecto', 400, 110, { tam: 19, peso: 700 });
      L.rectRed(ctx, 510, 70, 260, 150, 16); L.rellena(ctx, L.tono(V, 0.88), V, 3);
      UJ.rotulo(ctx, lz, 'AL FINAL', 640, 84, { tam: 20, peso: 800, color: V });
      UJ.rotulo(ctx, lz, '20 min', 640, 120, { tam: 34, peso: 800 });
      UJ.rotulo(ctx, lz, 'se mide igual', 640, 172, { tam: 18 });
      UJ.sello(ctx, lz, 60, 278, 22, false, 1);
      UJ.rotulo(ctx, lz, '«Mejoramos el proceso»: no demuestra nada', 96, 264, { tam: 21, peso: 700, alinear: 'left', ancho: 680 });
      UJ.sello(ctx, lz, 60, 338, 22, true, 1);
      UJ.rotulo(ctx, lz, '«De 2 h a 20 min»: sí lo demuestra', 96, 324, { tam: 21, peso: 700, alinear: 'left', ancho: 680 });
      L.rectRed(ctx, 30, 392, 360, 150, 16); L.rellena(ctx, L.tono(S, 0.55), L.tono(S, -0.35), 2);
      UJ.rotulo(ctx, lz, 'Toda cifra dice cómo y cuándo se obtuvo', 210, 416, { tam: 21, peso: 800, ancho: 320 });
      UJ.rotulo(ctx, lz, 'si es estimada: «estimado»', 210, 490, { tam: 18, ancho: 320 });
      L.rectRed(ctx, 410, 392, 360, 150, 16); L.rellena(ctx, L.tono(R, 0.9), R, 2);
      UJ.rotulo(ctx, lz, '¿No se puede contar nada?', 590, 416, { tam: 21, peso: 800, color: R, ancho: 320 });
      UJ.rotulo(ctx, lz, 'El problema es muy grande: bájelo', 590, 458, { tam: 19, ancho: 320 });
    }
  });
})();
