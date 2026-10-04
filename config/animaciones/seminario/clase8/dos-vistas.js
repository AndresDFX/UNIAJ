/* Los diagramas UML en dos vistas, estructural y de comportamiento, y los cinco que un analista
 * usa siempre. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dos-vistas', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Dos vistas del mismo sistema', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var vistas = [
        { x: 50, tit: 'Estructural', sub: 'de qué está hecho', it: ['Clases', 'Objetos', 'Componentes', 'Despliegue'], uso: [0, 3], c: A, a: L.tramo(t, 0.06, 0.16), n: L.tramo(t, 0.12, 0.3) * 4 },
        { x: 420, tit: 'Comportamiento', sub: 'qué pasa y en qué orden', it: ['Casos de uso', 'Actividades', 'Secuencia', 'Máquina de estados'], uso: [0, 1, 2], c: C, a: L.tramo(t, 0.38, 0.48), n: L.tramo(t, 0.44, 0.62) * 4 }
      ];
      var res = L.tramo(t, 0.7, 0.82);
      for (var v = 0; v < 2; v++) {
        var o = vistas[v];
        UJ.alfa(ctx, o.a, function () {
          UJ.rotulo(ctx, lz, o.sub, o.x + 165, 80, { tam: 19, peso: 700, color: L.tono(o.c, -0.25) });
        });
        // Resaltado de los que se usan siempre, debajo del texto
        UJ.alfa(ctx, o.a * res, function () {
          for (var k = 0; k < o.uso.length; k++) {
            L.rectRed(ctx, o.x + 6, 112 + 41 + 4 + o.uso[k] * 42, 318, 36, 8); L.rellena(ctx, L.tono(m.sello, 0.6));
          }
        });
        UJ.tarjeta(ctx, lz, o.x, 112, 330, o.tit, o.it, o.c, o.a, o.n, { tam: 20, fila: 42 });
        UJ.alfa(ctx, o.a * res, function () {
          for (var k = 0; k < o.uso.length; k++) UJ.sello(ctx, lz, o.x + 300, 112 + 41 + 22 + o.uso[k] * 42, 13, true, 1);
        });
      }
      UJ.alfa(ctx, res, function () {
        L.rectRed(ctx, 250, 370, 300, 44, 22); L.rellena(ctx, L.tono(m.sello, 0.6), L.tono(m.sello, -0.3), 2);
        UJ.rotulo(ctx, lz, 'los cinco que se usan siempre', 400, 381, { tam: 19, peso: 800 });
      });
      UJ.rotulo(ctx, lz, 'Un sistema necesita las dos: el plano de plantas y el de instalaciones', W / 2, 545,
                { tam: 21, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
