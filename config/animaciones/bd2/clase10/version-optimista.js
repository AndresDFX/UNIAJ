/* Control optimista: no bloquea al leer, verifica al escribir con una columna version. Se lee la
 * cita 812 con version 7; al guardar, el UPDATE exige version = 7. Si nadie paso, toca 1 fila y
 * queda en 8; si otra transaccion ya la dejo en 8, toca 0 filas: esa es la senal de conflicto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('version-optimista', {
    duracion: 5,
    // Pasos LOGICOS: 1) leer sin bloquear y el UPDATE condicionado; 2) sin conflicto: 1 fila;
    // 3) con conflicto: 0 filas; 4) que hace la aplicacion y cuando conviene cada enfoque.
    pasos: [0.24, 0.48, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      // 1 · Lectura sin bloqueo y escritura condicionada
      UJ.alfa(ctx, L.tramo(t, 0, 0.05), function () {
        UJ.tabla(ctx, lz, 30, 16, 330, 'cita', ['id_cita 812 · version 7'], 1, A, 0);
      });
      UJ.rotulo(ctx, lz, '1. lee version 7, sin bloquear', 580, 24, { tam: 19, peso: 700, ancho: 390, visible: L.tramo(t, 0.04, 0.09) });
      UJ.rotulo(ctx, lz, '2. el usuario edita la hora', 580, 62, { tam: 19, peso: 700, ancho: 390, visible: L.tramo(t, 0.09, 0.13) });
      UJ.codigo(ctx, lz, 30, 124, 740, 'UPDATE cita SET fecha_hora = …, version = version + 1', L.tramo(t, 0.13, 0.18), 17);
      UJ.codigo(ctx, lz, 30, 166, 740, ' WHERE id_cita = 812 AND version = 7;', L.tramo(t, 0.17, 0.22), 17);
      // 2 · Nadie paso
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.34), function () {
        L.rectRed(ctx, 30, 226, 360, 190, 16); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'Nadie pasó', 210, 240, { tam: 22, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'guardada: version 7', 210, 280, { tam: 18 });
        UJ.rotulo(ctx, lz, 'UPDATE 1', 210, 320, { tam: 26, peso: 800, color: V, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'queda en version 8', 210, 370, { tam: 18 });
      });
      UJ.sello(ctx, lz, 370, 236, 22, true, L.tramo(t, 0.36, 0.42));
      // 3 · Otra paso antes
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.58), function () {
        L.rectRed(ctx, 410, 226, 360, 190, 16); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'Otra pasó antes', 590, 240, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'guardada: version 8', 590, 280, { tam: 18 });
        UJ.rotulo(ctx, lz, 'UPDATE 0', 590, 320, { tam: 26, peso: 800, color: R, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'cero filas: señal de conflicto', 590, 370, { tam: 18 });
      });
      UJ.sello(ctx, lz, 750, 236, 22, false, L.tramo(t, 0.6, 0.66));
      // 4 · La aplicacion decide
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.86), function () {
        L.rectRed(ctx, 30, 440, 740, 170, 16); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'La aplicación reintenta o avisa que el dato cambió.', 400, 456, { tam: 20, peso: 800, color: L.tono(C, -0.4), ancho: 700 });
        UJ.rotulo(ctx, lz, 'Conflicto frecuente (stock del insumo más vendido): pesimista.', 400, 506, { tam: 18, ancho: 700 });
        UJ.rotulo(ctx, lz, 'Conflicto raro (teléfono de un dueño): optimista, nadie espera.', 400, 546, { tam: 18, ancho: 700 });
      });
    }
  });
})();
