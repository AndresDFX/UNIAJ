/* Una peticion de punta a punta: el telefono resuelve el nombre, entra por HTTPS al balanceador de
 * la zona publica, este elige una instancia de la API en la zona privada (HTTP 8080), y la API
 * consulta la base en la zona de datos (5432). La respuesta vuelve por el mismo camino. */
(function () {
  FP_ANIMADOR.registrar('peticion-punta-a-punta', {
    duracion: 5,
    pasos: [0.28, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'persona', x: 70, y: 250, tam: 64, t: 'teléfono', color: 'accion', en: 0 },
        { tipo: 'marco', x: 150, y: 120, w: 190, h: 330, t: 'Pública', color: 'sello', en: 0.02 },
        { tipo: 'marco', x: 360, y: 60, w: 200, h: 450, t: 'Privada', color: 'accion', en: 0.04 },
        { tipo: 'marco', x: 580, y: 120, w: 200, h: 330, t: 'Datos', color: 'acento', en: 0.06 },
        { tipo: 'caja', x: 165, y: 235, w: 160, h: 100, t: 'Balanceador', s: '443', tam: 19, en: 0.08 },
        { tipo: 'caja', x: 380, y: 130, w: 160, h: 90, t: 'API 1', s: '8080', tam: 20, en: 0.1 },
        { tipo: 'caja', x: 380, y: 350, w: 160, h: 90, t: 'API 2', s: '8080', tam: 20, en: 0.12 },
        { tipo: 'cilindro', x: 600, y: 220, w: 160, h: 130, t: 'Base', s: '5432', color: 'acento', en: 0.14 },
        { tipo: 'flecha', de: [105, 285], a: [160, 285], r: 'HTTPS', dy: -60, color: 'malva', grosor: 4, en: 0.18 },
        { tipo: 'flecha', de: [330, 270], a: [380, 210], r: 'HTTP 8080', dx: -10, dy: -100, color: 'malva', grosor: 4, en: 0.36 },
        { tipo: 'flecha', de: [545, 190], a: [600, 250], r: 'TCP 5432', dx: 80, dy: -125, color: 'malva', grosor: 4, en: 0.62 },
        { tipo: 'chip', x: 460, y: 530, t: 'responde JSON por el mismo camino', color: 'accion', en: 0.84 },
        { tipo: 'texto', t: 'el balanceador elige una de las dos instancias', x: 245, y: 470, tam: 18, ancho: 200, en: 0.42 }
      ]);
    }
  });
})();
