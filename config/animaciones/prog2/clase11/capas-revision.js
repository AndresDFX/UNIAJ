/* Revisar por capas: seis capas en orden de importancia; la ultima, el formato, la que menos vale. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('capas-revision', {
    duracion: 4.5,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      var capas = [
        ['1 · ¿Ejecuta?', 'compila y arranca'],
        ['2 · Corrección y bordes', 'vacío, null, límites'],
        ['3 · Diseño', 'responsabilidades, acoplamiento'],
        ['4 · Errores', 'excepciones bien manejadas'],
        ['5 · Legibilidad', 'nombres, métodos cortos'],
        ['6 · Formato', 'sangría, espacios']
      ];
      UJ.rotulo(ctx, lz, 'Se revisa de arriba hacia abajo', W / 2, 22, { tam: 24, peso: 700, visible: L.tramo(t, 0, 0.08) });
      for (var i = 0; i < 6; i++) {
        var y = 70 + i * 78, an = 620 - i * 60, x = 40;
        var a = i < 3 ? L.tramo(t, 0.05 + i * 0.08, 0.13 + i * 0.08) : L.tramo(t, 0.42 + (i - 3) * 0.08, 0.5 + (i - 3) * 0.08);
        UJ.alfa(ctx, a, function () {
          var c = i === 5 ? m.gris || L.tono(m.tinta, 0.5) : L.tono(A, i * 0.1);
          L.rectRed(ctx, x, y, an, 64, 12); L.rellena(ctx, L.tono(c, 0.88), c, 3);
          UJ.rotulo(ctx, lz, capas[i][0], x + 16, y + 8, { tam: 21, peso: 800, alinear: 'left', color: L.tono(c, -0.25), ancho: an - 24 });
          UJ.rotulo(ctx, lz, capas[i][1], x + 16, y + 37, { tam: 16, peso: 500, alinear: 'left', ancho: an - 24 });
        });
      }
      var f = L.tramo(t, 0.05, 0.3);
      UJ.alfa(ctx, f, function () {
        L.flecha(ctx, 720, 80, 720, 520, L.tono(A, -0.1), 6, 1);
        UJ.rotulo(ctx, lz, 'más', 720, 52, { tam: 18, peso: 700, color: A });
        UJ.rotulo(ctx, lz, 'menos', 720, 530, { tam: 18, peso: 700, color: A });
      });
      UJ.rotulo(ctx, lz, 'El formato es lo último: no tapa un error de fondo.', W / 2, 560, { tam: 21, ancho: W - 40, visible: L.tramo(t, 0.8, 0.95) });
    }
  });
})();
