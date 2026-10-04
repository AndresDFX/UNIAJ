/* Un plan es un arbol: se lee de adentro hacia afuera. Las hojas (mas indentadas) se ejecutan
 * primero; la primera linea impresa es la ULTIMA operacion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('leer-plan', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var lineas = ['Hash Join  (cost=… rows=… width=…)', '  ->  Seq Scan on cita c', '        Filter: (fecha del día)', '  ->  Hash', '        ->  Seq Scan on mascota m'];
      for (var i = 0; i < lineas.length; i++) {
        UJ.alfa(ctx, L.tramo(t, i * 0.05, 0.08 + i * 0.05), function () { UJ.codigo(ctx, lz, 40, 26 + i * 44, W - 80, lineas[i], 1, 18); });
      }
      UJ.rotulo(ctx, lz, 'Lo que imprime EXPLAIN', W / 2, 250, { tam: 18, peso: 600, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.2, 0.28) });
      // Arbol: [x, y, nombre, es hoja]
      var n = [[420, 320, 'Hash Join', false], [250, 420, 'Seq Scan cita', true], [600, 420, 'Hash', false], [600, 510, 'Seq Scan mascota', true]];
      var aa = L.tramo(t, 0.32, 0.42);
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
      // Orden de lectura: hojas primero, la raiz al final
      var orden = [1, 3, 2, 0];
      for (var j = 0; j < 4; j++) {
        var a = L.tramo(t, 0.46 + j * 0.06, 0.52 + j * 0.06);
        if (a <= 0) continue;
        var q = n[orden[j]];
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, q[0] - 122, q[1], 19); L.rellena(ctx, m.sello || C, m.tinta, 2);
          UJ.rotulo(ctx, lz, String(j + 1), q[0] - 122, q[1] - 12, { tam: 20, peso: 800 });
        });
      }
      UJ.rotulo(ctx, lz, 'Se lee desde las hojas: la primera línea es la ÚLTIMA operación.', W / 2, 570,
                { tam: 20, ancho: W - 40, color: A, visible: L.tramo(t, 0.82, 1) });
    }
  });
})();
