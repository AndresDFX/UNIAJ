/* ArrayList por dentro: arreglo interno de capacidad 4; size sube de 1 a 4; el quinto add crea
 * uno de 6 (~1,5x), copia y agrega; remove(0) corre a todos un puesto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('arraylist-crece', {
    duracion: 5,
    // Pasos LOGICOS: 1) el arreglo interno de 4 se llena (size = capacidad), 2) el quinto add
    // crea uno de 6 y copia los 4, 3) Nala entra y el viejo queda para el recolector,
    // 4) remove(0) corre a todos un puesto, 5) la conclusion.
    pasos: [0.24, 0.5, 0.72, 0.9, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      var nom = ['Luna', 'Michi', 'Rocky', 'Toby', 'Nala'], cw = 120, ch = 64, x0 = 40;
      function fila(y, n, titulo, color, a) {
        UJ.alfa(ctx, a, function () {
          UJ.rotulo(ctx, lz, titulo, x0, y - 30, { tam: 17, peso: 700, alinear: 'left', color: color, letra: 'Consolas, monospace' });
          for (var k = 0; k < n; k++) {
            L.rectRed(ctx, x0 + k * cw, y, cw, ch, 8); L.rellena(ctx, m.papel, color, 2);
            UJ.rotulo(ctx, lz, '[' + k + ']', x0 + k * cw + cw / 2, y + ch + 4, { tam: 15, color: m.gris, letra: 'Consolas, monospace' });
          }
        });
      }
      function ficha(x, y, texto, color, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x + 6, y + 6, cw - 12, ch - 12, 6); L.rellena(ctx, L.tono(color, 0.8));
          UJ.rotulo(ctx, lz, texto, x + cw / 2, y + 20, { tam: 19, peso: 700 });
        });
      }
      function contador(size, cap) {
        L.rectRed(ctx, 560, 20, 216, 90, 12); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'size = ' + size, 580, 32, { tam: 22, peso: 800, alinear: 'left', color: V, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'capacidad = ' + cap, 580, 68, { tam: 20, peso: 700, alinear: 'left', color: A, letra: 'Consolas, monospace' });
      }
      var yA = 80, yB = 260, viejo = 1 - L.tramo(t, 0.62, 0.68) * 0.75;
      // Arreglo interno de 4
      UJ.alfa(ctx, viejo, function () {
        fila(yA, 4, 'arreglo interno (4 casillas)', A, L.tramo(t, 0, 0.06));
        for (var i = 0; i < 4; i++) ficha(x0 + i * cw, yA, nom[i], V, L.tramo(t, 0.04 + i * 0.045, 0.08 + i * 0.045));
      });
      var size = 0;
      for (var s = 0; s < 4; s++) if (t >= 0.08 + s * 0.045) size = s + 1;
      // Quinto add: se crea uno de 6 y se copia
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.3), function () { UJ.codigo(ctx, lz, 560, 124, 216, 'add(nala); // lleno', 1, 17); });
      fila(yB, 6, 'nuevo arreglo: 4 × 1,5 = 6', C, L.tramo(t, 0.3, 0.36));
      for (var j = 0; j < 4; j++) {
        var tj = 0.36 + j * 0.03;
        L.flecha(ctx, x0 + j * cw + cw / 2, yA + ch + 22, x0 + j * cw + cw / 2, yB - 40, C, 3, L.tramo(t, tj, tj + 0.03, 'frena') * (1 - L.tramo(t, 0.62, 0.66)));
      }
      // Fichas en el nuevo, con remove(0) que corre a todos
      var corre = L.tramo(t, 0.78, 0.9, 'suave'), sale = L.tramo(t, 0.74, 0.78);
      for (var q = 0; q < 5; q++) {
        var a = q < 4 ? L.tramo(t, 0.38 + q * 0.03, 0.41 + q * 0.03) : L.tramo(t, 0.54, 0.6);
        var pos = q === 0 ? 0 : q - corre;
        var col = q === 4 ? C : V;
        if (q === 0) {
          var yy = yB - sale * 30;
          ficha(x0, yy, nom[0], sale > 0 ? R : V, a * (1 - sale));
        } else ficha(x0 + pos * cw, yB, nom[q], col, a);
      }
      if (t < 0.36) contador(size, 4);
      else if (t < 0.56) contador(4, 6);
      else if (t < 0.78) contador(5, 6);
      else contador(4, 6);
      UJ.rotulo(ctx, lz, 'el viejo queda para el recolector', 668, 176, { tam: 16, color: m.gris, ancho: 210, visible: L.tramo(t, 0.62, 0.7) });
      // remove(0)
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.76), function () { UJ.codigo(ctx, lz, 24, 380, 200, 'remove(0);', 1, 17); });
      for (var r = 1; r < 5; r++) {
        L.flecha(ctx, x0 + r * cw + cw / 2, yB + ch + 30, x0 + (r - 1) * cw + cw / 2 + 10, yB + ch + 30, R, 3, L.tramo(t, 0.78, 0.88, 'frena') * (1 - L.tramo(t, 0.92, 0.94)));
      }
      UJ.rotulo(ctx, lz, 'remove(0) corre a todos un puesto', 520, 386, { tam: 18, peso: 700, color: R, visible: L.tramo(t, 0.8, 0.88) });
      UJ.alfa(ctx, L.tramo(t, 0.9, 0.98), function () {
        L.rectRed(ctx, 24, 450, W - 48, 160, 14); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'size: elementos guardados · capacidad: casillas', W / 2, 466, { tam: 21, peso: 800, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'get(i) es inmediato y add al final es barato;', W / 2, 516, { tam: 19, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'add(0, x) o remove(0) mueven a todos.', W / 2, 548, { tam: 19, ancho: W - 80 });
      });
    }
  });
})();
