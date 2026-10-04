/* Error del motor y error de negocio. El motor detecta lo que conoce (CHECK, FK, tipo,
 * interbloqueo) y aborta solo. La regla de negocio no la conoce: un UPDATE que toca 0 filas es un
 * exito para el; hay que lanzar RAISE EXCEPTION. Y nada de capturar y silenciar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('error-motor-negocio', {
    duracion: 4.8,
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      // Error del motor
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.rectRed(ctx, 30, 30, 360, 360, 18); L.rellena(ctx, L.tono(A, 0.93), A, 3);
        UJ.rotulo(ctx, lz, 'Error del motor', 210, 46, { tam: 25, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'regla que la base conoce', 210, 88, { tam: 18 });
      });
      var reglas = ['CHECK', 'clave foránea', 'tipo incompatible', 'interbloqueo'];
      for (var i = 0; i < 4; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.08 + i * 0.04, 0.14 + i * 0.04), function () {
          L.rectRed(ctx, 70, 128 + i * 44, 280, 36, 8); L.rellena(ctx, m.papel, L.tono(A, 0.5), 2);
          UJ.rotulo(ctx, lz, reglas[i], 210, 135 + i * 44, { tam: 18, peso: 600 });
        });
      }
      UJ.rotulo(ctx, lz, 'el motor lanza y aborta solo', 210, 316, { tam: 19, peso: 800, color: A, ancho: 330, visible: L.tramo(t, 0.28, 0.36) });
      // Error de negocio
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () {
        L.rectRed(ctx, 410, 30, 360, 360, 18); L.rellena(ctx, L.tono(C, 0.9), C, 3);
        UJ.rotulo(ctx, lz, 'Error de negocio', 590, 46, { tam: 25, peso: 800, color: L.tono(C, -0.35) });
        UJ.rotulo(ctx, lz, 'regla que la base NO conoce así', 590, 88, { tam: 18, ancho: 330 });
        UJ.rotulo(ctx, lz, 'stock insuficiente · mascota inactiva · total que no cuadra', 590, 130, { tam: 18, ancho: 320 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.6), function () {
        UJ.rotulo(ctx, lz, 'UPDATE que toca 0 filas = éxito para el motor', 590, 212, { tam: 18, peso: 700, ancho: 320 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.6, 0.68), function () {
        UJ.codigo(ctx, lz, 430, 290, 320, 'RAISE EXCEPTION ...', 1, 17);
        UJ.rotulo(ctx, lz, 'lo lanzas tú', 590, 340, { tam: 19, peso: 800, color: L.tono(C, -0.35) });
      });
      // Nada de silenciar
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.82), function () {
        L.rectRed(ctx, 30, 420, 740, 180, 16); L.rellena(ctx, L.tono(R, 0.92), R, 2);
        UJ.rotulo(ctx, lz, 'Nada de capturar y silenciar', 400, 436, { tam: 23, peso: 800, color: R });
        UJ.codigo(ctx, lz, 160, 480, 480, 'EXCEPTION WHEN OTHERS THEN NULL;', 1, 17);
        UJ.rotulo(ctx, lz, 'si se captura, se relanza con RAISE a secas', 400, 540, { tam: 19, ancho: 700 });
      });
      UJ.sello(ctx, lz, 680, 498, 24, false, L.tramo(t, 0.84, 0.92));
    }
  });
})();
