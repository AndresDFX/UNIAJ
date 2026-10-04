/* Las tres etiquetas de una flecha: la IP dice a que maquina, el puerto a que proceso de esa
 * maquina, y el protocolo en que idioma. Puertos por convencion: 443, 5432, 8080. */
(function () {
  FP_ANIMADOR.registrar('ip-puerto-protocolo', {
    duracion: 5,
    // Pasos LOGICOS: 1) la flecha llega a una maquina con varios procesos, etiquetada
    // «10.0.2.15 : 8080 · HTTP», 2) que dice cada etiqueta (IP, puerto, protocolo),
    // 3) los puertos por convencion registrada.
    pasos: [0.28, 0.58, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1) La flecha y su direccion completa
        { tipo: 'caja', x: 20, y: 160, w: 170, h: 100, t: 'Balanceador', tam: 21, en: 0 },
        { tipo: 'marco', x: 330, y: 40, w: 450, h: 380, t: 'Máquina 10.0.2.15', color: 'accion', en: 0.02 },
        { tipo: 'caja', x: 380, y: 100, w: 340, h: 80, t: 'proceso API · puerto 8080', color: 'acento', tam: 21, en: 0.06 },
        { tipo: 'caja', x: 380, y: 200, w: 340, h: 80, t: 'otro proceso · puerto 9100', color: 'gris', tam: 21, en: 0.08 },
        { tipo: 'flecha', de: [195, 210], a: [375, 140], r: '10.0.2.15 : 8080 · HTTP', dx: -95, dy: -70, ancho: 260, color: 'malva', grosor: 4, en: 0.12 },
        // 2) Que dice cada etiqueta
        { tipo: 'chip', x: 155, y: 300, t: 'IP → a qué máquina', color: 'accion', en: 0.3 },
        { tipo: 'chip', x: 155, y: 350, t: 'puerto → a qué proceso', color: 'acento', en: 0.38 },
        { tipo: 'chip', x: 155, y: 400, t: 'protocolo → en qué idioma', color: 'malva', en: 0.46 },
        // 3) Puertos por convencion
        { tipo: 'texto', t: 'Puertos por convención registrada, no por ley física', x: 400, y: 455, tam: 21, ancho: 760, en: 0.62 },
        { tipo: 'chip', x: 125, y: 510, t: '443 · HTTPS', color: 'accion', en: 0.68 },
        { tipo: 'chip', x: 300, y: 510, t: '80 · HTTP', color: 'accion', en: 0.72 },
        { tipo: 'chip', x: 487, y: 510, t: '5432 · PostgreSQL', color: 'acento', en: 0.76 },
        { tipo: 'chip', x: 682, y: 510, t: '8080 · desarrollo', color: 'gris', en: 0.8 }
      ]);
    }
  });
})();
