/* Por que el promedio miente: 95 peticiones en 120 ms y 5 en 4000 ms. El promedio da 314 ms, que
 * no le paso a nadie; la mediana (p50) es 120 y el p99 es 4000. El percentil hace visibles a los
 * cinco usuarios que esperaron cuatro segundos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('promedio-percentil', {
    duracion: 5,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, base = 420, esc = 300 / 4000;
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: '100 peticiones, ordenadas de menor a mayor', x: 400, y: 14, tam: 22, peso: 700, color: 'accion', ancho: 760, en: 0 },
        { tipo: 'linea', pts: [[40, base], [770, base]], color: 'gris', grosor: 2, en: 0 }
      ]);
      for (var i = 0; i < 100; i++) {
        var v = i < 95 ? 120 : 4000, a = L.tramo(t, 0.02 + i * 0.0025, 0.06 + i * 0.0025);
        if (a <= 0) continue;
        var h = v * esc * a;
        L.rectRed(ctx, 45 + i * 7.2, base - h, 5.4, h, 1); L.rellena(ctx, i < 95 ? L.tono(m.accion, 0.35) : (m.malva || '#A02030'));
      }
      var yp = base - 314 * esc;
      UJ.escena(ctx, t, lz, [
        { tipo: 'linea', pts: [[40, yp], [770, yp]], color: 'malva', grosor: 3, punteada: true, en: 0.38 },
        { tipo: 'chip', x: 330, y: yp - 48, t: 'promedio 314 ms: nadie tardó eso', color: 'malva', en: 0.44 },
        { tipo: 'chip', x: 200, y: base + 20, t: 'p50 = 120 ms', color: 'accion', en: 0.68 },
        { tipo: 'chip', x: 640, y: 70, t: 'p99 = 4000 ms', color: 'malva', en: 0.74 },
        { tipo: 'texto', t: 'Objetivos en percentiles: «p95 < 300 ms con 5 RPS».', x: 400, y: 520, tam: 23, peso: 800, color: 'accion', ancho: 760, en: 0.88 }
      ]);
    }
  });
})();
