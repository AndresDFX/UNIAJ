/* El reporte diario de una tienda, en los cinco pasos del ejemplo: el recorrido, lo que se
 * repite (40 veces al dia), la etapa mas pesada (el servidor recalcula el mes entero), la
 * decision y el indicador que la mide (de 40 a 1). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('reporte-tienda', {
    duracion: 5,
    // Pasos LOGICOS, uno por paso del ejemplo. El servidor no se marca en rojo hasta el paso 3:
    // antes de eso, el docente todavia no ha dicho cual es la etapa pesada.
    pasos: [0.18, 0.4, 0.58, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var pesada = L.tramo(t, 0.42, 0.5);
      // 1 · El recorrido
      var nodos = ['Computador de la tienda', 'Internet', 'Servidor', 'Base de datos'];
      for (var i = 0; i < 4; i++) {
        var x = 20 + i * 195, a = L.tramo(t, i * 0.035, i * 0.035 + 0.05);
        UJ.caja(ctx, lz, x, 30, 175, 90, nodos[i], null, i === 2 ? L.mezclaColor(A, R, pesada) : A, a);
        if (i < 3) L.flecha(ctx, x + 177, 75, x + 193, 75, L.tono(m.tinta, 0.4), 3, L.tramo(t, i * 0.035 + 0.04, i * 0.035 + 0.06));
      }
      // 2 · Lo que se repite
      UJ.rotulo(ctx, lz, 'Cada vez que alguien abre el reporte, se genera completo', W / 2, 140, { tam: 21, peso: 600, ancho: W - 60, visible: L.tramo(t, 0.2, 0.26) });
      var n = Math.round(40 * L.tramo(t, 0.22, 0.36));
      for (var k = 0; k < n; k++) {
        var cx = 140 + (k % 10) * 58, cy = 200 + Math.floor(k / 10) * 44;
        L.circulo(ctx, cx, cy, 16); L.rellena(ctx, L.mezclaColor(L.tono(A, 0.55), L.tono(R, 0.35), pesada));
      }
      UJ.rotulo(ctx, lz, n + ' veces al día', W / 2, 360, { tam: 28, peso: 800, color: L.mezclaColor(A, R, pesada), visible: L.tramo(t, 0.22, 0.26) });
      // 3 · La etapa mas pesada
      UJ.rotulo(ctx, lz, 'Lo pesado: el servidor recalcula todo el mes, 40 veces, aunque nada cambió', W / 2, 406, { tam: 20, peso: 700, color: R, ancho: W - 60, visible: L.tramo(t, 0.44, 0.54) });
      // 4 · La decision, y 5 · el indicador
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.72), function () {
        L.rectRed(ctx, 60, 476, 680, 140, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'Guardar el resultado · recalcular solo si hay ventas nuevas', W / 2, 490, { tam: 21, peso: 700, ancho: 640 });
      });
      UJ.rotulo(ctx, lz, 'De 40 a 1 vez al día', W / 2, 556, { tam: 32, peso: 800, color: V, visible: L.tramo(t, 0.82, 0.94) });
    }
  });
})();
