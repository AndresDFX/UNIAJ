/* throw en el dominio, throws en la firma, catch en la interfaz que muestra el mensaje del negocio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('throw-throws', {
    duracion: 4.5,
    pasos: [0.35, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Dominio: Mascota', 30, 20, { tam: 20, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0, 0.05) });
      var lin = [
        'void setEdad(int e) throws DatoInvalidoException {',
        '  if (e < 0)',
        '    throw new DatoInvalidoException(',
        '      "La edad no puede ser negativa");'
      ];
      for (var i = 0; i < 4; i++) UJ.codigo(ctx, lz, 30, 54 + i * 40, W - 60, lin[i], L.tramo(t, 0.04 + i * 0.07, 0.1 + i * 0.07), 18);
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.34), function () {
        UJ.rotulo(ctx, lz, 'throws: la firma avisa', 540, 220, { tam: 17, peso: 700, alinear: 'left', color: C });
        UJ.rotulo(ctx, lz, 'throw: la lanza', 540, 246, { tam: 17, peso: 700, alinear: 'left', color: R });
      });
      // Clase propia
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.46), function () {
        L.rectRed(ctx, 30, 290, 470, 70, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'class DatoInvalidoException extends Exception', 265, 302, { tam: 17, peso: 700, ancho: 450 });
        UJ.rotulo(ctx, lz, 'excepción propia: nombra el error del negocio', 265, 330, { tam: 16, ancho: 450 });
      });
      // Sube a la interfaz
      var s = L.tramo(t, 0.5, 0.62);
      if (s > 0) L.flecha(ctx, 265, 364, 265, 410, R, 5, s);
      UJ.rotulo(ctx, lz, 'Interfaz: la ventana', 30, 416, { tam: 20, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0.56, 0.62) });
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.6), function () {
        UJ.codigo(ctx, lz, 30, 450, 470, 'catch (DatoInvalidoException ex)', L.tramo(t, 0.58, 0.64), 18);
        UJ.codigo(ctx, lz, 30, 490, 470, '  JOptionPane...(ex.getMessage());', L.tramo(t, 0.6, 0.66), 18);
      });
      // Ventana de mensaje
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.82), function () {
        L.rectRed(ctx, 530, 380, 240, 170, 10); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.4), 2);
        L.rectRed(ctx, 530, 380, 240, 34, 10); L.rellena(ctx, L.tono(A, 0.75));
        UJ.rotulo(ctx, lz, 'Mensaje', 548, 387, { tam: 16, peso: 700, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'La edad no puede ser negativa', 650, 432, { tam: 18, ancho: 210, peso: 600 });
        L.rectRed(ctx, 610, 500, 80, 34, 6); L.rellena(ctx, L.tono(A, 0.85), A, 2);
        UJ.rotulo(ctx, lz, 'OK', 650, 506, { tam: 17, peso: 700 });
      });
      UJ.rotulo(ctx, lz, 'El usuario lee la regla del negocio, no una traza.', W / 2, 580, { tam: 20, ancho: W - 40, visible: L.tramo(t, 0.86, 0.96) });
    }
  });
})();
