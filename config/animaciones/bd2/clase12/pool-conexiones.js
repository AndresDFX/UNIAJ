/* El pool de conexiones: abrir una conexion cuesta decenas de milisegundos y la consulta 2-3 ms.
 * El pool presta conexiones ya abiertas y las recupera; si una ruta no la devuelve, se agota. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pool-conexiones', {
    duracion: 5,
    pasos: [0.32, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // 1. Sin pool: el tramite domina
      UJ.rotulo(ctx, lz, 'Abrir y cerrar en cada consulta', 30, 14, { tam: 21, peso: 800, color: A, alinear: 'left' });
      var p = L.tramo(t, 0.04, 0.22, 'suave');
      if (p > 0) {
        L.rectRed(ctx, 30, 54, 640 * p, 46, 6); L.rellena(ctx, L.tono(R, 0.7));
        UJ.rotulo(ctx, lz, 'abrir: TCP · autenticar · proceso nuevo en el servidor (decenas de ms)', 44, 66, { tam: 16, peso: 700, alinear: 'left', visible: L.tramo(t, 0.16, 0.24) });
      }
      var q = L.tramo(t, 0.22, 0.27);
      if (q > 0) { L.rectRed(ctx, 674, 54, 40 * q, 46, 6); L.rellena(ctx, V); }
      UJ.rotulo(ctx, lz, 'consulta 2-3 ms', 694, 106, { tam: 16, peso: 700, color: V, visible: L.tramo(t, 0.24, 0.3) });
      UJ.rotulo(ctx, lz, 'casi todo el tiempo es trámite', 30, 112, { tam: 18, peso: 700, color: R, alinear: 'left', visible: L.tramo(t, 0.26, 0.32) });
      // 2. Pool
      UJ.rotulo(ctx, lz, 'Pool: conexiones ya abiertas, prestadas y devueltas', 30, 170, { tam: 21, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0.34, 0.38) });
      var fuga = L.tramo(t, 0.72, 0.86);
      for (var i = 0; i < 10; i++) {
        var x = 60 + i * 70, perdida = fuga * 10 > i + 0.01 ? 1 : 0;
        var presta = Math.sin(Math.PI * L.tramo(t, 0.4 + (i % 5) * 0.03, 0.52 + (i % 5) * 0.03));
        var y = 290 - 50 * presta * (1 - perdida);
        UJ.alfa(ctx, L.tramo(t, 0.34 + i * 0.006, 0.4 + i * 0.006), function () {
          L.circulo(ctx, x, y, 22); L.rellena(ctx, perdida ? R : L.tono(A, 0.4), m.papel, 3);
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.42), function () {
        L.rectRed(ctx, 30, 320, 740, 4, 2); L.rellena(ctx, L.tono(m.tinta, 0.5));
        UJ.rotulo(ctx, lz, '≈ 10 para empezar; se sube solo midiendo', W / 2, 334, { tam: 17, peso: 600 });
      });
      // 3. Fuga
      UJ.rotulo(ctx, lz, 'Fuga: una ruta sin finally no devuelve la conexión', 30, 390, { tam: 21, peso: 800, color: R, alinear: 'left', ancho: 740, visible: L.tramo(t, 0.68, 0.74) });
      for (var k = 0; k < 5; k++) UJ.alfa(ctx, L.tramo(t, 0.88 + k * 0.015, 0.92 + k * 0.015), function () {
        L.rectRed(ctx, 60 + k * 60, 450, 48, 40, 8); L.rellena(ctx, L.tono(C, 0.7), C, 2);
      });
      UJ.rotulo(ctx, lz, 'pool agotado: las peticiones esperan', 400, 458, { tam: 19, peso: 700, color: R, alinear: 'left', visible: L.tramo(t, 0.9, 0.96) });
      UJ.rotulo(ctx, lz, 'Funciona media hora y después no responde.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.94, 1) });
    }
  });
})();
