/* Verificaciones uno y dos. Uno: el ER contra el DDL, de ida (entidad sin tabla) y de vuelta
 * (tabla sin entidad), y la cardinalidad dibujada como restriccion: «una cita pertenece a una
 * mascota» = NOT NULL + REFERENCES. Dos: la matriz de roles contra los GRANT, donde el hallazgo
 * tipico es el auditor que recibio escritura porque se copio el bloque de recepcion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('er-contra-ddl', {
    duracion: 5,
    // Pasos LOGICOS: 1) de ida: entidad sin tabla; 2) de vuelta: tabla sin entidad;
    // 3) la cardinalidad como restriccion; 4) verificacion dos: matriz contra GRANT.
    pasos: [0.3, 0.52, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.rotulo(ctx, lz, 'Diagrama ER', 160, 6, { tam: 22, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'Script DDL', 620, 6, { tam: 22, peso: 800, color: C });
      var izq = ['Dueño', 'Mascota', 'Cita', 'Insumo'], der = ['dueno', 'mascota', 'cita', 'proveedor'];
      for (var i = 0; i < 4; i++) {
        var y = 44 + i * 58;
        UJ.caja(ctx, lz, 60, y, 200, 46, izq[i], '', A, 1);
        L.rectRed(ctx, 470, y, 310, 46, 8); L.rellena(ctx, L.tono(m.tinta, -0.55));
        UJ.rotulo(ctx, lz, 'CREATE TABLE ' + der[i], 486, y + 12, { tam: 18, alinear: 'left', color: '#E8F4FA' });
      }
      // 1 · Ida: entidad -> tabla
      for (var j = 0; j < 3; j++) L.flecha(ctx, 264, 67 + j * 58, 466, 67 + j * 58, A, 3, L.tramo(t, 0.05 + j * 0.06, 0.12 + j * 0.06));
      UJ.sello(ctx, lz, 296, 241, 18, false, L.tramo(t, 0.22, 0.27));
      UJ.rotulo(ctx, lz, 'entidad sin tabla', 160, 272, { tam: 16, peso: 700, color: R, visible: L.tramo(t, 0.24, 0.29) });
      // 2 · Vuelta: tabla -> entidad
      UJ.sello(ctx, lz, 440, 241, 18, false, L.tramo(t, 0.34, 0.4));
      UJ.alfa(ctx, L.tramo(t, 0.39, 0.47), function () {
        L.rectRed(ctx, 470, 268, 310, 30, 8); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'tabla sin entidad: la que nadie revisa', 625, 273, { tam: 15, peso: 700, color: R, ancho: 300 });
      });
      // 3 · Cardinalidad -> restriccion
      UJ.alfa(ctx, L.tramo(t, 0.54, 0.6), function () {
        UJ.caja(ctx, lz, 20, 310, 130, 48, 'Cita', '', A, 1);
        UJ.caja(ctx, lz, 250, 310, 150, 48, 'Mascota', '', A, 1);
        L.trazo(ctx, [[150, 334], [250, 334]], 1, A, 4);
        UJ.rotulo(ctx, lz, 'exactamente 1', 200, 362, { tam: 15, peso: 700, color: A });
      });
      L.flecha(ctx, 404, 334, 440, 334, C, 4, L.tramo(t, 0.6, 0.64, 'frena'));
      UJ.codigo(ctx, lz, 446, 302, 334, 'id_mascota INT NOT NULL', L.tramo(t, 0.63, 0.68), 15);
      UJ.codigo(ctx, lz, 446, 340, 334, 'REFERENCES mascota(id_mascota)', L.tramo(t, 0.67, 0.72), 15);
      UJ.rotulo(ctx, lz, 'Cardinalidad sin restricción es decoración.', W / 2, 384,
                { tam: 18, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.71, 0.75) });
      // 4 · Verificacion dos: matriz de roles contra GRANT
      UJ.rotulo(ctx, lz, 'Verificación dos: la matriz de roles contra los GRANT', 20, 424,
                { tam: 19, peso: 800, color: A, alinear: 'left', ancho: 760, visible: L.tramo(t, 0.78, 0.82) });
      UJ.alfa(ctx, L.tramo(t, 0.81, 0.86), function () {
        L.rectRed(ctx, 20, 460, 320, 96, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Matriz de la Clase 2', 180, 472, { tam: 18, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'auditor sobre cita: solo lectura', 180, 508, { tam: 16, ancho: 300 });
      });
      UJ.codigo(ctx, lz, 360, 462, 370, 'GRANT SELECT, INSERT, UPDATE', L.tramo(t, 0.85, 0.89), 15);
      UJ.codigo(ctx, lz, 360, 498, 370, '  ON cita TO auditor;', L.tramo(t, 0.88, 0.91), 15);
      UJ.sello(ctx, lz, 758, 494, 18, false, L.tramo(t, 0.9, 0.94));
      UJ.rotulo(ctx, lz, 'copiado del bloque de recepción', 570, 536, { tam: 15, peso: 700, color: R, ancho: 400, visible: L.tramo(t, 0.92, 0.95) });
      UJ.rotulo(ctx, lz, 'Cada celda de la matriz es un GRANT, y nada más.', W / 2, 590,
                { tam: 19, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.95, 0.99) });
    }
  });
})();
