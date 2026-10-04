/* Antes de los niveles: un indice unico PARCIAL sobre (id_veterinario, fecha_hora) resuelve la
 * doble cita. Las dos recepciones insertan la misma franja; el motor deja pasar la primera y
 * rechaza la segunda con violacion de unicidad (23505), y el procedimiento la traduce a un
 * mensaje de negocio. Es parcial porque una cita CANCELADA libera su franja: esa si entra. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('unique-una-linea', {
    duracion: 5,
    // Pasos LOGICOS: 1) la regla; 2) dos INSERT, uno pasa y el otro choca; 3) el procedimiento
    // traduce el error; 4) por que es parcial: la cancelada entra.
    pasos: [0.2, 0.5, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      // 1 · La regla
      UJ.codigo(ctx, lz, 20, 10, W - 40, 'CREATE UNIQUE INDEX uq_cita_vet_franja ON cita', L.tramo(t, 0, 0.06), 17);
      UJ.codigo(ctx, lz, 20, 48, W - 40, '  (id_veterinario, fecha_hora)', L.tramo(t, 0.05, 0.1), 17);
      UJ.codigo(ctx, lz, 20, 86, W - 40, "  WHERE estado <> 'CANCELADA';", L.tramo(t, 0.09, 0.14), 17);
      UJ.rotulo(ctx, lz, 'una regla declarativa: el motor la revisa en cada escritura', W / 2, 128, { tam: 18, peso: 800, color: A, ancho: W - 40, visible: L.tramo(t, 0.13, 0.19) });
      // 2 · Dos inserciones de la misma franja
      UJ.caja(ctx, lz, 20, 164, 350, 74, 'Recepción 1: INSERT', 'vet. 1 · 2026-09-01 08:00', A, L.tramo(t, 0.22, 0.27));
      UJ.caja(ctx, lz, 430, 164, 350, 74, 'Recepción 2: INSERT', 'vet. 1 · 2026-09-01 08:00', C, L.tramo(t, 0.25, 0.3));
      L.flecha(ctx, 195, 240, 300, 282, A, 3, L.tramo(t, 0.3, 0.35));
      UJ.alfa(ctx, L.tramo(t, 0.33, 0.38), function () {
        UJ.tabla(ctx, lz, 200, 286, 400, 'cita', ['vet. 1 · 2026-09-01 08:00 · vigente'], 1, A);
      });
      UJ.sello(ctx, lz, 168, 310, 22, true, L.tramo(t, 0.37, 0.42));
      L.flecha(ctx, 605, 240, 500, 282, C, 3, L.tramo(t, 0.4, 0.44));
      UJ.sello(ctx, lz, 632, 310, 22, false, L.tramo(t, 0.43, 0.47));
      UJ.rotulo(ctx, lz, 'violación de unicidad (23505)', 700, 338, { tam: 15, peso: 800, color: R, ancho: 190, visible: L.tramo(t, 0.45, 0.49) });
      // 3 · La traduccion a negocio
      UJ.alfa(ctx, L.tramo(t, 0.53, 0.62), function () {
        L.rectRed(ctx, 20, 384, 760, 100, 16); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'El procedimiento captura la excepción y responde:', 400, 392, { tam: 18, ancho: 720 });
        UJ.rotulo(ctx, lz, '«Ese horario acaba de ser tomado, elija otro.»', 400, 422, { tam: 21, peso: 800, color: V, ancho: 720 });
        UJ.rotulo(ctx, lz, 'Nadie tuvo que razonar sobre niveles de aislamiento.', 400, 456, { tam: 16, ancho: 720 });
      });
      // 4 · Por que es parcial
      UJ.rotulo(ctx, lz, 'Es parcial: una cita CANCELADA no ocupa la franja', 20, 500, { tam: 19, peso: 800, color: A, alinear: 'left', ancho: 760, visible: L.tramo(t, 0.75, 0.8) });
      UJ.codigo(ctx, lz, 20, 536, 700, "INSERT … vet. 1 · 2026-09-01 08:00 · 'CANCELADA'   -> entra", L.tramo(t, 0.8, 0.88), 16);
      UJ.sello(ctx, lz, 752, 552, 18, true, L.tramo(t, 0.87, 0.92));
      UJ.rotulo(ctx, lz, 'un UNIQUE de tabla no admite WHERE: también contaría las canceladas', W / 2, 584, { tam: 15, peso: 700, color: L.tono(m.tinta, 0.2), ancho: W - 40, visible: L.tramo(t, 0.92, 0.99) });
    }
  });
})();
