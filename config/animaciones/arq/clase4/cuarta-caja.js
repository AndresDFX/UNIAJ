/* Tres contenedores de entrada. La cuarta caja aparece solo con una razon: el correo tarda entre
 * 300 y 2000 ms y puede fallar, asi que se saca del camino de la reserva con una cola y un worker. */
(function () {
  FP_ANIMADOR.registrar('cuarta-caja', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 60, w: 200, h: 110, t: 'App web', s: 'React', en: 0.02 },
        { tipo: 'caja', x: 300, y: 60, w: 200, h: 110, t: 'API de turnos', s: 'Node.js', en: 0.06 },
        { tipo: 'cilindro', x: 580, y: 50, w: 200, h: 130, t: 'Base de turnos', s: 'PostgreSQL', color: 'acento', en: 0.1 },
        { tipo: 'flecha', de: [222, 115], a: [296, 115], en: 0.14 },
        { tipo: 'flecha', de: [502, 115], a: [576, 115], en: 0.16 },
        { tipo: 'texto', t: 'Tres contenedores para empezar.', x: 400, y: 215, tam: 22, en: 0.2, sale: 0.3 },
        { tipo: 'caja', x: 300, y: 270, w: 200, h: 90, t: 'Correo', s: 'proveedor externo', color: 'gris', en: 0.34, sale: 0.62 },
        { tipo: 'flecha', de: [400, 172], a: [400, 266], color: 'malva', en: 0.38, sale: 0.62 },
        { tipo: 'texto', t: '300 a 2000 ms y puede fallar: la reserva espera al correo', x: 650, y: 285, tam: 20, ancho: 260, color: 'malva', en: 0.44, sale: 0.62 },
        { tipo: 'caja', x: 300, y: 270, w: 200, h: 90, t: 'Cola', s: 'aviso-de-turno', color: 'sello', en: 0.66 },
        { tipo: 'flecha', de: [400, 172], a: [400, 266], r: 'publica y responde', dx: -100, dy: -12, ancho: 180, en: 0.68 },
        { tipo: 'caja', x: 300, y: 420, w: 200, h: 100, t: 'Worker de avisos', s: 'reintenta', en: 0.74 },
        { tipo: 'flecha', de: [400, 362], a: [400, 416], en: 0.76 },
        { tipo: 'caja', x: 580, y: 425, w: 190, h: 90, t: 'Correo', s: 'externo', color: 'gris', en: 0.8 },
        { tipo: 'flecha', de: [502, 470], a: [576, 470], en: 0.82 },
        { tipo: 'texto', t: 'La cuarta caja existe porque hay una razón.', x: 400, y: 570, tam: 24, peso: 800, color: 'accion', ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
