/* Como se elige el recorrido: dos tarjetas de criterio y dos partes de la clinica que caen
 * en la suya segun lo estables que sean sus requisitos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('elegir-recorrido', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.32, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, '¿Lineal o en ciclos?', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      UJ.tarjeta(ctx, lz, 40, 80, 340, 'Lineal', ['requisitos estables', 'contrato cerrado', 'sistema crítico'], A, L.tramo(t, 0.04, 0.12), L.tramo(t, 0.08, 0.2) * 3);
      UJ.tarjeta(ctx, lz, 420, 80, 340, 'En ciclos', ['dominio nuevo', 'el cliente descubre al ver', 'margen para ajustar'], V, L.tramo(t, 0.14, 0.22), L.tramo(t, 0.18, 0.3) * 3);

      function ficha(texto, xFin, color, a0) {
        var ap = L.tramo(t, a0, a0 + 0.05), mv = L.tramo(t, a0 + 0.08, a0 + 0.2, 'suave');
        if (ap <= 0) return;
        var x = 400 + (xFin - 400) * mv, y = 400 + (300 - 400) * mv;
        UJ.pildora(ctx, lz, x, y, texto, color, ap, { tam: 18, centrar: true });
        UJ.flecha(ctx, lz, xFin, 294, xFin, 236, color, L.tramo(t, a0 + 0.18, a0 + 0.24));
        UJ.sello(ctx, lz, xFin, 380, 20, true, L.tramo(t, a0 + 0.2, a0 + 0.26));
      }
      ficha('Datos del paciente (estables)', 210, A, 0.34);
      ficha('Tablero de métricas (incierto)', 590, V, 0.66);
      UJ.rotulo(ctx, lz, 'Se elige por la estabilidad de los requisitos, no por costumbre.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
