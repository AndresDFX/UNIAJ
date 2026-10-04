/* Los cuatro terminos en su orden: el Dockerfile es la receta, `build` produce la imagen
 * (inmutable), `run` crea contenedores (instancias) y `push` la guarda en un registro. */
(function () {
  FP_ANIMADOR.registrar('receta-imagen-contenedor', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 200, w: 190, h: 130, t: 'Dockerfile', s: 'la receta (texto)', color: 'gris', en: 0.02 },
        { tipo: 'flecha', de: [215, 265], a: [300, 265], r: 'build', en: 0.14 },
        { tipo: 'caja', x: 305, y: 190, w: 200, h: 150, t: 'Imagen', s: 'inmutable · solo lectura', lleno: true, en: 0.22 },
        { tipo: 'flecha', de: [510, 230], a: [590, 110], r: 'run', dx: -30, dy: -20, en: 0.36 },
        { tipo: 'flecha', de: [510, 265], a: [590, 265], en: 0.4 },
        { tipo: 'flecha', de: [510, 300], a: [590, 420], en: 0.44 },
        { tipo: 'caja', x: 595, y: 60, w: 185, h: 90, t: 'Contenedor 1', s: 'en ejecución', color: 'sello', tam: 20, en: 0.46 },
        { tipo: 'caja', x: 595, y: 220, w: 185, h: 90, t: 'Contenedor 2', s: 'en ejecución', color: 'sello', tam: 20, en: 0.5 },
        { tipo: 'caja', x: 595, y: 380, w: 185, h: 90, t: 'Contenedor 3', s: 'en ejecución', color: 'sello', tam: 20, en: 0.54 },
        { tipo: 'flecha', de: [405, 345], a: [405, 455], r: 'push', dx: 45, dy: -12, en: 0.68 },
        { tipo: 'cilindro', x: 300, y: 460, w: 210, h: 130, t: 'Registro', s: 'guarda las imágenes', color: 'acento', en: 0.74 },
        { tipo: 'texto', t: 'Una imagen, muchos contenedores.', x: 150, y: 50, tam: 24, peso: 800, color: 'accion', ancho: 270, en: 0.88 }
      ]);
    }
  });
})();
