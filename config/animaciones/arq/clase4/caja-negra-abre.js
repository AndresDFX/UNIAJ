/* Del nivel 1 al nivel 2: la caja negra del Context se abre y por dentro aparecen los
 * contenedores, cada uno con su razon de existir. */
(function () {
  FP_ANIMADOR.registrar('caja-negra-abre', {
    duracion: 5,
    // Pasos LOGICOS: 1) nivel 1, el sistema es una caja negra, 2) nivel 2, la caja abierta con
    // sus contenedores y sus flechas completas, 3) la pregunta del nivel: cuantas piezas y por que.
    pasos: [0.3, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1) Nivel 1
        { tipo: 'texto', t: 'Nivel 1 · Context', x: 400, y: 20, tam: 26, peso: 800, color: 'accion', en: 0, sale: 0.34 },
        { tipo: 'caja', x: 250, y: 160, w: 300, h: 200, t: 'Sistema de turnos', s: 'caja negra', lleno: true, tam: 28, en: 0.02, sale: 0.34 },
        // 2) Nivel 2
        { tipo: 'texto', t: 'Nivel 2 · Containers', x: 400, y: 20, tam: 26, peso: 800, color: 'accion', en: 0.4 },
        { tipo: 'marco', x: 30, y: 80, w: 740, h: 330, t: 'Sistema de turnos', color: 'accion', en: 0.4 },
        { tipo: 'caja', x: 60, y: 160, w: 200, h: 130, t: 'App web', s: 'React', tam: 22, en: 0.48 },
        { tipo: 'caja', x: 300, y: 160, w: 200, h: 130, t: 'API de turnos', s: 'Node.js', tam: 22, en: 0.53 },
        { tipo: 'cilindro', x: 545, y: 150, w: 200, h: 150, t: 'Base de turnos', s: 'PostgreSQL', color: 'acento', en: 0.58 },
        { tipo: 'flecha', de: [262, 225], a: [296, 225], en: 0.62 },
        { tipo: 'flecha', de: [502, 225], a: [541, 225], en: 0.64 },
        // 3) La pregunta del nivel
        { tipo: 'texto', t: '¿De cuántas piezas está hecho por dentro, y por qué?', x: 400, y: 450, tam: 24, ancho: 740, en: 0.83 },
        { tipo: 'texto', t: 'Cada caja nueva necesita una razón.', x: 400, y: 530, tam: 24, peso: 800, color: 'malva', ancho: 740, en: 0.9 }
      ]);
    }
  });
})();
