/* El plan de monitoreo es una tabla de tres columnas: senal, que se mide en MI dominio y umbral u
 * objetivo. Una senal sin umbral no permite decidir cuando actuar. */
(function () {
  FP_ANIMADOR.registrar('senal-umbral', {
    duracion: 5,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 20, w: 180, h: 60, t: 'Señal', lleno: true, r: 8, tam: 20, en: 0 },
        { tipo: 'caja', x: 210, y: 20, w: 330, h: 60, t: 'Qué se mide en MI dominio', lleno: true, r: 8, tam: 20, en: 0.02 },
        { tipo: 'caja', x: 550, y: 20, w: 230, h: 60, t: 'Umbral u objetivo', lleno: true, color: 'malva', r: 8, tam: 20, en: 0.04 },
        { tipo: 'caja', x: 20, y: 95, w: 180, h: 90, t: 'Latencia', r: 8, tam: 20, en: 0.1 },
        { tipo: 'caja', x: 210, y: 95, w: 330, h: 90, t: 'el listado de franjas libres', r: 8, tam: 19, en: 0.14 },
        { tipo: 'caja', x: 550, y: 95, w: 230, h: 90, t: '«que sea rápido»', color: 'malva', r: 8, tam: 19, en: 0.2 },
        { tipo: 'sello', x: 760, y: 100, r: 22, ok: false, en: 0.28 },
        { tipo: 'caja', x: 550, y: 200, w: 230, h: 120, t: '< 400 ms; si pasa de 800, se revisa', color: 'accion', r: 8, tam: 19, en: 0.44 },
        { tipo: 'sello', x: 760, y: 205, r: 22, ok: true, en: 0.52 },
        { tipo: 'flecha', de: [665, 186], a: [665, 196], en: 0.44 },
        { tipo: 'texto', t: 'Con umbral se sabe cuándo actuar.', x: 270, y: 245, tam: 22, ancho: 460, en: 0.6 },
        { tipo: 'texto', t: 'Una señal sin umbral no suma, aunque esté bien elegida.', x: 400, y: 400, tam: 24, peso: 800, color: 'malva', ancho: 740, en: 0.8 },
        { tipo: 'texto', t: 'Entre 4 y 6 filas.', x: 400, y: 490, tam: 22, ancho: 740, en: 0.9 }
      ]);
    }
  });
})();
