/* Lo que dibuja el codigo de «El mismo ciclo en tres vueltas»: tres subgrafos apilados, cada uno
 * con las mismas cuatro fases en fila, y la flecha de una vuelta a la siguiente. */
(function () {
  FP_ANIMADOR.registrar('dg-tres-vueltas', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var vueltas = ['Vuelta 1 - ficha del paciente', 'Vuelta 2 - historia clinica y busqueda', 'Vuelta 3 - reportes y metricas'];
      var fases = ['Requisitos', 'Diseno', 'Construccion', 'Pruebas'];
      var gx = 20, gw = 760, gh = 130, y0 = 40, salto = 200;
      for (var v = 0; v < 3; v++) {
        var gy = y0 + v * salto;
        DG.grupo(ctx, lz, gx, gy, gw, gh, vueltas[v], { tam: 16 });
        var w = 150, gap = 40, x0 = gx + (gw - (4 * w + 3 * gap)) / 2, cy = gy + 80;
        for (var i = 0; i < 4; i++) {
          var cx = x0 + w / 2 + i * (w + gap);
          DG.nodo(ctx, lz, cx, cy, w, 54, fases[i], 'rect', { tam: 16 });
          if (i < 3) DG.flecha(ctx, lz, [[cx + w / 2, cy], [cx + w / 2 + gap - 1, cy]]);
        }
        if (v < 2) DG.flecha(ctx, lz, [[400, gy + gh], [400, gy + salto - 1]]);
      }
      DG.marca(ctx, lz, 432, y0 + gh + 35, 1, 'Cada vuelta entrega algo que funciona', 320);
    }
  });
})();
