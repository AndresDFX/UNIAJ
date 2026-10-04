/* Los umbrales de percepcion son convenciones: bajo unos 100 ms se percibe instantaneo, hacia 1 s se
 * nota la espera y mas alla se pierde la atencion. Y junto al tiempo va la tasa de error. Las siglas:
 * SLI es lo que se mide, SLO el objetivo. */
(function () {
  FP_ANIMADOR.registrar('umbrales-percepcion', {
    duracion: 5,
    // Pasos LOGICOS: 1) los tres umbrales de percepcion y que son convenciones, 2) el tiempo va
    // con la tasa de error, 3) las siglas: SLI lo que se mide, SLO el objetivo.
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'linea', pts: [[40, 140], [770, 140]], color: 'tinta', grosor: 4, en: 0 },
        { tipo: 'caja', x: 40, y: 40, w: 230, h: 80, t: '< 100 ms', s: 'instantáneo', color: 'accion', en: 0.06 },
        { tipo: 'caja', x: 290, y: 40, w: 230, h: 80, t: '≈ 1 s', s: 'se nota la espera', color: 'acento', en: 0.14 },
        { tipo: 'caja', x: 540, y: 40, w: 230, h: 80, t: '≈ 10 s', s: 'se pierde la atención', color: 'malva', en: 0.22 },
        { tipo: 'texto', t: 'Convenciones, no reglas: un reporte pesado puede tener 3 s; un autocompletado, menos de 100 ms.', x: 400, y: 170, tam: 20, ancho: 740, en: 0.3 },
        { tipo: 'caja', x: 40, y: 280, w: 340, h: 110, t: 'Tiempo', s: 'p95 de POST /turnos', en: 0.44 },
        { tipo: 'caja', x: 420, y: 280, w: 340, h: 110, t: 'Tasa de error', s: '% de peticiones que fallan', color: 'malva', en: 0.5 },
        { tipo: 'texto', t: 'Rápido devolviendo errores no cumple.', x: 400, y: 410, tam: 21, ancho: 740, en: 0.56 },
        { tipo: 'chip', x: 220, y: 480, t: 'SLI · el indicador que se mide', color: 'accion', en: 0.76 },
        { tipo: 'chip', x: 580, y: 480, t: 'SLO · el objetivo para ese indicador', color: 'acento', en: 0.82 }
      ]);
    }
  });
})();
