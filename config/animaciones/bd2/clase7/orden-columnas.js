/* Experimento del orden: (estado, fecha_hora) contra (fecha_hora, estado), medidos con tres
 * consultas. Q1 igualdad + rango -> estado_fecha; Q2 solo rango -> fecha_estado; Q3 solo estado
 * -> fecha_estado no sirve. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('orden-columnas', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A, R = m.malva || '#A02030';
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.texto(ctx, 'idx_cita_estado_fecha', 450, 40, { tam: 15, peso: 700, color: A, alinear: 'center', letra: 'Consolas, monospace' });
        L.texto(ctx, '(estado, fecha_hora)', 450, 66, { tam: 16, peso: 500, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
        L.texto(ctx, 'idx_cita_fecha_estado', 680, 40, { tam: 15, peso: 700, color: C, alinear: 'center', letra: 'Consolas, monospace' });
        L.texto(ctx, '(fecha_hora, estado)', 680, 66, { tam: 16, peso: 500, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
      });
      // [nombre, filtro, gana a, gana b (1 si, 0 sirve menos, -1 no sirve)]
      var q = [['Q1', 'estado = … AND rango de fecha', 1, 0, 0.12], ['Q2', 'solo rango de fecha_hora', 0, 1, 0.36], ['Q3', 'solo estado = …', 1, -1, 0.6]];
      for (var i = 0; i < 3; i++) {
        var y = 120 + i * 120, a = L.tramo(t, q[i][4], q[i][4] + 0.08), b = L.tramo(t, q[i][4] + 0.08, q[i][4] + 0.16);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 20, y, W - 40, 100, 14); L.rellena(ctx, i % 2 ? L.tono(A, 0.93) : m.papel, L.tono(m.tinta, 0.6), 2);
          UJ.rotulo(ctx, lz, q[i][0], 60, y + 34, { tam: 26, peso: 800, color: A });
          UJ.rotulo(ctx, lz, q[i][1], 110, y + 38, { tam: 18, peso: 600, alinear: 'left', ancho: 250 });
        });
        [[450, q[i][2]], [680, q[i][3]]].forEach(function (c) {
          if (c[1] === 1) UJ.sello(ctx, lz, c[0], y + 50, 26, true, b);
          else if (c[1] === -1) UJ.sello(ctx, lz, c[0], y + 50, 26, false, b);
          else UJ.rotulo(ctx, lz, 'menos eficaz', c[0], y + 38, { tam: 17, peso: 600, color: L.tono(m.tinta, 0.35), visible: b });
        });
      }
      UJ.rotulo(ctx, lz, 'Igualdad en la columna líder, el rango al final.', W / 2, 500, { tam: 22, peso: 800, color: A, ancho: W - 40, visible: L.tramo(t, 0.84, 0.94) });
      UJ.rotulo(ctx, lz, 'Entre medición y medición: ANALYZE cita; y DROP INDEX al terminar.', W / 2, 546, { tam: 18, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
