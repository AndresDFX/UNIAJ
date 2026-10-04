/* Ilustracion: lo que corre en PostgreSQL dentro del navegador y lo que se documenta en papel
 * (los programas de linea de comandos necesitan sistema de archivos y servidor). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-navegador-papel', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // navegador
      L.rectRed(ctx, 24, 30, 370, 470, 16); L.rellena(ctx, m.papel, A, 3);
      L.rectRed(ctx, 24, 30, 370, 46, 16); L.rellena(ctx, A);
      for (var k = 0; k < 3; k++) { L.circulo(ctx, 50 + k * 22, 53, 7); L.rellena(ctx, m.papel); }
      UJ.rotulo(ctx, lz, 'PostgreSQL en el navegador', 250, 42, { tam: 16, peso: 700, color: m.papel });
      var si = ['CREATE FUNCTION … IMMUTABLE', 'trigger: función + asociación', 'RAISE EXCEPTION / NOTICE',
                'bloques DO', 'current_user · now()', 'IS DISTINCT FROM'];
      for (var i = 0; i < si.length; i++) {
        UJ.sello(ctx, lz, 56, 118 + i * 62, 14, true, 1);
        UJ.rotulo(ctx, lz, si[i], 82, 106 + i * 62, { tam: 17, alinear: 'left', ancho: 300 });
      }
      UJ.rotulo(ctx, lz, 'se ejecuta y se ve la salida', 209, 466, { tam: 16, peso: 700, color: A });
      // papel
      L.rectRed(ctx, 420, 30, 356, 470, 6); L.rellena(ctx, L.tono(C, 0.92), C, 3);
      UJ.rotulo(ctx, lz, 'Se documenta en el plan', 598, 50, { tam: 19, peso: 800, color: L.tono(C, -0.3) });
      var no = ['pg_dump', 'pg_dumpall', 'pg_basebackup', 'pg_restore'];
      for (var j = 0; j < no.length; j++) UJ.codigo(ctx, lz, 448, 110 + j * 70, 300, no[j], 1, 18);
      UJ.rotulo(ctx, lz, 'programas de línea de comandos: necesitan archivos y un servidor', 598, 410,
                { tam: 15, ancho: 310 });
      UJ.rotulo(ctx, lz, 'Lo que corre se demuestra con su salida; lo que no, se escribe bien.', W / 2, 540,
                { tam: 18, peso: 700, ancho: W - 40 });
    }
  });
})();
