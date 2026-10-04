/* Correlacionada: menciona una columna de la consulta exterior -> se ejecuta una vez por fila.
 * Es la consulta de la lamina de codigo: contar las mascotas de cada dueno. 2.006 duenos =
 * 2.006 ejecuciones, cada una recorre las 5.008 mascotas (unos 10 millones de filas leidas).
 * Con LEFT JOIN + GROUP BY: una sola pasada. Medido en la base sembrada. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('subconsulta-correlacionada', {
    duracion: 5,
    // Pasos LOGICOS: 1) la version ANTES y su costo; 2) la reescritura en una pasada;
    // 3) la conclusion: mismo resultado.
    pasos: [0.5, 0.85, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // 1 · ANTES
      UJ.caja(ctx, lz, 30, 30, 220, 100, 'dueno', '2.006 filas', A, L.tramo(t, 0, 0.08));
      UJ.caja(ctx, lz, 530, 30, 240, 100, 'subconsulta', 'cuenta sus mascotas', R, L.tramo(t, 0.06, 0.14));
      for (var i = 0; i < 6; i++) {
        var p = L.tramo(t, 0.14 + i * 0.04, 0.2 + i * 0.04, 'frena');
        if (p > 0) L.flecha(ctx, 254, 50 + i * 12, 526, 50 + i * 12, R, 2, p);
      }
      UJ.rotulo(ctx, lz, 'una vez por cada dueño', 390, 140, { tam: 18, peso: 700, color: R, visible: L.tramo(t, 0.14, 0.2) });
      var n = Math.round(2006 * L.tramo(t, 0.14, 0.44, 'suave'));
      var txt = n >= 1000 ? Math.floor(n / 1000) + '.' + String(n % 1000 + 1000).slice(1) : String(n);
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.2), function () {
        L.rectRed(ctx, 170, 180, 460, 90, 14); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'ejecuciones: ' + txt + '  (loops=2006)', 400, 190, { tam: 24, peso: 800, color: R, ancho: 440 });
        UJ.rotulo(ctx, lz, '2.006 × 5.008 mascotas ≈ 10 millones de filas leídas', 400, 232, { tam: 17, peso: 600, visible: L.tramo(t, 0.42, 0.48) });
      });
      // 2 · DESPUES
      UJ.rotulo(ctx, lz, 'Reescrita con LEFT JOIN + GROUP BY', W / 2, 304, { tam: 22, peso: 800, color: V, visible: L.tramo(t, 0.54, 0.6) });
      UJ.caja(ctx, lz, 30, 350, 210, 90, 'dueno', null, A, L.tramo(t, 0.56, 0.62));
      UJ.caja(ctx, lz, 295, 350, 210, 90, 'LEFT JOIN', 'mascota', A, L.tramo(t, 0.6, 0.66));
      UJ.caja(ctx, lz, 560, 350, 210, 90, 'GROUP BY', 'por dueño', A, L.tramo(t, 0.64, 0.7));
      L.flecha(ctx, 242, 395, 292, 395, V, 4, L.tramo(t, 0.62, 0.68, 'frena'));
      L.flecha(ctx, 507, 395, 557, 395, V, 4, L.tramo(t, 0.66, 0.72, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.8), function () {
        L.rectRed(ctx, 220, 462, 360, 56, 14); L.rellena(ctx, L.tono(V, 0.85), V, 2);
        UJ.rotulo(ctx, lz, 'una sola pasada', 400, 474, { tam: 24, peso: 800, color: V });
      });
      // 3 · la conclusion
      UJ.rotulo(ctx, lz, 'Las dos devuelven las mismas 2.006 filas.', W / 2, 560,
                { tam: 21, ancho: W - 40, color: A, visible: L.tramo(t, 0.88, 0.98) });
    }
  });
})();
