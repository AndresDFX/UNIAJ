/* Lo que dibuja el codigo de «El ciclo de vida en Mermaid: mismas cajas, dos recorridos»: las
 * cinco fases de arriba abajo, el artefacto que pasa en cada flecha y la flecha punteada que
 * devuelve una solicitud nueva a Requisitos. */
(function () {
  FP_ANIMADOR.registrar('dg-ciclo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var fases = ['Requisitos', 'Diseno', 'Construccion', 'Pruebas', 'Operacion y\nmantenimiento'];
      var rot = ['RF-01 a RF-12 aprobados', 'Casos de uso + clases + mockups', 'Modulo ficha del paciente', 'Acta de aceptacion'];
      var cx = 300, w = 230, h = 62, y0 = 30, paso = 130;
      for (var i = 0; i < 5; i++) {
        var cy = y0 + h / 2 + i * paso;
        DG.nodo(ctx, lz, cx, cy, w, h, fases[i], 'rect', { tam: 17 });
        if (i < 4) {
          DG.flecha(ctx, lz, [[cx, cy + h / 2], [cx, cy + paso - h / 2 - 1]]);
          DG.etiqueta(ctx, lz, rot[i], cx + 18 + 120, cy + paso / 2, { tam: 15 });
        }
      }
      var yA = y0 + h / 2, yE = y0 + h / 2 + 4 * paso;
      DG.flecha(ctx, lz, [[cx - w / 2, yE], [70, yE], [70, yA], [cx - w / 2 - 1, yA]], { punteada: true });
      DG.etiqueta(ctx, lz, 'Solicitud:\nvacunacion\na domicilio', 70, (yA + yE) / 2, { tam: 14 });
    }
  });
})();
