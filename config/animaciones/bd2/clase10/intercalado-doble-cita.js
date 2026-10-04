/* Todo o nada no basta: el motor intercala las operaciones de dos transacciones. Las dos
 * consultan la franja de las 10:00, las dos la ven libre, las dos insertan: dos citas al mismo
 * minuto con el mismo veterinario, y ninguna sentencia fallo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('intercalado-doble-cita', {
    duracion: 5,
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'T1', 130, 20, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      UJ.rotulo(ctx, lz, 'T2', 670, 20, { tam: 26, peso: 800, color: C, visible: L.tramo(t, 0, 0.06) });
      L.trazo(ctx, [[400, 20], [400, 330]], L.tramo(t, 0.02, 0.12), L.tono(m.tinta, 0.7), 3);
      UJ.rotulo(ctx, lz, 'tiempo ↓', 400, 336, { tam: 16, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.1, 0.14) });
      var ops = [
        [0, '¿10:00 con el vet. libre?', 'sí, 0 filas', 0.1],
        [1, '¿10:00 con el vet. libre?', 'sí, 0 filas', 0.2],
        [0, 'INSERT cita 10:00', 'COMMIT', 0.42],
        [1, 'INSERT cita 10:00', 'COMMIT', 0.52]
      ];
      for (var i = 0; i < ops.length; i++) {
        var o = ops[i], x = o[0] === 0 ? 30 : 420, c = o[0] === 0 ? A : C, y = 70 + i * 64;
        UJ.alfa(ctx, L.tramo(t, o[3], o[3] + 0.08), function () {
          L.rectRed(ctx, x, y, 350, 52, 10); L.rellena(ctx, L.tono(c, 0.9), c, 2);
          L.texto(ctx, o[1], x + 12, y + 6, { tam: 17, peso: 700, color: m.tinta, letra: lz.letra, ancho: 330 });
          L.texto(ctx, o[2], x + 12, y + 28, { tam: 15, peso: 600, color: c, letra: lz.letra });
          L.circulo(ctx, 400, y + 26, 7); L.rellena(ctx, c);
        });
      }
      // La agenda resultante
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.82), function () {
        UJ.tabla(ctx, lz, 140, 380, 520, 'cita', ['10:00 · vet. Ruiz · mascota 7', '10:00 · vet. Ruiz · mascota 12'], 2, R);
      });
      UJ.sello(ctx, lz, 690, 460, 26, false, L.tramo(t, 0.8, 0.86));
      UJ.rotulo(ctx, lz, 'Ninguna falló. Cumplió dos órdenes contradictorias.', W / 2, 530, { tam: 21, peso: 800, color: R, ancho: W - 40, visible: L.tramo(t, 0.86, 0.94) });
      UJ.rotulo(ctx, lz, 'Nadie le dijo que no debía.', W / 2, 570, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
