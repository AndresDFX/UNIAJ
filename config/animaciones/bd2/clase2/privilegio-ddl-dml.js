/* Dos cosas que se mezclan: privilegios de objeto (se escriben con GRANT) y atributos de rol (van
 * en CREATE/ALTER ROLE). Y la frontera: DDL cambia la estructura, DML lee o cambia los datos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('privilegio-ddl-dml', {
    duracion: 5,
    pasos: [0.46, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      function columna(x, col, titulo, se, items, t0) {
        UJ.alfa(ctx, L.tramo(t, t0, t0 + 0.08), function () {
          L.rectRed(ctx, x, 24, 360, 64, 12); L.rellena(ctx, col);
          UJ.rotulo(ctx, lz, titulo, x + 180, 42, { tam: 21, peso: 800, color: m.papel });
          UJ.rotulo(ctx, lz, se, x + 180, 98, { tam: 17, peso: 600, color: L.tono(col, -0.2) });
        });
        for (var i = 0; i < items.length; i++) {
          UJ.alfa(ctx, L.tramo(t, t0 + 0.08 + i * 0.04, t0 + 0.14 + i * 0.04), function () {
            L.rectRed(ctx, x + 60 + (i % 2) * 125, 136 + Math.floor(i / 2) * 50, 115, 40, 20); L.rellena(ctx, L.tono(col, 0.88), col, 2);
            L.texto(ctx, items[i], x + 117 + (i % 2) * 125, 145 + Math.floor(i / 2) * 50, { tam: 15, peso: 700, color: col, alinear: 'center', letra: 'Consolas, monospace' });
          });
        }
      }
      columna(20, A, 'Privilegios de objeto', 'se otorgan con GRANT', ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'TRUNCATE', 'REFERENCES', 'TRIGGER'], 0);
      columna(420, C, 'Atributos de rol', 'en CREATE / ALTER ROLE', ['LOGIN', 'CREATEDB', 'CREATEROLE', 'SUPERUSER'], 0.2);
      // DDL / DML
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.6), function () {
        L.trazo(ctx, [[W / 2, 360], [W / 2, 510]], 1, L.tono(m.tinta, 0.5), 3);
        UJ.rotulo(ctx, lz, 'DDL', 210, 370, { tam: 28, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'cambia la estructura', 210, 412, { tam: 18 });
        UJ.rotulo(ctx, lz, 'DML', 590, 370, { tam: 28, peso: 800, color: C });
        UJ.rotulo(ctx, lz, 'lee o cambia los datos', 590, 412, { tam: 18 });
      });
      UJ.codigo(ctx, lz, 40, 460, 340, 'CREATE · ALTER · DROP · TRUNCATE', L.tramo(t, 0.62, 0.76), 16);
      UJ.codigo(ctx, lz, 420, 460, 340, 'SELECT · INSERT · UPDATE · DELETE', L.tramo(t, 0.72, 0.86), 16);
      UJ.rotulo(ctx, lz, 'quien opera datos no necesita DDL', W / 2, 550, { tam: 20, peso: 700, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
