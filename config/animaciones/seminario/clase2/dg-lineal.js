/* Lo que dibuja el codigo de «El recorrido lineal del ciclo de vida»: cinco fases en fila, cada
 * una entra solo cuando la anterior cerro. Sin flecha de regreso: eso es lo lineal. */
(function () {
  FP_ANIMADOR.registrar('dg-lineal', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var fases = ['Requisitos', 'Diseno', 'Construccion', 'Pruebas', 'Mantenimiento'];
      var w = 128, gap = 32, x0 = 20, y = 300;
      for (var i = 0; i < 5; i++) {
        var cx = x0 + w / 2 + i * (w + gap);
        DG.nodo(ctx, lz, cx, y, w, 60, fases[i], 'rect', { tam: 15 });
        if (i < 4) DG.flecha(ctx, lz, [[cx + w / 2, y], [cx + w / 2 + gap - 1, y]]);
      }
      DG.marca(ctx, lz, 84, 200, 1, 'Cada fase cierra con un artefacto aprobado y la siguiente empieza sobre el', 640);
      DG.marca(ctx, lz, 84, 420, 2, 'No hay flecha de regreso: lineal significa que no se vuelve', 640);
    }
  });
})();
