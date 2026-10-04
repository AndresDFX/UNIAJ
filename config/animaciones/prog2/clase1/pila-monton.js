/* Pila y monton: a y b en la pila apuntan al mismo objeto del monton; b.setEdad(4) se ve
 * desde a. Contraste: los primitivos se copian (int y = x; y = 5 deja x en 3). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pila-monton', {
    duracion: 5,
    pasos: [0.22, 0.46, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      // Zonas
      L.rectRed(ctx, 24, 24, 230, 270, 14); L.rellena(ctx, L.tono(A, 0.93), A, 2);
      UJ.rotulo(ctx, lz, 'PILA', 139, 34, { tam: 22, peso: 800, color: A });
      L.rectRed(ctx, 300, 24, 476, 270, 14); L.rellena(ctx, L.tono(V, 0.93), V, 2);
      UJ.rotulo(ctx, lz, 'MONTÓN', 538, 34, { tam: 22, peso: 800, color: V });
      function variable(nombre, y, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 50, y, 180, 56, 10); L.rellena(ctx, m.papel, A, 2);
          UJ.rotulo(ctx, lz, nombre, 80, y + 14, { tam: 24, peso: 800, letra: 'Consolas, monospace' });
          L.circulo(ctx, 200, y + 28, 8); L.rellena(ctx, A);
        });
      }
      variable('a', 90, L.tramo(t, 0.02, 0.08));
      variable('b', 190, L.tramo(t, 0.26, 0.32));
      // El objeto
      var edad = t < 0.56 ? '3' : '4', marca = L.tramo(t, 0.56, 0.6);
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.12), function () {
        L.rectRed(ctx, 470, 100, 270, 140, 14); L.rellena(ctx, L.tono(V, 0.86), V, 3);
        UJ.rotulo(ctx, lz, 'Mascota', 605, 110, { tam: 20, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'nombre = "Luna"', 490, 148, { tam: 19, alinear: 'left', letra: 'Consolas, monospace' });
        if (marca > 0) { L.rectRed(ctx, 484, 184, 150, 34, 6); L.rellena(ctx, L.tono(m.sello, 0.4, marca)); }
        UJ.rotulo(ctx, lz, 'edad = ' + edad, 490, 190, { tam: 19, peso: marca > 0 ? 800 : 400, alinear: 'left', letra: 'Consolas, monospace' });
      });
      L.flecha(ctx, 208, 118, 466, 150, A, 4, L.tramo(t, 0.1, 0.18, 'frena'));
      L.flecha(ctx, 208, 218, 466, 200, C, 4, L.tramo(t, 0.32, 0.42, 'frena'));
      // Codigo, una linea por paso
      UJ.alfa(ctx, L.tramo(t, 0, 0.04), function () { UJ.codigo(ctx, lz, 24, 310, 752, 'Mascota a = new Mascota("Luna", "Canino", 3);', L.tramo(t, 0, 0.12), 18); });
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.27), function () { UJ.codigo(ctx, lz, 24, 352, 360, 'Mascota b = a;', L.tramo(t, 0.24, 0.32), 18); });
      UJ.rotulo(ctx, lz, 'una mascota, dos nombres', 590, 360, { tam: 19, peso: 700, color: C, visible: L.tramo(t, 0.38, 0.45) });
      UJ.alfa(ctx, L.tramo(t, 0.48, 0.5), function () { UJ.codigo(ctx, lz, 24, 394, 360, 'b.setEdad(4);', L.tramo(t, 0.48, 0.55), 18); });
      UJ.rotulo(ctx, lz, 'a.getEdad() → 4', 590, 400, { tam: 22, peso: 800, color: R, visible: L.tramo(t, 0.6, 0.68) });
      // Primitivos
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.76), function () {
        L.trazo(ctx, [[24, 448], [W - 24, 448]], 1, L.tono(m.gris, 0.5), 2);
        UJ.codigo(ctx, lz, 24, 462, 400, 'int x = 3;  int y = x;  y = 5;', L.tramo(t, 0.72, 0.8), 18);
      });
      var yv = t < 0.86 ? '3' : '5';
      function caja(nombre, valor, x, a, color) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, 520, 150, 60, 10); L.rellena(ctx, L.tono(color, 0.88), color, 3);
          UJ.rotulo(ctx, lz, nombre + ' = ' + valor, x + 75, 536, { tam: 24, peso: 800, letra: 'Consolas, monospace' });
        });
      }
      caja('x', '3', 40, L.tramo(t, 0.78, 0.82), A);
      caja('y', yv, 230, L.tramo(t, 0.81, 0.85), yv === '5' ? R : A);
      UJ.rotulo(ctx, lz, 'Los 8 primitivos se copian:', 610, 478, { tam: 19, peso: 700, ancho: 330, visible: L.tramo(t, 0.88, 0.94) });
      UJ.rotulo(ctx, lz, 'x sigue en 3', 610, 536, { tam: 26, peso: 800, color: V, visible: L.tramo(t, 0.9, 0.97) });
    }
  });
})();
