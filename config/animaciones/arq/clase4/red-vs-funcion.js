/* Lo que se paga al distribuir: la llamada a una funcion del mismo proceso cuesta nanosegundos y
 * no falla por red; la misma llamada como peticion HTTP entre contenedores cuesta de 1 a 5 ms y
 * puede perderse. */
(function () {
  FP_ANIMADOR.registrar('red-vs-funcion', {
    duracion: 5,
    pasos: [0.38, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Dentro del mismo proceso', x: 30, y: 20, tam: 24, peso: 800, alinear: 'left', color: 'accion', en: 0 },
        { tipo: 'caja', x: 30, y: 70, w: 740, h: 140, en: 0.02, color: 'accion', t: '' },
        { tipo: 'caja', x: 60, y: 100, w: 220, h: 80, t: 'reservar()', color: 'accion', r: 8, en: 0.06 },
        { tipo: 'flecha', de: [285, 140], a: [480, 140], r: 'llamada a función', dy: -30, en: 0.1 },
        { tipo: 'caja', x: 485, y: 100, w: 250, h: 80, t: 'validarFranja()', color: 'accion', r: 8, en: 0.14 },
        { tipo: 'chip', x: 400, y: 222, t: 'nanosegundos · no falla por red', color: 'accion', en: 0.22 },
        { tipo: 'texto', t: 'Entre dos contenedores', x: 30, y: 300, tam: 24, peso: 800, alinear: 'left', color: 'malva', en: 0.4 },
        { tipo: 'caja', x: 30, y: 350, w: 220, h: 100, t: 'API de turnos', s: 'contenedor', en: 0.44 },
        { tipo: 'caja', x: 550, y: 350, w: 220, h: 100, t: 'Servicio de agenda', s: 'contenedor', tam: 20, en: 0.48 },
        { tipo: 'flecha', de: [255, 400], a: [545, 400], r: 'HTTP por la red', dy: -32, color: 'malva', en: 0.52 },
        { tipo: 'chip', x: 400, y: 470, t: '1 a 5 ms', color: 'malva', en: 0.6 },
        { tipo: 'chip', x: 400, y: 530, t: 'puede tardar, perderse o fallar', color: 'malva', lleno: false, en: 0.78 },
        { tipo: 'texto', t: 'Distribuir no es gratis.', x: 400, y: 590, tam: 24, peso: 800, color: 'accion', en: 0.9 }
      ]);
    }
  });
})();
