/* El guion de humo: arranque en orden y cinco pasos que se marcan. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('guion-humo', {
    duracion: 4.5,
    // Pasos LOGICOS: 1) el arranque en el main, en su orden; 2) los cinco pasos del guion de
    // humo; 3) cada paso en verde y la regla de repetirlo tras cada cambio.
    pasos: [0.35, 0.65, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Arranque en el main, en este orden', W / 2, 20, { tam: 22, peso: 700, visible: L.tramo(t, 0, 0.06) });
      var orden = ['repositorio', 'servicio', 'cargar()', 'ventana'];
      for (var i = 0; i < 4; i++) {
        var x = 30 + i * 192;
        UJ.caja(ctx, lz, x, 62, 160, 70, String(i + 1), orden[i], A, L.tramo(t, 0.04 + i * 0.07, 0.11 + i * 0.07));
        if (i < 3) { var a = L.tramo(t, 0.1 + i * 0.07, 0.15 + i * 0.07); if (a > 0) L.flecha(ctx, x + 162, 97, x + 190, 97, A, 4, a); }
      }
      UJ.rotulo(ctx, lz, 'Guion de humo: 5 pasos, siempre los mismos', W / 2, 166, { tam: 22, peso: 700, visible: L.tramo(t, 0.38, 0.45) });
      // Los mismos cinco de la lamina: abrir con datos, registrar, buscar por id, cerrar guardando, reabrir.
      var pasos = ['Abrir: la tabla trae los datos del archivo', 'Registrar a Luna: aparece en la tabla', 'Buscar por id M-001: sale su ficha', 'Cerrar: guarda y avisa cuántas', 'Reabrir: Luna sigue ahí'];
      for (var k = 0; k < 5; k++) {
        var y = 212 + k * 66;
        UJ.alfa(ctx, L.tramo(t, 0.4 + k * 0.04, 0.46 + k * 0.04), function () {
          L.rectRed(ctx, 60, y, 560, 54, 10); L.rellena(ctx, L.tono(A, 0.92), L.tono(A, 0.4), 2);
          UJ.rotulo(ctx, lz, (k + 1) + '. ' + pasos[k], 80, y + 14, { tam: 21, peso: 600, alinear: 'left', ancho: 520 });
        });
        UJ.sello(ctx, lz, 670, y + 27, 22, true, L.tramo(t, 0.68 + k * 0.05, 0.74 + k * 0.05));
      }
      UJ.rotulo(ctx, lz, 'Tras cada cambio, se repite completo.', W / 2, 560, { tam: 21, ancho: W - 40, visible: L.tramo(t, 0.92, 0.98) });
    }
  });
})();
