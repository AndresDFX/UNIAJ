/* El trigger: dos objetos (la funcion RETURNS TRIGGER y la asociacion CREATE TRIGGER) y
 * nadie lo llama. Llega un UPDATE a `cita`, el evento lo dispara y aparece la fila en audit_cita. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('trigger-dos-objetos', {
    duracion: 4.8,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.56, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // Los dos objetos
      UJ.caja(ctx, lz, 24, 20, 360, 96, '1 · la función', 'fn_trg_audit_cita() RETURNS TRIGGER', A, L.tramo(t, 0.0, 0.12));
      UJ.caja(ctx, lz, 416, 20, 360, 96, '2 · la asociación', 'CREATE TRIGGER … AFTER UPDATE OF estado ON cita', C, L.tramo(t, 0.1, 0.22));
      L.flecha(ctx, 416, 68, 388, 68, C, 4, L.tramo(t, 0.22, 0.3));
      // El UPDATE llega
      UJ.codigo(ctx, lz, 24, 160, 470, "UPDATE cita SET estado = 'atendida' WHERE id_cita = 7;", L.tramo(t, 0.3, 0.46), 15);
      L.flecha(ctx, 260, 204, 260, 262, m.tinta, 4, L.tramo(t, 0.46, 0.52, 'frena'));
      UJ.tabla(ctx, lz, 60, 266, 400, 'cita', ["7 · estado: 'confirmada'"], 1, A, -1);
      var cambio = L.tramo(t, 0.52, 0.56);
      if (cambio > 0) UJ.alfa(ctx, cambio, function () {
        L.rectRed(ctx, 62, 314, 396, 38, 0); L.rellena(ctx, L.tono(m.sello || C, 0.5));
        UJ.rotulo(ctx, lz, "7 · estado: 'atendida'", 76, 323, { tam: 19, alinear: 'left' });
      });
      // El evento dispara
      UJ.rayo(ctx, 520, 250, 90, m.sello || C, L.tramo(t, 0.56, 0.62) * (1 - 0.5 * L.tramo(t, 0.7, 0.8)));
      UJ.rotulo(ctx, lz, 'evento', 560, 345, { tam: 18, color: m.tinta, visible: L.tramo(t, 0.58, 0.64) });
      L.flecha(ctx, 600, 300, 700, 300, C, 4, L.tramo(t, 0.62, 0.7, 'frena'));
      L.trazo(ctx, [[720, 290], [720, 140], [600, 120]], L.tramo(t, 0.62, 0.72), L.tono(A, 0.3), 3);
      // La fila de auditoria
      UJ.tabla(ctx, lz, 380, 410, 396, 'audit_cita', ["7 · confirmada → atendida · now()"], L.tramo(t, 0.74, 0.84), A, -1);
      UJ.rotulo(ctx, lz, 'Nadie lo llama: lo dispara el evento.', W / 2, 560,
                { tam: 24, ancho: W - 40, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
