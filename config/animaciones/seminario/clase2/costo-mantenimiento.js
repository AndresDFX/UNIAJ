/* El costo de toda la vida de un sistema: construir la 1.0 es el tramo corto; mantenerlo
 * (60-80 %) es el largo, con sus versiones nuevas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('costo-mantenimiento', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, M = m.acento, W = lz.ancho;
      var x0 = 40, x1 = 220, x2 = 760, y = 290, h = 96;
      UJ.rotulo(ctx, lz, 'El costo total de la vida del sistema', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.08) });
      var p1 = L.tramo(t, 0.08, 0.26, 'frena');
      if (p1 > 0) { L.rectRed(ctx, x0, y, (x1 - x0) * p1, h, 10); L.rellena(ctx, A, m.papel, 2); }
      UJ.alfa(ctx, L.tramo(t, 0.22, 0.32), function () {
        UJ.rotulo(ctx, lz, 'Proyecto: construir la 1.0', (x0 + x1) / 2, y + 22, { tam: 18, peso: 700, color: m.papel, ancho: x1 - x0 - 16 });
      });
      var p2 = L.tramo(t, 0.36, 0.58, 'frena');
      if (p2 > 0) { L.rectRed(ctx, x1, y, (x2 - x1) * p2, h, 10); L.rellena(ctx, M, m.papel, 2); }
      UJ.alfa(ctx, L.tramo(t, 0.55, 0.66), function () {
        UJ.rotulo(ctx, lz, 'Mantenimiento: 60-80 % del costo', (x1 + x2) / 2, y + 34, { tam: 22, peso: 800, color: m.papel });
      });
      // Llave del total
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.12), function () {
        L.trazo(ctx, [[x0, y + h + 14], [x0, y + h + 30], [x2, y + h + 30], [x2, y + h + 14]], 1, L.tono(m.tinta, 0.4), 2.5);
        UJ.rotulo(ctx, lz, 'una barra = todo lo que cuesta el sistema en su vida', W / 2, y + h + 42, { tam: 18, peso: 600, color: L.tono(m.tinta, 0.2) });
      });
      // Hitos
      var hitos = [[400, 'v1.1', 'vacunación a domicilio'], [610, 'v2.0', 'facturación electrónica']];
      for (var i = 0; i < 2; i++) {
        (function (hx, v, d, a) {
          UJ.alfa(ctx, a, function () {
            L.trazo(ctx, [[hx, 200], [hx, y - 4]], 1, L.tono(M, -0.3), 3);
            L.circulo(ctx, hx, 200, 8); L.rellena(ctx, L.tono(M, -0.3));
            UJ.rotulo(ctx, lz, v, hx, 108, { tam: 22, peso: 800, color: L.tono(M, -0.3) });
            UJ.rotulo(ctx, lz, d, hx, 138, { tam: 17, peso: 600, ancho: 180 });
          });
        })(hitos[i][0], hitos[i][1], hitos[i][2], L.tramo(t, 0.7 + i * 0.08, 0.78 + i * 0.08));
      }
      UJ.rotulo(ctx, lz, 'La vida más larga y más cara del sistema es mantenerlo.', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
