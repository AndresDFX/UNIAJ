/* Trazabilidad paso → mensaje → operacion: el paso del caso de uso se vuelve un mensaje de la
 * secuencia, y ese mensaje exige la operacion en la clase receptora. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('paso-mensaje-operacion', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.36, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, T = m.tinta, G = m.gris, R = m.malva, W = lz.ancho;

      // Paso del caso de uso
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, 60, 24, W - 120, 84, 12); L.rellena(ctx, L.tono(m.sello, 0.8), L.tono(m.sello, -0.35), 2.5);
        UJ.rotulo(ctx, lz, 'CU-04, paso 2', W / 2, 34, { tam: 18, peso: 800, color: L.tono(m.sello, -0.55) });
        UJ.rotulo(ctx, lz, 'El sistema verifica la disponibilidad del veterinario', W / 2, 62, { tam: 20, peso: 600, color: T, ancho: W - 150 });
      });
      L.flecha(ctx, W / 2 - 180, 112, 210, 158, L.tono(T, 0.3), 3, L.tramo(t, 0.1, 0.16));

      // Mensaje sobre la linea de vida
      var a = L.tramo(t, 0.16, 0.22);
      UJ.alfa(ctx, a, function () {
        var px = [100, 330];
        var ns = [':ControlAgenda', ':RepositorioCitas'];
        for (var i = 0; i < 2; i++) {
          L.rectRed(ctx, px[i] - 88, 166, 176, 40, 8); L.rellena(ctx, L.tono(A, 0.88), A, 2);
          UJ.rotulo(ctx, lz, ns[i], px[i], 176, { tam: 17, peso: 700, color: A });
          UJ.linea(ctx, px[i], 206, px[i], 330, L.tono(G, 0.2), 2, 1, true);
        }
      });
      L.flecha(ctx, 106, 266, 324, 266, A, 3, L.tramo(t, 0.22, 0.3, 'frena'));
      UJ.rotulo(ctx, lz, 'consultarDisponibilidad()', 215, 236, { tam: 17, peso: 700, color: A, visible: L.tramo(t, 0.28, 0.36) });

      // Clase receptora con la operacion
      function clase(x, y, ops, a, c, resalta) {
        UJ.alfa(ctx, a, function () {
          var w = 300, h = 46 + 36 + ops.length * 32 + 10;
          L.rectRed(ctx, x, y, w, h, 6); L.rellena(ctx, m.papel, c, 2.5);
          L.rectRed(ctx, x, y, w, 46, 6); L.rellena(ctx, L.tono(c, 0.8), c, 2.5);
          UJ.rotulo(ctx, lz, 'RepositorioCitas', x + w / 2, y + 12, { tam: 19, peso: 800, color: L.tono(c, -0.3) });
          L.trazo(ctx, [[x, y + 82], [x + w, y + 82]], 1, c, 2);
          UJ.rotulo(ctx, lz, '-citas: List<Cita>', x + 14, y + 54, { tam: 17, peso: 500, color: T, alinear: 'left' });
          for (var k = 0; k < ops.length; k++) {
            if (resalta === k) { L.rectRed(ctx, x + 6, y + 88 + k * 32, w - 12, 30, 5); L.rellena(ctx, L.tono(m.verde, 0.75)); }
            UJ.rotulo(ctx, lz, ops[k], x + 14, y + 92 + k * 32, { tam: 17, peso: 600, color: T, alinear: 'left' });
          }
        });
      }
      L.flecha(ctx, 420, 266, 464, 266, L.tono(T, 0.3), 3, L.tramo(t, 0.38, 0.43));
      clase(476, 190, ['+guardarCita()', '+consultarDisponibilidad()'], L.tramo(t, 0.42, 0.5), A, L.tramo(t, 0.5, 0.52) > 0 ? 1 : -1);
      UJ.sello(ctx, lz, 742, 176, 22, true, L.tramo(t, 0.54, 0.62));

      // Variante: la clase no tiene la operacion
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.7), function () {
        L.trazo(ctx, [[40, 378], [W - 40, 378]], 1, L.tono(G, 0.5), 2);
        UJ.rotulo(ctx, lz, 'Variante: el diagrama de clases no la tiene', 40, 392, { tam: 19, peso: 800, color: R, alinear: 'left' });
      });
      clase(40, 430, ['+guardarCita()'], L.tramo(t, 0.7, 0.78), L.tono(G, -0.1));
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.84), function () {
        L.rectRed(ctx, 48, 564, 284, 30, 5); L.rellena(ctx, null, R, 2);
        ctx.save(); ctx.setLineDash([6, 5]); L.rectRed(ctx, 48, 564, 284, 30, 5); L.rellena(ctx, L.tono(R, 0.9), R, 2); ctx.restore();
        UJ.rotulo(ctx, lz, '+consultarDisponibilidad() ?', 190, 568, { tam: 17, peso: 700, color: R });
      });
      UJ.sello(ctx, lz, 400, 494, 26, false, L.tramo(t, 0.84, 0.9));
      UJ.alfa(ctx, L.tramo(t, 0.88, 0.96), function () {
        UJ.rotulo(ctx, lz, 'Hallazgo: falta la operación en el diagrama de clases', 596, 466,
                  { tam: 19, peso: 700, color: R, ancho: 330 });
      });
    }
  });
})();
