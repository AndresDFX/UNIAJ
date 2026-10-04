/* Ilustracion: que observar en la demo de optimizacion. 1) la agenda ANTES y DESPUES devuelve
 * las mismas 91 filas, y el ANTES estima 1 fila; 2) el ranking pasa de loops=2006 a una pasada;
 * 3) las pruebas: 91 = 91 y EXCEPT en los dos sentidos con 0 filas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 10, { tam: 26, peso: 800, color: A });
      var b = [
        ['1 · La agenda del día', 'ANTES y DESPUÉS: las mismas 91 filas', 'el ANTES estima rows=1 y entrega 91', A],
        ['2 · El ranking de dueños', 'ANTES: SubPlan con loops=2006', 'DESPUÉS: un HashAggregate, una pasada', R],
        ['3 · La prueba', 'COUNT(*): 91 = 91', 'EXCEPT en los dos sentidos: 0 filas', V]
      ];
      for (var i = 0; i < 3; i++) {
        var y = 60 + i * 176;
        L.rectRed(ctx, 24, y, W - 48, 160, 16); L.rellena(ctx, L.tono(b[i][3], 0.92), b[i][3], 2);
        L.circulo(ctx, 70, y + 80, 30); L.rellena(ctx, b[i][3]);
        UJ.rotulo(ctx, lz, String(i + 1), 70, y + 62, { tam: 30, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, b[i][0].slice(4), 120, y + 18, { tam: 21, peso: 800, color: L.tono(b[i][3], -0.2), alinear: 'left' });
        UJ.codigo(ctx, lz, 120, y + 58, 620, b[i][1], 1, 16);
        UJ.codigo(ctx, lz, 120, y + 106, 620, b[i][2], 1, 16);
      }
      UJ.rotulo(ctx, lz, 'El ANTES del ranking tarda: no está colgado.', W / 2, 594, { tam: 18, peso: 700, color: R, ancho: W - 40 });
    }
  });
})();
