/* Lo que dibuja el codigo de «El mapa de dominio en Mermaid»: los actores de la clinica, dos
 * capacidades del sistema y el laboratorio externo, con sus tres flechas rotuladas. */
(function () {
  FP_ANIMADOR.registrar('dg-mapa-dominio', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      DG.grupo(ctx, lz, 20, 150, 210, 330, 'Clinica veterinaria');
      DG.grupo(ctx, lz, 300, 150, 260, 330, 'El sistema de la clinica');
      DG.nodo(ctx, lz, 125, 250, 170, 56, 'Recepcionista', 'redondo');
      DG.nodo(ctx, lz, 125, 390, 170, 56, 'Veterinario', 'redondo');
      DG.nodo(ctx, lz, 430, 250, 200, 56, 'Agendar cita', 'rect');
      DG.nodo(ctx, lz, 430, 390, 200, 56, 'Consultar\nexpediente', 'rect');
      DG.nodo(ctx, lz, 690, 390, 170, 56, 'Laboratorio\nexterno', 'rect');
      DG.flecha(ctx, lz, [[210, 250], [328, 250]], { rotulo: 'agenda', en: [269, 250] });
      DG.flecha(ctx, lz, [[210, 390], [328, 390]], { rotulo: 'consulta', en: [269, 390] });
      DG.flecha(ctx, lz, [[530, 390], [603, 390]], { rotulo: 'pide examen', en: [567, 362] });
    }
  });
})();
