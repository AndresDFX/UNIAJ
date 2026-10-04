/* Ilustracion: que observar en la demo de la Clase 2. El mismo ciclo de la clinica en dos
 * recorridos: una sola pasada, o tres vueltas que entregan una parte cada una. Las cajas son
 * identicas; lo unico que cambia es cuantas veces se recorren. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });
      var fases = ['Requisitos', 'Diseño', 'Construcción', 'Pruebas', 'Operación'];
      function fila(y, color) {
        for (var i = 0; i < 5; i++) {
          var x = 24 + i * 154;
          L.rectRed(ctx, x, y, 136, 52, 10); L.rellena(ctx, L.tono(color, 0.88), color, 2.5);
          UJ.rotulo(ctx, lz, fases[i], x + 68, y + 15, { tam: 17, peso: 800, color: L.tono(color, -0.3) });
          if (i < 4) L.flecha(ctx, x + 138, y + 26, x + 152, y + 26, color, 2.5, 1);
        }
      }

      // Una sola pasada
      UJ.rotulo(ctx, lz, '1 · Una sola pasada', 24, 62, { tam: 21, peso: 800, color: A, alinear: 'left' });
      fila(100, A);
      UJ.rotulo(ctx, lz, 'el cliente ve el sistema completo al final', W / 2, 166, { tam: 17, peso: 600, color: m.gris });

      // Tres vueltas
      UJ.rotulo(ctx, lz, '2 · Tres vueltas', 24, 222, { tam: 21, peso: 800, color: V, alinear: 'left' });
      fila(260, V);
      // la vuelta: de Operacion de regreso a Requisitos
      L.trazo(ctx, [[709, 314], [709, 344], [92, 344], [92, 318]], 1, V, 3);
      L.flecha(ctx, 92, 330, 92, 316, V, 3, 1);
      UJ.pildora(ctx, lz, W / 2, 330, 'otra vuelta', V, 1, { tam: 16, centrar: true, lleno: true });
      var vueltas = [['Vuelta 1', 'ficha del paciente'], ['Vuelta 2', 'historia clínica y búsqueda'], ['Vuelta 3', 'reportes y métricas']];
      for (var k = 0; k < 3; k++) {
        var x = 24 + k * 254;
        L.rectRed(ctx, x, 384, 236, 76, 12); L.rellena(ctx, L.tono(V, 0.92), V, 2);
        UJ.rotulo(ctx, lz, vueltas[k][0], x + 118, 394, { tam: 18, peso: 800, color: L.tono(V, -0.3) });
        UJ.rotulo(ctx, lz, vueltas[k][1], x + 118, 424, { tam: 17, peso: 600, ancho: 216 });
      }
      UJ.rotulo(ctx, lz, 'cada vuelta entrega una parte que la clínica revisa', W / 2, 474, { tam: 17, peso: 600, color: m.gris });

      L.rectRed(ctx, 24, 520, 752, 66, 14); L.rellena(ctx, L.tono(m.sello, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Las cajas son idénticas: cambia el recorrido', W / 2, 540, { tam: 22, peso: 800, ancho: 720 });
    }
  });
})();
