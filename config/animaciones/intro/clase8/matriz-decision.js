/* Una matriz de decision de dos alternativas: criterios, pesos decididos antes, calificacion
 * 1-3 por criterio y el total ponderado. A: 3x3 + 1x2 + 2x1 = 13; B: 1x3 + 3x2 + 2x1 = 11. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('matriz-decision', {
    duracion: 5,
    pasos: [0.25, 0.5, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', S = m.sello || C, W = lz.ancho;
      var cols = [40, 330, 450, 600], anc = [290, 120, 150, 150], y0 = 40, fh = 70;
      function celda(c, f, txt, a, o) {
        o = o || {};
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, cols[c], y0 + f * fh, anc[c], fh, 0);
          L.rellena(ctx, o.fondo || (f % 2 ? L.tono(A, 0.94) : m.papel), L.tono(A, 0.6), 1);
          UJ.rotulo(ctx, lz, txt, cols[c] + anc[c] / 2, y0 + f * fh + 20, { tam: o.tam || 22, peso: o.peso || 600, color: o.color, ancho: anc[c] - 16 });
        });
      }
      var a1 = L.tramo(t, 0, 0.12), a2 = L.tramo(t, 0.28, 0.4), a3 = L.tramo(t, 0.52, 0.7), a4 = L.tramo(t, 0.8, 0.9);
      celda(0, 0, 'Criterio', a1, { fondo: L.tono(A, 0.75), peso: 800 });
      celda(1, 0, 'Peso', a2, { fondo: L.tono(S, 0.5), peso: 800 });
      celda(2, 0, 'A · web', a1, { fondo: L.tono(A, 0.75), peso: 800 });
      celda(3, 0, 'B · app', a1, { fondo: L.tono(A, 0.75), peso: 800 });
      var crit = [['Costo', 3, 3, 1], ['Facilidad de uso', 2, 1, 3], ['Tiempo de construir', 1, 2, 2]];
      for (var i = 0; i < 3; i++) {
        celda(0, i + 1, crit[i][0], a1);
        celda(1, i + 1, '× ' + crit[i][1], a2, { color: L.tono(S, -0.45), peso: 800 });
        celda(2, i + 1, String(crit[i][2]), L.tramo(t, 0.52 + i * 0.05, 0.6 + i * 0.05));
        celda(3, i + 1, String(crit[i][3]), L.tramo(t, 0.54 + i * 0.05, 0.62 + i * 0.05));
      }
      celda(0, 4, 'Total ponderado', a4, { peso: 800 });
      celda(2, 4, '13', a4, { fondo: L.tono(V, 0.8), peso: 800, tam: 28, color: V });
      celda(3, 4, '11', a4, { fondo: L.tono(R, 0.85), peso: 800, tam: 28, color: R });
      UJ.rotulo(ctx, lz, 'pesos decididos ANTES de calificar', 390, 410, { tam: 18, peso: 700, color: L.tono(S, -0.45), visible: L.tramo(t, 0.34, 0.44) });
      UJ.rotulo(ctx, lz, 'escala 1-3, con su porqué', 600, 450, { tam: 18, peso: 700, visible: L.tramo(t, 0.66, 0.74) });
      UJ.alfa(ctx, L.tramo(t, 0.9, 1), function () {
        L.rectRed(ctx, 40, 500, 720, 100, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'Gana A. Lo que se pierde: facilidad de uso.', W / 2, 514, { tam: 24, peso: 800, ancho: 680 });
        UJ.rotulo(ctx, lz, 'Escribirlo es lo que vuelve profesional la decisión.', W / 2, 556, { tam: 19, ancho: 680 });
      });
    }
  });
})();
