/* Las tres reglas del nivel Container: cada caja con tres datos (nombre, tecnologia,
 * responsabilidad); lo que guarda datos es un almacen (ContainerDb); cada flecha con protocolo
 * y formato. */
(function () {
  FP_ANIMADOR.registrar('tres-reglas-container', {
    duracion: 5,
    pasos: [0.34, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'chip', x: 175, y: 20, t: '1 · tres datos por caja', color: 'accion', en: 0 },
        { tipo: 'caja', x: 30, y: 80, w: 290, h: 70, t: 'API', color: 'gris', tam: 24, en: 0.04, sale: 0.2 },
        { tipo: 'tacha', x: 20, y: 72, w: 310, h: 86, en: 0.1, sale: 0.2 },
        { tipo: 'caja', x: 30, y: 80, w: 290, h: 70, t: 'API de turnos', color: 'accion', r: 10, tam: 22, en: 0.22 },
        { tipo: 'caja', x: 30, y: 155, w: 290, h: 60, t: 'Node.js', color: 'acento', r: 10, tam: 20, en: 0.25 },
        { tipo: 'caja', x: 30, y: 220, w: 290, h: 80, t: 'valida la franja y registra el turno', color: 'sello', r: 10, tam: 18, en: 0.28 },
        { tipo: 'chip', x: 600, y: 20, t: '2 · el almacén es ContainerDb', color: 'acento', en: 0.36 },
        { tipo: 'cilindro', x: 500, y: 80, w: 200, h: 200, t: 'Base de turnos', s: 'ContainerDb · PostgreSQL', color: 'acento', en: 0.42 },
        { tipo: 'chip', x: 400, y: 340, t: '3 · cada flecha: protocolo y formato', color: 'malva', en: 0.66 },
        { tipo: 'flecha', de: [325, 190], a: [495, 190], r: 'TCP/SQL', dy: -32, color: 'malva', grosor: 4, en: 0.72 },
        { tipo: 'caja', x: 30, y: 430, w: 180, h: 80, t: 'App web', s: 'React', tam: 20, en: 0.74 },
        { tipo: 'flecha', de: [215, 470], a: [515, 470], r: 'POST /turnos · HTTPS/JSON', dy: -36, ancho: 290, color: 'malva', grosor: 4, en: 0.8 },
        { tipo: 'caja', x: 520, y: 430, w: 200, h: 80, t: 'API de turnos', s: 'Node.js', tam: 20, en: 0.78 },
        { tipo: 'texto', t: 'Una caja que dice solo «API» es una etiqueta, no un contenedor.', x: 400, y: 560, tam: 21, ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
