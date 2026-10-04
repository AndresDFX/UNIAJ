/* Un plan es un arbol: se lee de adentro hacia afuera. Las hojas (mas indentadas) se ejecutan
 * primero; la primera linea impresa es la ULTIMA operacion. Es el plan real de la consulta del
 * dia (cita JOIN mascota, 2026-03-10) en la base sembrada. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('leer-plan', {
    duracion: 5,
    // Pasos LOGICOS: 1) lo que imprime EXPLAIN, tal cual; 2) esas lineas son un arbol;
    // 3) el orden en que se ejecuta (hojas primero) y la regla.
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // 1 · la salida de EXPLAIN
      var lineas = ['Hash Join  (cost=149.68..851.22 rows=150)', '  ->  Seq Scan on cita c',
                    '        Filter: (fecha del 2026-03-10)', '  ->  Hash', '        ->  Seq Scan on mascota m'];
      for (var i = 0; i < lineas.length; i++) {
        UJ.alfa(ctx, L.tramo(t, i * 0.04, 0.06 + i * 0.04), function () { UJ.codigo(ctx, lz, 40, 26 + i * 44, W - 80, lineas[i], 1, 18); });
      }
      UJ.rotulo(ctx, lz, 'Lo que imprime EXPLAIN', W / 2, 250, { tam: 18, peso: 600, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.2, 0.26) });
      // 2 · el mismo plan como arbol
      var n = [[420, 320, 'Hash Join', false], [250, 420, 'Seq Scan cita', true], [600, 420, 'Hash', false], [600, 510, 'Seq Scan mascota', true]];
      var aa = L.tramo(t, 0.34, 0.46);
      L.trazo(ctx, [[420, 346], [250, 394]], aa, L.tono(m.tinta, 0.5), 3);
      L.trazo(ctx, [[420, 346], [600, 394]], aa, L.tono(m.tinta, 0.5), 3);
      L.trazo(ctx, [[600, 446], [600, 484]], aa, L.tono(m.tinta, 0.5), 3);
      for (var k = 0; k < 4; k++) {
        UJ.alfa(ctx, aa, function () {
          var x = n[k][0], y = n[k][1];
          L.rectRed(ctx, x - 100, y - 26, 200, 52, 12);
          L.rellena(ctx, n[k][3] ? L.tono(C, 0.85) : L.tono(A, 0.88), n[k][3] ? C : A, 2);
          UJ.rotulo(ctx, lz, n[k][2], x, y - 12, { tam: 19, peso: 700 });
        });
      }
      UJ.rotulo(ctx, lz, 'hoja', 250, 450, { tam: 16, peso: 700, color: L.tono(C, -0.3), visible: L.tramo(t, 0.48, 0.56) });
      UJ.rotulo(ctx, lz, 'hoja', 600, 540, { tam: 16, peso: 700, color: L.tono(C, -0.3), visible: L.tramo(t, 0.48, 0.56) });
      UJ.rotulo(ctx, lz, 'raíz', 560, 306, { tam: 18, peso: 700, color: A, visible: L.tramo(t, 0.48, 0.56) });
      // 3 · el orden de ejecucion: hojas primero, la raiz al final
      var orden = [1, 3, 2, 0];
      for (var j = 0; j < 4; j++) {
        var a = L.tramo(t, 0.64 + j * 0.05, 0.69 + j * 0.05);
        if (a <= 0) continue;
        var q = n[orden[j]];
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, q[0] - 122, q[1], 19); L.rellena(ctx, m.sello || C, m.tinta, 2);
          UJ.rotulo(ctx, lz, String(j + 1), q[0] - 122, q[1] - 12, { tam: 20, peso: 800 });
        });
      }
      UJ.rotulo(ctx, lz, 'Se lee desde las hojas: la primera línea es la ÚLTIMA operación.', W / 2, 576,
                { tam: 20, ancho: W - 40, color: A, visible: L.tramo(t, 0.86, 0.98) });
    }
  });
})();
