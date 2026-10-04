/* Control optimista: no bloquea al leer, verifica al escribir con una columna version. Se lee la
 * cita 812 con version 7; al guardar, el UPDATE exige version = 7. Si nadie paso, toca 1 fila; si
 * otra transaccion ya la dejo en 8, toca 0: esa es la senal de conflicto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('version-optimista', {
    duracion: 5,
    pasos: [0.34, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      // Lectura sin bloqueo
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        UJ.tabla(ctx, lz, 30, 20, 330, 'cita', ['id_cita 812 · version 7'], 1, A, 0);
      });
      UJ.rotulo(ctx, lz, '1. lee: version 7, sin bloquear', 580, 30, { tam: 19, peso: 700, ancho: 380, visible: L.tramo(t, 0.08, 0.16) });
      UJ.rotulo(ctx, lz, '2. el usuario edita la hora', 580, 70, { tam: 19, peso: 700, ancho: 380, visible: L.tramo(t, 0.16, 0.24) });
      // UPDATE condicionado
      var lineas = ['UPDATE cita SET hora = ..., version = version + 1', ' WHERE id_cita = 812 AND version = 7;'];
      for (var i = 0; i < 2; i++) UJ.codigo(ctx, lz, 30, 140 + i * 42, 740, lineas[i], L.tramo(t, 0.22 + i * 0.05, 0.3 + i * 0.05), 17);
      // Caso sin conflicto
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.44), function () {
        L.rectRed(ctx, 30, 250, 360, 200, 16); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'Nadie pasó', 210, 264, { tam: 22, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'guardada: version 7', 210, 306, { tam: 18 });
        UJ.rotulo(ctx, lz, '1 fila afectada', 210, 350, { tam: 24, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'queda en version 8', 210, 396, { tam: 18 });
      });
      UJ.sello(ctx, lz, 370, 260, 22, true, L.tramo(t, 0.46, 0.52));
      // Caso con conflicto
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        L.rectRed(ctx, 410, 250, 360, 200, 16); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'Otra pasó antes', 590, 264, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'guardada: version 8', 590, 306, { tam: 18 });
        UJ.rotulo(ctx, lz, '0 filas afectadas', 590, 350, { tam: 24, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'señal de conflicto', 590, 396, { tam: 18 });
      });
      UJ.sello(ctx, lz, 750, 260, 22, false, L.tramo(t, 0.8, 0.86));
      UJ.alfa(ctx, L.tramo(t, 0.86, 0.96), function () {
        L.rectRed(ctx, 30, 480, 740, 120, 16); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'La aplicación reintenta o avisa que el dato cambió.', 400, 496, { tam: 20, peso: 800, color: L.tono(C, -0.4), ancho: 700 });
        UJ.rotulo(ctx, lz, 'Se elige por la frecuencia real del conflicto: si es alta, pesimista.', 400, 540, { tam: 18, ancho: 700 });
      });
    }
  });
})();
