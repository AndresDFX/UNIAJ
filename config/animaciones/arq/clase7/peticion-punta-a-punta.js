/* Una peticion de punta a punta, salto por salto: el telefono resuelve el nombre en el DNS, entra
 * por HTTPS 443 al balanceador de la zona publica, este elige una instancia de la API en la zona
 * privada (HTTP 8080), y la API consulta la base en la zona de datos (5432). La respuesta vuelve
 * por el mismo camino. Cada zona aparece con el salto que llega a ella. */
(function () {
  FP_ANIMADOR.registrar('peticion-punta-a-punta', {
    duracion: 6,
    // Pasos LOGICOS (los 4 saltos y la vuelta): 1) el DNS traduce el nombre a la IP, 2) HTTPS 443
    // al balanceador de la zona publica, 3) HTTP 8080 a una de las dos API de la zona privada,
    // 4) TCP 5432 a la base de la zona de datos, 5) la respuesta vuelve por el mismo camino.
    pasos: [0.22, 0.42, 0.64, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1) DNS
        { tipo: 'persona', x: 70, y: 250, tam: 64, t: 'teléfono', color: 'accion', en: 0 },
        { tipo: 'caja', x: 16, y: 24, w: 176, h: 92, t: 'DNS', s: 'turnos.example → IP', tam: 20, tamSub: 15, en: 0.01 },
        { tipo: 'flecha', de: [50, 244], a: [50, 122], en: 0.04 },
        { tipo: 'flecha', de: [112, 122], a: [112, 244], r: 'IP', dx: 22, dy: -10, tam: 17, en: 0.08 },
        // 2) Zona publica: el balanceador
        { tipo: 'marco', x: 204, y: 140, w: 166, h: 290, color: 'sello', en: 0.24 },
        { tipo: 'texto', t: 'Pública', x: 220, y: 150, tam: 18, peso: 700, alinear: 'left', en: 0.24 },
        { tipo: 'caja', x: 214, y: 238, w: 146, h: 96, t: 'Balanceador', s: '443', tam: 18, en: 0.26 },
        { tipo: 'flecha', de: [104, 288], a: [210, 288], r: 'HTTPS 443', dy: -30, tam: 16, color: 'malva', grosor: 4, en: 0.28 },
        // 3) Zona privada: una de las dos instancias de la API
        { tipo: 'marco', x: 384, y: 70, w: 194, h: 400, t: 'Privada', color: 'accion', en: 0.44 },
        { tipo: 'caja', x: 401, y: 112, w: 160, h: 86, t: 'API 1', s: '8080', tam: 20, en: 0.46 },
        { tipo: 'caja', x: 401, y: 362, w: 160, h: 86, t: 'API 2', s: '8080', tam: 20, en: 0.48 },
        { tipo: 'flecha', de: [360, 262], a: [398, 196], color: 'malva', grosor: 4, en: 0.49 },
        { tipo: 'flecha', de: [360, 312], a: [398, 368], color: 'gris', punteada: true, en: 0.5 },
        { tipo: 'texto', t: 'HTTP 8080', x: 481, y: 210, tam: 17, color: 'malva', en: 0.52 },
        { tipo: 'texto', t: 'el balanceador elige una de las dos', x: 481, y: 260, tam: 17, ancho: 170, en: 0.54 },
        // 4) Zona de datos: la base
        { tipo: 'marco', x: 592, y: 140, w: 192, h: 290, t: 'Datos', color: 'acento', en: 0.66 },
        { tipo: 'cilindro', x: 610, y: 222, w: 156, h: 125, t: 'Base', s: '5432', color: 'acento', en: 0.68 },
        { tipo: 'flecha', de: [562, 160], a: [614, 236], color: 'malva', grosor: 4, en: 0.68 },
        { tipo: 'texto', t: 'TCP 5432', x: 690, y: 182, tam: 17, color: 'malva', en: 0.72 },
        // 5) La vuelta
        { tipo: 'flecha', de: [210, 308], a: [104, 308], r: 'JSON', dy: 14, tam: 16, color: 'verde', grosor: 4, en: 0.84 },
        { tipo: 'chip', x: 400, y: 500, t: 'la respuesta vuelve por el mismo camino', color: 'verde', en: 0.86 },
        { tipo: 'texto', t: 'Cada salto dentro del centro de datos suma del orden de 1 ms.', x: 400, y: 565, tam: 20, ancho: 760, en: 0.88 }
      ]);
    }
  });
})();
