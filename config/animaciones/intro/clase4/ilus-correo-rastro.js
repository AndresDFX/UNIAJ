/* Ilustracion: anatomia del correo de cinco lineas que deja rastro. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-correo-rastro', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, S = m.sello || m.acento, W = lz.ancho;
      L.rectRed(ctx, 20, 16, W - 40, 470, 16); L.rellena(ctx, m.papel, A, 3);
      L.rectRed(ctx, 20, 16, W - 40, 50, 16); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'Correo al jefe', 44, 28, { tam: 22, peso: 800, color: m.papel, alinear: 'left' });
      var f = [['Asunto', 'Riesgo en exportar clientes'], ['Lo que me piden', 'cédula y celular en un archivo compartido'],
        ['El riesgo', 'si se filtra: datos de unas 2.000 personas'], ['Lo que propongo', 'exportar solo nombre y ciudad'],
        ['Quedo atento', 'firmado, con fecha']];
      for (var i = 0; i < 5; i++) {
        var y = 84 + i * 80;
        L.circulo(ctx, 64, y + 30, 22); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, String(i + 1), 64, y + 16, { tam: 24, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, f[i][0], 100, y + 16, { tam: 22, peso: 800, color: A, alinear: 'left' });
        UJ.rotulo(ctx, lz, f[i][1], 310, y + 16, { tam: 20, alinear: 'left', ancho: 450 });
      }
      L.rectRed(ctx, 20, 506, 180, 110, 16); L.rellena(ctx, S, m.tinta, 2);
      UJ.rotulo(ctx, lz, '5 líneas', 110, 544, { tam: 28, peso: 800 });
      L.rectRed(ctx, 220, 506, 560, 110, 16); L.rellena(ctx, L.tono(A, 0.9), A, 2);
      UJ.rotulo(ctx, lz, 'Si el jefe insiste, la decisión ya no es suya, y queda escrito que avisó', 500, 524, { tam: 21, peso: 700, ancho: 520 });
    }
  });
})();
