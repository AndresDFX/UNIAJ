/* El limite fisico: la instancia nueva no aparece al instante. Un contenedor liviano tarda de 10 a 60 s
 * (descarga de imagen, arranque, conexion a la base, chequeo de salud); una maquina virtual, de 2 a
 * 5 minutos. Un pico mas rapido golpea antes de que llegue la ayuda. */
(function () {
  FP_ANIMADOR.registrar('arranque-no-instantaneo', {
    duracion: 5,
    pasos: [0.5, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Contenedor liviano · 10 a 60 s', x: 30, y: 14, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0 },
        { tipo: 'caja', x: 30, y: 60, w: 175, h: 80, t: 'descargar imagen', tam: 18, color: 'acento', r: 8, en: 0.04 },
        { tipo: 'caja', x: 215, y: 60, w: 175, h: 80, t: 'arrancar proceso', tam: 18, color: 'acento', r: 8, en: 0.1 },
        { tipo: 'caja', x: 400, y: 60, w: 175, h: 80, t: 'conectar a la base', tam: 18, color: 'acento', r: 8, en: 0.16 },
        { tipo: 'caja', x: 585, y: 60, w: 185, h: 80, t: 'pasar /health', tam: 18, color: 'acento', r: 8, en: 0.22 },
        { tipo: 'sello', x: 760, y: 170, r: 22, ok: true, en: 0.3 },
        { tipo: 'texto', t: 'recién ahí recibe tráfico útil', x: 560, y: 160, tam: 19, ancho: 300, en: 0.32 },
        { tipo: 'texto', t: 'Máquina virtual completa', x: 30, y: 230, tam: 23, peso: 800, alinear: 'left', color: 'malva', en: 0.52 },
        { tipo: 'barra', x: 250, y: 280, w: 430, h: 34, valor: 0.2, t: 'contenedor', r: '10-60 s', color: 'accion', en: 0.56, tam: 19 },
        { tipo: 'barra', x: 250, y: 335, w: 430, h: 34, valor: 1, t: 'máquina virtual', color: 'malva', en: 0.6, tam: 19 },
        { tipo: 'texto', t: '2-5 min', x: 695, y: 338, tam: 19, peso: 700, alinear: 'left', color: 'malva', en: 0.68 },
        { tipo: 'texto', t: 'Un pico más rápido que el arranque golpea antes de que llegue la ayuda: por eso el umbral deja holgura.', x: 400, y: 440, tam: 21, ancho: 740, en: 0.8 }
      ]);
    }
  });
})();
