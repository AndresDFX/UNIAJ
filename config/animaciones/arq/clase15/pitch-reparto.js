/* El reparto del pitch de 5 a 8 minutos (convencion, no regla): problema, arquitectura, decision
 * principal con su trade-off, evidencia ejecutable, punto debil declarado y cierre. */
(function () {
  FP_ANIMADOR.registrar('pitch-reparto', {
    duracion: 5,
    pasos: [0.6, 1],
    dibujar: function (ctx, t, lz) {
      var b = [['Problema y dominio', 60, '45-60 s', 'gris'], ['Arquitectura', 90, '90 s', 'accion'], ['Decisión y trade-off', 90, '90 s', 'malva'],
               ['Evidencia ejecutable', 90, '60-90 s', 'acento'], ['Punto débil declarado', 45, '45 s', 'malva'], ['Cierre', 30, '30 s', 'gris']];
      var e = [{ tipo: 'texto', t: 'Pitch de 5 a 8 minutos', x: 400, y: 14, tam: 24, peso: 800, color: 'accion', en: 0 }];
      for (var i = 0; i < b.length; i++) {
        e.push({ tipo: 'barra', x: 290, y: 75 + i * 64, w: 400, h: 38, valor: b[i][1] / 90, t: b[i][0], r: b[i][2], color: b[i][3], en: 0.04 + i * 0.08, tam: 19 });
      }
      e.push({ tipo: 'texto', t: 'Suma: entre 6 y 7 minutos, con margen.', x: 400, y: 470, tam: 22, ancho: 740, en: 0.62 });
      e.push({ tipo: 'texto', t: 'Una idea por diapositiva, ocho como máximo.', x: 400, y: 530, tam: 22, ancho: 740, peso: 700, color: 'accion', en: 0.74 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
