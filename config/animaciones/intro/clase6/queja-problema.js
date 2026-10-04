/* De la queja al problema: cuatro frases que se van precisando, como un embudo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('queja-problema', {
    duracion: 5,
    // Pasos LOGICOS: una frase por clic. La flecha hacia la frase siguiente llega CON ella (si
    // llegara al final del paso anterior, apuntaria a una caja que todavia no existe).
    pasos: [0.2, 0.45, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var f = [
        ['La queja', '«La gente se queja de la biblioteca del barrio»', R],
        ['¿Se queja de qué?', '«No encuentran los libros»', L.mezclaColor(R, A, 0.5)],
        ['¿A quién le pasa qué?', 'Estudiantes de colegio pierden tiempo: el catálogo es un cuaderno', A],
        ['Con su consecuencia', 'Muchos se van sin el libro y no vuelven', V]
      ];
      for (var i = 0; i < 4; i++) {
        var t0 = i * 0.25, a = L.tramo(t, t0 + 0.02, t0 + 0.12), y = 24 + i * 150, ind = i * 36, an = W - 60 - ind * 2;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 30 + ind, y, an, 118, 16); L.rellena(ctx, L.tono(f[i][2], 0.88), f[i][2], 3);
          UJ.rotulo(ctx, lz, f[i][0], W / 2, y + 12, { tam: 24, peso: 800, color: f[i][2] });
          UJ.rotulo(ctx, lz, f[i][1], W / 2, y + 50, { tam: 21, ancho: an - 40 });
        });
        if (i > 0) L.flecha(ctx, W / 2, y - 30, W / 2, y - 2, L.tono(m.tinta, 0.4), 3, L.tramo(t, t0, t0 + 0.04));
      }
      UJ.sello(ctx, lz, W - 120, 530, 26, true, L.tramo(t, 0.88, 0.98));
    }
  });
})();
