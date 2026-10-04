/* Las cuatro diferencias que mas cuestan, de Oracle a PostgreSQL, como contraste. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('oracle-postgres', {
    duracion: 4.6,
    pasos: [0.5, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Oracle', 190, 20, { tam: 26, peso: 800, color: L.tono(m.tinta, 0.35), visible: L.tramo(t, 0, 0.05) });
      UJ.rotulo(ctx, lz, 'PostgreSQL (hoy)', 600, 20, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      var par = [['IS', 'AS'], ['VARCHAR2 · NUMBER', 'TEXT · INT'], ['RAISE_APPLICATION_ERROR', 'RAISE EXCEPTION'], ['/ al final', 'error de sintaxis']];
      for (var i = 0; i < 4; i++) {
        var y = 80 + i * 100, a = L.tramo(t, 0.06 + i * 0.1, 0.12 + i * 0.1), b = L.tramo(t, 0.1 + i * 0.1, 0.18 + i * 0.1, 'frena');
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 30, y, 320, 70, 12); L.rellena(ctx, L.tono(m.tinta, 0.88), L.tono(m.tinta, 0.4), 2);
          L.texto(ctx, par[i][0], 190, y + 22, { tam: 19, peso: 700, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace', ancho: 300 });
        });
        L.flecha(ctx, 356, y + 35, 440, y + 35, A, 4, b);
        UJ.alfa(ctx, b, function () {
          L.rectRed(ctx, 446, y, 320, 70, 12); L.rellena(ctx, L.tono(i === 3 ? R : A, 0.88), i === 3 ? R : A, 2);
          L.texto(ctx, par[i][1], 606, y + 22, { tam: 19, peso: 700, color: i === 3 ? R : A, alinear: 'center', letra: 'Consolas, monospace', ancho: 300 });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.55, 0.7), function () {
        L.rectRed(ctx, 40, 500, W - 80, 100, 14); L.rellena(ctx, L.tono(m.sello || C, 0.6), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Fuente de verdad: el archivo .sql en la carpeta,', W / 2, 518, { tam: 21, peso: 700, ancho: W - 120 });
        UJ.rotulo(ctx, lz, 'nunca la pestaña del navegador.', W / 2, 554, { tam: 21, peso: 700, ancho: W - 120 });
      });
    }
  });
})();
