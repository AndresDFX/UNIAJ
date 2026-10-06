/* Lo que dibuja el codigo de «El diagrama de casos de uso en Mermaid»: los dos actores fuera del
 * limite del sistema, los cuatro casos dentro, sus asociaciones y el «include» punteado de
 * Agendar cita hacia Validar disponibilidad. */
(function () {
  FP_ANIMADOR.registrar('dg-casos-uso', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      DG.grupo(ctx, lz, 210, 30, 570, 580, 'Sistema de la clinica', { tam: 18 });
      UJ.monigote(ctx, lz, 90, 140, 90, 'Recepcionista', '#1A2B3C');
      UJ.monigote(ctx, lz, 90, 420, 90, 'Veterinario', '#1A2B3C');
      var cu = { cu1: [380, 150], cu3: [380, 330], cu2: [380, 510], cu4: [665, 330] };
      UJ.elipse(ctx, lz, cu.cu1[0], cu.cu1[1], 120, 52, 'CU-01 Registrar mascota', '#095292', 1, { tam: 17 });
      UJ.elipse(ctx, lz, cu.cu3[0], cu.cu3[1], 120, 52, 'CU-04 Agendar cita', '#095292', 1, { tam: 17 });
      UJ.elipse(ctx, lz, cu.cu2[0], cu.cu2[1], 120, 52, 'CU-02 Buscar expediente', '#095292', 1, { tam: 17 });
      UJ.elipse(ctx, lz, cu.cu4[0], cu.cu4[1], 100, 52, 'Validar disponibilidad', '#095292', 1, { tam: 17 });
      DG.flecha(ctx, lz, [[125, 175], [258, 155]]);
      DG.flecha(ctx, lz, [[125, 185], [266, 312]]);
      DG.flecha(ctx, lz, [[125, 465], [262, 505]]);
      DG.flecha(ctx, lz, [[500, 330], [563, 330]], { punteada: true, abierta: true });
      DG.etiqueta(ctx, lz, '«include»', 532, 292, { tam: 15 });
      DG.marca(ctx, lz, 560, 200, 1, 'include: agendar SIEMPRE valida', 190);
    }
  });
})();
