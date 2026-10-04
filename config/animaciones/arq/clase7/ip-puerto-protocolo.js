/* Las tres etiquetas de una flecha: la IP dice a que maquina, el puerto a que proceso de esa
 * maquina, y el protocolo en que idioma. Puertos por convencion: 443, 5432, 8080. */
(function () {
  FP_ANIMADOR.registrar('ip-puerto-protocolo', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 160, w: 170, h: 100, t: 'Balanceador', tam: 21, en: 0 },
        { tipo: 'marco', x: 330, y: 40, w: 450, h: 380, t: 'Máquina 10.0.2.15', color: 'accion', en: 0.04 },
        { tipo: 'caja', x: 380, y: 100, w: 340, h: 80, t: 'proceso API · puerto 8080', color: 'acento', tam: 21, en: 0.1 },
        { tipo: 'caja', x: 380, y: 200, w: 340, h: 80, t: 'otro proceso · puerto 9100', color: 'gris', tam: 21, en: 0.12 },
        { tipo: 'flecha', de: [195, 210], a: [375, 140], r: '10.0.2.15 : 8080 · HTTP', dy: -75, dx: -40, ancho: 220, color: 'malva', grosor: 4, en: 0.2 },
        { tipo: 'chip', x: 130, y: 300, t: 'IP → a qué máquina', color: 'accion', en: 0.34 },
        { tipo: 'chip', x: 130, y: 350, t: 'puerto → a qué proceso', color: 'acento', en: 0.44 },
        { tipo: 'chip', x: 130, y: 400, t: 'protocolo → en qué idioma', color: 'malva', en: 0.54 },
        { tipo: 'texto', t: 'Puertos por convención registrada, no por ley física', x: 400, y: 455, tam: 21, ancho: 760, en: 0.66 },
        { tipo: 'chip', x: 140, y: 510, t: '443 · HTTPS', color: 'accion', en: 0.72 },
        { tipo: 'chip', x: 330, y: 510, t: '80 · HTTP', color: 'accion', en: 0.75 },
        { tipo: 'chip', x: 500, y: 510, t: '5432 · PostgreSQL', color: 'acento', en: 0.78 },
        { tipo: 'chip', x: 690, y: 510, t: '8080 · desarrollo', color: 'gris', en: 0.81 }
      ]);
    }
  });
})();
