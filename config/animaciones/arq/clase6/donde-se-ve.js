/* Cada amenaza en tres columnas: amenaza, control y donde se ve. La tercera solo admite una CAJA o
 * una FLECHA del diagrama, con su nombre exacto: un nombre de archivo no cierra la fila. */
(function () {
  FP_ANIMADOR.registrar('donde-se-ve', {
    duracion: 5,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 20, w: 240, h: 60, t: 'Amenaza', lleno: true, r: 8, tam: 21, en: 0 },
        { tipo: 'caja', x: 280, y: 20, w: 240, h: 60, t: 'Control', lleno: true, r: 8, tam: 21, en: 0.03 },
        { tipo: 'caja', x: 540, y: 20, w: 240, h: 60, t: 'Dónde se ve', color: 'malva', lleno: true, r: 8, tam: 21, en: 0.06 },
        { tipo: 'caja', x: 20, y: 95, w: 240, h: 110, t: 'Spoofing con token robado', r: 8, tam: 19, color: 'gris', en: 0.1 },
        { tipo: 'caja', x: 280, y: 95, w: 240, h: 110, t: 'HTTPS y el id sale del token', r: 8, tam: 19, color: 'gris', en: 0.14 },
        { tipo: 'caja', x: 540, y: 95, w: 240, h: 110, t: 'flecha App web → API de turnos', r: 8, tam: 19, color: 'accion', en: 0.2 },
        { tipo: 'sello', x: 760, y: 100, r: 22, ok: true, en: 0.28 },
        { tipo: 'caja', x: 20, y: 220, w: 240, h: 110, t: 'Llave filtrada en la imagen', r: 8, tam: 19, color: 'gris', en: 0.44 },
        { tipo: 'caja', x: 280, y: 220, w: 240, h: 110, t: 'el .env no entra a la imagen', r: 8, tam: 19, color: 'gris', en: 0.48 },
        { tipo: 'caja', x: 540, y: 220, w: 240, h: 110, t: '«.dockerignore»', s: 'es un archivo, no una pieza', r: 8, tam: 19, color: 'malva', en: 0.54 },
        { tipo: 'sello', x: 760, y: 225, r: 22, ok: false, en: 0.6 },
        { tipo: 'texto', t: 'Verificable = otra persona señala la pieza y dice si el control está.', x: 400, y: 380, tam: 22, ancho: 740, en: 0.8 },
        { tipo: 'texto', t: '«Usamos buenas prácticas» no se puede señalar.', x: 400, y: 470, tam: 22, ancho: 740, color: 'malva', en: 0.88 }
      ]);
    }
  });
})();
