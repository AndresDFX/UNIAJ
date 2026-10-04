/* Seq Scan: lee todas las paginas en orden y descarta en memoria. Index Scan: baja el arbol
 * (2 o 3 lecturas) y por cada coincidencia salta a la tabla (lecturas dispersas). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('seq-vs-index', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var N = 12, pw = 52, x0 = 92;
      function paginas(y, marcada) {
        for (var i = 0; i < N; i++) {
          L.rectRed(ctx, x0 + i * pw, y, pw - 8, 56, 6);
          L.rellena(ctx, marcada(i) ? L.tono(C, 0.45) : m.papel, L.tono(m.tinta, 0.5), 2);
        }
      }
      // Seq Scan
      UJ.rotulo(ctx, lz, 'Seq Scan · lee todas las páginas, en orden', W / 2, 26, { tam: 21, peso: 800, color: L.tono(C, -0.3), visible: L.tramo(t, 0, 0.08) });
      var s = L.tramo(t, 0.06, 0.34);
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () { paginas(70, function (i) { return i < s * N; }); });
      UJ.rotulo(ctx, lz, 'lectura secuencial · descarta en memoria lo que no cumple', W / 2, 140, { tam: 17, peso: 500, ancho: W - 60, visible: L.tramo(t, 0.3, 0.38) });
      // Index Scan
      var yi = 200;
      UJ.rotulo(ctx, lz, 'Index Scan · baja el índice y salta a la tabla', W / 2, yi, { tam: 21, peso: 800, color: A, visible: L.tramo(t, 0.42, 0.48) });
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        ctx.strokeStyle = A; ctx.lineWidth = 3; ctx.beginPath();
        ctx.moveTo(400, yi + 64); ctx.lineTo(320, yi + 116); ctx.moveTo(400, yi + 64); ctx.lineTo(480, yi + 116); ctx.stroke();
        L.circulo(ctx, 400, yi + 60, 18); L.rellena(ctx, A);
        L.circulo(ctx, 320, yi + 120, 16); L.rellena(ctx, A); L.circulo(ctx, 480, yi + 120, 16); L.rellena(ctx, L.tono(A, 0.5));
        UJ.rotulo(ctx, lz, '2 o 3 lecturas', 600, yi + 76, { tam: 18, peso: 700, color: A });
      });
      var dest = [1, 9, 4, 11, 6];
      var yp = yi + 210;
      var visto = L.tramo(t, 0.54, 0.78);
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.56), function () {
        paginas(yp, function (i) { for (var k = 0; k < dest.length; k++) if (dest[k] === i && k < visto * dest.length) return true; return false; });
      });
      for (var k = 0; k < dest.length; k++) {
        var p = L.tramo(t, 0.54 + k * 0.048, 0.6 + k * 0.048, 'frena');
        if (p > 0) L.flecha(ctx, 320, yi + 138, x0 + dest[k] * pw + 22, yp - 4, R, 2, p);
      }
      UJ.rotulo(ctx, lz, 'una lectura dispersa por cada fila encontrada', W / 2, yp + 70, { tam: 17, peso: 500, visible: L.tramo(t, 0.76, 0.82) });
      UJ.rotulo(ctx, lz, 'Muchas coincidencias: gana el Seq Scan. Pocas: gana el índice.', W / 2, 580,
                { tam: 20, ancho: W - 40, color: A, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
