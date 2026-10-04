/* El parametro lo evita por construccion: el motor analiza primero la sentencia con su marcador,
 * y solo despues recibe el valor como dato tipado en una casilla ya reservada. Nunca se re-analiza. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('parametro', {
    duracion: 5,
    pasos: [0.34, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // 1. La sentencia sola
      UJ.rotulo(ctx, lz, '1 · llega la sentencia, sin valores', 30, 20, { tam: 21, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 58, 740, 'SELECT id_mascota, nombre FROM mascota WHERE nombre = $1', L.tramo(t, 0, 0.14), 18);
      L.flecha(ctx, 160, 104, 160, 160, A, 4, L.tramo(t, 0.14, 0.2, 'frena'));
      UJ.caja(ctx, lz, 40, 164, 240, 80, 'analizador', 'estructura fija', A, L.tramo(t, 0.18, 0.26));
      L.flecha(ctx, 284, 204, 380, 204, A, 4, L.tramo(t, 0.24, 0.3, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.28, 0.34), function () {
        L.rectRed(ctx, 384, 164, 386, 80, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'nombre =', 400, 190, { tam: 21, peso: 700, color: A, alinear: 'left' });
        ctx.setLineDash([6, 5]); L.rectRed(ctx, 558, 186, 194, 38, 8); ctx.strokeStyle = A; ctx.lineWidth = 2; ctx.stroke(); ctx.setLineDash([]);
        UJ.rotulo(ctx, lz, 'casilla', 655, 228, { tam: 15, peso: 600, color: A });
      });
      // 2. Llega el valor
      UJ.rotulo(ctx, lz, '2 · después llega el valor, como dato', 30, 290, { tam: 21, peso: 800, color: C, alinear: 'left', visible: L.tramo(t, 0.36, 0.42) });
      var y = L.claves(t, [[0.42, 340], [0.58, 188, 'frena']]);
      if (t >= 0.42) UJ.alfa(ctx, 1, function () {
        L.rectRed(ctx, 560, y, 190, 34, 8); L.rellena(ctx, m.sello || C, m.tinta, 2);
        UJ.rotulo(ctx, lz, "' OR 1=1 --", 655, y + 6, { tam: 18, peso: 700 });
      });
      UJ.rotulo(ctx, lz, 'texto literal; no vuelve al analizador', 577, 254, { tam: 17, peso: 700, color: C, visible: L.tramo(t, 0.58, 0.66) });
      // 3. Resultado
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.8), function () {
        L.rectRed(ctx, 200, 380, 400, 70, 12); L.rellena(ctx, L.tono(V, 0.85), V, 2);
        UJ.rotulo(ctx, lz, '0 filas: ninguna se llama así', 400, 402, { tam: 21, peso: 800, color: L.tono(V, -0.3) });
      });
      UJ.sello(ctx, lz, 640, 415, 24, true, L.tramo(t, 0.78, 0.86));
      UJ.rotulo(ctx, lz, 'No se filtra la entrada: la estructura ya estaba cerrada.', W / 2, 520,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
