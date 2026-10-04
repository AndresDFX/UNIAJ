/* El insumo de la revision son seis piezas, y el criterio central es la trazabilidad: lo que
 * aparece en una tiene que reaparecer, con el mismo nombre, en la siguiente. */
(function () {
  FP_ANIMADOR.registrar('seis-piezas', {
    duracion: 5,
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var p = [['Context', 'accion'], ['Containers', 'accion'], ['Despliegue', 'accion'], ['Dockerfile', 'acento'], ['Workflow', 'acento'], ['Informe', 'gris']];
      var e = [];
      for (var i = 0; i < 6; i++) {
        var x = 20 + (i % 3) * 262, y = 30 + Math.floor(i / 3) * 170;
        e.push({ tipo: 'caja', x: x, y: y, w: 236, h: 120, t: p[i][0], color: p[i][1], tam: 24, en: 0.03 + i * 0.05 });
      }
      e.push({ tipo: 'flecha', de: [258, 90], a: [280, 90], en: 0.34 });
      e.push({ tipo: 'flecha', de: [520, 90], a: [542, 90], en: 0.36 });
      e.push({ tipo: 'texto', t: 'Trazabilidad: el mismo nombre, de una pieza a la siguiente.', x: 400, y: 345, tam: 22, ancho: 760, en: 0.4 });
      e.push({ tipo: 'chip', x: 138, y: 420, t: 'Pasarela de pagos', color: 'accion', en: 0.5 });
      e.push({ tipo: 'flecha', de: [240, 437], a: [360, 437], color: 'malva', punteada: true, en: 0.56 });
      e.push({ tipo: 'chip', x: 462, y: 420, t: 'no aparece', color: 'malva', en: 0.62 });
      e.push({ tipo: 'texto', t: 'Context → Containers: la cadena se rompió.', x: 400, y: 490, tam: 22, ancho: 760, color: 'malva', en: 0.68 });
      e.push({ tipo: 'texto', t: 'La revisión busca decisiones sin argumento, incoherencias y riesgos sin nombre.', x: 400, y: 560, tam: 21, ancho: 760, en: 0.86 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
