/* La matriz de trazabilidad delata los dos defectos: el requisito huerfano (sin diseño) y el
 * caso de uso viudo (sin requisito que lo pida). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('huerfano-viudo', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      var cols = [['RF', 130], ['Casos de uso', 400], ['Clases', 670]];
      var filas = [[['RF-03', 'CU-02', 'Mascota']], [['RF-05', 'CU-03', 'Cita']], [['RF-07', 'CU-04', 'Propietario']]];
      var ys = [110, 190, 270], an = 160, al = 50;
      for (var c = 0; c < 3; c++) {
        UJ.rotulo(ctx, lz, cols[c][0], cols[c][1], 30, { tam: 23, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      }
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () { UJ.linea(ctx, 40, 70, W - 40, 70, L.tono(m.gris, 0.4), 2); });
      for (var f = 0; f < 3; f++) {
        for (c = 0; c < 3; c++) {
          var nombre = filas[f][0][c];
          var color = A;
          if (nombre === 'RF-07' && t >= 0.44) color = m.malva;
          if (nombre === 'CU-04' && t >= 0.74) color = m.sello;
          UJ.caja(ctx, lz, cols[c][1] - an / 2, ys[f], an, al, nombre, null, color, L.tramo(t, 0.04 + f * 0.05, 0.1 + f * 0.05));
        }
      }
      // Enlaces
      var pE = L.tramo(t, 0.2, 0.34);
      for (f = 0; f < 3; f++) {
        var y = ys[f] + al / 2;
        if (f < 2) UJ.flecha(ctx, lz, 212, y, 318, y, m.tinta, pE, null, { grosor: 2.5 });
        UJ.flecha(ctx, lz, 482, y, 588, y, m.tinta, pE, null, { grosor: 2.5 });
      }

      // Huerfano
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        UJ.rotulo(ctx, lz, '?', 236, ys[2] + 8, { tam: 24, peso: 800, color: m.malva });
      });
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.58), function () {
        UJ.rotulo(ctx, lz, 'Huérfano', 130, 350, { tam: 21, peso: 800, color: m.malva });
        UJ.rotulo(ctx, lz, 'se prometió y no se diseñó', 130, 380, { tam: 18, peso: 600, color: m.tinta, ancho: 220 });
      });
      // Viudo
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.82), function () {
        UJ.rotulo(ctx, lz, 'Viudo', 400, 350, { tam: 21, peso: 800, color: L.tono(m.sello, -0.35) });
        UJ.rotulo(ctx, lz, 'nadie lo pidió', 400, 380, { tam: 18, peso: 600, color: m.tinta, ancho: 220 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.92), function () {
        L.rectRed(ctx, 120, 450, 560, 64, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Fila sin enlace = defecto a la vista', 400, 470, { tam: 20, peso: 700, color: A });
      });
      UJ.rotulo(ctx, lz, 'La matriz de trazabilidad es la prueba objetiva', W / 2, 560,
        { tam: 22, peso: 700, color: m.tinta, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
