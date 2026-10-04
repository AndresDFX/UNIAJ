/* Cada hallazgo entra al backlog con responsable, severidad y criterio de cierre, y termina en
 * uno de tres estados; el paquete se cierra contra una Definicion de Terminado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('backlog-deuda', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.56, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Del hallazgo al backlog', W / 2, 16, { tam: 25, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var h = [
        ['H-01', ['Consulta sin Veterinario', 'resp.: Ana · mayor', 'cierre: relación en clases'], 'aceptado', m.verde],
        ['H-02', ['RF-07 sin caso de uso', 'resp.: Luis · mayor', 'cierre: CU nuevo o RF fuera'], 'aplazado por acuerdo', m.sello],
        ['H-03', ['Renombrar Cita a Reserva', 'resp.: Ana · menor', 'cierre: ya está en glosario'], 'rechazado con justificación', m.gris]
      ];
      for (var i = 0; i < 3; i++) {
        var x = 24 + i * 258;
        UJ.tarjeta(ctx, lz, x, 58, 236, h[i][0], h[i][1], A, L.tramo(t, 0.04 + i * 0.07, 0.1 + i * 0.07),
          L.tramo(t, 0.06 + i * 0.07, 0.16 + i * 0.07) * 3, { tam: 17, alto: 150 });
        (function (x, e, c, a) {
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, x + 18, 222, 200, 58, 14); L.rellena(ctx, L.tono(c, 0.82), L.tono(c, -0.2), 2);
            var alto = L.texto(ctx, e, -9999, -9999, { tam: 17, peso: 700, letra: lz.letra, ancho: 180 });
            UJ.rotulo(ctx, lz, e, x + 118, 251 - alto / 2, { tam: 17, peso: 700, color: L.tono(c, -0.45), ancho: 180 });
          });
        })(x, h[i][2], h[i][3], L.tramo(t, 0.32 + i * 0.06, 0.38 + i * 0.06));
      }

      // Definicion de Terminado
      UJ.alfa(ctx, L.tramo(t, 0.58, 0.62), function () {
        L.rectRed(ctx, 150, 300, 500, 236, 14); L.rellena(ctx, L.tono(A, 0.94), A, 2);
        UJ.rotulo(ctx, lz, 'Definición de Terminado del paquete', W / 2, 312, { tam: 20, peso: 800, color: A });
      });
      var dod = ['RF y RNF sin huérfanos', 'Casos de uso especificados', 'Clases con multiplicidades', 'Mockups de las pantallas', 'Diccionario de datos'];
      for (var k = 0; k < dod.length; k++) {
        (function (k) {
          var y = 350 + k * 36, a = L.tramo(t, 0.6 + k * 0.03, 0.64 + k * 0.03);
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, 190, y, 24, 24, 5); L.rellena(ctx, m.papel, A, 2);
            UJ.rotulo(ctx, lz, dod[k], 228, y + 1, { tam: 18, peso: 600, alinear: 'left' });
          });
          var v = L.tramo(t, 0.76 + k * 0.04, 0.8 + k * 0.04);
          if (v > 0) L.trazo(ctx, [[194, y + 12], [200, y + 19], [211, y + 5]], v, m.verde, 4);
        })(k);
      }
      UJ.rotulo(ctx, lz, 'Sin la lista marcada, el paquete no está terminado', W / 2, 562,
        { tam: 21, peso: 700, color: m.tinta, ancho: W - 40, visible: L.tramo(t, 0.94, 1) });
    }
  });
})();
