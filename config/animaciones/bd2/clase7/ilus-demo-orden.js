/* Ilustracion: el script de la demo en sus cinco bloques, en el orden en que se proyecta, con lo
 * que cada bloque tiene que mostrar. Cifras reales de la siembra (PGlite). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo-orden', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El script de la demo, bloque por bloque', W / 2, 8, { tam: 23, peso: 800, color: A });
      var b = [
        ['0', 'Siembra y control', '18.187 PROGRAMADA · 9.095 ATENDIDA · 2.728 CANCELADA', L.tono(m.tinta, 0.3)],
        ['1', 'Línea base', 'las dos consultas: Seq Scan on cita y Seq Scan on mascota', A],
        ['2', 'Tres índices + ANALYZE', 'las MISMAS consultas: el plan nombra el índice usado', V],
        ['3', 'Orden de columnas', 'los dos compuestos, tres consultas y un DROP INDEX', C],
        ['4', 'Particionamiento', 'DDL, migración, reparto con tableoid y poda en el plan', A]
      ];
      for (var i = 0; i < b.length; i++) {
        var y = 52 + i * 106;
        L.rectRed(ctx, 20, y, W - 40, 92, 14); L.rellena(ctx, L.tono(b[i][3], 0.92), b[i][3], i === 2 ? 4 : 2);
        L.circulo(ctx, 62, y + 46, 26); L.rellena(ctx, b[i][3]);
        UJ.rotulo(ctx, lz, b[i][0], 62, y + 32, { tam: 26, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, b[i][1], 104, y + 14, { tam: 20, peso: 800, color: L.tono(b[i][3], -0.25), alinear: 'left' });
        UJ.rotulo(ctx, lz, b[i][2], 104, y + 50, { tam: 16, alinear: 'left', ancho: W - 150 });
        if (i < b.length - 1) L.flecha(ctx, 62, y + 92, 62, y + 104, L.tono(m.tinta, 0.4), 3, 1);
      }
      UJ.rotulo(ctx, lz, 'El bloque 2 es el corazón de la clase: no se recorta.', W / 2, 594, { tam: 18, peso: 800, color: V });
    }
  });
})();
