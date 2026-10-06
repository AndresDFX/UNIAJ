/* Lo que dibuja el codigo de «El tablero de flujo con limite de trabajo en curso»: cuatro
 * columnas (subgrafos) con sus historias y las flechas que marcan el flujo; el limite va en el
 * titulo de la columna. */
(function () {
  FP_ANIMADOR.registrar('dg-tablero', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var cols = [['Backlog', ['HU-04', 'HU-05']], ['En curso -\nLIMITE 2', ['HU-02', 'HU-03']],
                  ['En revision -\nLIMITE 1', ['HU-01']], ['Terminado', ['HU-00']]];
      var w = 158, gap = 42, x0 = 20, y = 150, h = 300;
      cols.forEach(function (c, i) {
        var x = x0 + i * (w + gap);
        var lim = i === 1 || i === 2;
        DG.grupo(ctx, lz, x, y, w, h, '', lim ? { borde: '#B8860B', relleno: '#FFFBEA' } : {});
        DG.txtc(ctx, lz, c[0], x + w / 2, y + 30, 16, 800, lim ? '#8A6400' : '#3A5068', w - 10);
        c[1].forEach(function (hu, k) { DG.nodo(ctx, lz, x + w / 2, y + 110 + k * 80, 120, 50, hu, 'rect', { tam: 17 }); });
        if (i < 3) DG.flecha(ctx, lz, [[x + w, y + h / 2], [x + w + gap - 1, y + h / 2]]);
      });
      DG.marca(ctx, lz, 240, 112, 1, 'El LIMITE: con 2 en curso, HU-04 no entra hasta cerrar una', 520);
    }
  });
})();
