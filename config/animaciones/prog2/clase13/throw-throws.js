/* throw en el dominio, throws en la firma, catch en la interfaz que muestra el mensaje del negocio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('throw-throws', {
    duracion: 4.5,
    // Pasos LOGICOS: 1) el dominio lanza: throws en la firma, throw en el cuerpo y el tipo es una
    // excepcion propia; 2) la interfaz la atrapa y muestra el mensaje (catch + ventana, con su
    // resultado); 3) la conclusion. El catch ya no aparece sin la ventana que le da sentido.
    pasos: [0.4, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, W = lz.ancho;
      var TAM = 17, AN = 520, X0 = 30;
      // Recuadra `sub` dentro de una linea de codigo ya dibujada en (X0, y): mide con la misma letra.
      function marca(linea, sub, y, color, a) {
        UJ.alfa(ctx, a, function () {
          ctx.font = '500 ' + TAM + 'px Consolas, monospace';
          var i = linea.indexOf(sub);
          var x = X0 + 14 + ctx.measureText(linea.slice(0, i)).width;
          L.rectRed(ctx, x - 3, y + 3, ctx.measureText(sub).width + 6, TAM * 2 - 6, 5);
          ctx.strokeStyle = color; ctx.lineWidth = 3; ctx.stroke();
        });
      }
      // 1) Dominio: Mascota valida y lanza
      UJ.rotulo(ctx, lz, 'Dominio: Mascota', X0, 18, { tam: 20, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0, 0.04) });
      var lin = [
        'void setEdad(int e) throws DatoInvalidoException {',
        '  if (e < 0)',
        '    throw new DatoInvalidoException(',
        '        "La edad no puede ser negativa");',
        '  this.edad = e;',
        '}'
      ];
      for (var i = 0; i < lin.length; i++) UJ.codigo(ctx, lz, X0, 50 + i * 36, AN, lin[i], L.tramo(t, 0.03 + i * 0.035, 0.065 + i * 0.035), TAM);
      var am = L.tramo(t, 0.25, 0.3);
      marca(lin[0], 'throws DatoInvalidoException', 50, C, am);
      marca(lin[2], 'throw', 122, R, am);
      UJ.alfa(ctx, am, function () {
        UJ.rotulo(ctx, lz, 'throws: la firma avisa', 564, 57, { tam: 18, peso: 700, alinear: 'left', color: C });
        UJ.rotulo(ctx, lz, 'throw: la lanza', 564, 129, { tam: 18, peso: 700, alinear: 'left', color: R });
      });
      UJ.alfa(ctx, L.tramo(t, 0.31, 0.38), function () {
        L.rectRed(ctx, X0, 280, AN, 64, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'class DatoInvalidoException extends Exception', X0 + AN / 2, 288, { tam: 18, peso: 700, ancho: AN - 20 });
        UJ.rotulo(ctx, lz, 'excepción propia: nombra el error del negocio', X0 + AN / 2, 316, { tam: 16, ancho: AN - 20 });
      });
      // 2) Sube a la interfaz, que la atrapa y la muestra
      var s = L.tramo(t, 0.42, 0.5);
      if (s > 0) L.flecha(ctx, 290, 348, 290, 392, R, 5, s);
      UJ.rotulo(ctx, lz, 'Interfaz: la ventana', X0, 396, { tam: 20, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0.48, 0.52) });
      var ui = [
        'try { m.setEdad(edad); }',
        'catch (DatoInvalidoException ex) {',
        '  JOptionPane.showMessageDialog(',
        '      this, ex.getMessage()); }'
      ];
      for (var k = 0; k < ui.length; k++) UJ.codigo(ctx, lz, X0, 428 + k * 36, AN, ui[k], L.tramo(t, 0.52 + k * 0.045, 0.565 + k * 0.045), TAM);
      UJ.alfa(ctx, L.tramo(t, 0.71, 0.79), function () {
        L.rectRed(ctx, 578, 392, 202, 170, 10); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.4), 2);
        L.rectRed(ctx, 578, 392, 202, 34, 10); L.rellena(ctx, L.tono(A, 0.75));
        UJ.rotulo(ctx, lz, 'Mensaje', 592, 399, { tam: 16, peso: 700, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'La edad no puede ser negativa', 679, 442, { tam: 18, ancho: 170, peso: 600 });
        L.rectRed(ctx, 639, 512, 80, 34, 6); L.rellena(ctx, L.tono(A, 0.85), A, 2);
        UJ.rotulo(ctx, lz, 'OK', 679, 518, { tam: 17, peso: 700 });
      });
      // 3) Conclusion
      UJ.rotulo(ctx, lz, 'El usuario lee la regla del negocio, no una traza.', W / 2, 590, { tam: 20, ancho: W - 40, visible: L.tramo(t, 0.86, 0.96) });
    }
  });
})();
