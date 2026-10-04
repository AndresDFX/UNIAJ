/* La transaccion como unidad de todo o nada, y por que no basta. Primero la idea: las sentencias
 * de un mismo hecho (agendar y descontar la vacuna) se confirman juntas o no queda ninguna.
 * Despues el problema: dos transacciones a la vez consultan la franja de las 10:00, las dos la
 * ven libre, las dos insertan, y quedan dos citas al mismo minuto sin que nada fallara. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('intercalado-doble-cita', {
    duracion: 5,
    // Pasos LOGICOS: 1) todo o nada; 2) las dos consultan y ven libre; 3) las dos insertan y
    // confirman; 4) el resultado: dos citas al mismo minuto y ningun error.
    pasos: [0.22, 0.48, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      // 1 · Todo o nada
      UJ.rotulo(ctx, lz, 'Una transacción: todo o nada', 20, 8, { tam: 22, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0, 0.04) });
      UJ.codigo(ctx, lz, 20, 44, 450, 'INSERT INTO cita …            -- agendar', L.tramo(t, 0.03, 0.09), 16);
      UJ.codigo(ctx, lz, 20, 84, 450, 'UPDATE insumo SET stock = stock - 1 …', L.tramo(t, 0.08, 0.14), 16);
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.2), function () {
        L.rectRed(ctx, 490, 44, 290, 32, 16); L.rellena(ctx, L.tono(V, 0.8), V, 2);
        UJ.rotulo(ctx, lz, 'COMMIT: quedan las dos', 635, 50, { tam: 16, peso: 800, color: L.tono(V, -0.4) });
        L.rectRed(ctx, 490, 84, 290, 32, 16); L.rellena(ctx, L.tono(R, 0.82), R, 2);
        UJ.rotulo(ctx, lz, 'ROLLBACK: no queda ninguna', 635, 90, { tam: 16, peso: 800, color: L.tono(R, -0.3) });
      });
      // 2 · Dos transacciones a la vez
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.28), function () {
        L.trazo(ctx, [[20, 136], [780, 136]], 1, L.tono(m.tinta, 0.75), 2);
        UJ.rotulo(ctx, lz, 'T1 · recepción A', 205, 146, { tam: 20, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'T2 · recepción B', 595, 146, { tam: 20, peso: 800, color: C });
        L.trazo(ctx, [[400, 146], [400, 410]], 1, L.tono(m.tinta, 0.7), 3);
        UJ.rotulo(ctx, lz, 'tiempo ↓', 400, 412, { tam: 15, color: L.tono(m.tinta, 0.3) });
      });
      var ops = [
        [0, '¿10:00 con la vet. Restrepo?', 'libre: 0 filas', 0.29],
        [1, '¿10:00 con la vet. Restrepo?', 'libre: 0 filas', 0.37],
        [0, 'INSERT cita 10:00 · Mishi', 'COMMIT: sin error', 0.52],
        [1, 'INSERT cita 10:00 · Toby', 'COMMIT: sin error', 0.6]
      ];
      for (var i = 0; i < ops.length; i++) {
        var o = ops[i], x = o[0] === 0 ? 30 : 420, c = o[0] === 0 ? A : C, y = 186 + i * 56;
        UJ.alfa(ctx, L.tramo(t, o[3], o[3] + 0.08), function () {
          L.rectRed(ctx, x, y, 350, 48, 10); L.rellena(ctx, L.tono(c, 0.9), c, 2);
          L.texto(ctx, o[1], x + 12, y + 4, { tam: 17, peso: 700, color: m.tinta, letra: lz.letra, ancho: 330 });
          L.texto(ctx, o[2], x + 12, y + 26, { tam: 15, peso: 600, color: c, letra: lz.letra });
          L.circulo(ctx, 400, y + 24, 7); L.rellena(ctx, c);
        });
      }
      // 4 · El resultado
      UJ.alfa(ctx, L.tramo(t, 0.75, 0.83), function () {
        UJ.tabla(ctx, lz, 140, 436, 520, 'cita', ['10:00 · vet. Restrepo · Mishi', '10:00 · vet. Restrepo · Toby'], 2, R);
      });
      UJ.sello(ctx, lz, 696, 500, 26, false, L.tramo(t, 0.82, 0.88));
      UJ.rotulo(ctx, lz, 'Ninguna falló: el motor cumplió dos órdenes contradictorias.', W / 2, 572, { tam: 20, peso: 800, color: R, ancho: W - 40, visible: L.tramo(t, 0.87, 0.94) });
      UJ.rotulo(ctx, lz, 'Todo o nada protege UNA transacción, no a dos que se cruzan.', W / 2, 606, { tam: 17, ancho: W - 40, visible: L.tramo(t, 0.93, 0.99) });
    }
  });
})();
