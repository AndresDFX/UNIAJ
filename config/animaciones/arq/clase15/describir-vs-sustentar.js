/* Describir es decir que contiene un artefacto; sustentar es decir por que quedo asi y no de otra
 * forma, y que se acepto perder al elegirlo (el trade-off). */
(function () {
  FP_ANIMADOR.registrar('describir-vs-sustentar', {
    duracion: 5,
    pasos: [0.4, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 760, h: 150, t: 'Describir', s: '«Aquí está el contenedor de la API, aquí la base de datos.»', color: 'gris', tam: 26, tamSub: 21, en: 0.02 },
        { tipo: 'texto', t: 'una leyenda de imagen', x: 400, y: 195, tam: 20, color: 'malva', en: 0.16 },
        { tipo: 'caja', x: 20, y: 260, w: 760, h: 190, t: 'Sustentar', s: '«La base es gestionada aunque cuesta el doble, porque no podemos garantizar respaldos manuales: aceptamos más costo a cambio de no perder datos.»', tam: 26, tamSub: 20, en: 0.42 },
        { tipo: 'chip', x: 210, y: 480, t: 'por qué así', color: 'accion', en: 0.6 },
        { tipo: 'chip', x: 400, y: 480, t: 'y no de otra forma', color: 'acento', en: 0.66 },
        { tipo: 'chip', x: 600, y: 480, t: 'qué se perdió', color: 'malva', en: 0.72 },
        { tipo: 'texto', t: 'Un trade-off es lo que se sacrifica al decidir.', x: 400, y: 570, tam: 23, peso: 800, color: 'accion', ancho: 760, en: 0.86 }
      ]);
    }
  });
})();
