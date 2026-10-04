/* MoSCoW: cuatro cajones y los requisitos de la clínica cayendo en el suyo; Won't queda escrito
 * y los Must no pasan del 60 % del esfuerzo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('moscow', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.2, 0.56, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, W = lz.ancho;
      var caj = [['Must', 'sin ello no sale a producción', m.accion], ['Should', 'importante, con plan B manual', m.acento],
        ['Could', 'si sobra tiempo', m.verde], ['Won\'t', 'no en ESTA versión', m.malva]];
      function cx(i) { return 26 + i * 190; }
      UJ.rotulo(ctx, lz, 'Priorizar con MoSCoW', W / 2, 18, { tam: 25, peso: 800, color: m.accion, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 4; i++) {
        (function (i) {
          var c = caj[i][2];
          UJ.alfa(ctx, L.tramo(t, 0.03 + i * 0.035, 0.08 + i * 0.035), function () {
            L.rectRed(ctx, cx(i), 140, 178, 390, 12); L.rellena(ctx, L.tono(c, 0.93), c, 2.5);
            L.rectRed(ctx, cx(i), 140, 178, 96, 12); L.rellena(ctx, L.tono(c, 0.78), c, 2.5);
            UJ.rotulo(ctx, lz, caj[i][0], cx(i) + 89, 150, { tam: 24, peso: 800, color: L.tono(c, -0.35) });
            UJ.rotulo(ctx, lz, caj[i][1], cx(i) + 89, 184, { tam: 16, peso: 600, color: m.tinta, ancho: 160 });
          });
        })(i);
      }
      var items = [
        ['Registrar dueño y mascota', 0, 0, 0.22], ['Consultar historial', 0, 1, 0.28], ['Agendar cita', 0, 2, 0.34],
        ['Reporte mensual', 1, 0, 0.41], ['Exportar a Excel', 2, 0, 0.48],
        ['Recordatorios por WhatsApp', 3, 0, 0.6], ['Facturación electrónica', 3, 1, 0.68]
      ];
      items.forEach(function (it) {
        var p = L.tramo(t, it[3], it[3] + 0.06, 'frena');
        if (p <= 0) return;
        var x = cx(it[1]) + 8, yf = 248 + it[2] * 62, y = 64 + (yf - 64) * p, c = caj[it[1]][2];
        UJ.alfa(ctx, Math.min(1, p * 3), function () {
          L.rectRed(ctx, x, y, 162, 54, 8); L.rellena(ctx, m.papel, c, 2);
          var h = L.texto(ctx, it[0], -9999, -9999, { tam: 16, peso: 700, letra: lz.letra, ancho: 148 });
          UJ.rotulo(ctx, lz, it[0], x + 81, y + (54 - h) / 2 + 1, { tam: 16, peso: 700, color: m.tinta, ancho: 148 });
        });
      });
      UJ.alfa(ctx, L.tramo(t, 0.75, 0.82), function () {
        L.rectRed(ctx, cx(3) + 8, 384, 162, 60, 8); L.rellena(ctx, L.tono(m.sello, 0.8), L.tono(m.sello, -0.2), 2);
        UJ.rotulo(ctx, lz, 'escrito: no en esta versión', cx(3) + 89, 392, { tam: 16, peso: 700, color: m.tinta, ancho: 150 });
      });
      // Barra de esfuerzo
      var b = L.tramo(t, 0.86, 0.96, 'frena');
      UJ.alfa(ctx, L.tramo(t, 0.86, 0.88), function () {
        L.rectRed(ctx, 26, 556, 748, 40, 8); L.rellena(ctx, L.tono(m.gris, 0.9), m.gris, 2);
        L.rectRed(ctx, 26, 556, 748 * 0.6 * b, 40, 8); L.rellena(ctx, L.tono(m.accion, 0.3));
        UJ.rotulo(ctx, lz, 'Must ≤ 60 % del esfuerzo', 26 + 748 * 0.3, 564, { tam: 20, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, 'el resto', 26 + 748 * 0.8, 564, { tam: 18, peso: 700, color: m.gris });
      });
    }
  });
})();
