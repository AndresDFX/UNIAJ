/* El escenario de carga con aritmetica de servilleta: 1000 usuarios x 20 peticiones = 20 000 al dia;
 * el 40 % en dos horas son 8000 en 7200 s, algo mas de 1 RPS; con un factor de pico de 3 a 5, se
 * dimensiona para unos 5 RPS. */
(function () {
  FP_ANIMADOR.registrar('aritmetica-servilleta', {
    duracion: 5,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 40, y: 30, w: 720, h: 100, t: '1000 usuarios × 20 peticiones', s: '= 20 000 peticiones al día', en: 0.02 },
        { tipo: 'flecha', de: [400, 135], a: [400, 165], en: 0.3 },
        { tipo: 'caja', x: 40, y: 170, w: 720, h: 100, t: '40 % en una ventana de 2 horas', s: '8000 peticiones / 7200 s ≈ 1,1 RPS en la hora pico', color: 'acento', en: 0.32 },
        { tipo: 'flecha', de: [400, 275], a: [400, 305], en: 0.6 },
        { tipo: 'caja', x: 40, y: 310, w: 720, h: 100, t: 'factor de pico × 3 a 5', s: 'el tráfico real llega en ráfagas', color: 'malva', en: 0.62 },
        { tipo: 'chip', x: 400, y: 440, t: 'se dimensiona para ≈ 5 RPS', color: 'accion', tam: 24, en: 0.72 },
        { tipo: 'texto', t: 'Un escenario razonado sin ejecución vale más que una ejecución sin objetivo.', x: 400, y: 540, tam: 21, ancho: 740, en: 0.86 }
      ]);
    }
  });
})();
