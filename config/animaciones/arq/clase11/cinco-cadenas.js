/* Las cinco preguntas de coherencia, en orden: cada una es una cadena entre dos artefactos. El
 * acta no es una nota: dice cuales de las cinco cadenas estan rotas. */
(function () {
  FP_ANIMADOR.registrar('cinco-cadenas', {
    duracion: 5,
    pasos: [0.6, 1],
    dibujar: function (ctx, t, lz) {
      var c = [['Containers', 'Despliegue', 'cada contenedor, mismo nombre'],
               ['Context', 'Containers', 'cada actor y sistema externo sigue'],
               ['STRIDE', 'Despliegue', 'cada amenaza, un control visible'],
               ['Costos', 'Containers', 'los mismos componentes'],
               ['Workflow', 'ejecución', 'corrió al menos una vez']];
      var e = [];
      for (var i = 0; i < 5; i++) {
        var y = 20 + i * 92, en = 0.04 + i * 0.1, rota = i === 0;
        e.push({ tipo: 'caja', x: 20, y: y, w: 170, h: 70, t: c[i][0], r: 10, tam: 20, en: en });
        e.push({ tipo: 'flecha', de: [195, y + 35], a: [265, y + 35], color: 'gris', en: en + 0.02 });
        e.push({ tipo: 'caja', x: 270, y: y, w: 170, h: 70, t: c[i][1], r: 10, tam: 20, en: en + 0.03 });
        e.push({ tipo: 'texto', t: c[i][2], x: 460, y: y + 22, tam: 19, alinear: 'left', ancho: 260, en: en + 0.04 });
        e.push({ tipo: 'sello', x: 760, y: y + 35, r: 20, ok: !rota, en: 0.62 + i * 0.04 });
      }
      e.push({ tipo: 'texto', t: 'El worker de avisos está en el Containers y en ninguna zona del Despliegue.', x: 400, y: 495, tam: 20, ancho: 760, color: 'malva', en: 0.84 });
      e.push({ tipo: 'texto', t: 'El acta dice qué cadenas están rotas, no una nota.', x: 400, y: 570, tam: 22, peso: 800, color: 'accion', ancho: 760, en: 0.9 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
