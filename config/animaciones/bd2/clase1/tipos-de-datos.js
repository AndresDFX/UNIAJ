/* Tres facturas caras: telefono no es numero (VARCHAR(30)), fecha no es texto (TIMESTAMP), dinero
 * no es flotante (DECIMAL(12,2)). Cada una: el tipo tentador, lo que falla y el tipo correcto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('tipos-de-datos', {
    duracion: 5,
    // Pasos LOGICOS: un caso completo por clic (tipo tentador, lo que falla, tipo correcto)
    // y al final la tentacion contraria, todo VARCHAR(4000).
    pasos: [0.3, 0.62, 0.9, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var casos = [
        ['teléfono', 'NUMERIC', 'pierde el 0 inicial, el + y la extensión', 'VARCHAR(30)'],
        ['fecha_hora', 'VARCHAR(20)', "ORDER BY alfabético; no suma 30 minutos", 'TIMESTAMP'],
        ['dinero', 'FLOAT', '0.1 + 0.2 ≠ 0.3: el total no cuadra', 'DECIMAL(12,2)']
      ];
      for (var i = 0; i < 3; i++) {
        var t0 = i * 0.32, y = 24 + i * 196;
        UJ.alfa(ctx, L.tramo(t, t0, t0 + 0.05), function () {
          UJ.rotulo(ctx, lz, casos[i][0], 30, y, { tam: 24, peso: 800, color: A, alinear: 'left' });
          L.rectRed(ctx, 30, y + 40, 220, 52, 10); L.rellena(ctx, L.tono(R, 0.88), R, 2);
          L.texto(ctx, casos[i][1], 140, y + 54, { tam: 20, peso: 700, color: R, alinear: 'center', letra: 'Consolas, monospace' });
        });
        UJ.rotulo(ctx, lz, casos[i][2], 270, y + 56, { tam: 17, alinear: 'left', ancho: 280, visible: L.tramo(t, t0 + 0.06, t0 + 0.16) });
        var a = L.tramo(t, t0 + 0.18, t0 + 0.26);
        UJ.alfa(ctx, a, function () {
          L.flecha(ctx, 140, y + 96, 140, y + 124, L.tono(m.tinta, 0.4), 3);
          L.rectRed(ctx, 30, y + 128, 220, 52, 10); L.rellena(ctx, L.tono(V, 0.85), V, 2);
          L.texto(ctx, casos[i][3], 140, y + 142, { tam: 20, peso: 700, color: V, alinear: 'center', letra: 'Consolas, monospace' });
        });
        UJ.sello(ctx, lz, 280, y + 154, 18, true, a);
        if (i < 2) UJ.alfa(ctx, a, function () { L.trazo(ctx, [[30, y + 190], [W - 30, y + 190]], 1, L.tono(m.tinta, 0.85), 1); });
      }
      UJ.alfa(ctx, L.tramo(t, 0.9, 1), function () {
        L.rectRed(ctx, 580, 420, 200, 150, 12); L.rellena(ctx, L.tono(m.sello || A, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Todo VARCHAR(4000):', 680, 436, { tam: 17, peso: 800, ancho: 180 });
        UJ.rotulo(ctx, lz, 'la base ya no valida nada', 680, 486, { tam: 17, ancho: 170 });
      });
    }
  });
})();
