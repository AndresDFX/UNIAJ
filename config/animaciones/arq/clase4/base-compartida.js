/* Los datos: si dos servicios comparten tablas estan acoplados y no se despliegan por separado.
 * La regla: cada servicio es dueno de sus datos y los demas se los piden por su API. */
(function () {
  FP_ANIMADOR.registrar('base-compartida', {
    duracion: 5,
    pasos: [0.42, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 40, y: 40, w: 200, h: 100, t: 'Turnos', s: 'servicio', en: 0 },
        { tipo: 'caja', x: 280, y: 40, w: 200, h: 100, t: 'Avisos', s: 'servicio', en: 0.04 },
        { tipo: 'cilindro', x: 150, y: 210, w: 220, h: 130, t: 'tablas compartidas', color: 'malva', en: 0.08 },
        { tipo: 'flecha', de: [140, 143], a: [210, 205], color: 'malva', en: 0.14 },
        { tipo: 'flecha', de: [380, 143], a: [310, 205], color: 'malva', en: 0.16 },
        { tipo: 'chip', x: 260, y: 370, t: 'acoplados: no se despliegan por separado', color: 'malva', en: 0.24 },
        { tipo: 'sello', x: 60, y: 275, r: 30, ok: false, en: 0.3 },
        { tipo: 'caja', x: 440, y: 40, w: 180, h: 95, t: 'Turnos', s: 'dueño de sus datos', tamSub: 16, en: 0.46 },
        { tipo: 'cilindro', x: 640, y: 35, w: 140, h: 105, t: 'turnos', color: 'acento', tam: 18, en: 0.5 },
        { tipo: 'flecha', de: [622, 88], a: [638, 88], en: 0.5 },
        { tipo: 'caja', x: 440, y: 300, w: 180, h: 95, t: 'Avisos', s: 'dueño de sus datos', tamSub: 16, en: 0.54 },
        { tipo: 'cilindro', x: 640, y: 295, w: 140, h: 105, t: 'avisos', color: 'acento', tam: 18, en: 0.58 },
        { tipo: 'flecha', de: [622, 348], a: [638, 348], en: 0.58 },
        { tipo: 'flecha', de: [530, 296], a: [530, 139], r: 'le pide a Turnos por su API', dx: 120, dy: -10, ancho: 200, en: 0.66 },
        { tipo: 'sello', x: 530, y: 450, r: 30, ok: true, en: 0.74 },
        { tipo: 'texto', t: 'Aquí es donde se rompen los proyectos académicos.', x: 400, y: 570, tam: 23, ancho: 760, peso: 800, color: 'accion', en: 0.86 }
      ]);
    }
  });
})();
