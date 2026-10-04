/* Metricas y registros: la metrica es un numero en el tiempo, barata, y detecta QUE algo cambio;
 * el registro es un evento con contexto, caro en volumen, y explica POR QUE. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('metricas-vs-logs', {
    duracion: 5,
    pasos: [0.45, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca;
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Métrica: p95 de POST /turnos', x: 30, y: 14, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0 },
        { tipo: 'linea', pts: [[40, 260], [760, 260]], color: 'gris', grosor: 2, en: 0 },
        { tipo: 'linea', pts: [[40, 230], [140, 225], [240, 232], [340, 228], [420, 226], [480, 110], [560, 100], [640, 104], [760, 98]], color: 'accion', grosor: 4, en: 0.04, dur: 0.3 },
        { tipo: 'linea', pts: [[40, 160], [760, 160]], color: 'malva', grosor: 2, punteada: true, en: 0.2 },
        { tipo: 'texto', t: 'umbral', x: 700, y: 165, tam: 18, color: 'malva', en: 0.22 },
        { tipo: 'chip', x: 470, y: 280, t: 'detecta QUE algo cambió', color: 'accion', en: 0.36 },
        { tipo: 'texto', t: 'Registro (log) de ese momento', x: 30, y: 350, tam: 23, peso: 800, alinear: 'left', color: 'malva', en: 0.5 },
        { tipo: 'texto', t: '10:42:07 POST /turnos 1830 ms', x: 40, y: 400, tam: 20, mono: true, alinear: 'left', en: 0.56 },
        { tipo: 'texto', t: '10:42:07 SELECT franja · pool de conexiones agotado', x: 40, y: 435, tam: 20, mono: true, alinear: 'left', color: 'malva', en: 0.62 },
        { tipo: 'texto', t: '10:42:08 POST /turnos 1795 ms', x: 40, y: 470, tam: 20, mono: true, alinear: 'left', en: 0.66 },
        { tipo: 'chip', x: 470, y: 520, t: 'explica POR QUÉ cambió', color: 'malva', en: 0.74 },
        { tipo: 'texto', t: 'Al menos una señal del plan debe ser un registro.', x: 400, y: 590, tam: 21, ancho: 760, en: 0.88 }
      ]);
    }
  });
})();
