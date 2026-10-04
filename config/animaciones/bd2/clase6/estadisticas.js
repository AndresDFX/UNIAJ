/* ANALYZE deja metadatos de la tabla: filas, paginas, valores distintos, nulos y como se reparten
 * los valores. El optimizador decide con ellos, sin leer los datos. Cifras reales de la base
 * sembrada (pg_class y pg_stats tras ANALYZE cita). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('estadisticas', {
    duracion: 5,
    // Pasos LOGICOS: 1) ANALYZE recorre la tabla y deja los numeros generales; 2) el reparto de
    // los valores (concentrado en estado, parejo en fecha_hora); 3) la conclusion.
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // 1 · ANALYZE y los numeros generales
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        UJ.tabla(ctx, lz, 30, 40, 220, 'cita', ['fecha_hora', 'estado', 'id_mascota', '…'], 4, A);
      });
      UJ.alfa(ctx, L.tramo(t, 0.08, 0.14), function () { UJ.codigo(ctx, lz, 262, 96, 126, 'ANALYZE', 1, 18); });
      L.flecha(ctx, 270, 160, 386, 160, C, 5, L.tramo(t, 0.1, 0.16, 'frena'));
      var datos = [['filas', '30.010'], ['páginas de 8 KB', '251'], ['distintos en estado', '3'], ['distintos en fecha_hora', '1.810'], ['fracción de nulos', '0']];
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.26), function () {
        L.rectRed(ctx, 400, 30, 370, 250, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Estadísticas (metadatos)', 585, 40, { tam: 20, peso: 800, color: L.tono(C, -0.3) });
        for (var i = 0; i < datos.length; i++) {
          UJ.rotulo(ctx, lz, datos[i][0], 416, 84 + i * 38, { tam: 17, peso: 600, alinear: 'left' });
          UJ.rotulo(ctx, lz, datos[i][1], 754, 84 + i * 38, { tam: 18, peso: 800, alinear: 'right', color: A });
        }
      });
      // 2 · como se reparten los valores
      UJ.rotulo(ctx, lz, 'Y cómo se reparten los valores', W / 2, 302, { tam: 21, peso: 800, color: A, visible: L.tramo(t, 0.32, 0.38) });
      UJ.rotulo(ctx, lz, 'estado: concentrado', 210, 344, { tam: 18, peso: 700, visible: L.tramo(t, 0.34, 0.4) });
      UJ.rotulo(ctx, lz, 'fecha_hora: parejo', 590, 344, { tam: 18, peso: 700, visible: L.tramo(t, 0.34, 0.4) });
      L.trazo(ctx, [[60, 522], [360, 522]], L.tramo(t, 0.36, 0.42), m.tinta, 3);
      L.trazo(ctx, [[440, 522], [740, 522]], L.tramo(t, 0.36, 0.42), m.tinta, 3);
      var est = [['PROG.', 0.61], ['ATEND.', 0.30], ['CANC.', 0.09]];
      for (var b = 0; b < 3; b++) {
        var h = 220 * est[b][1] / 0.61 * 0.6 * L.tramo(t, 0.42 + b * 0.04, 0.52 + b * 0.04, 'suave');
        if (h > 0) { L.rectRed(ctx, 80 + b * 95, 520 - h, 70, h, 4); L.rellena(ctx, b === 0 ? C : L.tono(A, 0.4)); }
        UJ.rotulo(ctx, lz, est[b][0] + ' ' + Math.round(est[b][1] * 100) + ' %', 115 + b * 95, 530, { tam: 14, peso: 700, visible: L.tramo(t, 0.52 + b * 0.04, 0.58 + b * 0.04) });
      }
      for (var d = 0; d < 8; d++) {
        var hd = 60 * L.tramo(t, 0.44 + d * 0.02, 0.54 + d * 0.02, 'suave');
        if (hd > 0) { L.rectRed(ctx, 452 + d * 36, 520 - hd, 28, hd, 4); L.rellena(ctx, L.tono(A, 0.4)); }
      }
      UJ.rotulo(ctx, lz, '150 citas cada día', 590, 530, { tam: 14, peso: 700, visible: L.tramo(t, 0.6, 0.66) });
      // 3 · la conclusion
      UJ.rotulo(ctx, lz, 'El optimizador decide con esto, sin leer los datos.', W / 2, 580,
                { tam: 21, ancho: W - 40, color: A, visible: L.tramo(t, 0.8, 0.98) });
    }
  });
})();
