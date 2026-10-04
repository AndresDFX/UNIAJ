/* B-Tree: raiz, ramas y hojas (con todas las claves y sus punteros). Una busqueda baja de la
 * raiz a una hoja; cada nodo es una pagina de 8 KB con del orden de 400 claves. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('btree', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      function nodo(x, y, an, txt, col, a, activo) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x - an / 2, y, an, 50, 10);
          L.rellena(ctx, activo ? (m.sello || C) : L.tono(col, 0.88), col, activo ? 4 : 2);
          L.texto(ctx, txt, x, y + 14, { tam: 18, peso: 700, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
        });
      }
      var bus = L.tramo(t, 0.4, 0.7);
      var arA = L.tramo(t, 0.08, 0.2), hoA = L.tramo(t, 0.16, 0.28);
      // aristas
      L.trazo(ctx, [[400, 110], [220, 170]], arA, L.tono(m.tinta, 0.5), 3);
      L.trazo(ctx, [[400, 110], [580, 170]], arA, L.tono(m.tinta, 0.5), 3);
      var hojas = [[100, '10 · 20'], [260, '35 · 40'], [460, '55 · 60'], [660, '80 · 95']];
      for (var i = 0; i < 4; i++) L.trazo(ctx, [[i < 2 ? 220 : 580, 220], [hojas[i][0], 300]], hoA, L.tono(m.tinta, 0.5), 3);
      nodo(400, 60, 160, '50', A, L.tramo(t, 0, 0.1), bus > 0.1);
      nodo(220, 170, 160, '30', A, arA, false);
      nodo(580, 170, 160, '70', A, arA, bus > 0.4);
      for (var k = 0; k < 4; k++) nodo(hojas[k][0], 300, 150, hojas[k][1], C, hoA, k === 2 && bus > 0.75);
      UJ.rotulo(ctx, lz, 'raíz', 560, 72, { tam: 18, peso: 700, color: A, visible: L.tramo(t, 0.22, 0.3) });
      UJ.rotulo(ctx, lz, 'ramas', 720, 182, { tam: 18, peso: 700, color: A, visible: L.tramo(t, 0.22, 0.3) });
      UJ.rotulo(ctx, lz, 'hojas: todas las claves con sus punteros', W / 2, 364, { tam: 18, peso: 700, color: L.tono(C, -0.3), visible: L.tramo(t, 0.24, 0.32) });
      // la busqueda
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.44), function () { UJ.codigo(ctx, lz, 30, 410, 250, 'buscar 60', 1, 18); });
      if (bus > 0) {
        L.flecha(ctx, 400, 112, 572, 166, m.malva || '#A02030', 4, L.tramo(bus, 0.1, 0.4, 'frena'));
        L.flecha(ctx, 580, 222, 466, 296, m.malva || '#A02030', 4, L.tramo(bus, 0.45, 0.75, 'frena'));
      }
      UJ.rotulo(ctx, lz, '3 lecturas: una por nivel', 470, 416, { tam: 19, peso: 800, color: m.malva || '#A02030', visible: L.tramo(t, 0.66, 0.72) });
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.88), function () {
        L.rectRed(ctx, 30, 480, W - 60, 110, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Cada nodo es una página de 8 KB', W / 2, 494, { tam: 21, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'con entradas de unos 20 bytes caben del orden de 400 claves', W / 2, 536, { tam: 18, ancho: W - 100 });
      });
    }
  });
})();
