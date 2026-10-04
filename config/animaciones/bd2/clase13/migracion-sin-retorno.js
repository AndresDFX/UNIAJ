/* Caso MySpace, 2019: una migracion de servidores sin copia verificada perdio la musica subida
 * entre 2003 y 2015, sin camino de vuelta. Lo que faltaba: plan de retorno probado y conteos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('migracion-sin-retorno', {
    duracion: 5,
    // Pasos LOGICOS: 1) la migracion y lo que se perdio, 2) lo que faltaba (las tres
    // practicas), 3) la leccion, con el caso paralelo de la banca.
    pasos: [0.44, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      function servidor(x, y, nombre, col, a) {
        UJ.alfa(ctx, a, function () {
          for (var k = 0; k < 3; k++) { L.rectRed(ctx, x, y + k * 44, 200, 38, 8); L.rellena(ctx, L.tono(col, 0.8), col, 2); L.circulo(ctx, x + 20, y + 19 + k * 44, 6); L.rellena(ctx, col); }
          UJ.rotulo(ctx, lz, nombre, x + 100, y + 140, { tam: 19, peso: 800, color: col });
        });
      }
      // 1. La migracion y la perdida
      servidor(40, 40, 'servidores viejos', A, 1 - 0.75 * L.tramo(t, 0.3, 0.38));
      servidor(560, 40, 'servidores nuevos', A, L.tramo(t, 0, 0.08));
      for (var i = 0; i < 6; i++) {
        var p = L.tramo(t, 0.08 + i * 0.03, 0.26 + i * 0.03, 'suave'), pierde = i % 2 === 1;
        if (p <= 0 || p >= 1) continue;
        var x = L.mezcla(250, 550, p), y = 70 + i * 16 + (pierde ? 60 * p * p : 0);
        UJ.alfa(ctx, pierde ? 1 - L.tramo(p, 0.6, 1) : 1, function () {
          L.rectRed(ctx, x, y, 34, 26, 4); L.rellena(ctx, pierde ? R : V);
        });
      }
      UJ.rotulo(ctx, lz, 'sin copia verificada', W / 2, 200, { tam: 18, peso: 800, color: R, visible: L.tramo(t, 0.2, 0.28) });
      UJ.sello(ctx, lz, 140, 110, 30, false, L.tramo(t, 0.32, 0.4));
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.42), function () {
        L.rectRed(ctx, 30, 250, 740, 80, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'Música subida entre 2003 y 2015: perdida, sin camino de vuelta', 400, 262, { tam: 20, peso: 700, color: R, ancho: 700 });
      });
      // 2. Lo que faltaba
      UJ.rotulo(ctx, lz, 'Lo que faltaba', 30, 356, { tam: 21, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0.48, 0.52) });
      var falta = ['expandir · migrar · contraer', 'conteos origen = destino', 'plan de retorno probado antes'];
      for (var j = 0; j < 3; j++) UJ.caja(ctx, lz, 30 + j * 250, 394, 236, 90, falta[j], '', V, L.tramo(t, 0.5 + j * 0.06, 0.56 + j * 0.06));
      // 3. La leccion
      UJ.rotulo(ctx, lz, 'Una migración sin retorno probado es una apuesta.', W / 2, 512, { tam: 22, peso: 800, color: A, ancho: W - 40, visible: L.tramo(t, 0.76, 0.88) });
      UJ.rotulo(ctx, lz, 'Mismo patrón en la banca: TSB, Reino Unido, 2018.', W / 2, 566, { tam: 19, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
