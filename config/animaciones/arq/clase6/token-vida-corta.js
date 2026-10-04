/* Spoofing con un token copiado de un registro. Controles: HTTPS en todo el trayecto, el token en
 * el encabezado y nunca en la URL, y vida corta (convencion: 15 a 60 min, refresco de dias). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('token-vida-corta', {
    duracion: 5,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca;
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'GET /turnos?token=eyJhbGci…', x: 30, y: 30, tam: 22, mono: true, alinear: 'left', color: 'malva', en: 0.02 },
        { tipo: 'flecha', de: [300, 70], a: [300, 120], color: 'malva', en: 0.1 },
        { tipo: 'caja', x: 160, y: 125, w: 280, h: 80, t: 'archivo de registro', s: 'guarda la URL entera', color: 'gris', tam: 20, en: 0.14 },
        { tipo: 'persona', x: 560, y: 110, tam: 60, t: 'lo copia y se hace pasar por el usuario', ancho: 260, color: 'malva', en: 0.22 },
        { tipo: 'texto', t: 'Authorization: Bearer eyJhbGci…', x: 30, y: 290, tam: 22, mono: true, alinear: 'left', color: 'accion', en: 0.38 },
        { tipo: 'chip', x: 220, y: 335, t: 'en el encabezado, nunca en la URL', color: 'accion', en: 0.44 },
        { tipo: 'chip', x: 600, y: 335, t: 'HTTPS en todo el trayecto', color: 'accion', en: 0.5 },
        { tipo: 'texto', t: 'Vida corta', x: 30, y: 420, tam: 24, peso: 800, alinear: 'left', color: 'accion', en: 0.68 },
        { tipo: 'barra', x: 210, y: 468, w: 560, h: 30, valor: 0.12, t: 'acceso', r: '15 a 60 min', color: 'accion', en: 0.72 },
        { tipo: 'barra', x: 210, y: 518, w: 560, h: 30, valor: 0.7, t: 'refresco', r: 'días', color: 'acento', en: 0.78 },
        { tipo: 'texto', t: 'Convención, no regla: comodidad contra ventana de daño.', x: 400, y: 585, tam: 21, ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
