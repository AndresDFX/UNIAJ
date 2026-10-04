/* La cascada como escalera: cada fase cierra con un documento firmado que abre la siguiente.
 * Requisitos queda como linea base y un cambio entra por solicitud y nueva version. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cascada-linea-base', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, R = m.malva, W = lz.ancho;
      var fases = ['Requisitos', 'Diseño', 'Construcción', 'Pruebas', 'Operación'];
      var an = 140, al = 48, dx = 150, dy = 80, x0 = 30, y0 = 70;
      UJ.rotulo(ctx, lz, 'Cascada: cada fase cierra con una firma', W / 2, 20, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      function doc(x, y, a) {
        UJ.alfa(ctx, a, function () {
          ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + 20, y); ctx.lineTo(x + 28, y + 8); ctx.lineTo(x + 28, y + 34); ctx.lineTo(x, y + 34); ctx.closePath();
          L.rellena(ctx, m.papel, L.tono(m.tinta, 0.3), 2);
          for (var k = 0; k < 3; k++) L.trazo(ctx, [[x + 5, y + 10 + k * 7], [x + 21, y + 10 + k * 7]], 1, L.tono(m.tinta, 0.55), 1.5);
          UJ.sello(ctx, lz, x + 32, y + 30, 10, true, 1);
        });
      }
      for (var i = 0; i < 5; i++) {
        var x = x0 + i * dx, y = y0 + i * dy, a0 = 0.04 + i * 0.065;
        UJ.caja(ctx, lz, x, y, an, al, fases[i], null, A, L.tramo(t, a0, a0 + 0.05));
        doc(x + 12, y + 54, L.tramo(t, a0 + 0.04, a0 + 0.07));
        if (i < 4) {
          var p = L.tramo(t, a0 + 0.05, a0 + 0.08);
          if (p > 0) {
            L.trazo(ctx, [[x + an, y + 24], [x + dx + an / 2, y + 24]], Math.min(1, p * 2), L.tono(A, 0.2), 3);
            if (p > 0.5) L.flecha(ctx, x + dx + an / 2, y + 24, x + dx + an / 2, y + dy - 2, L.tono(A, 0.2), 3, (p - 0.5) * 2);
          }
        }
      }
      // Linea base
      UJ.pildora(ctx, lz, 30, 168, 'Línea base v1.0', m.sello, L.tramo(t, 0.42, 0.5), { tam: 16, lleno: true });
      // El cambio
      UJ.rayo(ctx, 44, 258, 40, m.sello, L.tramo(t, 0.62, 0.67));
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.68), function () {
        L.rectRed(ctx, 76, 256, 240, 48, 10); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, '«buscar también por microchip»', 196, 262, { tam: 17, peso: 700, color: R, ancho: 228 });
      });
      UJ.flecha(ctx, lz, 196, 306, 196, 340, m.gris, L.tramo(t, 0.69, 0.73));
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.78), function () {
        L.rectRed(ctx, 46, 344, 300, 66, 10); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Solicitud de cambio', 196, 352, { tam: 18, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'costo y tiempo', 196, 378, { tam: 17, peso: 600 });
      });
      UJ.flecha(ctx, lz, 196, 412, 196, 446, m.gris, L.tramo(t, 0.79, 0.83));
      UJ.pildora(ctx, lz, 196, 450, 'Requisitos v1.1', V, L.tramo(t, 0.82, 0.88), { tam: 18, lleno: true, centrar: true });
      UJ.rotulo(ctx, lz, 'La cascada admite cambios: con solicitud y nueva versión.', W / 2, 556,
                { tam: 22, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
