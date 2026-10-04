/* Cambiar el esquema sin romper: nunca en su lugar. Expandir, escribir en ambos lados, rellenar
 * por lotes, mover lecturas y contraer; en cada paso conviven la version vieja y la nueva. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('expandir-contraer', {
    duracion: 5,
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var pasos = [['1 · Expandir', 'columna nueva que admite nulos'], ['2 · Escribir en ambos', 'el procedimiento llena las dos'],
                   ['3 · Rellenar histórico', 'UPDATE por lotes, sin bloquear'], ['4 · Mover lecturas', 'reportes a la columna nueva'],
                   ['5 · Contraer', 'borrar lo viejo cuando nadie lo usa']];
      var tiempos = [0.04, 0.34, 0.46, 0.58, 0.74];
      for (var i = 0; i < 5; i++) {
        var y = 20 + i * 92, a = L.tramo(t, tiempos[i], tiempos[i] + 0.08);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 20 + i * 24, y, 440, 78, 12); L.rellena(ctx, L.tono(i === 4 ? C : A, 0.9), i === 4 ? C : A, 2);
          UJ.rotulo(ctx, lz, pasos[i][0], 36 + i * 24, y + 10, { tam: 21, peso: 800, alinear: 'left', color: i === 4 ? L.tono(C, -0.3) : A });
          UJ.rotulo(ctx, lz, pasos[i][1], 36 + i * 24, y + 42, { tam: 17, peso: 500, alinear: 'left', ancho: 410 });
        });
      }
      // Versiones conviviendo
      var x0 = 600;
      UJ.rotulo(ctx, lz, 'vieja', x0, 2, { tam: 17, peso: 800, color: R, visible: L.tramo(t, 0.04, 0.1) });
      UJ.rotulo(ctx, lz, 'nueva', x0 + 152, 2, { tam: 17, peso: 800, color: V, visible: L.tramo(t, 0.04, 0.1) });
      var hv = L.tramo(t, 0.04, 0.82) * 4 * 92 + 10, hn = L.tramo(t, 0.04, 0.9) * 470;
      L.rectRed(ctx, x0 - 22, 30, 44, Math.min(hv, 4 * 92 + 10), 8); L.rellena(ctx, L.tono(R, 0.6));
      L.rectRed(ctx, x0 + 130, 30, 44, hn, 8); L.rellena(ctx, L.tono(V, 0.5));
      UJ.rotulo(ctx, lz, 'conviven', x0 + 65, 200, { tam: 16, peso: 700, visible: L.tramo(t, 0.4, 0.5) });
      UJ.rotulo(ctx, lz, 'Nunca se cambia en su lugar: se expande, se migra, se contrae.', W / 2, 545,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
