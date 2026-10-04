/* Verificacion tres: que compile no es que sirva. Se ejecuta el caso valido (inserta y confirma)
 * y el caso invalido declarado (devuelve el mensaje de negocio, no un error crudo del motor). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('compila-funciona', {
    duracion: 5,
    pasos: [0.26, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A;
      UJ.alfa(ctx, L.tramo(t, 0, 0 + 0.02), function () { UJ.codigo(ctx, lz, 30, 24, 600, 'CREATE PROCEDURE sp_agendar_cita(…)', L.tramo(t, 0, 0.14), 18); });
      UJ.rotulo(ctx, lz, 'compila', 700, 32, { tam: 20, peso: 700, color: m.tinta, visible: L.tramo(t, 0.14, 0.2) });
      UJ.rotulo(ctx, lz, '…y todavía no se sabe si sirve', W / 2, 92, { tam: 20, peso: 600, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.18, 0.26) });
      // 1. caso valido
      UJ.rotulo(ctx, lz, '1 · caso válido', 30, 150, { tam: 22, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0.28, 0.32) });
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.32), function () { UJ.codigo(ctx, lz, 30, 188, 470, 'CALL sp_agendar_cita(3, 1, …);', L.tramo(t, 0.3, 0.42), 17); });
      L.flecha(ctx, 506, 205, 560, 205, A, 4, L.tramo(t, 0.42, 0.48, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.54), function () {
        L.rectRed(ctx, 566, 178, 210, 56, 10); L.rellena(ctx, L.tono(V, 0.85), V, 2);
        UJ.rotulo(ctx, lz, 'cita insertada', 671, 194, { tam: 19, peso: 700 });
      });
      UJ.sello(ctx, lz, 740, 150, 20, true, L.tramo(t, 0.52, 0.58));
      // 2. caso invalido declarado
      UJ.rotulo(ctx, lz, '2 · caso inválido declarado', 30, 290, { tam: 22, peso: 800, alinear: 'left', color: C, visible: L.tramo(t, 0.62, 0.66) });
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.64 + 0.02), function () { UJ.codigo(ctx, lz, 30, 328, 470, 'CALL … mascota inactiva / franja tomada', L.tramo(t, 0.64, 0.76), 17); });
      L.flecha(ctx, 506, 345, 560, 345, C, 4, L.tramo(t, 0.76, 0.8, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.86), function () {
        L.rectRed(ctx, 566, 310, 210, 74, 10); L.rellena(ctx, L.tono(C, 0.85), C, 2);
        UJ.rotulo(ctx, lz, 'mensaje de negocio, no error crudo', 671, 320, { tam: 18, peso: 700, ancho: 196 });
      });
      UJ.sello(ctx, lz, 740, 290, 20, true, L.tramo(t, 0.84, 0.9));
      UJ.rotulo(ctx, lz, 'Compila ≠ funciona: se muestran las dos ejecuciones.', W / 2, 470,
                { tam: 23, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
