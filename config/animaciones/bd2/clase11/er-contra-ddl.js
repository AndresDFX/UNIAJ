/* Verificaciones uno y dos: entidad -> CREATE TABLE, y en sentido contrario. Y la cardinalidad
 * dibujada debe existir como restriccion: cita pertenece a una mascota = NOT NULL + FOREIGN KEY. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('er-contra-ddl', {
    duracion: 5,
    pasos: [0.34, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.rotulo(ctx, lz, 'Diagrama ER', 160, 12, { tam: 24, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'Script DDL', 620, 12, { tam: 24, peso: 800, color: C });
      var izq = ['Dueño', 'Mascota', 'Cita', 'Insumo'], der = ['dueno', 'mascota', 'cita', 'proveedor'];
      for (var i = 0; i < 4; i++) {
        var y = 56 + i * 76;
        UJ.caja(ctx, lz, 60, y, 200, 58, izq[i], '', A, 1);
        UJ.alfa(ctx, 1, function () {
          L.rectRed(ctx, 470, y, 300, 58, 8); L.rellena(ctx, L.tono(m.tinta, -0.55));
          UJ.rotulo(ctx, lz, 'CREATE TABLE ' + der[i], 486, y + 18, { tam: 18, alinear: 'left', color: '#E8F4FA' });
        });
      }
      // Ida: entidad -> tabla
      for (var j = 0; j < 3; j++) L.flecha(ctx, 264, 85 + j * 76, 466, 85 + j * 76, A, 3, L.tramo(t, 0.05 + j * 0.06, 0.12 + j * 0.06));
      UJ.sello(ctx, lz, 300, 313, 20, false, L.tramo(t, 0.24, 0.3));
      UJ.rotulo(ctx, lz, 'entidad sin tabla', 160, 348, { tam: 17, peso: 700, color: R, visible: L.tramo(t, 0.26, 0.32) });
      // Vuelta: tabla -> entidad
      UJ.sello(ctx, lz, 440, 313, 20, false, L.tramo(t, 0.42, 0.48));
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        L.rectRed(ctx, 470, 350, 300, 34, 8); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'tabla sin entidad: la que nadie revisa', 620, 357, { tam: 16, peso: 700, color: R, ancho: 290 });
      });
      // Cardinalidad -> restriccion
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.74), function () {
        UJ.caja(ctx, lz, 30, 420, 140, 56, 'Cita', '', A, 1);
        UJ.caja(ctx, lz, 270, 420, 160, 56, 'Mascota', '', A, 1);
        L.trazo(ctx, [[170, 448], [270, 448]], 1, A, 4);
        UJ.rotulo(ctx, lz, 'exactamente 1', 220, 484, { tam: 16, peso: 700, color: A });
      });
      L.flecha(ctx, 440, 448, 470, 448, C, 4, L.tramo(t, 0.74, 0.8, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.78 + 0.02), function () { UJ.codigo(ctx, lz, 474, 404, 306, 'id_mascota … NOT NULL', L.tramo(t, 0.78, 0.86), 16); });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.84 + 0.02), function () { UJ.codigo(ctx, lz, 474, 448, 306, 'FOREIGN KEY → mascota', L.tramo(t, 0.84, 0.92), 16); });
      UJ.rotulo(ctx, lz, 'Cardinalidad sin restricción es decoración.', W / 2, 560,
                { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
