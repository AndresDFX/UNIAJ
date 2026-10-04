/* Ilustracion: lo que se demuestra de transacciones con PostgreSQL dentro del navegador y lo que
 * no (una sola sesion, sin apagar el servidor), que se documenta como linea de tiempo T1/T2. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-donde-corre', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      L.rectRed(ctx, 24, 24, 370, 470, 16); L.rellena(ctx, m.papel, A, 3);
      L.rectRed(ctx, 24, 24, 370, 46, 16); L.rellena(ctx, A);
      for (var k = 0; k < 3; k++) { L.circulo(ctx, 50 + k * 22, 47, 7); L.rellena(ctx, m.papel); }
      UJ.rotulo(ctx, lz, 'PostgreSQL en el navegador', 250, 36, { tam: 16, peso: 700, color: m.papel });
      var si = ['CALL de un procedimiento', 'GET DIAGNOSTICS … ROW_COUNT', "RAISE EXCEPTION '… %'", 'función que devuelve BOOLEAN',
                'foto · CALL · foto en un panel', 'DDL dentro de una transacción'];
      for (var i = 0; i < si.length; i++) {
        UJ.sello(ctx, lz, 56, 112 + i * 60, 14, true, 1);
        UJ.rotulo(ctx, lz, si[i], 82, 100 + i * 60, { tam: 17, alinear: 'left', ancho: 300 });
      }
      UJ.rotulo(ctx, lz, 'nadie escribe BEGIN ni COMMIT', 209, 464, { tam: 16, peso: 700, color: A });
      L.rectRed(ctx, 420, 24, 356, 470, 6); L.rellena(ctx, L.tono(C, 0.92), C, 3);
      UJ.rotulo(ctx, lz, 'No se demuestra aquí', 598, 44, { tam: 20, peso: 800, color: L.tono(C, -0.3) });
      var no = [['dos sesiones a la vez', 'espera por bloqueo, interbloqueo, actualización perdida'],
                ['la durabilidad real', 'nadie puede apagar el servidor'],
                ['se documenta en papel', 'una línea de tiempo T1 / T2: qué ve cada una']];
      for (var j = 0; j < no.length; j++) {
        var y = 100 + j * 118;
        UJ.sello(ctx, lz, 452, y + 14, 14, j < 2 ? false : true, 1);
        UJ.rotulo(ctx, lz, no[j][0], 476, y, { tam: 17, peso: 700, alinear: 'left', ancho: 290 });
        UJ.rotulo(ctx, lz, no[j][1], 476, y + 30, { tam: 15, alinear: 'left', ancho: 290 });
      }
      UJ.rotulo(ctx, lz, 'eso es la Clase 10', 598, 464, { tam: 16, peso: 700, color: L.tono(C, -0.3) });
      UJ.rotulo(ctx, lz, 'El CALL ya es su propia transacción: el autocommit no rompe la demostración.', W / 2, 530,
                { tam: 18, peso: 700, ancho: W - 40 });
    }
  });
})();
