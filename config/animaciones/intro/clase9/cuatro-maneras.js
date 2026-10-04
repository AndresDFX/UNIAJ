/* Cuatro maneras de generar una mejora sobre un antecedente: quitar, combinar, invertir y
 * adaptar de otro dominio. Una por cuadrante, con su gesto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cuatro-maneras', {
    duracion: 5,
    pasos: [0.25, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      function panel(x, y, tit, sub, col, a, gesto) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, 360, 290, 16); L.rellena(ctx, L.tono(col, 0.92), col, 3);
          UJ.rotulo(ctx, lz, tit, x + 180, y + 16, { tam: 28, peso: 800, color: col });
          UJ.rotulo(ctx, lz, sub, x + 180, y + 226, { tam: 18, ancho: 330 });
          gesto(x, y);
        });
      }
      var a = [L.tramo(t, 0, 0.1), L.tramo(t, 0.25, 0.35), L.tramo(t, 0.5, 0.6), L.tramo(t, 0.75, 0.85)];
      panel(30, 20, 'QUITAR', 'sacar un paso: la más subestimada', R, a[0], function (x, y) {
        for (var i = 0; i < 3; i++) { L.rectRed(ctx, x + 40 + i * 100, y + 100, 80, 60, 10); L.rellena(ctx, m.papel, R, 3); UJ.rotulo(ctx, lz, 'paso ' + (i + 1), x + 80 + i * 100, y + 118, { tam: 17 }); }
        var c = L.tramo(t, 0.08, 0.18);
        L.trazo(ctx, [[x + 140, y + 92], [x + 220, y + 168]], c, R, 7);
        L.trazo(ctx, [[x + 220, y + 92], [x + 140, y + 168]], c, R, 7);
      });
      panel(410, 20, 'COMBINAR', 'juntar dos cosas que ya existen', A, a[1], function (x, y) {
        var d = L.mezcla(60, 0, L.tramo(t, 0.3, 0.44, 'frena'));
        L.rectRed(ctx, x + 50 - d, y + 95, 120, 70, 10); L.rellena(ctx, L.tono(A, 0.7), A, 2);
        UJ.rotulo(ctx, lz, 'lista pública', x + 110 - d, y + 118, { tam: 17, peso: 700 });
        L.rectRed(ctx, x + 190 + d, y + 95, 120, 70, 10); L.rellena(ctx, L.tono(C, 0.7), C, 2);
        UJ.rotulo(ctx, lz, 'mensaje', x + 250 + d, y + 118, { tam: 17, peso: 700 });
      });
      panel(30, 330, 'INVERTIR', 'cambiar quién hace el trabajo', C, a[2], function (x, y) {
        var g = L.tramo(t, 0.56, 0.7, 'suave');
        UJ.rotulo(ctx, lz, g < 0.5 ? 'alguien responde' : 'el usuario consulta', x + 180, y + 120, { tam: 22, peso: 700, color: L.tono(C, -0.3) });
        L.flecha(ctx, x + 90, y + 170, x + 270, y + 170, C, 4, 1);
        L.flecha(ctx, x + 270, y + 90, x + 90, y + 90, C, 4, 1);
      });
      panel(410, 330, 'ADAPTAR', 'traer una solución de otro campo', V, a[3], function (x, y) {
        function bx(bx0, t1, t2, al) {
          UJ.alfa(ctx, al, function () {
            L.rectRed(ctx, bx0, y + 80, 145, 100, 12); L.rellena(ctx, L.tono(V, 0.88), V, 2);
            UJ.rotulo(ctx, lz, t1, bx0 + 72, y + 96, { tam: 19, peso: 800, color: V, ancho: 135 });
            UJ.rotulo(ctx, lz, t2, bx0 + 72, y + 136, { tam: 16, ancho: 135 });
          });
        }
        bx(x + 20, '¿mesa libre?', 'restaurante', 1);
        L.flecha(ctx, x + 168, y + 130, x + 192, y + 130, V, 4, L.tramo(t, 0.82, 0.9));
        bx(x + 195, '¿libro libre?', 'biblioteca', L.tramo(t, 0.86, 0.96));
      });
    }
  });
})();
