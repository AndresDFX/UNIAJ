/* Flujo de la tarea «registrar mascota»: primero el camino feliz y luego las ramas alternas
 * que lo vuelven un diseño y no una postal. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('flujo-tarea', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, R = m.malva, T = m.tinta, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Flujo de la tarea: registrar mascota', W / 2, 18, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      UJ.rotulo(ctx, lz, 'Camino feliz', 24, 70, { tam: 19, peso: 800, color: V, alinear: 'left', visible: L.tramo(t, 0.03, 0.08) });
      var pasos = ['llega el dueño', 'buscarlo', 'encontrado', 'registrar mascota', 'código'];
      var bw = 132, gap = 20, x0 = (W - (5 * bw + 4 * gap)) / 2, by = 104, bh = 62;
      var cx = function (i) { return x0 + i * (bw + gap) + bw / 2; };
      for (var i = 0; i < 5; i++) {
        (function (i) {
          var a = L.tramo(t, 0.06 + i * 0.05, 0.11 + i * 0.05);
          UJ.alfa(ctx, a, function () {
            var x = x0 + i * (bw + gap), c = i === 4 ? V : A;
            L.rectRed(ctx, x, by, bw, bh, 12); L.rellena(ctx, L.tono(c, 0.86), c, 2.5);
            var h = L.texto(ctx, pasos[i], -9999, -9999, { tam: 17, peso: 700, letra: lz.letra, ancho: bw - 14 });
            UJ.rotulo(ctx, lz, pasos[i], cx(i), by + bh / 2 - h / 2, { tam: 17, peso: 700, color: L.tono(c, -0.3), ancho: bw - 14 });
          });
          if (i < 4) L.flecha(ctx, x0 + i * (bw + gap) + bw + 2, by + bh / 2, x0 + (i + 1) * (bw + gap) - 2, by + bh / 2, A, 2.5, L.tramo(t, 0.1 + i * 0.05, 0.13 + i * 0.05));
        })(i);
      }
      // Ramas alternas
      UJ.rotulo(ctx, lz, 'Ramas alternas', 24, 214, { tam: 19, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0.37, 0.42) });
      var ramas = [
        [1, 'sin documento', 'teléfono como identificador temporal'],
        [2, 'dueño no registrado', 'crearlo sin perder lo escrito'],
        [3, 'mascota ya existe', 'avisar, no duplicar']
      ];
      var rw = 240, rx = [24, 280, 536], ry = 290, rh = 124;
      for (var k = 0; k < 3; k++) {
        (function (k) {
          var s = 0.42 + k * 0.13, r = ramas[k];
          var tx = rx[k] + rw / 2;
          UJ.flecha(ctx, lz, cx(r[0]), by + bh + 4, tx, ry - 4, R, L.tramo(t, s, s + 0.05), null, { punteada: true, grosor: 2.5 });
          UJ.alfa(ctx, L.tramo(t, s + 0.04, s + 0.1), function () {
            L.rectRed(ctx, rx[k], ry, rw, rh, 12); L.rellena(ctx, L.tono(R, 0.92), R, 2.5);
            UJ.rotulo(ctx, lz, r[1], tx, ry + 16, { tam: 18, peso: 800, color: R, ancho: rw - 20 });
            L.trazo(ctx, [[rx[k] + 20, ry + 52], [rx[k] + rw - 20, ry + 52]], 1, L.tono(R, 0.5), 1.5);
            UJ.rotulo(ctx, lz, '→ ' + r[2], tx, ry + 66, { tam: 18, peso: 600, color: T, ancho: rw - 24 });
          });
        })(k);
      }
      UJ.rotulo(ctx, lz, 'Un flujo con solo el camino feliz es una postal.', W / 2, 540,
                { tam: 23, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
