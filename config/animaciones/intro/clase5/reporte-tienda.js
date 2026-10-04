/* El reporte diario de una tienda: el recorrido, las 40 veces que el servidor recalcula el mes
 * entero, y la decision que lo deja en 1. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('reporte-tienda', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var nodos = ['Computador de la tienda', 'Internet', 'Servidor', 'Base de datos'];
      for (var i = 0; i < 4; i++) {
        var x = 20 + i * 195, a = L.tramo(t, i * 0.06, i * 0.06 + 0.08);
        UJ.caja(ctx, lz, x, 40, 175, 90, nodos[i], null, i === 2 ? R : A, a);
        if (i < 3) L.flecha(ctx, x + 177, 85, x + 193, 85, L.tono(m.tinta, 0.4), 3, L.tramo(t, i * 0.06 + 0.06, i * 0.06 + 0.1));
      }
      // 40 recalculos
      UJ.rotulo(ctx, lz, 'Cada vez que alguien abre el reporte, el servidor recalcula todo el mes', W / 2, 160, { tam: 21, peso: 600, ancho: W - 60, visible: L.tramo(t, 0.32, 0.4) });
      var n = Math.round(40 * L.tramo(t, 0.36, 0.58));
      for (var k = 0; k < n; k++) {
        var cx = 140 + (k % 10) * 58, cy = 240 + Math.floor(k / 10) * 46;
        L.circulo(ctx, cx, cy, 16); L.rellena(ctx, L.tono(R, 0.35));
      }
      UJ.rotulo(ctx, lz, n + ' veces al día', W / 2, 424, { tam: 28, peso: 800, color: R, visible: L.tramo(t, 0.36, 0.4) });
      // La decision
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.78), function () {
        L.rectRed(ctx, 60, 480, 680, 130, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'Guardar el resultado · recalcular solo si hay ventas nuevas', W / 2, 496, { tam: 21, peso: 700, ancho: 640 });
        UJ.rotulo(ctx, lz, 'De 40 a 1 vez al día', W / 2, 548, { tam: 32, peso: 800, color: V, visible: L.tramo(t, 0.82, 0.92) });
      });
    }
  });
})();
