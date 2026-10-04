/* La cuarta pregunta: por que la regla en un disparador. La cobertura: la aplicacion, un script de
 * carga y un cliente SQL a mano escriben en la tabla; el disparador los ataja a los tres, la
 * validacion en la aplicacion solo al primero. Y el contra-argumento: es logica invisible. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('trigger-cobertura', {
    duracion: 5,
    // Pasos LOGICOS: 1) la regla en la aplicacion: solo la cumple quien pasa por ella, 2) la
    // regla en el disparador: la cumplen los tres, 3) el argumento y su contra-argumento.
    pasos: [0.44, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var quien = ['Aplicación', 'Script de carga', 'Cliente SQL a mano'];
      function escena(y0, titulo, enApp, a, p) {
        UJ.rotulo(ctx, lz, titulo, 30, y0, { tam: 21, peso: 800, alinear: 'left', color: enApp ? R : V, visible: a });
        UJ.alfa(ctx, a, function () {
          for (var i = 0; i < 3; i++) {
            L.rectRed(ctx, 30, y0 + 40 + i * 62, 220, 50, 10); L.rellena(ctx, L.tono(A, 0.9), A, 2);
            UJ.rotulo(ctx, lz, quien[i], 140, y0 + 53 + i * 62, { tam: 18, peso: 700 });
          }
          UJ.tabla(ctx, lz, 590, y0 + 70, 180, 'insumo', ['stock ≥ 0'], 1, A, -1);
          if (enApp) { L.rectRed(ctx, 262, y0 + 40, 26, 50, 6); L.rellena(ctx, C); UJ.rotulo(ctx, lz, 'regla', 275, y0 + 96, { tam: 15, peso: 700, color: C }); }
          else { L.rectRed(ctx, 500, y0 + 40, 30, 174, 8); L.rellena(ctx, C); UJ.rotulo(ctx, lz, 'trigger', 515, y0 + 220, { tam: 16, peso: 800, color: C }); }
        });
        for (var k = 0; k < 3; k++) {
          var ok = enApp ? k === 0 : true, yy = y0 + 65 + k * 62;
          L.flecha(ctx, 254, yy, 584, y0 + 112, ok ? V : R, 3, L.tramo(p, k * 0.25, 0.35 + k * 0.25));
          UJ.sello(ctx, lz, 380, (yy + y0 + 112) / 2, 15, ok, L.tramo(p, 0.3 + k * 0.25, 0.4 + k * 0.25));
        }
      }
      escena(10, 'Regla en la aplicación', true, L.tramo(t, 0, 0.08), L.tramo(t, 0.08, 0.42));
      escena(262, 'Regla en el disparador', false, L.tramo(t, 0.46, 0.54), L.tramo(t, 0.54, 0.84));
      UJ.alfa(ctx, L.tramo(t, 0.88, 0.98), function () {
        L.rectRed(ctx, 30, 516, 740, 104, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'A favor: se cumple no importa quién escriba (cobertura).', W / 2, 528, { tam: 19, peso: 800, color: A, ancho: 700 });
        UJ.rotulo(ctx, lz, 'En contra: es lógica invisible. Solo para integridad y auditoría.', W / 2, 570, { tam: 18, peso: 700, color: R, ancho: 700 });
      });
    }
  });
})();
