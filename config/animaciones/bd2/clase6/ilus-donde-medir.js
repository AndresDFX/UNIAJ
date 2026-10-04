/* Ilustracion: lo que se mide con PostgreSQL dentro del navegador (planes, filas, paginas) y lo
 * que no se puede medir ahi y se documenta (memoria vacia, varias sesiones, volumen grande). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-donde-medir', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // navegador
      L.rectRed(ctx, 24, 24, 370, 470, 16); L.rellena(ctx, m.papel, A, 3);
      L.rectRed(ctx, 24, 24, 370, 46, 16); L.rellena(ctx, A);
      for (var k = 0; k < 3; k++) { L.circulo(ctx, 50 + k * 22, 47, 7); L.rellena(ctx, m.papel); }
      UJ.rotulo(ctx, lz, 'PostgreSQL en el navegador', 250, 36, { tam: 16, peso: 700, color: m.papel });
      var si = ['EXPLAIN y EXPLAIN ANALYZE', '(ANALYZE, BUFFERS): páginas leídas', 'filas estimadas contra reales',
                'loops de cada nodo', 'conteos con COUNT(*)', '30.010 citas ya sembradas'];
      for (var i = 0; i < si.length; i++) {
        UJ.sello(ctx, lz, 56, 112 + i * 60, 14, true, 1);
        UJ.rotulo(ctx, lz, si[i], 82, 100 + i * 60, { tam: 17, alinear: 'left', ancho: 300 });
      }
      UJ.rotulo(ctx, lz, 'se mide y se ve en la salida', 209, 462, { tam: 16, peso: 700, color: A });
      // papel
      L.rectRed(ctx, 420, 24, 356, 470, 6); L.rellena(ctx, L.tono(C, 0.92), C, 3);
      UJ.rotulo(ctx, lz, 'No se puede medir aquí', 598, 44, { tam: 20, peso: 800, color: L.tono(C, -0.3) });
      var no = [['tiempos con la memoria vacía', 'vaciarla exige ser administrador'],
                ['varias sesiones a la vez', 'el navegador corre una sola'],
                ['cientos de miles de filas', 'o más: otro orden de magnitud']];
      for (var j = 0; j < no.length; j++) {
        var y = 100 + j * 120;
        UJ.sello(ctx, lz, 452, y + 14, 14, false, 1);
        UJ.rotulo(ctx, lz, no[j][0], 476, y, { tam: 17, peso: 700, alinear: 'left', ancho: 290 });
        UJ.rotulo(ctx, lz, no[j][1], 476, y + 30, { tam: 15, alinear: 'left', ancho: 290 });
      }
      UJ.rotulo(ctx, lz, 'se declara por escrito', 598, 462, { tam: 16, peso: 700, color: L.tono(C, -0.3) });
      UJ.rotulo(ctx, lz, 'Los conteos de filas no cambian entre corridas; los milisegundos sí.', W / 2, 530,
                { tam: 18, peso: 700, ancho: W - 40 });
    }
  });
})();
