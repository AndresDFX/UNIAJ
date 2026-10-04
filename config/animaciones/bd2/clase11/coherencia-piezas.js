/* Lo que se audita es la coherencia entre piezas: cada artefacto puede estar bien por separado
 * y aun asi describir, juntos, bases distintas (el ER no se actualizo cuando cambio el DDL). Por
 * eso se corren cuatro verificaciones CRUZADAS, cada una entre dos piezas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('coherencia-piezas', {
    duracion: 5,
    // Pasos LOGICOS: 1) las cinco piezas, cada una bien; 2) el ER y el DDL ya no coinciden;
    // 3) las cuatro verificaciones cruzadas; 4) la conclusion.
    pasos: [0.26, 0.5, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var piezas = [['Diagrama ER', 'dibujado en la Clase 1'], ['Script DDL', 'parchado en las Clases 3 a 8'], ['Matriz de roles', 'quién puede qué'],
                    ['Procedimientos', 'la lógica de negocio'], ['Informe de optimización', 'índices y planes']];
      for (var i = 0; i < 5; i++) {
        var y = 20 + i * 104;
        UJ.caja(ctx, lz, 60, y, 360, 84, piezas[i][0], piezas[i][1], A, L.tramo(t, i * 0.03, 0.06 + i * 0.03));
        UJ.sello(ctx, lz, 462, y + 42, 20, true, L.tramo(t, 0.14 + i * 0.015, 0.18 + i * 0.015));
      }
      UJ.rotulo(ctx, lz, 'cada pieza, sola: bien', 650, 22, { tam: 20, peso: 700, color: V, ancho: 250, visible: L.tramo(t, 0.2, 0.25) });
      // 2 · El enlace ER - DDL se rompe
      var r = L.tramo(t, 0.28, 0.38);
      if (r > 0) {
        L.trazo(ctx, [[56, 62], [32, 62], [32, 166], [56, 166]], r, R, 5);
        UJ.sello(ctx, lz, 32, 114, 18, false, L.tramo(t, 0.37, 0.42));
      }
      UJ.alfa(ctx, L.tramo(t, 0.41, 0.48), function () {
        L.rectRed(ctx, 510, 60, 270, 96, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'ER y DDL describen bases distintas', 645, 72, { tam: 19, peso: 800, color: R, ancho: 250 });
        UJ.rotulo(ctx, lz, 'y ninguna de las dos «falla»', 645, 124, { tam: 15, ancho: 250 });
      });
      // 3 · Las cuatro verificaciones cruzadas
      var cruces = [['1', 'el ER contra el DDL'], ['2', 'la matriz contra los GRANT'], ['3', 'los procedimientos contra un CALL real'], ['4', 'el informe contra EXPLAIN antes y después']];
      UJ.rotulo(ctx, lz, 'Cuatro cruces', 645, 176, { tam: 19, peso: 800, color: A, ancho: 270, visible: L.tramo(t, 0.52, 0.56) });
      for (var k = 0; k < 4; k++) {
        UJ.alfa(ctx, L.tramo(t, 0.56 + k * 0.05, 0.61 + k * 0.05), function () {
          var yy = 210 + k * 74;
          L.rectRed(ctx, 510, yy, 270, 62, 10); L.rellena(ctx, L.tono(C, 0.88), C, 2);
          L.circulo(ctx, 534, yy + 31, 15); L.rellena(ctx, C);
          UJ.rotulo(ctx, lz, cruces[k][0], 534, yy + 20, { tam: 17, peso: 800, color: m.papel });
          UJ.rotulo(ctx, lz, cruces[k][1], 662, yy + 10, { tam: 15, peso: 700, ancho: 220 });
        });
      }
      UJ.rotulo(ctx, lz, 'Se audita la coherencia entre piezas, no cada pieza.', W / 2, 560,
                { tam: 22, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.82, 0.98) });
    }
  });
})();
