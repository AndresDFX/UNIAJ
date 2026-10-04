/* La pila de responsabilidades debajo de cualquier aplicacion, de abajo hacia arriba. Los tres
 * modelos se distinguen por una sola cosa: hasta que capa administra el proveedor. */
(function () {
  FP_ANIMADOR.registrar('pila-responsabilidades', {
    duracion: 5,
    pasos: [0.45, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var capas = ['Edificio, energía y red', 'Hardware', 'Virtualización', 'Sistema operativo',
                   'Runtime (Node.js, Python…)', 'Aplicación', 'Datos, usuarios y permisos'];
      var els = [];
      for (var i = 0; i < capas.length; i++) {
        els.push({ tipo: 'caja', x: 60, y: 520 - i * 72, w: 420, h: 62, t: capas[i], r: 10, tam: 21,
                   color: i < 3 ? 'gris' : (i < 5 ? 'acento' : 'accion'), en: 0.02 + i * 0.055 });
      }
      els.push({ tipo: 'flecha', de: [505, 580], a: [505, 90], color: 'tinta', en: 0.42 });
      els.push({ tipo: 'texto', t: 'se sube por la pila', x: 525, y: 330, tam: 20, alinear: 'left', ancho: 240, en: 0.46 });
      els.push({ tipo: 'texto', t: '¿Hasta qué capa administra el proveedor?', x: 525, y: 110, tam: 24, alinear: 'left', ancho: 260, color: 'accion', en: 0.8 });
      UJ.escena(ctx, t, lz, els);
    }
  });
})();
