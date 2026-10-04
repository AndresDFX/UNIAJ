/* Por que un secreto no se arregla borrandolo: la imagen esta hecha de capas, y el borrado es UNA
 * CAPA MAS encima; la de abajo sigue ahi. Lo mismo con Git. Lo que lo invalida es rotarlo. */
(function () {
  FP_ANIMADOR.registrar('secreto-en-capas', {
    duracion: 5,
    // Pasos LOGICOS: 1) la llave queda escrita en una capa de la imagen, 2) el borrado es una
    // capa mas encima y docker history sigue leyendo la de abajo, 3) el remedio: borrar el
    // commit no sirve (Git guarda historia), rotar si. La tacha sobre el texto se cambio por
    // un sello en la esquina: tapaba lo que habia que leer.
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Capas de la imagen', x: 30, y: 14, tam: 24, peso: 800, alinear: 'left', color: 'accion', en: 0 },
        { tipo: 'caja', x: 30, y: 280, w: 400, h: 70, t: 'FROM node:20-alpine', r: 8, tam: 20, en: 0.02 },
        { tipo: 'caja', x: 30, y: 200, w: 400, h: 70, t: 'ENV CORREO_API_KEY=sk_live…', color: 'malva', r: 8, tam: 20, en: 0.1 },
        { tipo: 'caja', x: 30, y: 120, w: 400, h: 70, t: 'RUN rm -f /app/.env', r: 8, tam: 20, en: 0.34 },
        { tipo: 'flecha', de: [470, 155], a: [440, 155], en: 0.38 },
        { tipo: 'texto', t: 'el borrado es UNA CAPA MÁS', x: 480, y: 142, tam: 20, alinear: 'left', ancho: 300, en: 0.4 },
        { tipo: 'flecha', de: [470, 235], a: [440, 235], color: 'malva', en: 0.46 },
        { tipo: 'texto', t: 'la llave sigue aquí: docker history la lee', x: 480, y: 210, tam: 20, alinear: 'left', ancho: 300, color: 'malva', en: 0.5 },
        { tipo: 'caja', x: 30, y: 410, w: 360, h: 100, t: 'Borrar el commit', s: 'sigue en el historial y en cada clon', color: 'gris', en: 0.66 },
        { tipo: 'sello', x: 380, y: 416, r: 24, ok: false, en: 0.72 },
        { tipo: 'caja', x: 420, y: 410, w: 360, h: 100, t: 'ROTAR la llave', s: 'una nueva, y la vieja deja de servir', lleno: true, en: 0.8 },
        { tipo: 'sello', x: 770, y: 416, r: 24, ok: true, en: 0.84 },
        { tipo: 'texto', t: 'Lo único que invalida una llave filtrada es rotarla.', x: 400, y: 560, tam: 23, peso: 800, color: 'accion', ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
