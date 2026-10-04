/* Arbol Throwable: Error / Exception; IOException (checked) y RuntimeException (unchecked). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('checked-unchecked', {
    duracion: 4.5,
    pasos: [0.3, 0.65, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, G = m.gris || L.tono(m.tinta, 0.5), W = lz.ancho;
      function nodo(cx, y, an, txt, c, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, cx - an / 2, y, an, 50, 10); L.rellena(ctx, L.tono(c, 0.88), c, 3);
          UJ.rotulo(ctx, lz, txt, cx, y + 13, { tam: 19, peso: 800, color: L.tono(c, -0.3), ancho: an - 12 });
        });
      }
      function rama(x1, y1, x2, y2, a) { if (a > 0) L.trazo(ctx, [[x1, y1], [x1, (y1 + y2) / 2], [x2, (y1 + y2) / 2], [x2, y2]], a, L.tono(m.tinta, 0.5), 3); }
      var a0 = L.tramo(t, 0, 0.08), a1 = L.tramo(t, 0.08, 0.18), a2 = L.tramo(t, 0.34, 0.46), a3 = L.tramo(t, 0.68, 0.8);
      nodo(400, 20, 200, 'Throwable', A, a0);
      rama(400, 70, 160, 120, a1); rama(400, 70, 520, 120, a1);
      nodo(160, 120, 200, 'Error', G, a1);
      nodo(520, 120, 200, 'Exception', A, a1);
      UJ.rotulo(ctx, lz, 'fallas graves de la JVM: no se manejan', 160, 178, { tam: 16, ancho: 220, visible: L.tramo(t, 0.16, 0.22) });
      // checked
      rama(520, 170, 300, 260, a2);
      nodo(300, 260, 220, 'IOException', C, a2);
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.52), function () {
        L.rectRed(ctx, 30, 340, 360, 120, 12); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'CHECKED', 210, 352, { tam: 22, peso: 800, color: L.tono(C, -0.35) });
        UJ.rotulo(ctx, lz, 'el compilador exige catch o throws', 210, 388, { tam: 18, ancho: 330 });
        UJ.rotulo(ctx, lz, 'ej.: leer un archivo', 210, 420, { tam: 16, ancho: 330 });
      });
      // unchecked
      rama(520, 170, 620, 260, a3);
      nodo(620, 260, 240, 'RuntimeException', R, a3);
      var a4 = L.tramo(t, 0.76, 0.86);
      rama(620, 310, 530, 360, a4); rama(620, 310, 700, 360, a4);
      nodo(530, 360, 170, 'NumberFormat…', R, a4);
      nodo(700, 360, 150, 'NullPointer…', R, a4);
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 420, 440, 360, 110, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'UNCHECKED', 600, 452, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'no la exige: suele ser un error del programa', 600, 488, { tam: 18, ancho: 330 });
      });
    }
  });
})();
