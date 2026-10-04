/* Un indice es una estructura auxiliar, redundante y opcional: cada entrada guarda la clave
 * ordenada y un puntero fisico a la fila (ctid en PostgreSQL, ROWID en Oracle). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('indice-puntero', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var filas = ['(0,1) · 2026-03-12 · ATENDIDA', '(0,2) · 2026-03-09 · PROGRAMADA', '(0,3) · 2026-03-15 · CANCELADA', '(0,4) · 2026-03-10 · PROGRAMADA', '(0,5) · 2026-03-11 · ATENDIDA'];
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () { UJ.tabla(ctx, lz, 330, 40, 440, 'tabla cita (desordenada)', filas, 5, A); });
      var ent = [['2026-03-09', 1], ['2026-03-10', 3], ['2026-03-11', 4], ['2026-03-12', 0], ['2026-03-15', 2]];
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.24), function () {
        UJ.tabla(ctx, lz, 30, 40, 250, 'índice (ordenado)', ent.map(function (e) { return e[0] + ' → (0,' + (e[1] + 1) + ')'; }), 5, C);
      });
      for (var i = 0; i < 5; i++) {
        var p = L.tramo(t, 0.4 + i * 0.05, 0.48 + i * 0.05, 'frena');
        if (p > 0) L.flecha(ctx, 282, 106 + i * 40, 328, 106 + ent[i][1] * 40, C, 2, p);
      }
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.4), function () {
        L.rectRed(ctx, 30, 340, 360, 110, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'Cada entrada guarda', 210, 352, { tam: 20, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'el valor de la clave + un puntero físico a la fila', 210, 386, { tam: 17, ancho: 330 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.72), function () {
        L.rectRed(ctx, 410, 340, 360, 110, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'El puntero se llama', 590, 352, { tam: 20, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'ctid en PostgreSQL · ROWID en Oracle', 590, 390, { tam: 17, ancho: 330 });
      });
      UJ.rotulo(ctx, lz, 'Estructura auxiliar, redundante y opcional:', W / 2, 500, { tam: 21, peso: 800, color: A, ancho: W - 40, visible: L.tramo(t, 0.82, 0.92) });
      UJ.rotulo(ctx, lz, 'si se borra, los datos siguen intactos.', W / 2, 536, { tam: 20, peso: 500, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
