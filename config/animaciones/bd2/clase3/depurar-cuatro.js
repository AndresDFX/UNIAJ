/* Depurar sin depurador: cuatro movimientos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('depurar-cuatro', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var mov = [
        ['1 · ¿Qué error leo?', 'CREATE → sintaxis, con línea · CALL → ejecución, nombres', null],
        ['2 · Dejar trazas', null, "RAISE NOTICE 'paso 2, v_activa = %', v_activa;"],
        ['3 · Aislar', null, 'SELECT activa FROM mascota WHERE id_mascota = 3;'],
        ['4 · Casos deliberados', 'uno correcto y tres de error, cada uno en su bloque', null]
      ];
      var tiempos = [0.02, 0.32, 0.57, 0.82];
      for (var i = 0; i < 4; i++) {
        var y = 20 + i * 150, a = L.tramo(t, tiempos[i], tiempos[i] + 0.08);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 20, y, W - 40, 130, 14); L.rellena(ctx, L.tono(i % 2 ? C : A, 0.92), i % 2 ? C : A, 3);
          UJ.rotulo(ctx, lz, mov[i][0], 40, y + 14, { tam: 24, peso: 800, color: i % 2 ? C : A, alinear: 'left' });
          if (mov[i][1]) UJ.rotulo(ctx, lz, mov[i][1], 40, y + 60, { tam: 19, alinear: 'left', ancho: W - 90 });
        });
        if (mov[i][2]) UJ.alfa(ctx, a, function () {
          UJ.codigo(ctx, lz, 40, y + 58, W - 80, mov[i][2], L.tramo(t, tiempos[i] + 0.04, tiempos[i] + 0.16), 17);
        });
      }
    }
  });
})();
