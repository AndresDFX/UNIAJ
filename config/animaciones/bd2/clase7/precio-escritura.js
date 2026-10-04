/* El precio del indice se paga en cada escritura: un INSERT en una tabla con cuatro indices son
 * cinco escrituras. Cada indice adicional: del orden de 5 % a 15 % mas lento al escribir. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('precio-escritura', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.codigo(ctx, lz, 200, 30, 400, 'INSERT INTO cita …', L.tramo(t, 0, 0.1), 20);
      var dest = [['tabla cita', A], ['índice 1', C], ['índice 2', C], ['índice 3', C], ['índice 4', C]];
      for (var i = 0; i < 5; i++) {
        var x = 30 + i * 150;
        L.flecha(ctx, 400, 76, x + 65, 186, dest[i][1], 3, L.tramo(t, 0.12 + i * 0.07, 0.2 + i * 0.07, 'frena'));
        UJ.caja(ctx, lz, x, 190, 130, 80, dest[i][0], null, dest[i][1], L.tramo(t, 0.16 + i * 0.07, 0.22 + i * 0.07));
        UJ.alfa(ctx, L.tramo(t, 0.18 + i * 0.07, 0.24 + i * 0.07), function () {
          L.circulo(ctx, x + 65, 300, 20); L.rellena(ctx, m.sello || C, m.tinta, 2);
          UJ.rotulo(ctx, lz, String(i + 1), x + 65, 288, { tam: 20, peso: 800 });
        });
      }
      UJ.rotulo(ctx, lz, 'Un INSERT con cuatro índices no es una operación: son cinco.', W / 2, 350,
                { tam: 21, peso: 800, color: A, ancho: W - 40, visible: L.tramo(t, 0.52, 0.6) });
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.76), function () {
        L.rectRed(ctx, 30, 420, W - 60, 140, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'Cada índice adicional: entre 5 % y 15 % más lento al escribir', W / 2, 436, { tam: 20, peso: 800, color: L.tono(C, -0.3), ancho: W - 100 });
        UJ.rotulo(ctx, lz, 'diez índices pueden escribir varias veces más lento que dos', W / 2, 480, { tam: 18, ancho: W - 100 });
        UJ.rotulo(ctx, lz, '(orden de magnitud, no una ley)', W / 2, 516, { tam: 16, peso: 500, color: L.tono(m.tinta, 0.3) });
      });
      UJ.rotulo(ctx, lz, 'Se indexa lo que se consulta, no todo.', W / 2, 590, { tam: 21, ancho: W - 40, color: A, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
