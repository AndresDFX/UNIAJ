/* Tres criterios de aceptación en Dado | Cuando | Entonces; el camino alterno se resalta y cada
 * fila se responde con sí o no. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dado-cuando-entonces', {
    duracion: 5,
    // Pasos LOGICOS: 1) los tres criterios en Dado | Cuando | Entonces; 2) el camino alterno;
    // 3) la columna ¿Pasa? con su sí / no. La columna vacía no se ve antes de su paso.
    pasos: [0.38, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Criterios de aceptación', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var cols = [['Dado', 30, 220], ['Cuando', 250, 170], ['Entonces', 420, 250], ['¿Pasa?', 670, 100]];
      var y0 = 80, cab = 44, alto = 96;
      var filas = [
        ['dueño con 3 mascotas', 'busco por documento', 'lista las 3'],
        ['selecciono a Rocky', 'abro su historial', 'atenciones de la más reciente a la más antigua'],
        ['documento que no existe', 'busco', 'mensaje claro y ofrece crear el dueño']
      ];
      var ap = L.tramo(t, 0.68, 0.72);
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.12), function () {
        for (var c = 0; c < 3; c++) {
          L.rectRed(ctx, cols[c][1], y0, cols[c][2], cab, 0); L.rellena(ctx, c === 3 ? m.gris : A, m.papel, 2);
          UJ.rotulo(ctx, lz, cols[c][0], cols[c][1] + cols[c][2] / 2, y0 + 11, { tam: 20, peso: 800, color: m.papel });
        }
      });
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, 0.12 + i * 0.07, 0.2 + i * 0.07), y = y0 + cab + i * alto;
        (function (i, y) {
          UJ.alfa(ctx, a, function () {
            for (var c = 0; c < 3; c++) {
              L.rectRed(ctx, cols[c][1], y, cols[c][2], alto, 0);
              L.rellena(ctx, i % 2 ? L.tono(A, 0.93) : m.papel, L.tono(A, 0.55), 1.5);
              L.texto(ctx, filas[i][c], cols[c][1] + 12, y + 14, { tam: 18, peso: 500, color: m.tinta, ancho: cols[c][2] - 22, letra: lz.letra });
            }
          });
          // La columna ¿Pasa? llega en el paso 3, con su respuesta.
          UJ.alfa(ctx, ap, function () {
            L.rectRed(ctx, cols[3][1], y, cols[3][2], alto, 0);
            L.rellena(ctx, i % 2 ? L.tono(A, 0.93) : m.papel, L.tono(A, 0.55), 1.5);
          });
        })(i, y);
      }
      UJ.alfa(ctx, ap, function () {
        L.rectRed(ctx, cols[3][1], y0, cols[3][2], cab, 0); L.rellena(ctx, m.gris, m.papel, 2);
        UJ.rotulo(ctx, lz, cols[3][0], cols[3][1] + cols[3][2] / 2, y0 + 11, { tam: 20, peso: 800, color: m.papel });
      });
      // El camino alterno
      var yr = y0 + cab + 2 * alto, ar = L.tramo(t, 0.42, 0.56);
      UJ.alfa(ctx, ar, function () {
        L.rectRed(ctx, 30, yr, 640, alto, 6); L.rellena(ctx, null, R, 4);
        UJ.rotulo(ctx, lz, 'camino alterno: el que siempre falta', 350, yr + alto + 14, { tam: 20, peso: 800, color: R });
      });
      // Sí / no
      for (var j = 0; j < 3; j++) {
        UJ.pildora(ctx, lz, 720, y0 + cab + j * alto + 30, 'sí / no', m.verde, L.tramo(t, 0.72 + j * 0.05, 0.77 + j * 0.05), { tam: 16, centrar: true });
      }
      UJ.rotulo(ctx, lz, 'Se responde con sí o no mirando la pantalla, nunca con «depende»', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
