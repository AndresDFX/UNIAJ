/* Therac-25: cuatro decisiones que parecian razonables, una detras de otra, y el resultado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('therac25', {
    duracion: 5,
    // Pasos LOGICOS: una decision por clic (la flecha llega con la caja a la que apunta, no
    // antes) y el resultado al final.
    pasos: [0.16, 0.36, 0.56, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', W = lz.ancho;
      var pasos = [
        ['1 · Se quitaron los seguros físicos', '«el software lo evita»'],
        ['2 · Se reutilizó el código viejo', 'con errores que los seguros tapaban'],
        ['3 · Apareció la falla', 'corregir la pantalla rápido la desconfiguraba'],
        ['4 · Los errores no se entendían', 'un código sin explicación; se ignoraba']
      ];
      var t0 = [0, 0.2, 0.4, 0.6];
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, t0[i] + 0.02, t0[i] + 0.12), y = 30 + i * 112;
        var c = L.mezclaColor(A, R, i / 3);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 40, y, 720, 88, 14); L.rellena(ctx, L.tono(c, 0.88), c, 3);
          UJ.rotulo(ctx, lz, pasos[i][0], 64, y + 12, { tam: 25, peso: 800, color: c, alinear: 'left', ancho: 680 });
          UJ.rotulo(ctx, lz, pasos[i][1], 64, y + 50, { tam: 20, alinear: 'left', ancho: 680 });
        });
        if (i > 0) L.flecha(ctx, 400, y - 22, 400, y - 2, L.tono(m.tinta, 0.4), 3, L.tramo(t, t0[i], t0[i] + 0.04));
      }
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.92), function () {
        L.rectRed(ctx, 40, 482, 720, 120, 14); L.rellena(ctx, R);
        UJ.rotulo(ctx, lz, 'Sobredosis y muertes', W / 2, 496, { tam: 30, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, 'El software hacía lo que estaba programado.', W / 2, 546, { tam: 22, color: m.papel, ancho: 680 });
      });
    }
  });
})();
