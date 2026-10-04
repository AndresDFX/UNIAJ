/* Particionar: una tabla logica dividida en fragmentos fisicos por rango de fechas. Una consulta
 * de 2026 lee solo la particion de 2026. El indice ordena; la particion separa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('particionar', {
    duracion: 5,
    // Pasos LOGICOS: 1) una tabla logica, dos particiones por ano; 2) la consulta de 2026 lee
    // solo la suya (poda); 3) la diferencia con el indice.
    pasos: [0.4, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A;
      UJ.caja(ctx, lz, 200, 30, 400, 90, 'cita_hist', 'una sola tabla lógica', A, L.tramo(t, 0, 0.1));
      var sep = L.tramo(t, 0.14, 0.32, 'suave');
      var ys = 170 + 0 * sep;
      var pts = [['cita_hist_2025', '2025-01-01 → 2026-01-01'], ['cita_hist_2026', '2026-01-01 → 2027-01-01']];
      for (var i = 0; i < 2; i++) {
        var x = 400 + (i ? 1 : -1) * 200 * sep - 170;
        L.flecha(ctx, 400, 122, x + 170, ys - 4, L.tono(m.tinta, 0.4), 3, sep);
        var leida = i === 1 && t > 0.58;
        UJ.alfa(ctx, L.tramo(t, 0.14, 0.22) * (t > 0.58 && i === 0 ? 0.4 : 1), function () {
          L.rectRed(ctx, x, ys, 340, 110, 14);
          L.rellena(ctx, leida ? L.tono(V, 0.8) : L.tono(C, 0.88), leida ? V : C, leida ? 4 : 2);
          L.texto(ctx, pts[i][0], x + 170, ys + 16, { tam: 22, peso: 800, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, pts[i][1], x + 170, ys + 60, { tam: 16, peso: 500 });
        });
      }
      UJ.rotulo(ctx, lz, 'fragmentos físicos: particiones por rango de fechas', W / 2, 300, { tam: 18, peso: 600, visible: L.tramo(t, 0.3, 0.38) });
      UJ.codigo(ctx, lz, 30, 352, W - 60, "SELECT COUNT(*) FROM cita_hist WHERE fecha_hora >= TIMESTAMP '2026-01-01'", L.tramo(t, 0.44, 0.54), 15);
      UJ.sello(ctx, lz, 742, 176, 24, true, L.tramo(t, 0.58, 0.64));
      UJ.rotulo(ctx, lz, 'el plan solo nombra cita_hist_2026: la otra se descarta sin leerla', W / 2, 414, { tam: 19, peso: 800, color: V, ancho: W - 40, visible: L.tramo(t, 0.62, 0.7) });
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.92), function () {
        L.rectRed(ctx, 30, 470, 355, 100, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'el índice ORDENA', 207, 504, { tam: 24, peso: 800, color: A });
        L.rectRed(ctx, 415, 470, 355, 100, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'la partición SEPARA', 592, 504, { tam: 24, peso: 800, color: L.tono(C, -0.3) });
      });
    }
  });
})();
