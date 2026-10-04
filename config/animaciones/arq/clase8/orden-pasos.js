/* Tres bloques nombrados (disparadores, entorno, pasos) y tres pasos en ORDEN: construccion,
 * prueba y despliegue simulado. Probar antes de construir no prueba el artefacto que se entrega. */
(function () {
  FP_ANIMADOR.registrar('orden-pasos', {
    duracion: 5,
    pasos: [0.34, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 20, w: 240, h: 90, t: 'on', s: 'disparadores', en: 0.02 },
        { tipo: 'caja', x: 280, y: 20, w: 240, h: 90, t: 'runs-on', s: 'entorno', en: 0.08 },
        { tipo: 'caja', x: 540, y: 20, w: 240, h: 90, t: 'steps', s: 'pasos', en: 0.14 },
        { tipo: 'caja', x: 30, y: 180, w: 220, h: 100, t: '1 · Construir', s: 'docker build', color: 'acento', en: 0.38 },
        { tipo: 'flecha', de: [255, 230], a: [285, 230], en: 0.42 },
        { tipo: 'caja', x: 290, y: 180, w: 220, h: 100, t: '2 · Probar', s: 'npm test', color: 'acento', en: 0.46 },
        { tipo: 'flecha', de: [515, 230], a: [545, 230], en: 0.5 },
        { tipo: 'caja', x: 550, y: 180, w: 220, h: 100, t: '3 · Desplegar', s: 'SIMULADO, y lo dice', color: 'malva', en: 0.54 },
        { tipo: 'caja', x: 140, y: 380, w: 220, h: 80, t: 'Probar', color: 'gris', en: 0.72 },
        { tipo: 'flecha', de: [365, 420], a: [435, 420], color: 'gris', en: 0.74 },
        { tipo: 'caja', x: 440, y: 380, w: 220, h: 80, t: 'Construir', color: 'gris', en: 0.76 },
        { tipo: 'tacha', x: 140, y: 470, w: 520, h: -100, simple: true, grosor: 4, en: 0.8 },
        { tipo: 'texto', t: 'Probar antes de construir no prueba lo que se va a entregar.', x: 400, y: 520, tam: 22, ancho: 760, color: 'malva', en: 0.86 }
      ]);
    }
  });
})();
