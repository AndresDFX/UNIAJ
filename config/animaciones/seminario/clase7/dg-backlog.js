/* Lo que dibuja el codigo de «El mapa del backlog: epicas, historias y orden»: dos epicas arriba
 * y, colgadas de cada una, sus historias con los puntos de estimacion. */
(function () {
  FP_ANIMADOR.registrar('dg-backlog', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var epica = { relleno: '#095292', borde: '#063A68', color: '#FFFFFF' };
      DG.nodo(ctx, lz, 280, 150, 260, 60, 'EPICA 1 - Agenda', 'rect', { tam: 18, relleno: epica.relleno, borde: epica.borde, color: epica.color });
      DG.nodo(ctx, lz, 680, 150, 200, 60, 'EPICA 2 -\nExpediente', 'rect', { tam: 17, relleno: epica.relleno, borde: epica.borde, color: epica.color });
      var hus = [[110, 'HU-01 Registrar\ndueno', '3 pts'], [290, 'HU-02 Registrar\nmascota', '5 pts'],
                 [470, 'HU-03 Agendar\ncita', '8 pts'], [680, 'HU-04 Abrir\nexpediente', '5 pts']];
      hus.forEach(function (h, i) {
        DG.nodo(ctx, lz, h[0], 400, 165, 100, h[1] + '\n' + h[2], 'rect', { tam: 16 });
        var desde = i < 3 ? [280, 180] : [680, 180];
        DG.flecha(ctx, lz, [desde, [h[0], 349]]);
      });
      DG.marca(ctx, lz, 60, 500, 1, 'Los puntos son relativos, no horas: HU-03 es «como HU-02, pero mas»', 680);
      DG.marca(ctx, lz, 60, 560, 2, 'El orden del backlog sale del valor, no de los puntos', 680);
    }
  });
})();
