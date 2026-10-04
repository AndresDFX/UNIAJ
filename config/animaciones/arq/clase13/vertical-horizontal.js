/* Escalar vertical: mas recursos a la MISMA maquina; simple, pero con techo fisico y con reinicio
 * (30 s a 2 min sin servicio). Escalar horizontal: mas instancias iguales detras del balanceador. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('vertical-horizontal', {
    duracion: 5,
    pasos: [0.45, 1],
    dibujar: function (ctx, t, lz) {
      var crece = L.tramo(t, 0.06, 0.3, 'suave');
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Vertical', x: 200, y: 14, tam: 26, peso: 800, color: 'accion', en: 0 },
        { tipo: 'caja', x: 120 - 40 * crece, y: 330 - 200 * crece, w: 160 + 80 * crece, h: 120 + 200 * crece, t: crece > 0.5 ? '8 vCPU · 32 GB' : '2 vCPU · 8 GB', s: 'la misma máquina', en: 0 },
        { tipo: 'chip', x: 200, y: 470, t: 'techo físico', color: 'malva', en: 0.3 },
        { tipo: 'chip', x: 200, y: 520, t: 'reinicio: 30 s a 2 min', color: 'malva', en: 0.36 },
        { tipo: 'texto', t: 'Horizontal', x: 600, y: 14, tam: 26, peso: 800, color: 'accion', en: 0.48 },
        { tipo: 'caja', x: 500, y: 70, w: 200, h: 70, t: 'Balanceador', lleno: true, tam: 20, en: 0.5 },
        { tipo: 'caja', x: 440, y: 230, w: 100, h: 110, t: 'API', s: '2 vCPU', tam: 18, en: 0.56 },
        { tipo: 'caja', x: 550, y: 230, w: 100, h: 110, t: 'API', s: '2 vCPU', tam: 18, en: 0.62 },
        { tipo: 'caja', x: 660, y: 230, w: 100, h: 110, t: 'API', s: '2 vCPU', tam: 18, en: 0.68 },
        { tipo: 'flecha', de: [560, 145], a: [490, 225], en: 0.58 },
        { tipo: 'flecha', de: [600, 145], a: [600, 225], en: 0.64 },
        { tipo: 'flecha', de: [640, 145], a: [710, 225], en: 0.7 },
        { tipo: 'chip', x: 600, y: 380, t: 'instancias iguales', color: 'accion', en: 0.76 },
        { tipo: 'texto', t: 'Exige algo del código: que la instancia no guarde estado.', x: 600, y: 440, tam: 20, ancho: 330, color: 'malva', en: 0.84 }
      ]);
    }
  });
})();
