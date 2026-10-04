/* Ilustracion: los cinco indices de la clase, cada uno con sus columnas y la consulta que lo
 * justifica. Tres para medir y dos para el experimento del orden. Tamanos reales en la base
 * sembrada (pg_relation_size). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-cinco-indices', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Cada índice, con la consulta que lo justifica', W / 2, 8, { tam: 23, peso: 800, color: A, ancho: W - 30 });
      var f = [
        ['idx_cita_fecha_hora', 'cita (fecha_hora)', 'cualquier rango de fechas', '256 kB', A],
        ['idx_mascota_dueno', 'mascota (id_dueno)', 'las mascotas de un dueño', '104 kB', A],
        ['idx_cita_programada_fecha', "cita (fecha_hora) WHERE estado = 'PROGRAMADA'", 'la agenda del día de recepción', '168 kB', V],
        ['idx_cita_estado_fecha', 'cita (estado, fecha_hora)', 'estado por igualdad + rango', '368 kB', C],
        ['idx_cita_fecha_estado', 'cita (fecha_hora, estado)', 'el mismo par, en orden inverso', '360 kB', C]
      ];
      UJ.rotulo(ctx, lz, 'para medir', 30, 50, { tam: 15, peso: 800, color: A, alinear: 'left' });
      for (var i = 0; i < f.length; i++) {
        var y = 72 + i * 100 + (i >= 3 ? 26 : 0);
        if (i === 3) UJ.rotulo(ctx, lz, 'para el experimento del orden de columnas', 30, y - 24, { tam: 15, peso: 800, color: L.tono(C, -0.3), alinear: 'left' });
        L.rectRed(ctx, 20, y, W - 40, 88, 12); L.rellena(ctx, L.tono(f[i][4], 0.92), f[i][4], 2);
        L.texto(ctx, f[i][0], 36, y + 10, { tam: 19, peso: 700, color: L.tono(f[i][4], -0.25), letra: 'Consolas, monospace' });
        L.texto(ctx, f[i][1], 36, y + 40, { tam: 14, peso: 500, color: m.tinta, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, '→ ' + f[i][2], 36, y + 62, { tam: 15, peso: 600, alinear: 'left' });
        UJ.rotulo(ctx, lz, f[i][3], W - 40, y + 12, { tam: 16, peso: 800, alinear: 'right', color: L.tono(m.tinta, 0.2) });
      }
      UJ.rotulo(ctx, lz, 'La PK ya trae su índice; la FK no: por eso idx_mascota_dueno sí suma.', W / 2, 604, { tam: 16, peso: 700, ancho: W - 40 });
    }
  });
})();
