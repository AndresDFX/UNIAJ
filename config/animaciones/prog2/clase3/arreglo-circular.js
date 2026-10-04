/* Por que son rapidas: ArrayDeque es un arreglo circular con punteros frente/final que avanzan
 * y dan la vuelta; sacar del frente no mueve a nadie. Contraste: ArrayList remove(0) desplaza
 * a todos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('arreglo-circular', {
    duracion: 5,
    // Pasos LOGICOS: 1) poll: sale Luna y solo avanza el frente, 2) offer x3: el final da la
    // vuelta a la casilla 0, 3) LinkedList: sacar el primero es mover la cabeza, 4) el
    // contraste: ArrayList remove(0) corre a todos. La linea de LinkedList ya no comparte
    // paso con la vuelta del arreglo circular.
    pasos: [0.34, 0.6, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'ArrayDeque: arreglo circular con dos punteros', W / 2, 20, { tam: 22, peso: 700, color: A });
      function sx(i) { return 80 + i * 82; }
      // casillas
      for (var i = 0; i < 8; i++) {
        L.rectRed(ctx, sx(i), 64, 74, 56, 6); L.rellena(ctx, m.papel, L.tono(A, 0.4), 2);
        UJ.rotulo(ctx, lz, String(i), sx(i) + 37, 124, { tam: 15, color: m.gris || m.tinta });
      }
      // contenido: indice -> [nombre, aparece, desaparece]
      var cont = [[2, 'Luna', 0, 0.2], [3, 'Michi', 0, 2], [4, 'Rocky', 0, 2], [5, 'Kira', 0, 2],
                  [6, 'Max', 0.4, 2], [7, 'Nina', 0.46, 2], [0, 'Coco', 0.52, 2]];
      cont.forEach(function (c) {
        var a = L.tramo(t, c[2], c[2] + 0.05) * (1 - L.tramo(t, c[3], c[3] + 0.06));
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, sx(c[0]) + 4, 68, 66, 48, 6); L.rellena(ctx, L.tono(c[2] > 0 ? V : A, 0.82));
          UJ.rotulo(ctx, lz, c[1], sx(c[0]) + 37, 82, { tam: 17, peso: 700 });
        });
      });
      // punteros (posicion fraccional en casillas)
      var fr = L.claves(t, [[0.16, 2], [0.28, 3, 'suave']]);
      var fi = L.claves(t, [[0.4, 6], [0.46, 7, 'suave'], [0.52, 8, 'suave'], [0.58, 9, 'suave']]);
      function puntero(pos, txt, c, y) {
        var p = pos % 8, x = sx(p) + 37;
        ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x - 9, y + 14); ctx.lineTo(x + 9, y + 14); ctx.closePath(); ctx.fillStyle = c; ctx.fill();
        UJ.rotulo(ctx, lz, txt, x, y + 18, { tam: 16, peso: 700, color: c });
      }
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.1), function () { puntero(fr, 'frente', R, 148); puntero(fi, 'final', V, 148); });
      UJ.rotulo(ctx, lz, 'poll(): sale Luna y solo avanza el frente; nadie se mueve.', W / 2, 200, { tam: 18, ancho: W - 40, visible: L.tramo(t, 0.22, 0.3) });
      UJ.rotulo(ctx, lz, 'offer() al llegar al borde: el final da la vuelta a la casilla 0.', W / 2, 232, { tam: 18, color: V, ancho: W - 40, visible: L.tramo(t, 0.53, 0.59) });
      UJ.rotulo(ctx, lz, 'LinkedList: cadena de nodos; sacar el primero es mover la cabeza.', W / 2, 264, { tam: 18, color: A, ancho: W - 40, visible: L.tramo(t, 0.61, 0.67) });
      // ArrayList remove(0)
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.74), function () {
        ctx.strokeStyle = L.tono(m.tinta, 0.75); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(20, 316); ctx.lineTo(W - 20, 316); ctx.stroke();
        UJ.rotulo(ctx, lz, 'ArrayList como cola: remove(0)', W / 2, 334, { tam: 22, peso: 700, color: R });
        for (var j = 0; j < 7; j++) { L.rectRed(ctx, 80 + j * 92, 384, 84, 56, 6); L.rellena(ctx, m.papel, L.tono(R, 0.4), 2); }
      });
      var nombres = ['Luna', 'Michi', 'Rocky', 'Kira', 'Max', 'Nina'];
      var corre = L.tramo(t, 0.8, 0.9, 'suave');
      for (var k = 0; k < 6; k++) {
        var a = L.tramo(t, 0.7, 0.74) * (k === 0 ? 1 - L.tramo(t, 0.75, 0.79) : 1);
        var x = 80 + (k - (k > 0 ? corre : 0)) * 92;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x + 4, 388, 76, 48, 6); L.rellena(ctx, L.tono(A, 0.82));
          UJ.rotulo(ctx, lz, nombres[k], x + 42, 402, { tam: 17, peso: 700 });
        });
        if (k > 0) UJ.alfa(ctx, L.tramo(t, 0.79, 0.81), function () {
          L.flecha(ctx, 80 + k * 92 + 42, 460, 80 + (k - 1) * 92 + 50, 460, R, 3, 1);
        });
      }
      UJ.rotulo(ctx, lz, 'remove(0) corre a todos los demás un puesto: más lenta cuanto más larga la lista.', W / 2, 500, { tam: 19, peso: 700, color: R, ancho: W - 60, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
