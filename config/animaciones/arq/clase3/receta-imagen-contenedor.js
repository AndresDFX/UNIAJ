/* Los cuatro terminos en su orden: el Dockerfile es la receta, `build` produce la imagen
 * (inmutable), `run` crea contenedores (instancias) y `push` la guarda en un registro. */
(function () {
  FP_ANIMADOR.registrar('receta-imagen-contenedor', {
    duracion: 5,
    // Pasos LOGICOS: 1) la receta: el Dockerfile, con build, produce la imagen (termina en 0.28);
    // 2) la instancia: run lanza muchos contenedores de la misma imagen, con su frase «una imagen,
    // muchos contenedores» (antes salia en el paso 3, junto al registro); 3) el registro: push
    // guarda la imagen donde se publica y se descarga.
    pasos: [0.31, 0.69, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1 · receta → imagen
        { tipo: 'caja', x: 20, y: 200, w: 190, h: 130, t: 'Dockerfile', s: 'la receta (texto)', color: 'gris', en: 0.02 },
        { tipo: 'flecha', de: [215, 265], a: [300, 265], r: 'build', en: 0.1 },
        { tipo: 'caja', x: 305, y: 190, w: 200, h: 150, t: 'Imagen', s: 'inmutable · solo lectura', lleno: true, en: 0.2 },
        // 2 · imagen → contenedores
        { tipo: 'flecha', de: [510, 230], a: [590, 110], r: 'run', dx: -30, dy: -20, en: 0.35 },
        { tipo: 'flecha', de: [510, 265], a: [590, 265], en: 0.38 },
        { tipo: 'flecha', de: [510, 300], a: [590, 420], en: 0.41 },
        { tipo: 'caja', x: 595, y: 60, w: 185, h: 90, t: 'Contenedor 1', s: 'en ejecución', color: 'sello', tam: 20, en: 0.44 },
        { tipo: 'caja', x: 595, y: 220, w: 185, h: 90, t: 'Contenedor 2', s: 'en ejecución', color: 'sello', tam: 20, en: 0.48 },
        { tipo: 'caja', x: 595, y: 380, w: 185, h: 90, t: 'Contenedor 3', s: 'en ejecución', color: 'sello', tam: 20, en: 0.52 },
        { tipo: 'texto', t: 'Una imagen, muchos contenedores.', x: 150, y: 50, tam: 24, peso: 800, color: 'accion', ancho: 270, en: 0.59 },
        // 3 · imagen → registro
        { tipo: 'flecha', de: [405, 345], a: [405, 455], r: 'push', dx: 45, dy: -12, en: 0.73 },
        { tipo: 'cilindro', x: 300, y: 460, w: 210, h: 130, t: 'Registro', s: 'guarda las imágenes', color: 'acento', en: 0.82 }
      ]);
    }
  });
})();
