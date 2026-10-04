/* Ilustracion: cuando SI conviene el enfoque tradicional. Cuatro situaciones en las que escribir
 * el detalle antes no es burocracia sino la unica forma de estimar y de cumplir. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-cuando-tradicional', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El detalle previo conviene cuando…', W / 2, 12, { tam: 26, peso: 800, color: A });
      var casos = [
        ['Requisitos estables', 'se conocen desde el principio y casi no cambian'],
        ['Precio fijo o licitación', 'el alcance debe estar cerrado para cotizar'],
        ['Sistema crítico o regulado', 'equipos médicos, aviación, banca, datos personales'],
        ['Varios proveedores', 'necesitan un documento común para trabajar en paralelo']
      ];
      for (var i = 0; i < 4; i++) {
        var col = i % 2, fil = Math.floor(i / 2);
        var x = 24 + col * 384, y = 66 + fil * 178;
        L.rectRed(ctx, x, y, 368, 160, 14); L.rellena(ctx, L.tono(A, 0.92), A, 2.5);
        UJ.sello(ctx, lz, x + 36, y + 36, 20, true, 1);
        UJ.rotulo(ctx, lz, casos[i][0], x + 68, y + 22, { tam: 21, peso: 800, color: L.tono(A, -0.3), alinear: 'left', ancho: 290 });
        UJ.rotulo(ctx, lz, casos[i][1], x + 184, y + 82, { tam: 18, peso: 500, ancho: 320 });
      }
      // De las cuatro a la conclusion
      L.flecha(ctx, W / 2, 426, W / 2, 462, A, 4, 1);
      L.rectRed(ctx, 24, 470, 752, 110, 16); L.rellena(ctx, L.tono(m.sello, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Ahí el detalle previo no es burocracia:', W / 2, 488, { tam: 22, peso: 700 });
      UJ.rotulo(ctx, lz, 'es la única forma de estimar y cumplir', W / 2, 526, { tam: 24, peso: 800, color: A });
    }
  });
})();
