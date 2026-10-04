/* Sargable: el motor puede resolver el predicado navegando un indice. Una funcion sobre la
 * columna lo impide; reescribirlo sobre la columna desnuda lo devuelve. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('sargable', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.rotulo(ctx, lz, 'No sargable: función sobre la columna', 40, 30, { tam: 21, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0, 0.06) });
      UJ.codigo(ctx, lz, 40, 70, 650, "to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'", L.tramo(t, 0.04, 0.16), 17);
      UJ.codigo(ctx, lz, 40, 124, 650, "UPPER(c.estado) = 'PROGRAMADA'", L.tramo(t, 0.16, 0.24), 17);
      UJ.sello(ctx, lz, 732, 87, 20, false, L.tramo(t, 0.26, 0.32));
      UJ.sello(ctx, lz, 732, 141, 20, false, L.tramo(t, 0.28, 0.34));
      UJ.rotulo(ctx, lz, 'el índice guarda fecha_hora, no to_char(fecha_hora)', W / 2, 186, { tam: 17, peso: 500, ancho: W - 60, visible: L.tramo(t, 0.32, 0.4) });
      L.flecha(ctx, W / 2, 222, W / 2, 262, A, 5, L.tramo(t, 0.42, 0.5, 'frena'));
      UJ.rotulo(ctx, lz, 'Sargable: la columna desnuda, el cálculo al otro lado', 40, 276, { tam: 21, peso: 800, color: V, alinear: 'left', ancho: W - 80, visible: L.tramo(t, 0.48, 0.54) });
      UJ.codigo(ctx, lz, 40, 316, 650, "c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'", L.tramo(t, 0.52, 0.62), 17);
      UJ.codigo(ctx, lz, 40, 370, 650, "AND c.fecha_hora < TIMESTAMP '2026-03-11 00:00:00'", L.tramo(t, 0.6, 0.68), 17);
      UJ.codigo(ctx, lz, 40, 424, 650, "c.estado = 'PROGRAMADA'", L.tramo(t, 0.68, 0.74), 17);
      UJ.sello(ctx, lz, 732, 360, 20, true, L.tramo(t, 0.74, 0.8));
      UJ.sello(ctx, lz, 732, 441, 20, true, L.tramo(t, 0.76, 0.82));
      UJ.rotulo(ctx, lz, 'Mismo resultado; ahora el motor puede navegar un índice.', W / 2, 520,
                { tam: 21, ancho: W - 40, color: A, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
