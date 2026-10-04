/* Ilustracion: el proyecto del curso como un recorrido de la Clase 1 a la 16. Arranca hoy con
 * la semilla (un problema del entorno) y crece clase a clase hasta el informe. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-proyecto', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, S = m.sello || m.acento, V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un proyecto de equipo, de la Clase 1 a la 16', W / 2, 14, { tam: 26, peso: 800, color: A, ancho: W - 40 });
      var etapas = [
        ['Clase 1 · hoy', 'la semilla: un problema del entorno'],
        ['Clase 6', 'el problema y la propuesta inicial'],
        ['Clases 7 a 11', 'el ciclo de vida y un prototipo'],
        ['Clases 12 a 14', 'el impacto y el ensayo'],
        ['Clase 15', 'la exposición final'],
        ['Clase 16', 'el informe']
      ];
      var y0 = 74, paso = 78;
      L.rectRed(ctx, 57, y0 + 30, 6, paso * 5, 3); L.rellena(ctx, L.tono(A, 0.5));
      for (var i = 0; i < etapas.length; i++) {
        var y = y0 + i * paso, hoy = i === 0, fin = i === etapas.length - 1;
        L.rectRed(ctx, 90, y, 690, 62, 14);
        L.rellena(ctx, hoy ? L.tono(S, 0.6) : L.tono(A, 0.93), hoy ? L.tono(S, -0.35) : L.tono(A, 0.5), 2);
        L.circulo(ctx, 60, y + 31, 18); L.rellena(ctx, hoy ? L.tono(S, -0.2) : (fin ? V : A), m.papel, 3);
        UJ.rotulo(ctx, lz, etapas[i][0], 110, y + 17, { tam: 22, peso: 800, color: hoy ? m.tinta : A, alinear: 'left' });
        UJ.rotulo(ctx, lz, etapas[i][1], 310, y + 18, { tam: 21, alinear: 'left', ancho: 460 });
      }
      L.rectRed(ctx, 20, 556, W - 40, 66, 33); L.rellena(ctx, L.tono(V, 0.88), V, 2);
      UJ.rotulo(ctx, lz, 'No hay que programarla: se diseña y se defiende.', W / 2, 576, { tam: 22, peso: 800, color: L.tono(V, -0.3), ancho: W - 80 });
    }
  });
})();
