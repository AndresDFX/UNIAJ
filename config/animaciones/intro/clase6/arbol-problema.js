/* El arbol del problema, leido de abajo hacia arriba: causas de fondo, causas directas, el
 * tronco (el problema) y las ramas (los efectos). El proyecto ataca una causa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('arbol-problema', {
    duracion: 5,
    // Pasos LOGICOS, de abajo hacia arriba: 1) causas de fondo (con el sentido de lectura),
    // 2) causas directas, 3) el problema, 4) los efectos, 5) la regla: el proyecto ataca una causa.
    pasos: [0.2, 0.4, 0.6, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, S = m.sello || C, R = m.malva || '#A02030', W = lz.ancho;
      var cafe = '#7A5230';
      // Suelo
      L.rectRed(ctx, 0, 330, W, 6, 0); L.rellena(ctx, L.tono(cafe, 0.4));
      // 1 · Causas de fondo (abajo)
      var a1 = L.tramo(t, 0, 0.1);
      L.trazo(ctx, [[400, 420], [250, 520]], a1, cafe, 8);
      L.trazo(ctx, [[400, 420], [550, 520]], a1, cafe, 8);
      UJ.caja(ctx, lz, 60, 520, 330, 90, 'CAUSAS DE FONDO', 'aquí está lo que se puede cambiar', V, L.tramo(t, 0.04, 0.12));
      UJ.caja(ctx, lz, 410, 520, 330, 90, 'CAUSAS DE FONDO', 'el porqué de cada causa', V, L.tramo(t, 0.06, 0.14));
      UJ.rotulo(ctx, lz, 'se lee ↑', 720, 250, { tam: 20, peso: 700, visible: L.tramo(t, 0.1, 0.16) });
      // 2 · Causas directas
      L.trazo(ctx, [[400, 336], [400, 420]], L.tramo(t, 0.22, 0.3), cafe, 12);
      UJ.caja(ctx, lz, 230, 360, 340, 70, 'CAUSAS DIRECTAS', 'dos o tres, no diez', C, L.tramo(t, 0.24, 0.34));
      // 3 · Tronco = problema
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () {
        L.rectRed(ctx, 370, 200, 60, 130, 6); L.rellena(ctx, cafe);
      });
      UJ.caja(ctx, lz, 200, 220, 400, 80, 'PROBLEMA · el tronco', 'a quién le pasa qué', A, L.tramo(t, 0.46, 0.56));
      // 4 · Ramas = efectos
      var a4 = L.tramo(t, 0.62, 0.7);
      L.trazo(ctx, [[400, 200], [220, 110]], a4, cafe, 8);
      L.trazo(ctx, [[400, 200], [580, 110]], a4, cafe, 8);
      UJ.caja(ctx, lz, 40, 40, 330, 80, 'EFECTOS · ramas', 'quejas, demoras: síntomas', R, L.tramo(t, 0.66, 0.74));
      UJ.caja(ctx, lz, 430, 40, 330, 80, 'EFECTOS · ramas', 'lo que se ve y duele', R, L.tramo(t, 0.68, 0.76));
      // 5 · Donde ataca el proyecto
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 20, 448, 270, 48, 24); L.rellena(ctx, S, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'el proyecto ataca aquí ↓', 155, 460, { tam: 18, peso: 800, ancho: 260 });
      });
    }
  });
})();
