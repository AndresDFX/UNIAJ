/* Include y extend: el comportamiento comun que siempre se ejecuta se incluye; el opcional
 * extiende, y su flecha va del extensor al caso base. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('include-extend', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.45, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, '«include»: siempre', W / 2, 20, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });

      UJ.elipse(ctx, lz, 170, 110, 140, 44, 'CU-03 Registrar consulta', A, L.tramo(t, 0.02, 0.08));
      UJ.elipse(ctx, lz, 170, 250, 140, 44, 'CU-04 Agendar cita', A, L.tramo(t, 0.05, 0.11));
      UJ.elipse(ctx, lz, 620, 180, 150, 50, 'Verificar existencia de la mascota', C, L.tramo(t, 0.1, 0.16));
      UJ.flecha(ctx, lz, 300, 125, 476, 168, A, L.tramo(t, 0.16, 0.28), '«include»', { punteada: true, dy: -30 });
      UJ.flecha(ctx, lz, 300, 235, 476, 196, A, L.tramo(t, 0.2, 0.32), '«include»', { punteada: true, dy: 10 });
      UJ.rotulo(ctx, lz, 'se ejecuta siempre', 620, 240, { tam: 18, peso: 700, color: C, visible: L.tramo(t, 0.32, 0.4) });

      // Extend
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.5), function () {
        UJ.linea(ctx, 30, 320, W - 30, 320, L.tono(m.gris, 0.5), 2, 1, true);
        UJ.rotulo(ctx, lz, '«extend»: a veces', W / 2, 334, { tam: 24, peso: 800, color: m.malva });
      });
      UJ.elipse(ctx, lz, 170, 440, 140, 44, 'CU-06 Exportar expediente a PDF', m.malva, L.tramo(t, 0.5, 0.56));
      UJ.elipse(ctx, lz, 630, 440, 140, 44, 'CU-02 Buscar expediente', A, L.tramo(t, 0.53, 0.59));
      UJ.flecha(ctx, lz, 310, 440, 488, 440, m.malva, L.tramo(t, 0.6, 0.72), '«extend»', { punteada: true, dy: -30 });
      UJ.rotulo(ctx, lz, 'solo si el veterinario lo pide', 400, 494, { tam: 18, peso: 700, color: m.malva, visible: L.tramo(t, 0.72, 0.8) });

      UJ.rotulo(ctx, lz, 'La flecha de extend va del extensor al caso base', W / 2, 560,
        { tam: 22, peso: 700, color: m.tinta, ancho: W - 40, visible: L.tramo(t, 0.86, 0.98) });
    }
  });
})();
