/* Los datos: si dos servicios comparten tablas estan acoplados y no se despliegan por separado.
 * La regla: cada servicio es dueno de sus datos y los demas se los piden por su API. */
(function () {
  FP_ANIMADOR.registrar('base-compartida', {
    duracion: 5,
    // Pasos LOGICOS: 1) dos servicios sobre las mismas tablas: acoplados, 2) cada servicio
    // dueno de sus datos y el otro le pide por su API, 3) la conclusion. Cada lado en su mitad
    // del lienzo, sin solaparse.
    pasos: [0.4, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1) Tablas compartidas, en la mitad izquierda
        { tipo: 'texto', t: 'Tablas compartidas', x: 195, y: 14, tam: 24, peso: 800, color: 'malva', en: 0 },
        { tipo: 'caja', x: 20, y: 70, w: 165, h: 95, t: 'Turnos', s: 'servicio', en: 0.02 },
        { tipo: 'caja', x: 205, y: 70, w: 165, h: 95, t: 'Avisos', s: 'servicio', en: 0.05 },
        { tipo: 'cilindro', x: 90, y: 240, w: 210, h: 130, t: 'tablas compartidas', color: 'malva', en: 0.08 },
        { tipo: 'flecha', de: [102, 168], a: [150, 236], color: 'malva', en: 0.12 },
        { tipo: 'flecha', de: [288, 168], a: [240, 236], color: 'malva', en: 0.14 },
        { tipo: 'caja', x: 40, y: 400, w: 310, h: 95, t: 'Acoplados', s: 'no se despliegan por separado', color: 'malva', tam: 22, tamSub: 18, en: 0.22 },
        { tipo: 'sello', x: 195, y: 535, r: 26, ok: false, en: 0.28 },
        // 2) Cada servicio, dueno de sus datos, en la mitad derecha
        { tipo: 'texto', t: 'Cada uno, dueño de sus datos', x: 605, y: 14, tam: 24, peso: 800, color: 'accion', ancho: 370, en: 0.44 },
        { tipo: 'caja', x: 430, y: 70, w: 175, h: 95, t: 'Turnos', s: 'dueño de sus datos', tamSub: 16, en: 0.46 },
        { tipo: 'cilindro', x: 640, y: 63, w: 140, h: 110, t: 'turnos', color: 'acento', tam: 18, en: 0.5 },
        { tipo: 'flecha', de: [607, 118], a: [636, 118], en: 0.5 },
        { tipo: 'caja', x: 430, y: 300, w: 175, h: 95, t: 'Avisos', s: 'dueño de sus datos', tamSub: 16, en: 0.54 },
        { tipo: 'cilindro', x: 640, y: 293, w: 140, h: 110, t: 'avisos', color: 'acento', tam: 18, en: 0.58 },
        { tipo: 'flecha', de: [607, 348], a: [636, 348], en: 0.58 },
        { tipo: 'flecha', de: [517, 296], a: [517, 169], r: 'le pide a Turnos por su API', dx: 118, dy: 0, ancho: 210, tam: 17, en: 0.62 },
        { tipo: 'sello', x: 605, y: 460, r: 26, ok: true, en: 0.74 },
        // 3) Conclusion
        { tipo: 'texto', t: 'Aquí es donde se rompen los proyectos académicos.', x: 400, y: 575, tam: 23, ancho: 760, peso: 800, color: 'accion', en: 0.88 }
      ]);
    }
  });
})();
