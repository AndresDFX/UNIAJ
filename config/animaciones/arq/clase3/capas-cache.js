/* Cada instruccion del Dockerfile es una capa. Si cambia el codigo y no las dependencias, las
 * capas de arriba se reconstruyen y la del `npm ci` sale de la cache. */
(function () {
  FP_ANIMADOR.registrar('capas-cache', {
    duracion: 5,
    // Pasos LOGICOS: 1) cada instruccion del Dockerfile es una capa (la pila completa, 0.37);
    // 2) cambio una linea del codigo: las cuatro de abajo salen de la cache, las dos de arriba
    // se reconstruyen, y la conclusion (dependencias antes que el codigo).
    pasos: [0.42, 1],
    dibujar: function (ctx, t, lz) {
      var capas = ['FROM node:20-alpine', 'WORKDIR /app', 'COPY package*.json ./', 'RUN npm ci --omit=dev', 'COPY . .', 'CMD ["node", "server.js"]'];
      var e = [{ tipo: 'texto', t: 'Cada instrucción, una capa', x: 30, y: 14, tam: 24, peso: 800, alinear: 'left', color: 'accion', en: 0 }];
      for (var i = 0; i < capas.length; i++) {
        e.push({ tipo: 'caja', x: 30, y: 490 - i * 76, w: 420, h: 64, t: capas[i], color: 'accion', r: 8, tam: 20, en: 0.04 + i * 0.05 });
      }
      e.push({ tipo: 'texto', t: 'Cambió una línea del código:', x: 480, y: 60, tam: 22, peso: 700, alinear: 'left', ancho: 300, color: 'malva', en: 0.46 });
      for (var k = 0; k < 4; k++) {
        e.push({ tipo: 'chip', x: 610, y: 506 - k * 76, t: 'sale de la caché', color: 'accion', en: 0.55 + k * 0.04 });
      }
      e.push({ tipo: 'chip', x: 610, y: 506 - 4 * 76, t: 'se reconstruye', color: 'malva', en: 0.72 });
      e.push({ tipo: 'chip', x: 610, y: 506 - 5 * 76, t: 'se reconstruye', color: 'malva', en: 0.76 });
      e.push({ tipo: 'texto', t: 'Dependencias antes que el código: el build tarda segundos.', x: 400, y: 588, tam: 21, ancho: 760, en: 0.88 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
