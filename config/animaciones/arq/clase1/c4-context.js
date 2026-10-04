/* Nivel Context: el sistema es UNA caja; alrededor, las personas y los sistemas externos.
 * Cada flecha lleva verbo y protocolo. Lo interior (API, base de datos) no va en este nivel. */
(function () {
  FP_ANIMADOR.registrar('c4-context', {
    duracion: 5,
    pasos: [0.28, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 330, y: 190, w: 200, h: 150, t: 'Sistema de turnos', s: 'System · una sola caja', lleno: true, tam: 24, en: 0.02 },
        { tipo: 'persona', x: 90, y: 40, tam: 70, t: 'Cliente · Person', color: 'sello', en: 0.1 },
        { tipo: 'persona', x: 90, y: 400, tam: 70, t: 'Barbero · Person', color: 'sello', en: 0.14 },
        { tipo: 'caja', x: 600, y: 40, w: 180, h: 100, t: 'Correo', s: 'System_Ext', color: 'acento', en: 0.18 },
        { tipo: 'caja', x: 600, y: 365, w: 180, h: 100, t: 'Identidad', s: 'System_Ext', color: 'acento', en: 0.22 },
        { tipo: 'flecha', de: [140, 95], a: [325, 225], r: 'reserva turno · HTTPS', dx: -40, dy: 35, ancho: 170, en: 0.32 },
        { tipo: 'flecha', de: [140, 445], a: [325, 315], r: 'consulta su agenda · HTTPS', dx: -45, dy: -85, ancho: 170, en: 0.4 },
        { tipo: 'flecha', de: [535, 235], a: [640, 145], r: 'envía recordatorio · API REST', dx: 90, dy: -8, ancho: 190, en: 0.46 },
        { tipo: 'flecha', de: [535, 300], a: [640, 360], r: 'valida identidad · OIDC', dx: 90, dy: -22, ancho: 190, en: 0.52 },
        { tipo: 'caja', x: 200, y: 525, w: 150, h: 70, t: 'API', color: 'gris', en: 0.66 },
        { tipo: 'caja', x: 370, y: 525, w: 150, h: 70, t: 'Base de datos', color: 'gris', tam: 19, en: 0.7 },
        { tipo: 'tacha', x: 190, y: 517, w: 340, h: 86, en: 0.8 },
        { tipo: 'texto', t: 'Eso es interior: nivel 2', x: 670, y: 545, tam: 21, color: 'malva', ancho: 230, en: 0.86 }
      ]);
    }
  });
})();
