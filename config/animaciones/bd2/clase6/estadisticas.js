/* ANALYZE deja metadatos de la tabla: filas, bloques, distintos, nulos e histograma. El
 * optimizador decide con ellos, sin leer los datos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('estadisticas', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        UJ.tabla(ctx, lz, 30, 40, 220, 'cita', ['fecha_hora', 'estado', 'id_mascota', '…'], 4, A);
      });
      UJ.alfa(ctx, L.tramo(t, 0.12, 0.2), function () { UJ.codigo(ctx, lz, 262, 96, 126, 'ANALYZE', 1, 18); });
      L.flecha(ctx, 270, 160, 386, 160, C, 5, L.tramo(t, 0.14, 0.22, 'frena'));
      var datos = [['filas', '30.010'], ['bloques', 'del orden de 240'], ['valores distintos', 'por columna'], ['fracción de nulos', 'por columna']];
      UJ.alfa(ctx, L.tramo(t, 0.2, 0.3), function () {
        L.rectRed(ctx, 400, 40, 370, 236, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Estadísticas (metadatos)', 585, 52, { tam: 20, peso: 800, color: L.tono(C, -0.3) });
        for (var i = 0; i < 4; i++) {
          UJ.rotulo(ctx, lz, datos[i][0], 418, 100 + i * 42, { tam: 17, peso: 600, alinear: 'left' });
          UJ.rotulo(ctx, lz, datos[i][1], 752, 100 + i * 42, { tam: 17, peso: 800, alinear: 'right', color: A });
        }
      });
      // Histograma
      var alt = [30, 45, 60, 120, 150, 110, 70, 40, 25, 20];
      UJ.rotulo(ctx, lz, 'Histograma: los valores repartidos en cubos', W / 2, 306, { tam: 20, peso: 700, visible: L.tramo(t, 0.34, 0.42) });
      L.trazo(ctx, [[90, 502], [710, 502]], L.tramo(t, 0.36, 0.44), m.tinta, 3);
      for (var b = 0; b < alt.length; b++) {
        var h = alt[b] * L.tramo(t, 0.4 + b * 0.02, 0.5 + b * 0.02, 'suave');
        if (h <= 0) continue;
        L.rectRed(ctx, 110 + b * 60, 500 - h, 46, h, 4); L.rellena(ctx, b >= 3 && b <= 5 ? C : L.tono(A, 0.4));
      }
      UJ.rotulo(ctx, lz, '¿parejos o concentrados?', 400, 514, { tam: 18, peso: 700, color: L.tono(C, -0.3), visible: L.tramo(t, 0.62, 0.7) });
      UJ.rotulo(ctx, lz, 'El optimizador decide con esto, sin leer los datos.', W / 2, 572,
                { tam: 21, ancho: W - 40, color: A, visible: L.tramo(t, 0.8, 1) });
    }
  });
})();
