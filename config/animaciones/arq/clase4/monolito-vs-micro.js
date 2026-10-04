/* Monolito: una sola unidad de despliegue; todo se construye y sale al aire junto. Microservicio:
 * unidad de despliegue independiente, con frontera de negocio y duena de sus datos. */
(function () {
  FP_ANIMADOR.registrar('monolito-vs-micro', {
    duracion: 5,
    pasos: [0.4, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Monolito', x: 200, y: 14, tam: 26, peso: 800, color: 'accion', en: 0 },
        { tipo: 'marco', x: 30, y: 60, w: 340, h: 300, t: 'UNA unidad de despliegue', color: 'accion', en: 0.02 },
        { tipo: 'caja', x: 60, y: 110, w: 280, h: 60, t: 'módulo turnos', r: 8, tam: 20, en: 0.08 },
        { tipo: 'caja', x: 60, y: 180, w: 280, h: 60, t: 'módulo avisos', r: 8, tam: 20, en: 0.11 },
        { tipo: 'caja', x: 60, y: 250, w: 280, h: 60, t: 'módulo usuarios', r: 8, tam: 20, en: 0.14 },
        { tipo: 'cilindro', x: 110, y: 380, w: 180, h: 110, t: 'una base', color: 'acento', en: 0.2 },
        { tipo: 'chip', x: 200, y: 515, t: 'se construye y sale junto', color: 'accion', en: 0.28 },
        { tipo: 'texto', t: 'Microservicios', x: 600, y: 14, tam: 26, peso: 800, color: 'accion', en: 0.42 },
        { tipo: 'caja', x: 430, y: 70, w: 160, h: 110, t: 'Turnos', s: 'se despliega solo', tam: 21, tamSub: 15, en: 0.46 },
        { tipo: 'caja', x: 610, y: 70, w: 160, h: 110, t: 'Avisos', s: 'se despliega solo', tam: 21, tamSub: 15, en: 0.5 },
        { tipo: 'cilindro', x: 445, y: 220, w: 130, h: 100, t: 'sus datos', color: 'acento', tam: 18, en: 0.56 },
        { tipo: 'cilindro', x: 625, y: 220, w: 130, h: 100, t: 'sus datos', color: 'acento', tam: 18, en: 0.6 },
        { tipo: 'flecha', de: [510, 182], a: [510, 218], en: 0.58 },
        { tipo: 'flecha', de: [690, 182], a: [690, 218], en: 0.62 },
        { tipo: 'chip', x: 600, y: 350, t: 'frontera de negocio propia', color: 'acento', en: 0.68 },
        { tipo: 'texto', t: 'El monolito es la arquitectura correcta por defecto en un sistema pequeño.', x: 400, y: 575, tam: 22, ancho: 760, color: 'malva', en: 0.84 }
      ]);
    }
  });
})();
