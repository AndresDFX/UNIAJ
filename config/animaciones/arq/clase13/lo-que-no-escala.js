/* Lo que NO escala: la base relacional tiene un unico escritor. Y la aritmetica que la tumba: 6
 * instancias x 20 conexiones = 120, contra una base pequena que admite del orden de 100. Las replicas
 * de lectura ayudan, con retraso de replicacion. */
(function () {
  FP_ANIMADOR.registrar('lo-que-no-escala', {
    duracion: 5,
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var e = [];
      for (var i = 0; i < 6; i++) {
        e.push({ tipo: 'caja', x: 20 + i * 128, y: 30, w: 112, h: 80, t: 'API', s: '20 conex.', tam: 19, tamSub: 15, en: 0.03 + i * 0.04 });
        e.push({ tipo: 'flecha', de: [76 + i * 128, 115], a: [400, 230], color: 'malva', grosor: 2, en: 0.08 + i * 0.04 });
      }
      e.push({ tipo: 'cilindro', x: 290, y: 235, w: 220, h: 130, t: 'Base primaria', s: 'un solo escritor', color: 'malva', en: 0.04 });
      e.push({ tipo: 'chip', x: 400, y: 380, t: '6 × 20 = 120 conexiones · admite ≈ 100', color: 'malva', en: 0.36 });
      e.push({ tipo: 'texto', t: 'Escalar la API tumba la base.', x: 400, y: 430, tam: 23, peso: 800, color: 'malva', en: 0.44 });
      e.push({ tipo: 'cilindro', x: 600, y: 230, w: 170, h: 120, t: 'Réplica de lectura', color: 'acento', tam: 18, en: 0.72 });
      e.push({ tipo: 'flecha', de: [515, 290], a: [597, 290], r: 'retraso', dy: -30, color: 'acento', en: 0.76 });
      e.push({ tipo: 'texto', t: 'Lees de la réplica justo después de guardar y el dato aún no está.', x: 400, y: 500, tam: 20, ancho: 740, en: 0.82 });
      e.push({ tipo: 'texto', t: 'Declararlo en el informe es una respuesta correcta, no una debilidad.', x: 400, y: 570, tam: 21, ancho: 740, peso: 700, color: 'accion', en: 0.9 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
