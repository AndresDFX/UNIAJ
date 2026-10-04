/* Los tres nombres de almacenamiento, por la caracteristica del dato: relacional (registros que se
 * cruzan con consultas y transacciones), bloque (disco crudo de una sola instancia) y objetos
 * (archivos por HTTP con una clave). */
(function () {
  FP_ANIMADOR.registrar('tres-almacenamientos', {
    duracion: 5,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'cilindro', x: 30, y: 40, w: 230, h: 170, t: 'RELACIONAL', s: 'motor de base de datos', color: 'accion', tam: 22, en: 0.02 },
        { tipo: 'texto', t: 'registros que se cruzan con consultas y transacciones', x: 145, y: 230, tam: 19, ancho: 230, en: 0.08 },
        { tipo: 'caja', x: 285, y: 40, w: 230, h: 170, t: 'BLOQUE', s: 'disco crudo que el SO formatea y monta', color: 'acento', tam: 22, en: 0.32 },
        { tipo: 'texto', t: 'una sola instancia a la vez; debajo del volumen de un contenedor', x: 400, y: 230, tam: 19, ancho: 230, en: 0.38 },
        { tipo: 'caja', x: 540, y: 40, w: 230, h: 170, t: 'OBJETOS', s: 'archivos con una clave, por HTTP', color: 'malva', tam: 22, en: 0.62 },
        { tipo: 'texto', t: 'barato y durable; no se monta como disco', x: 655, y: 230, tam: 19, ancho: 230, en: 0.68 },
        { tipo: 'chip', x: 145, y: 320, t: 'turnos y clientes', color: 'accion', en: 0.8 },
        { tipo: 'chip', x: 400, y: 320, t: 'temporales, caché', color: 'acento', en: 0.84 },
        { tipo: 'chip', x: 655, y: 320, t: 'fotos, adjuntos, respaldos', color: 'malva', en: 0.88 },
        { tipo: 'texto', t: 'Se decide por la característica del dato, no por costumbre.', x: 400, y: 420, tam: 23, peso: 800, color: 'accion', ancho: 740, en: 0.9 }
      ]);
    }
  });
})();
