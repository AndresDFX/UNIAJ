/* De la busqueda lineal al HashMap: a la izquierda se recorre comparando uno por uno; a la
 * derecha la clave pasa por hashCode() y va directo a su casilla; si dos claves caen en la
 * misma casilla (colision), equals() decide. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('busqueda-hash', {
    duracion: 5,
    pasos: [0.28, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, S = m.sello;
      // ---------------- izquierda: ArrayList
      UJ.rotulo(ctx, lz, 'ArrayList: recorrer', 190, 20, { tam: 22, peso: 700, color: A });
      var ids = ['M-007', 'M-002', 'M-010', 'M-004', 'M-001', '… 5.000'];
      for (var i = 0; i < ids.length; i++) {
        var y = 70 + i * 50;
        L.rectRed(ctx, 40, y, 230, 42, 6); L.rellena(ctx, i % 2 ? L.tono(A, 0.94) : m.papel, L.tono(A, 0.5), 1);
        UJ.rotulo(ctx, lz, ids[i], 60, y + 10, { tam: 19, alinear: 'left' });
        var a = L.tramo(t, 0.04 + i * 0.045, 0.07 + i * 0.045);
        if (i < 3) UJ.rotulo(ctx, lz, '≠', 300, y + 6, { tam: 26, peso: 800, color: R, visible: a });
        if (i === 3) UJ.sello(ctx, lz, 300, y + 21, 16, true, a);
      }
      var py = L.claves(t, [[0.04, 70], [0.19, 220, 'lineal']]);
      UJ.alfa(ctx, L.tramo(t, 0.02, 0.05), function () { L.flecha(ctx, 14, py + 21, 34, py + 21, S, 4, 1); });
      UJ.rotulo(ctx, lz, 'Uno por uno: en el peor caso, los 5.000.', 190, 380, { tam: 18, peso: 700, color: R, ancho: 340, visible: L.tramo(t, 0.2, 0.26) });
      // separador
      ctx.strokeStyle = L.tono(m.tinta, 0.8); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(390, 20); ctx.lineTo(390, 450); ctx.stroke();
      // ---------------- derecha: HashMap
      UJ.rotulo(ctx, lz, 'HashMap: calcular', 595, 20, { tam: 22, peso: 700, color: A, visible: L.tramo(t, 0.29, 0.32) });
      var col = L.tramo(t, 0.57, 0.6) > 0.5;
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.34), function () {
        L.rectRed(ctx, 410, 62, 120, 46, 10); L.rellena(ctx, L.tono(S, 0.7), m.tinta, 2);
        UJ.rotulo(ctx, lz, col ? '"M-011"' : '"M-004"', 470, 74, { tam: 19, peso: 700 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.33, 0.37), function () {
        L.flecha(ctx, 532, 85, 572, 85, m.tinta, 3, 1);
        L.rectRed(ctx, 578, 62, 190, 46, 10); L.rellena(ctx, L.tono(C, 0.85), C, 2);
        UJ.rotulo(ctx, lz, 'hashCode() → casilla 3', 673, 76, { tam: 16, peso: 700 });
      });
      // casillas
      for (var k = 0; k < 6; k++) {
        var by = 140 + k * 46;
        UJ.alfa(ctx, L.tramo(t, 0.3, 0.34), function () {
          L.rectRed(ctx, 410, by, 320, 40, 6); L.rellena(ctx, k === 3 && t > 0.44 ? L.tono(S, 0.75) : m.papel, L.tono(A, 0.5), 1);
          UJ.rotulo(ctx, lz, '[' + k + ']', 418, by + 9, { tam: 17, alinear: 'left', color: m.gris || m.tinta });
        });
      }
      var tr = L.tramo(t, 0.37, 0.45);
      if (tr > 0) L.trazo(ctx, [[760, 110], [760, 298], [736, 298]], tr, m.tinta, 3);
      if (tr >= 1) L.flecha(ctx, 750, 298, 734, 298, m.tinta, 3, 1);
      function chip(x, txt, c, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, 282, 122, 32, 6); L.rellena(ctx, L.tono(c, 0.85), c, 2);
          UJ.rotulo(ctx, lz, txt, x + 61, 288, { tam: 15, peso: 700 });
        });
      }
      chip(446, 'M-004 → Luna', A, L.tramo(t, 0.3, 0.34) * (1 - 0.55 * L.tramo(t, 0.7, 0.74)));
      chip(574, 'M-011 → Rocky', A, L.tramo(t, 0.6, 0.66));
      UJ.rotulo(ctx, lz, 'Directo a la casilla: no recorre.', 580, 430, { tam: 18, peso: 700, color: V, ancho: 360, visible: L.tramo(t, 0.46, 0.52) * (1 - L.tramo(t, 0.56, 0.58)) });
      UJ.rotulo(ctx, lz, 'Colisión: equals() compara y elige M-011.', 580, 420, { tam: 18, peso: 700, color: R, ancho: 360, visible: L.tramo(t, 0.66, 0.74) });
      UJ.sello(ctx, lz, 714, 298, 13, true, L.tramo(t, 0.72, 0.76));
      // cierre
      UJ.rotulo(ctx, lz, 'get("M-004") tarda lo mismo con 10 que con 100.000 elementos.', 400, 500, { tam: 22, peso: 700, ancho: 760, visible: L.tramo(t, 0.84, 0.92) });
      UJ.rotulo(ctx, lz, 'hashCode() elige la casilla; equals() distingue dentro de ella.', 400, 560, { tam: 19, color: A, ancho: 760, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
