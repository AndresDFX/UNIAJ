/* Ilustracion: como amarra la clase con las vecinas — lo que dejo cada clase anterior y lo que
 * se usa hoy de ello. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-amarre', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var cl = [
        ['Clase 1', 'el esquema y el CHECK de stock', 'hoy se retira para ver el hueco'],
        ['Clase 2', 'los roles', 'current_user en la auditoría · pg_dumpall'],
        ['Clase 3', 'procedimientos y bloques DO', 'con ellos se prueban los triggers']
      ];
      for (var i = 0; i < 3; i++) {
        var y = 40 + i * 150;
        L.rectRed(ctx, 24, y, 220, 110, 14); L.rellena(ctx, L.tono(A, 0.88), A, 2);
        UJ.rotulo(ctx, lz, cl[i][0], 134, y + 16, { tam: 22, peso: 800, color: A });
        UJ.rotulo(ctx, lz, cl[i][1], 134, y + 54, { tam: 16, ancho: 200 });
        L.flecha(ctx, 250, y + 55, 330, y + 55, A, 4, 1);
        L.rectRed(ctx, 336, y + 10, 270, 90, 14); L.rellena(ctx, m.papel, C, 2);
        UJ.rotulo(ctx, lz, cl[i][2], 471, y + 30, { tam: 16, ancho: 250 });
        L.trazo(ctx, [[606, y + 55], [650, y + 55], [650, 265], [664, 265]], 1, L.tono(C, 0.2), 3);
      }
      L.rectRed(ctx, 668, 200, 112, 130, 16); L.rellena(ctx, m.sello || C, m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Clase 4', 724, 230, { tam: 20, peso: 800 });
      UJ.rotulo(ctx, lz, 'hoy', 724, 266, { tam: 18 });
      UJ.rotulo(ctx, lz, 'Nada de hoy es una isla: cada pieza viene de una clase anterior.', W / 2, 520,
                { tam: 18, peso: 700, ancho: W - 40 });
    }
  });
})();
