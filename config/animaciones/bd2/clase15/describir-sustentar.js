/* Sustentar no es describir: describir es decir que hay; sustentar es por que quedo asi y que se
 * descarto. Importa mas en bases de datos por el costo de revertir un esquema con datos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('describir-sustentar', {
    duracion: 5,
    pasos: [0.32, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.rotulo(ctx, lz, 'Describir: qué hay', 200, 16, { tam: 24, peso: 800, color: L.tono(m.tinta, 0.2) });
      var tablas = ['Dueño', 'Mascota', 'Cita', 'Veterinario', 'Insumo', 'Factura'];
      for (var i = 0; i < 6; i++) UJ.alfa(ctx, L.tramo(t, 0.02 + i * 0.04, 0.08 + i * 0.04), function () {
        L.rectRed(ctx, 60, 64 + i * 50, 280, 40, 8); L.rellena(ctx, L.tono(m.tinta, 0.88), L.tono(m.tinta, 0.5), 1);
        UJ.rotulo(ctx, lz, 'tenemos ' + tablas[i], 200, 73 + i * 50, { tam: 18 });
      });
      UJ.rotulo(ctx, lz, 'Sustentar: por qué', 600, 16, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0.34, 0.4) });
      UJ.caja(ctx, lz, 430, 64, 340, 120, '¿Por qué quedó así?', 'la razón de la decisión', A, L.tramo(t, 0.38, 0.48));
      UJ.caja(ctx, lz, 430, 214, 340, 120, '¿Qué se descartó?', 'la alternativa y por qué no', C, L.tramo(t, 0.48, 0.58));
      // Costo de revertir
      UJ.rotulo(ctx, lz, 'Costo de revertir', 30, 386, { tam: 21, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0.7, 0.74) });
      var a = L.tramo(t, 0.72, 0.8, 'suave'), b = L.tramo(t, 0.78, 0.9, 'suave');
      UJ.rotulo(ctx, lz, 'cambiar código', 30, 430, { tam: 18, peso: 700, alinear: 'left', visible: L.tramo(t, 0.72, 0.76) });
      if (a > 0) { L.rectRed(ctx, 250, 428, 90 * a, 30, 6); L.rellena(ctx, V); }
      UJ.rotulo(ctx, lz, 'cambiar esquema con datos', 30, 476, { tam: 18, peso: 700, alinear: 'left', ancho: 220, visible: L.tramo(t, 0.78, 0.82) });
      if (b > 0) { L.rectRed(ctx, 250, 474, 500 * b, 30, 6); L.rellena(ctx, R); }
      UJ.rotulo(ctx, lz, 'Nombrar tablas no defiende nada.', W / 2, 560, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
