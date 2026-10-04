/* Ilustracion: el indice parcial frente al completo en la agenda del 2026-03-10. El completo
 * encuentra las 150 citas del dia y debe ir a la tabla a descartar 59; el parcial solo contiene
 * PROGRAMADA y encuentra directamente las 91. Mas chico (168 kB contra 256 kB) y solo sirve si la
 * consulta trae la misma condicion. Cifras reales de PGlite. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-parcial-gana', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, "La agenda del 2026-03-10 (estado = 'PROGRAMADA')", W / 2, 8, { tam: 22, peso: 800, color: A, ancho: W - 30 });
      function panel(x, col, nombre, def, n, extra, kb) {
        L.rectRed(ctx, x, 46, 370, 344, 14); L.rellena(ctx, L.tono(col, 0.92), col, 2);
        L.texto(ctx, nombre, x + 185, 58, { tam: 17, peso: 700, color: L.tono(col, -0.25), alinear: 'center', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, def, x + 185, 86, { tam: 14, ancho: 340 });
        UJ.rotulo(ctx, lz, n, x + 185, 132, { tam: 44, peso: 800, color: col });
        UJ.rotulo(ctx, lz, 'entradas encontradas', x + 185, 190, { tam: 15 });
        UJ.rotulo(ctx, lz, extra, x + 185, 230, { tam: 16, peso: 700, ancho: 330 });
        UJ.rotulo(ctx, lz, 'tamaño del índice: ' + kb, x + 185, 340, { tam: 15, peso: 700, color: L.tono(m.tinta, 0.2) });
      }
      panel(16, A, 'idx_cita_fecha_hora', 'todas las citas: 30.010 entradas', '150', 'va a la tabla y descarta 59 que no están programadas', '256 kB');
      panel(414, V, 'idx_cita_programada_fecha', 'solo PROGRAMADA: 18.187 entradas', '91', 'todas sirven: ya sabe que cumplen el estado', '168 kB');
      UJ.sello(ctx, lz, 762, 52, 22, true, 1);
      L.rectRed(ctx, 16, 404, W - 32, 92, 12); L.rellena(ctx, L.tono(V, 0.9), V, 2);
      UJ.rotulo(ctx, lz, 'Plan real: Bitmap Index Scan on idx_cita_programada_fecha (rows=91)', W / 2, 414, { tam: 16, peso: 700, ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'si en otra corrida gana el completo, se reporta lo que se vio', W / 2, 450, { tam: 15, ancho: W - 60 });
      L.rectRed(ctx, 16, 510, W - 32, 110, 12); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.rotulo(ctx, lz, 'La condición: la consulta tiene que traer el mismo filtro', W / 2, 520, { tam: 18, peso: 800, color: R, ancho: W - 60 });
      UJ.rotulo(ctx, lz, "sin «estado = 'PROGRAMADA'» el parcial no se puede usar: le faltan las atendidas y las canceladas", W / 2, 554, { tam: 15, ancho: W - 70 });
    }
  });
})();
