/* La condicion de fallo: un pipeline cuyo unico paso imprime exito sale verde siempre y no sirve.
 * Un CI de verdad se explica en tres campos: que construye, que prueba y que lo vuelve rojo. */
(function () {
  FP_ANIMADOR.registrar('ci-que-falla', {
    duracion: 5,
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'run: echo "todo OK"', x: 30, y: 30, tam: 24, mono: true, alinear: 'left', color: 'gris', en: 0 },
        { tipo: 'sello', x: 470, y: 45, r: 24, ok: true, en: 0.06 },
        { tipo: 'texto', t: 'con el código roto', x: 520, y: 30, tam: 20, alinear: 'left', color: 'malva', en: 0.12 },
        { tipo: 'sello', x: 470, y: 115, r: 24, ok: true, en: 0.18 },
        { tipo: 'texto', t: 'sin pruebas', x: 520, y: 100, tam: 20, alinear: 'left', color: 'malva', en: 0.22 },
        { tipo: 'chip', x: 220, y: 100, t: 'siempre verde: no sirve', color: 'malva', en: 0.28 },
        { tipo: 'texto', t: 'run: npm test', x: 30, y: 210, tam: 24, mono: true, alinear: 'left', color: 'accion', en: 0.4 },
        { tipo: 'texto', t: '1 failing · expected 409, got 201', x: 30, y: 255, tam: 20, mono: true, alinear: 'left', color: 'malva', en: 0.48 },
        { tipo: 'sello', x: 600, y: 245, r: 30, ok: false, en: 0.54 },
        { tipo: 'chip', x: 600, y: 290, t: 'pipeline rojo', color: 'malva', en: 0.58 },
        { tipo: 'caja', x: 20, y: 380, w: 240, h: 110, t: '¿Qué se construye?', s: 'la imagen etiquetada', en: 0.72 },
        { tipo: 'caja', x: 280, y: 380, w: 240, h: 110, t: '¿Qué se prueba?', s: 'las pruebas del servicio', en: 0.76 },
        { tipo: 'caja', x: 540, y: 380, w: 240, h: 110, t: '¿Qué lo vuelve rojo?', s: 'una prueba que falla', color: 'malva', en: 0.8 },
        { tipo: 'texto', t: 'Si nada puede ponerlo rojo, no es CI.', x: 400, y: 550, tam: 24, peso: 800, color: 'accion', en: 0.9 }
      ]);
    }
  });
})();
