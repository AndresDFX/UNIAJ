/* Trazabilidad de un RF: hacia atrás, la necesidad de donde salió; hacia adelante, el caso de
 * uso, la pantalla y la prueba. Si el cliente cambia de opinión, se ve qué se rompe. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('traza-atras-adelante', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.32, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, C = m.acento, W = lz.ancho;
      function bx(i) { return 26 + i * 154; }
      var cajas = [['NEC-02', 'entrevista Dr. Ramírez, frase 2', C], ['RF-03', 'Consultar historial', A],
        ['CU-04', 'caso de uso', A], ['P-02', 'pantalla', A], ['PR-07', 'prueba', A]];
      var rojo = L.tramo(t, 0.8, 0.9);
      var aparece = [L.tramo(t, 0.18, 0.26), L.tramo(t, 0, 0.08), L.tramo(t, 0.34, 0.4), L.tramo(t, 0.42, 0.48), L.tramo(t, 0.5, 0.56)];
      UJ.rotulo(ctx, lz, 'Trazabilidad de un requisito', W / 2, 22, { tam: 25, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 5; i++) {
        (function (i) {
          var c = cajas[i][2];
          if (i >= 2) c = L.mezclaColor(A, R, rojo);
          var x = bx(i);
          UJ.alfa(ctx, aparece[i], function () {
            L.rectRed(ctx, x, 210, 130, 120, 12);
            L.rellena(ctx, L.tono(c, i === 1 ? 0.78 : 0.9), c, i === 1 ? 4 : 2.5);
            UJ.rotulo(ctx, lz, cajas[i][0], x + 65, 224, { tam: 21, peso: 800, color: L.tono(c, -0.3) });
            UJ.rotulo(ctx, lz, cajas[i][1], x + 65, 258, { tam: 16, peso: 600, color: m.tinta, ancho: 116 });
          });
        })(i);
      }
      UJ.flecha(ctx, lz, 158, 270, 178, 270, C, L.tramo(t, 0.22, 0.26));
      for (var k = 1; k < 4; k++) {
        UJ.flecha(ctx, lz, bx(k) + 132, 270, bx(k + 1) - 2, 270, L.mezclaColor(A, R, rojo), aparece[k + 1]);
      }
      // Llaves de dirección
      UJ.alfa(ctx, L.tramo(t, 0.2, 0.28), function () {
        L.trazo(ctx, [[30, 196], [30, 186], [152, 186], [152, 196]], 1, C, 3);
        UJ.rotulo(ctx, lz, 'hacia atrás', 91, 116, { tam: 19, peso: 800, color: C });
        UJ.rotulo(ctx, lz, '¿quién lo pidió?', 91, 146, { tam: 17, peso: 600, color: m.tinta });
      });
      UJ.alfa(ctx, L.tramo(t, 0.54, 0.6), function () {
        L.trazo(ctx, [[338, 196], [338, 186], [770, 186], [770, 196]], 1, A, 3);
        UJ.rotulo(ctx, lz, 'hacia adelante', 554, 116, { tam: 19, peso: 800, color: A });
        UJ.rotulo(ctx, lz, '¿dónde termina?', 554, 146, { tam: 17, peso: 600, color: m.tinta });
      });
      // El cliente cambia de opinión
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.74), function () {
        UJ.rayo(ctx, 60, 372, 56, m.sello, 1);
        UJ.rotulo(ctx, lz, 'el cliente cambia de opinión', 94, 386, { tam: 19, peso: 700, color: m.tinta, alinear: 'left' });
      });
      UJ.alfa(ctx, rojo, function () {
        L.trazo(ctx, [[338, 340], [338, 350], [770, 350], [770, 340]], 1, R, 3);
        UJ.pildora(ctx, lz, 554, 450, 'qué se rompe, en dos minutos', R, 1, { tam: 20, centrar: true, lleno: true });
      });
      UJ.rotulo(ctx, lz, 'Cada RF dice de dónde viene y hasta dónde llega.', W / 2, 560,
        { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
