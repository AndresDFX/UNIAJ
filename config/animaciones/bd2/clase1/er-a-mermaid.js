/* Del ER al codigo Mermaid: boceto -> texto erDiagram (la IA traduce, el estudiante revisa) ->
 * visor que lo renderiza. Un diagrama que no renderiza no comunica nada. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('er-a-mermaid', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A;
      UJ.caja(ctx, lz, 30, 30, 220, 90, 'Boceto', 'draw.io · Excalidraw', C, L.tramo(t, 0, 0.08));
      L.flecha(ctx, 256, 75, 310, 75, L.tono(m.tinta, 0.4), 3, L.tramo(t, 0.08, 0.14));
      UJ.caja(ctx, lz, 316, 30, 180, 90, 'IA', 'traduce la sintaxis', A, L.tramo(t, 0.12, 0.2));
      L.flecha(ctx, 502, 75, 556, 75, L.tono(m.tinta, 0.4), 3, L.tramo(t, 0.18, 0.24));
      UJ.caja(ctx, lz, 562, 30, 210, 90, 'Texto', 'erDiagram', A, L.tramo(t, 0.22, 0.3));
      var lineas = ['erDiagram', 'DUENO ||--o{ MASCOTA : posee', 'DUENO {', 'int id_dueno PK', 'string telefono', '}'], sangria = [0, 1, 1, 2, 2, 1];
      var n = L.tramo(t, 0.32, 0.5) * lineas.length;
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.34), function () {
        L.rectRed(ctx, 30, 150, 420, 250, 10); L.rellena(ctx, L.tono(m.tinta, -0.55));
      });
      for (var i = 0; i < lineas.length; i++) {
        if (n > i) L.texto(ctx, lineas[i], 46 + sangria[i] * 22, 166 + i * 38, { tam: 18, color: '#E8F4FA', letra: 'Consolas, monospace', visible: Math.min(1, n - i) });
      }
      var rev = ['entidades completas', 'cardinalidad bien orientada', 'PK y FK marcadas'];
      UJ.rotulo(ctx, lz, 'El modelo es tuyo: revisa', 615, 150, { tam: 19, peso: 800, color: C, visible: L.tramo(t, 0.5, 0.56) });
      for (var k = 0; k < 3; k++) {
        UJ.sello(ctx, lz, 490, 212 + k * 56, 14, true, L.tramo(t, 0.52 + k * 0.03, 0.58 + k * 0.03));
        UJ.rotulo(ctx, lz, rev[k], 514, 200 + k * 56, { tam: 18, alinear: 'left', ancho: 260, visible: L.tramo(t, 0.52 + k * 0.03, 0.6 + k * 0.03) });
      }
      // Visor
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.76), function () {
        L.flecha(ctx, 240, 404, 240, 440, L.tono(m.tinta, 0.4), 3);
        L.rectRed(ctx, 30, 446, W - 60, 130, 12); L.rellena(ctx, m.papel, V, 3);
        UJ.rotulo(ctx, lz, 'Visor Mermaid', 110, 456, { tam: 17, peso: 800, color: V });
        L.rectRed(ctx, 230, 480, 150, 60, 6); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'DUENO', 305, 497, { tam: 18, peso: 700, color: A });
        L.rectRed(ctx, 480, 480, 150, 60, 6); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'MASCOTA', 555, 497, { tam: 18, peso: 700, color: A });
        L.trazo(ctx, [[380, 510], [480, 510]], 1, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'posee', 430, 484, { tam: 15, color: C });
      });
      UJ.rotulo(ctx, lz, 'Si no renderiza, no comunica: se mira siempre.', W / 2, 594,
                { tam: 19, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
