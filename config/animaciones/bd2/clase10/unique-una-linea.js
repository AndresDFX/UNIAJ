/* Antes de los niveles: una restriccion UNIQUE (id_veterinario, fecha_hora) resuelve la doble
 * cita. Las dos recepcionistas insertan; el motor deja pasar la primera y rechaza la segunda con
 * violacion de unicidad, y el procedimiento la traduce a un mensaje de negocio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('unique-una-linea', {
    duracion: 5,
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'ALTER TABLE cita ADD CONSTRAINT uq_vet_fecha', L.tramo(t, 0, 0.1), 18);
      UJ.codigo(ctx, lz, 20, 62, W - 40, '  UNIQUE (id_veterinario, fecha_hora);', L.tramo(t, 0.08, 0.18), 18);
      UJ.rotulo(ctx, lz, 'una línea, declarativa', W / 2, 120, { tam: 20, peso: 800, color: A, visible: L.tramo(t, 0.18, 0.26) });
      // Dos inserciones
      UJ.caja(ctx, lz, 30, 170, 330, 90, 'Recepción 1', 'INSERT cita · vet. Ruiz 10:00', A, L.tramo(t, 0.32, 0.38));
      UJ.caja(ctx, lz, 440, 170, 330, 90, 'Recepción 2', 'INSERT cita · vet. Ruiz 10:00', C, L.tramo(t, 0.36, 0.42));
      L.flecha(ctx, 195, 262, 300, 330, A, 3, L.tramo(t, 0.42, 0.5));
      L.flecha(ctx, 605, 262, 500, 330, C, 3, L.tramo(t, 0.5, 0.58));
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.5), function () {
        UJ.tabla(ctx, lz, 200, 336, 400, 'cita', ['vet. Ruiz · 10:00 · mascota 7'], 1, A);
      });
      UJ.sello(ctx, lz, 160, 360, 24, true, L.tramo(t, 0.48, 0.54));
      UJ.sello(ctx, lz, 640, 360, 24, false, L.tramo(t, 0.58, 0.64));
      UJ.rotulo(ctx, lz, 'violación de unicidad', 680, 392, { tam: 17, peso: 800, color: R, visible: L.tramo(t, 0.62, 0.68) });
      // Traduccion
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.82), function () {
        L.rectRed(ctx, 30, 450, 740, 150, 16); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'El procedimiento captura la excepción y responde:', 400, 466, { tam: 19, ancho: 700 });
        UJ.rotulo(ctx, lz, '«Ese horario acaba de ser tomado, elija otro.»', 400, 504, { tam: 22, peso: 800, color: V, ancho: 700 });
        UJ.rotulo(ctx, lz, 'Nadie tuvo que razonar sobre niveles de aislamiento.', 400, 556, { tam: 18, ancho: 700 });
      });
    }
  });
})();
