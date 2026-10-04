/* Tres diagramas, el mismo sistema: el Context dice con quien habla, el Containers de que piezas
 * esta hecho, y el Despliegue donde corre cada pieza y por que camino de red. */
(function () {
  FP_ANIMADOR.registrar('tres-angulos', {
    duracion: 5,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 240, h: 170, t: 'Context', s: '¿con quién habla el sistema?', tam: 26, en: 0.02 },
        { tipo: 'caja', x: 280, y: 30, w: 240, h: 170, t: 'Containers', s: '¿de qué piezas está hecho?', tam: 26, color: 'acento', en: 0.3 },
        { tipo: 'caja', x: 540, y: 30, w: 240, h: 170, t: 'Despliegue', s: '¿dónde corre cada pieza y por qué red?', tam: 26, color: 'malva', en: 0.6 },
        { tipo: 'marco', x: 60, y: 260, w: 680, h: 270, t: 'Nodo: máquina virtual, host de contenedores o servicio gestionado', color: 'malva', en: 0.68 },
        { tipo: 'caja', x: 110, y: 330, w: 250, h: 90, t: 'API de turnos', s: 'contenedor · 8080', en: 0.74 },
        { tipo: 'cilindro', x: 450, y: 310, w: 240, h: 130, t: 'Base de turnos', s: 'servicio gestionado · 5432', color: 'acento', en: 0.78 },
        { tipo: 'flecha', de: [365, 375], a: [445, 375], r: 'TCP 5432', dy: -32, color: 'malva', en: 0.84 },
        { tipo: 'texto', t: 'Zona, puerto y protocolo en cada flecha.', x: 400, y: 465, tam: 22, ancho: 640, en: 0.9 },
        { tipo: 'texto', t: 'Mismo sistema, tres ángulos: los nombres no cambian.', x: 400, y: 570, tam: 23, peso: 800, color: 'accion', ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
