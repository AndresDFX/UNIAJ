/* Abortar o informar: misma regla de negocio, dos contratos. sp_facturar aborta con RAISE cuando
 * no alcanza; fn_descontar_stock devuelve BOOLEAN (false si no alcanza) y solo lanza excepcion
 * ante un dato invalido (cantidad no positiva). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('abortar-o-informar', {
    duracion: 5,
    // Pasos LOGICOS: 1) la misma regla y el contrato que aborta; 2) el contrato que informa;
    // 3) las cuatro llamadas reales y lo que devuelve cada una.
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.rectRed(ctx, 150, 20, 500, 90, 14); L.rellena(ctx, L.tono(m.tinta, 0.92), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'La misma regla', 400, 30, { tam: 20, peso: 800 });
        L.texto(ctx, 'UPDATE ... AND stock >= cantidad', 400, 66, { tam: 18, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
      });
      L.flecha(ctx, 300, 112, 200, 160, L.tono(m.tinta, 0.4), 3, L.tramo(t, 0.1, 0.18));
      L.flecha(ctx, 500, 112, 600, 160, L.tono(m.tinta, 0.4), 3, L.tramo(t, 0.36, 0.44));
      // Abortar
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.22), function () {
        L.rectRed(ctx, 30, 170, 350, 290, 16); L.rellena(ctx, L.tono(R, 0.93), R, 2);
        UJ.rotulo(ctx, lz, 'Abortar', 205, 184, { tam: 26, peso: 800, color: R });
        L.texto(ctx, 'sp_facturar', 205, 226, { tam: 19, peso: 700, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, '0 filas →', 205, 280, { tam: 19 });
        UJ.codigo(ctx, lz, 50, 312, 310, 'RAISE EXCEPTION', 1, 18);
        UJ.rotulo(ctx, lz, 'se deshace toda la factura', 205, 388, { tam: 18, ancho: 320 });
      });
      // Informar
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.46), function () {
        L.rectRed(ctx, 420, 170, 350, 290, 16); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Informar', 595, 184, { tam: 26, peso: 800, color: L.tono(C, -0.35) });
        L.texto(ctx, 'fn_descontar_stock', 595, 226, { tam: 19, peso: 700, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'RETURNS BOOLEAN', 595, 262, { tam: 18, peso: 700 });
        UJ.codigo(ctx, lz, 440, 312, 310, 'RETURN v_filas = 1;', 1, 18);
        UJ.rotulo(ctx, lz, 'no alcanza → false, sin excepción; el llamador decide', 595, 376, { tam: 18, ancho: 320 });
      });
      // Tres llamadas
      var casos = [
        ['fn_descontar_stock(5, 3)', 'true: hay 8, quedan 5', V],
        ['fn_descontar_stock(2, 10)', 'false: hay 3, no alcanza', C],
        ['fn_descontar_stock(2, 3)', 'true: pide justo lo que queda', V],
        ['fn_descontar_stock(5, 0)', 'ERROR: cantidad no positiva', R]
      ];
      for (var i = 0; i < 4; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.72 + i * 0.06, 0.76 + i * 0.06), function () {
          L.texto(ctx, casos[i][0], 40, 474 + i * 40, { tam: 18, peso: 600, color: m.tinta, letra: 'Consolas, monospace' });
          L.texto(ctx, '→ ' + casos[i][1], 340, 474 + i * 40, { tam: 18, peso: 800, color: casos[i][2], letra: lz.letra });
        });
      }
    }
  });
})();
