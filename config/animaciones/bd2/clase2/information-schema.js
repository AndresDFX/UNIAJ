/* La matriz en un documento es una intencion; consultada en el motor es un hecho:
 * information_schema.role_table_grants (rol, tabla, privilegio) y column_privileges (+ columna). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('information-schema', {
    duracion: 5,
    pasos: [0.24, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A;
      UJ.caja(ctx, lz, 40, 30, 300, 100, 'Documento', 'una intención', L.tono(m.tinta, 0.3), L.tramo(t, 0, 0.08));
      L.flecha(ctx, 346, 80, 454, 80, L.tono(m.tinta, 0.4), 4, L.tramo(t, 0.1, 0.18));
      UJ.caja(ctx, lz, 460, 30, 300, 100, 'Motor', 'un hecho consultable', V, L.tramo(t, 0.14, 0.22));
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.3), function () {
        L.rectRed(ctx, 40, 160, W - 80, 112, 10); L.rellena(ctx, L.tono(m.tinta, -0.55));
      });
      var q = ['SELECT grantee, table_name, privilege_type', 'FROM information_schema.role_table_grants', 'ORDER BY grantee, table_name, privilege_type;'];
      for (var i = 0; i < 3; i++)
        L.texto(ctx, q[i], 56, 172 + i * 32, { tam: 18, color: '#E8F4FA', letra: 'Consolas, monospace', visible: L.tramo(t, 0.28 + i * 0.06, 0.36 + i * 0.06) });
      var cab = ['grantee', 'table_name', 'privilege_type'], cx = [40, 290, 520];
      var filas = [['recepcion', 'cita', 'INSERT'], ['recepcion', 'cita', 'SELECT'], ['recepcion', 'cita', 'UPDATE'], ['recepcion', 'dueno', 'SELECT']];
      UJ.alfa(ctx, L.tramo(t, 0.48, 0.52), function () {
        L.rectRed(ctx, 40, 296, W - 80, 46, 10); L.rellena(ctx, A);
        for (var j = 0; j < 3; j++) L.texto(ctx, cab[j], cx[j] + 16, 308, { tam: 19, peso: 700, color: m.papel, letra: 'Consolas, monospace' });
      });
      for (var r = 0; r < 4; r++) {
        UJ.alfa(ctx, L.tramo(t, 0.52 + r * 0.03, 0.56 + r * 0.03), function () {
          var fy = 342 + r * 40;
          L.rectRed(ctx, 40, fy, W - 80, 40, 0); L.rellena(ctx, r % 2 ? L.tono(A, 0.94) : m.papel, L.tono(A, 0.6), 1);
          for (var j = 0; j < 3; j++) L.texto(ctx, filas[r][j], cx[j] + 16, fy + 9, { tam: 19, color: m.tinta, letra: 'Consolas, monospace' });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.82), function () {
        L.rectRed(ctx, 40, 530, W - 80, 80, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        L.texto(ctx, 'column_privileges', 60, 545, { tam: 19, peso: 700, color: L.tono(C, -0.35), letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, '+ column_name: prueba el privilegio por columna', 60, 575, { tam: 17, alinear: 'left', ancho: W - 120 });
      });
    }
  });
})();
