/* Los tres fenomenos indeseables. Lectura sucia: T2 ve una cita que T1 luego deshace. Lectura no
 * repetible: el mismo stock leido dos veces da 3 y luego 0. Fantasma: el mismo conteo da 4 y luego
 * 5 porque aparecio una fila nueva. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('tres-fenomenos', {
    duracion: 5,
    pasos: [0.33, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      function panel(y, titulo, color, a, celdas, remate, ar) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 20, y, W - 40, 190, 16); L.rellena(ctx, L.tono(color, 0.93), color, 2);
          UJ.rotulo(ctx, lz, titulo, 40, y + 12, { tam: 21, peso: 800, color: color, alinear: 'left', ancho: 700 });
        });
        for (var i = 0; i < celdas.length; i++) {
          var cx = 40 + i * 248;
          UJ.alfa(ctx, L.tramo(ar, i / 3, (i + 1) / 3), function () {
            L.rectRed(ctx, cx, y + 52, 230, 74, 10); L.rellena(ctx, m.papel, L.tono(color, 0.4), 2);
            UJ.rotulo(ctx, lz, celdas[i], cx + 115, y + 62, { tam: 17, ancho: 214 });
            if (i < 2) L.flecha(ctx, cx + 232, y + 89, cx + 246, y + 89, color, 2, 1);
          });
        }
        UJ.rotulo(ctx, lz, remate, W / 2, y + 144, { tam: 19, peso: 700, color: color, ancho: 720, visible: L.tramo(ar, 0.9, 1) });
      }
      panel(16, 'Lectura sucia (dirty read)', R, L.tramo(t, 0, 0.04),
        ['T1 inserta cita 10:00, sin COMMIT', 'T2 la ve: «franja ocupada»', 'T1 hace ROLLBACK'],
        'T2 decidió con un dato que jamás fue real', L.tramo(t, 0.04, 0.3));
      panel(222, 'Lectura no repetible', C, L.tramo(t, 0.34, 0.38),
        ['T1 lee el stock del insumo 2: 3', 'T2 vende 3 y hace COMMIT', 'T1 relee el mismo stock: 0'],
        'la misma fila, dos valores dentro de una transacción', L.tramo(t, 0.38, 0.64));
      panel(428, 'Lectura fantasma', A, L.tramo(t, 0.67, 0.71),
        ['T1 cuenta citas del martes: 4', 'T2 inserta otra y confirma', 'T1 vuelve a contar: 5'],
        'apareció una fila nueva que cumple el criterio', L.tramo(t, 0.71, 0.98));
    }
  });
})();
