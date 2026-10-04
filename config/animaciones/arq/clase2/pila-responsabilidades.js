/* La pila de responsabilidades debajo de cualquier aplicacion, de abajo hacia arriba. En
 * on-premise todas las capas son del cliente; en la nube el proveedor toma las de abajo, y los
 * tres modelos se distinguen por una sola cosa: hasta que capa administra el proveedor. */
(function () {
  FP_ANIMADOR.registrar('pila-responsabilidades', {
    duracion: 5,
    // Pasos LOGICOS: 1) la pila: siete capas, de abajo hacia arriba; 2) on-premise: todas las
    // capas las administra el cliente; 3) en la nube el proveedor administra desde abajo, y la
    // pregunta que distingue los tres modelos es hasta que capa llega.
    pasos: [0.36, 0.58, 1],
    dibujar: function (ctx, t, lz) {
      var capas = ['Edificio, energía y red', 'Hardware', 'Virtualización', 'Sistema operativo',
                   'Runtime (Node.js, Python…)', 'Aplicación', 'Datos, usuarios y permisos'];
      var els = [];
      // Idea 1: la pila
      for (var i = 0; i < capas.length; i++) {
        els.push({ tipo: 'caja', x: 40, y: 520 - i * 72, w: 400, h: 62, t: capas[i], r: 10, tam: 21,
                   color: i < 3 ? 'gris' : (i < 5 ? 'acento' : 'accion'), en: 0.02 + i * 0.04 });
      }
      // Idea 2: on-premise, todo es del cliente
      els.push({ tipo: 'linea', pts: [[452, 90], [468, 90], [468, 580], [452, 580]], color: 'sello', grosor: 7, en: 0.4 });
      els.push({ tipo: 'texto', t: 'On-premise', x: 492, y: 92, tam: 26, peso: 800, color: 'accion', alinear: 'left', ancho: 290, en: 0.44 });
      els.push({ tipo: 'texto', t: 'todas las capas las administra el cliente', x: 492, y: 130, tam: 20, alinear: 'left', ancho: 280, en: 0.46 });
      // Idea 3: en la nube, el proveedor sube desde abajo
      els.push({ tipo: 'flecha', de: [500, 580], a: [500, 300], color: 'acento', grosor: 5, en: 0.62 });
      els.push({ tipo: 'texto', t: 'En la nube, el proveedor administra desde abajo', x: 522, y: 470, tam: 20, alinear: 'left', ancho: 260, en: 0.7 });
      els.push({ tipo: 'texto', t: '¿Hasta qué capa?', x: 522, y: 292, tam: 26, peso: 800, color: 'accion', alinear: 'left', ancho: 260, en: 0.78 });
      els.push({ tipo: 'texto', t: 'Esa línea distingue IaaS, PaaS y SaaS', x: 522, y: 330, tam: 20, alinear: 'left', ancho: 260, en: 0.8 });
      UJ.escena(ctx, t, lz, els);
    }
  });
})();
