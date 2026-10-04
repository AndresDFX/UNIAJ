/* La politica de secretos en cuatro respuestas, mas el orden ante una filtracion: primero se
 * rota, despues se limpia el historial. */
(function () {
  FP_ANIMADOR.registrar('politica-cuatro-respuestas', {
    duracion: 5,
    pasos: [0.5, 1],
    dibujar: function (ctx, t, lz) {
      var r = [['¿Dónde viven?', 'secretos del repositorio y variables de entorno; en local, .env ignorado'],
               ['¿Quién los rota?', 'un responsable con rol, escrito en el README'],
               ['¿Cada cuánto?', 'un número o un evento: al cierre de cada corte'],
               ['¿Qué está prohibido?', 'Dockerfile, README, YAML en claro, imprimirlo en el log']];
      var e = [];
      for (var i = 0; i < 4; i++) {
        e.push({ tipo: 'caja', x: 20, y: 20 + i * 96, w: 250, h: 82, t: r[i][0], lleno: true, r: 10, tam: 21, en: 0.03 + i * 0.1 });
        e.push({ tipo: 'caja', x: 280, y: 20 + i * 96, w: 500, h: 82, t: '', s: r[i][1], r: 10, tamSub: 19, en: 0.06 + i * 0.1 });
      }
      e.push({ tipo: 'texto', t: 'Ante una filtración', x: 400, y: 418, tam: 24, peso: 800, color: 'malva', en: 0.55 });
      e.push({ tipo: 'caja', x: 60, y: 460, w: 300, h: 100, t: '1 · Rotar', s: 'la llave vieja deja de servir', color: 'malva', lleno: true, en: 0.62 });
      e.push({ tipo: 'flecha', de: [365, 510], a: [435, 510], en: 0.7 });
      e.push({ tipo: 'caja', x: 440, y: 460, w: 300, h: 100, t: '2 · Limpiar el historial', s: 'para que no quede a la vista', color: 'gris', en: 0.76 });
      e.push({ tipo: 'texto', t: 'Limpiar no invalida la llave: ya está en cada clon.', x: 400, y: 588, tam: 21, ancho: 760, en: 0.88 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
