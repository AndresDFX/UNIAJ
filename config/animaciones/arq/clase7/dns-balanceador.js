/* El DNS traduce el nombre a una IP (y la respuesta se guarda en cache por su TTL). El balanceador
 * termina el TLS y reparte entre instancias; su funcion mas importante es el chequeo de salud:
 * la instancia que no responde deja de recibir trafico. */
(function () {
  FP_ANIMADOR.registrar('dns-balanceador', {
    duracion: 5,
    // Pasos LOGICOS: 1) el DNS traduce el nombre a la IP (y su TTL), 2) el balanceador termina el
    // TLS y reparte entre dos instancias, 3) el chequeo de salud saca a la que no responde.
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1) DNS
        { tipo: 'persona', x: 70, y: 40, tam: 64, t: 'navegador', color: 'accion', en: 0 },
        { tipo: 'caja', x: 250, y: 30, w: 300, h: 90, t: 'DNS · registro A', s: 'turnos.example → 203.0.113.10', tamSub: 17, en: 0.04 },
        { tipo: 'flecha', de: [125, 75], a: [245, 75], en: 0.08 },
        { tipo: 'chip', x: 670, y: 55, t: 'TTL: segundos en caché', color: 'acento', en: 0.18 },
        // 2) Balanceador e instancias
        { tipo: 'caja', x: 250, y: 210, w: 300, h: 100, t: 'Balanceador', s: 'aquí termina el TLS', lleno: true, en: 0.32 },
        { tipo: 'flecha', de: [100, 135], a: [245, 250], r: 'HTTPS 443', dx: -40, dy: 10, en: 0.34 },
        { tipo: 'caja', x: 90, y: 420, w: 230, h: 90, t: 'API instancia 1', s: '8080', en: 0.4 },
        { tipo: 'caja', x: 480, y: 420, w: 230, h: 90, t: 'API instancia 2', s: '8080', en: 0.42 },
        { tipo: 'flecha', de: [350, 315], a: [220, 415], r: 'HTTP', dx: -60, dy: -10, en: 0.44 },
        { tipo: 'flecha', de: [450, 315], a: [585, 415], en: 0.45, sale: 0.68 },
        // 3) Chequeo de salud
        { tipo: 'chip', x: 400, y: 345, t: 'GET /health', color: 'acento', en: 0.62 },
        { tipo: 'tacha', x: 480, y: 420, w: 230, h: 90, en: 0.72 },
        { tipo: 'texto', t: 'no responde: deja de recibir tráfico', x: 595, y: 530, tam: 19, color: 'malva', ancho: 250, en: 0.76 },
        { tipo: 'texto', t: 'El chequeo de salud es lo que hace útil al balanceador.', x: 400, y: 590, tam: 21, ancho: 760, en: 0.86 }
      ]);
    }
  });
})();
