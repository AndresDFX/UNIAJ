/* Lo que dibuja el codigo de «El diagrama de actividad con decisiones en Mermaid»: inicio, dos
 * rombos con todas sus salidas rotuladas (Si / No), los pasos de cada camino y el fin. */
(function () {
  FP_ANIMADOR.registrar('dg-actividad', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var rombo = 'rombo';
      DG.nodo(ctx, lz, 230, 34, 130, 44, 'Inicio', 'redondo', { tam: 16 });
      DG.nodo(ctx, lz, 230, 112, 260, 50, 'La mascota llega a consulta', 'rect', { tam: 15 });
      DG.nodo(ctx, lz, 230, 222, 210, 110, 'Tiene cita\nprogramada?', rombo, { tam: 15 });
      DG.nodo(ctx, lz, 540, 222, 190, 110, 'Es urgencia?', rombo, { tam: 15 });
      DG.nodo(ctx, lz, 230, 365, 220, 50, 'Registrar consulta', 'rect', { tam: 15 });
      DG.nodo(ctx, lz, 540, 365, 220, 50, 'Crear cita de urgencia', 'rect', { tam: 15 });
      DG.nodo(ctx, lz, 230, 470, 240, 50, 'Emitir receta e insumos', 'rect', { tam: 15 });
      DG.nodo(ctx, lz, 690, 470, 190, 50, 'Agendar para otro dia', 'rect', { tam: 14 });
      DG.nodo(ctx, lz, 460, 590, 110, 44, 'Fin', 'redondo', { tam: 16 });
      DG.flecha(ctx, lz, [[230, 56], [230, 86]]);
      DG.flecha(ctx, lz, [[230, 137], [230, 166]]);
      DG.flecha(ctx, lz, [[230, 277], [230, 339]], { rotulo: 'Si', en: [230, 306] });
      DG.flecha(ctx, lz, [[335, 222], [444, 222]], { rotulo: 'No', en: [390, 222] });
      DG.flecha(ctx, lz, [[540, 277], [540, 339]], { rotulo: 'Si', en: [540, 306] });
      DG.flecha(ctx, lz, [[635, 222], [690, 222], [690, 444]], { rotulo: 'No', en: [690, 300] });
      DG.flecha(ctx, lz, [[430, 365], [341, 365]]);
      DG.flecha(ctx, lz, [[230, 390], [230, 444]]);
      DG.flecha(ctx, lz, [[230, 495], [230, 590], [404, 590]]);
      DG.flecha(ctx, lz, [[690, 495], [690, 590], [516, 590]]);
      DG.marca(ctx, lz, 380, 150, 1, 'Cada rombo: TODAS sus salidas rotuladas', 330);
    }
  });
})();
