/* Un GRANT sobre la tabla es todo o nada. La vista recorta filas (WHERE) y columnas (SELECT); el
 * privilegio por columna recorta solo columnas y no crea objeto nuevo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('vista-columna', {
    duracion: 5,
    pasos: [0.26, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var nc = 5, nf = 4, x0 = 40, y0 = 70, cw = 60, ch = 34;
      var cols = ['id', 'fecha', 'estado', 'nombre', 'email'];
      var estados = ['OK', 'CANC', 'OK', 'OK'];
      // Modo: 0 tabla completa, 1 vista, 2 por columna
      function grilla(ox, oy, keepCol, keepFila, titulo, col, a) {
        UJ.alfa(ctx, a, function () {
          UJ.rotulo(ctx, lz, titulo, ox + nc * cw / 2, oy - 40, { tam: 18, peso: 800, color: col, ancho: 300 });
          for (var j = 0; j < nc; j++) {
            var cj = keepCol(j);
            L.rectRed(ctx, ox + j * cw, oy, cw, ch, 0); L.rellena(ctx, cj ? col : L.tono(m.tinta, 0.85), m.papel, 1);
            L.texto(ctx, cols[j], ox + j * cw + cw / 2, oy + 9, { tam: 15, peso: 700, color: cj ? m.papel : L.tono(m.tinta, 0.55), alinear: 'center', letra: lz.letra });
            for (var i = 0; i < nf; i++) {
              var ok = cj && keepFila(i);
              L.rectRed(ctx, ox + j * cw, oy + ch * (i + 1), cw, ch, 0); L.rellena(ctx, ok ? L.tono(col, 0.85) : L.tono(m.tinta, 0.93), m.papel, 1);
              if (j === 2) L.texto(ctx, estados[i], ox + j * cw + cw / 2, oy + ch * (i + 1) + 9, { tam: 15, color: ok ? m.tinta : L.tono(m.tinta, 0.6), alinear: 'center', letra: 'Consolas, monospace' });
            }
          }
        });
      }
      grilla(x0 + 210, y0, function () { return true; }, function () { return true; }, 'GRANT sobre la tabla: todo', R, L.tramo(t, 0, 0.1) * (1 - L.tramo(t, 0.26, 0.32)));
      UJ.rotulo(ctx, lz, 'todas las filas y todas las columnas', W / 2, 260, { tam: 18, visible: L.tramo(t, 0.1, 0.18) * (1 - L.tramo(t, 0.26, 0.32)) });
      // Vista
      grilla(x0, y0, function (j) { return j !== 4; }, function (i) { return estados[i] !== 'CANC'; }, 'Vista', A, L.tramo(t, 0.3, 0.4));
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.5), function () {
        L.rectRed(ctx, x0, 260, 300, 120, 10); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'recorta filas Y columnas', x0 + 150, 270, { tam: 17, peso: 800, color: A });
        L.texto(ctx, "WHERE estado <> 'CANCELADA'", x0 + 14, 306, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
        L.texto(ctx, 'SELECT sin email', x0 + 14, 336, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
      });
      // Columna
      grilla(x0 + 420, y0, function (j) { return j === 0 || j === 3; }, function () { return true; }, 'Privilegio por columna', C, L.tramo(t, 0.66, 0.76));
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.84), function () {
        L.rectRed(ctx, x0 + 420, 260, 300, 120, 10); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'recorta solo columnas', x0 + 570, 270, { tam: 17, peso: 800, color: L.tono(C, -0.3) });
        L.texto(ctx, 'GRANT SELECT (id_dueno, nombre)', x0 + 434, 306, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
        L.texto(ctx, 'sin objeto nuevo', x0 + 434, 336, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
      });
      UJ.alfa(ctx, L.tramo(t, 0.86, 0.96), function () {
        L.rectRed(ctx, 40, 420, W - 80, 130, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, '¿Filtra filas o cruza tablas? → vista', W / 2, 438, { tam: 21, peso: 800 });
        UJ.rotulo(ctx, lz, '¿Solo columnas? → privilegio por columna', W / 2, 488, { tam: 21, peso: 800 });
      });
    }
  });
})();
