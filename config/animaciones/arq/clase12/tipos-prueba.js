/* Los tipos de prueba por la forma de la carga en el tiempo: carga (lo esperado), estres (sube
 * hasta que se degrada), pico (subida subita) y resistencia o soak (moderada durante horas). */
(function () {
  FP_ANIMADOR.registrar('tipos-prueba', {
    duracion: 5,
    // Pasos LOGICOS: un tipo de prueba por paso, cada uno con su forma de carga y su pregunta:
    // 1) carga, 2) estres, 3) pico, 4) resistencia.
    pasos: [0.25, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      function panel(x, y, tit, preg, pts, color, en) {
        var w = 360, h = 140, P = pts.map(function (p) { return [x + 20 + p[0] * (w - 40), y + h - 10 - p[1] * (h - 50)]; });
        return [
          { tipo: 'caja', x: x, y: y, w: w, h: h + 95, t: '', color: color, en: en },
          { tipo: 'texto', t: tit, x: x + 18, y: y + 12, tam: 22, peso: 800, alinear: 'left', color: color, en: en },
          { tipo: 'linea', pts: P, color: color, grosor: 4, en: en + 0.02 },
          { tipo: 'texto', t: preg, x: x + w / 2, y: y + h + 12, tam: 18, ancho: w - 30, en: en + 0.06 }
        ];
      }
      var e = [].concat(
        panel(20, 20, 'Carga', '¿cumple el objetivo con lo esperado?', [[0, 0.1], [0.15, 0.55], [1, 0.55]], 'accion', 0.02),
        panel(420, 20, 'Estrés', '¿cuál es el máximo y cómo falla?', [[0, 0.05], [0.8, 0.95], [0.85, 0.3], [1, 0.25]], 'malva', 0.26),
        panel(20, 300, 'Pico', '¿reacciona a tiempo a la subida súbita?', [[0, 0.2], [0.4, 0.2], [0.45, 0.95], [0.6, 0.95], [0.65, 0.2], [1, 0.2]], 'acento', 0.51),
        panel(420, 300, 'Resistencia', '¿hay fugas tras horas de carga moderada?', [[0, 0.1], [0.05, 0.45], [1, 0.45]], 'gris', 0.76)
      );
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
