/* Ilustracion: lo que se mide de indices y particiones con PostgreSQL dentro del navegador y lo
 * que no se puede medir ahi (se declara por escrito). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-donde-medir', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      L.rectRed(ctx, 24, 24, 370, 480, 16); L.rellena(ctx, m.papel, A, 3);
      L.rectRed(ctx, 24, 24, 370, 46, 16); L.rellena(ctx, A);
      for (var k = 0; k < 3; k++) { L.circulo(ctx, 50 + k * 22, 47, 7); L.rellena(ctx, m.papel); }
      UJ.rotulo(ctx, lz, 'PostgreSQL en el navegador', 250, 36, { tam: 16, peso: 700, color: m.papel });
      var si = ['de Seq Scan a acceso por índice', 'qué índice gana entre dos', 'el efecto del orden de columnas',
                'la poda de particiones', 'el tamaño: pg_relation_size', 'filas estimadas contra reales'];
      for (var i = 0; i < si.length; i++) {
        UJ.sello(ctx, lz, 56, 112 + i * 60, 14, true, 1);
        UJ.rotulo(ctx, lz, si[i], 82, 100 + i * 60, { tam: 17, alinear: 'left', ancho: 300 });
      }
      UJ.rotulo(ctx, lz, 'se mide y se ve en el plan', 209, 474, { tam: 16, peso: 700, color: A });
      L.rectRed(ctx, 420, 24, 356, 480, 6); L.rellena(ctx, L.tono(C, 0.92), C, 3);
      UJ.rotulo(ctx, lz, 'No se puede medir aquí', 598, 44, { tam: 20, peso: 800, color: L.tono(C, -0.3) });
      var no = [['tiempos con la memoria vacía', 'exige ser administrador'],
                ['crear un índice sobre millones de filas', 'otro orden de magnitud'],
                ['la fragmentación tras meses', 'de escrituras'],
                ['dos sesiones a la vez', 'el navegador corre una sola']];
      for (var j = 0; j < no.length; j++) {
        var y = 96 + j * 92;
        UJ.sello(ctx, lz, 452, y + 14, 14, false, 1);
        UJ.rotulo(ctx, lz, no[j][0], 476, y, { tam: 16, peso: 700, alinear: 'left', ancho: 290 });
        UJ.rotulo(ctx, lz, no[j][1], 476, y + 44, { tam: 14, alinear: 'left', ancho: 290 });
      }
      UJ.rotulo(ctx, lz, 'se declara por escrito', 598, 474, { tam: 16, peso: 700, color: L.tono(C, -0.3) });
      UJ.rotulo(ctx, lz, 'El tipo de nodo y las filas son estables; los milisegundos no.', W / 2, 540,
                { tam: 18, peso: 700, ancho: W - 40 });
    }
  });
})();
