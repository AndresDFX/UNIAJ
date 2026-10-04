/* Por que el driver importa mas que el nivel: 5000 archivos de 2 MB son 10 GB, que guardados cuestan
 * unos US$ 0.25 al mes; descargados 20 veces cada uno son 200 GB de salida, unos US$ 18. */
(function () {
  FP_ANIMADOR.registrar('egress-driver', {
    duracion: 5,
    // Pasos LOGICOS: 1) guardar 10 GB cuesta centavos, 2) descargarlos 20 veces cuesta 18 dolares,
    // 3) la comparacion lado a lado y la conclusion: el driver es el trafico de salida.
    pasos: [0.36, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 360, h: 110, t: '5.000 archivos × 2 MB', s: '= 10 GB guardados', en: 0 },
        { tipo: 'flecha', de: [385, 85], a: [455, 85], en: 0.08 },
        { tipo: 'caja', x: 460, y: 30, w: 320, h: 110, t: '≈ US$ 0.25 al mes', s: 'almacenamiento', color: 'acento', en: 0.12 },
        { tipo: 'caja', x: 20, y: 200, w: 360, h: 110, t: '20 descargas por archivo', s: '= 200 GB de salida al mes', color: 'malva', en: 0.38 },
        { tipo: 'flecha', de: [385, 255], a: [455, 255], color: 'malva', en: 0.44 },
        { tipo: 'caja', x: 460, y: 200, w: 320, h: 110, t: '≈ US$ 18 al mes', s: '200 GB × US$ 0.09', color: 'malva', en: 0.48 },
        { tipo: 'barra', x: 250, y: 380, w: 480, h: 36, valor: 0.014, t: 'guardar', r: '0.25', color: 'acento', en: 0.74, tam: 20 },
        { tipo: 'barra', x: 250, y: 440, w: 480, h: 36, valor: 1, t: 'descargar', color: 'malva', en: 0.78, tam: 20 },
        { tipo: 'texto', t: '18', x: 745, y: 444, tam: 20, peso: 700, alinear: 'left', color: 'malva', en: 0.86 },
        { tipo: 'texto', t: 'El driver es el tráfico de salida, no el tamaño.', x: 400, y: 540, tam: 24, peso: 800, color: 'accion', ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
