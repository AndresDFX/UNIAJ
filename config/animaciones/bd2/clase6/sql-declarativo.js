/* SQL dice QUE; el motor decide COMO: analizador -> optimizador (planes candidatos con costo,
 * elige el mas barato) -> ejecutor. Todos los planes dan el mismo resultado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('sql-declarativo', {
    duracion: 5,
    // Pasos LOGICOS: 1) la consulta dice QUE y el analizador la revisa; 2) el optimizador
    // estima el costo de varios planes y elige el mas barato; 3) el ejecutor corre ese plan, y
    // la conclusion: todos los planes devuelven lo mismo. Nada de un paso asoma en el anterior.
    pasos: [0.3, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A;
      // 1 · la consulta y el analizador
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, 40, 30, W - 80, 76, 12); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'La consulta dice QUÉ datos quiere', W / 2, 40, { tam: 22, peso: 700, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'nunca CÓMO obtenerlos', W / 2, 72, { tam: 18, peso: 500 });
      });
      L.flecha(ctx, 145, 108, 145, 142, A, 4, L.tramo(t, 0.08, 0.14, 'frena'));
      UJ.caja(ctx, lz, 30, 146, 230, 110, 'Analizador', 'sintaxis, tablas y columnas', A, L.tramo(t, 0.12, 0.22));
      // 2 · el optimizador y los planes candidatos
      L.flecha(ctx, 262, 201, 292, 201, A, 4, L.tramo(t, 0.32, 0.36, 'frena'));
      UJ.caja(ctx, lz, 296, 146, 230, 110, 'Optimizador', 'estima el costo de cada plan', C, L.tramo(t, 0.34, 0.4));
      var planes = [['Plan A', 'costo 1.240'], ['Plan B', 'costo 85'], ['Plan C', 'costo 9.600']];
      for (var i = 0; i < 3; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.4 + i * 0.05, 0.46 + i * 0.05), function () {
          var x = 80 + i * 225, gana = i === 1 && t > 0.58;
          L.rectRed(ctx, x, 300, 190, 90, 12);
          L.rellena(ctx, gana ? L.tono(V, 0.8) : m.papel, gana ? V : L.tono(m.tinta, 0.5), gana ? 4 : 2);
          UJ.rotulo(ctx, lz, planes[i][0], x + 95, 312, { tam: 22, peso: 800, color: gana ? V : m.tinta });
          UJ.rotulo(ctx, lz, planes[i][1], x + 95, 350, { tam: 18, peso: 600 });
        });
      }
      UJ.sello(ctx, lz, 470, 300, 22, true, L.tramo(t, 0.56, 0.62));
      UJ.rotulo(ctx, lz, 'elige el más barato', W / 2, 404, { tam: 19, peso: 700, color: V, visible: L.tramo(t, 0.58, 0.64) });
      // 3 · el ejecutor y la conclusion
      L.flecha(ctx, 528, 201, 556, 201, A, 4, L.tramo(t, 0.68, 0.72, 'frena'));
      UJ.caja(ctx, lz, 560, 146, 210, 110, 'Ejecutor', 'corre el plan elegido', A, L.tramo(t, 0.7, 0.78));
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.92), function () {
        L.rectRed(ctx, 40, 470, W - 80, 110, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Los tres planes devuelven EXACTAMENTE el mismo resultado', W / 2, 486, { tam: 21, peso: 700, ancho: W - 120 });
        UJ.rotulo(ctx, lz, 'y pueden diferir en tiempo por factores de cien o de mil.', W / 2, 532, { tam: 19, peso: 500, ancho: W - 120 });
      });
    }
  });
})();
