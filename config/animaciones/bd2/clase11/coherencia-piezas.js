/* Lo que se audita es la coherencia entre piezas: cada artefacto puede estar bien por separado
 * y aun asi describir, juntos, bases distintas (el ER no se actualizo cuando cambio el DDL). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('coherencia-piezas', {
    duracion: 4.6,
    pasos: [0.36, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var piezas = [['Diagrama ER', 'dibujado al inicio'], ['Script DDL', 'parchado después'], ['Matriz de roles', 'quién ve qué'],
                    ['Procedimientos', 'la lógica'], ['Informe de optimización', 'índices y planes']];
      for (var i = 0; i < 5; i++) {
        var y = 20 + i * 104;
        UJ.caja(ctx, lz, 60, y, 360, 84, piezas[i][0], piezas[i][1], A, L.tramo(t, i * 0.05, 0.1 + i * 0.05));
        UJ.sello(ctx, lz, 470, y + 42, 22, true, L.tramo(t, 0.3 + i * 0.012, 0.36 + i * 0.012));
      }
      UJ.rotulo(ctx, lz, 'cada pieza, sola: bien', 600, 230, { tam: 20, peso: 700, color: V, ancho: 230, visible: L.tramo(t, 0.28, 0.36) });
      // El enlace ER - DDL se rompe
      var r = L.tramo(t, 0.4, 0.55);
      if (r > 0) {
        L.trazo(ctx, [[40, 62], [24, 62], [24, 166], [40, 166]], r, R, 5);
        UJ.sello(ctx, lz, 24, 114, 18, false, L.tramo(t, 0.52, 0.6));
      }
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.7), function () {
        L.rectRed(ctx, 520, 50, 260, 120, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'ER y DDL describen bases distintas', 650, 68, { tam: 20, peso: 700, color: R, ancho: 230 });
      });
      UJ.rotulo(ctx, lz, 'Se audita la coherencia entre piezas, no cada pieza.', W / 2, 560,
                { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.8, 1) });
    }
  });
})();
