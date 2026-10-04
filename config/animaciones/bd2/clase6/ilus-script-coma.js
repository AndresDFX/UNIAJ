/* Ilustracion: lo que hay que mirar en el script de la clase antes y durante la medicion. Los
 * conteos de control, el peligro aritmetico de la coma (producto cartesiano), que JOIN ... ON no
 * acelera pero hace visible el ON faltante, y que LIMIT 50 no evita ordenar las 91. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-script-coma', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      function tarjeta(x, y, col, titulo, cuerpo) {
        L.rectRed(ctx, x, y, 376, 284, 14); L.rellena(ctx, L.tono(col, 0.92), col, 2);
        UJ.rotulo(ctx, lz, titulo, x + 188, y + 12, { tam: 19, peso: 800, color: L.tono(col, -0.2), ancho: 350 });
        cuerpo(x, y);
      }
      // 1 · control
      tarjeta(16, 16, A, '1 · Control, antes de tocar nada', function (x, y) {
        UJ.rotulo(ctx, lz, '30.010 citas', x + 188, y + 60, { tam: 30, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'el 2026-03-10:', x + 188, y + 118, { tam: 17 });
        var e = [['PROGRAMADA', '91'], ['ATENDIDA', '45'], ['CANCELADA', '14']];
        for (var i = 0; i < 3; i++) {
          L.texto(ctx, e[i][0], x + 60, y + 154 + i * 36, { tam: 16, peso: 600, color: m.tinta, letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, e[i][1], x + 300, y + 152 + i * 36, { tam: 20, peso: 800, color: A });
        }
      });
      // 2 · la coma
      tarjeta(408, 16, R, '2 · La coma: si falta una condición', function (x, y) {
        UJ.codigo(ctx, lz, x + 14, y + 56, 348, 'FROM cita c, mascota m', 1, 16);
        UJ.rotulo(ctx, lz, 'sin c.id_mascota = m.id_mascota', x + 188, y + 104, { tam: 16 });
        UJ.rotulo(ctx, lz, '30.010 × 5.008', x + 188, y + 146, { tam: 28, peso: 800, color: R });
        UJ.rotulo(ctx, lz, '≈ 150 millones de filas', x + 188, y + 190, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'no da error: el motor las produce todas', x + 188, y + 236, { tam: 16, peso: 700 });
      });
      // 3 · JOIN ... ON
      tarjeta(16, 316, V, '3 · JOIN … ON', function (x, y) {
        UJ.codigo(ctx, lz, x + 14, y + 56, 348, 'JOIN mascota m ON m.id_mascota = …', 1, 15);
        UJ.rotulo(ctx, lz, 'el mismo plan que la coma: no acelera', x + 188, y + 108, { tam: 17, peso: 700, ancho: 340 });
        UJ.rotulo(ctx, lz, 'si falta el ON, es un error de sintaxis: el olvido salta a la vista', x + 188, y + 160, { tam: 16, ancho: 340 });
        UJ.sello(ctx, lz, x + 188, y + 244, 20, true, 1);
      });
      // 4 · LIMIT 50
      tarjeta(408, 316, C, '4 · ORDER BY … LIMIT 50', function (x, y) {
        UJ.rotulo(ctx, lz, 'Sin un índice que ya venga ordenado:', x + 188, y + 60, { tam: 17, ancho: 340 });
        UJ.rotulo(ctx, lz, 'lee las 30.010, encuentra las 91, las ordena', x + 188, y + 100, { tam: 17, peso: 700, ancho: 340 });
        UJ.rotulo(ctx, lz, 'y recién ahí entrega 50', x + 188, y + 152, { tam: 17, peso: 700, ancho: 340 });
        UJ.rotulo(ctx, lz, 'el LIMIT no salva la consulta', x + 188, y + 220, { tam: 18, peso: 800, color: L.tono(C, -0.35), ancho: 340 });
      });
    }
  });
})();
