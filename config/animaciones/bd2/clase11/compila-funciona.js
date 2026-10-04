/* Verificaciones tres y cuatro. Tres: que compile no es que sirva; se ejecuta el caso valido
 * (inserta la cita) y el caso invalido declarado (la mascota 3 esta inactiva: el procedimiento
 * responde con su mensaje de negocio). Cuatro: la optimizacion se demuestra con el plan antes y
 * despues; sin medicion, el informe es una opinion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('compila-funciona', {
    duracion: 5,
    // Pasos LOGICOS: 1) compila, y no se sabe si sirve; 2) el caso valido; 3) el caso invalido
    // y la conclusion; 4) verificacion cuatro: la optimizacion medida.
    pasos: [0.22, 0.46, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A, R = m.malva || '#A02030';
      UJ.codigo(ctx, lz, 20, 18, 580, 'CREATE PROCEDURE sp_agendar_cita(…)', L.tramo(t, 0, 0.1), 17);
      UJ.rotulo(ctx, lz, 'compila', 690, 24, { tam: 20, peso: 700, color: m.tinta, visible: L.tramo(t, 0.1, 0.15) });
      UJ.rotulo(ctx, lz, '…y todavía no se sabe si sirve', W / 2, 70, { tam: 20, peso: 600, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.14, 0.2) });
      // 2 · Caso valido
      UJ.rotulo(ctx, lz, '1 · caso válido', 20, 116, { tam: 21, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0.24, 0.27) });
      UJ.codigo(ctx, lz, 20, 150, 460, 'CALL sp_agendar_cita(1, 2, …);', L.tramo(t, 0.26, 0.33), 16);
      L.flecha(ctx, 486, 166, 524, 166, A, 4, L.tramo(t, 0.33, 0.37, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.41), function () {
        L.rectRed(ctx, 530, 142, 250, 48, 10); L.rellena(ctx, L.tono(V, 0.85), V, 2);
        UJ.rotulo(ctx, lz, 'cita insertada', 655, 154, { tam: 19, peso: 700 });
      });
      UJ.sello(ctx, lz, 772, 136, 16, true, L.tramo(t, 0.4, 0.45));
      // 3 · Caso invalido declarado
      UJ.rotulo(ctx, lz, '2 · caso inválido declarado', 20, 216, { tam: 21, peso: 800, alinear: 'left', color: C, visible: L.tramo(t, 0.48, 0.51) });
      UJ.codigo(ctx, lz, 20, 250, 460, 'CALL sp_agendar_cita(3, 2, …);  -- inactiva', L.tramo(t, 0.5, 0.57), 16);
      L.flecha(ctx, 486, 266, 524, 266, C, 4, L.tramo(t, 0.57, 0.6, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.59, 0.64), function () {
        L.rectRed(ctx, 530, 236, 250, 64, 10); L.rellena(ctx, L.tono(C, 0.85), C, 2);
        UJ.rotulo(ctx, lz, 'la mascota 3 esta inactiva; no se agenda cita', 655, 244, { tam: 15, peso: 700, ancho: 236 });
      });
      UJ.sello(ctx, lz, 772, 230, 16, true, L.tramo(t, 0.63, 0.67));
      UJ.rotulo(ctx, lz, 'Compila ≠ funciona: se muestran las dos ejecuciones.', W / 2, 322,
                { tam: 21, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.66, 0.71) });
      // 4 · Verificacion cuatro: la optimizacion, medida
      UJ.rotulo(ctx, lz, 'Verificación cuatro: la optimización, medida', 20, 384, { tam: 21, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0.74, 0.78) });
      UJ.codigo(ctx, lz, 20, 422, 760, 'antes:    Seq Scan on cita', L.tramo(t, 0.78, 0.84), 16);
      UJ.codigo(ctx, lz, 20, 462, 760, 'después:  Index Scan using idx_cita_fecha_hora on cita', L.tramo(t, 0.84, 0.9), 16);
      UJ.rotulo(ctx, lz, 'Sin el plan antes y después, el informe es una opinión.', W / 2, 520,
                { tam: 20, peso: 800, color: R, ancho: W - 40, visible: L.tramo(t, 0.9, 0.95) });
      UJ.rotulo(ctx, lz, 'Y un índice que ninguna consulta usa también es un hallazgo.', W / 2, 560,
                { tam: 17, ancho: W - 40, visible: L.tramo(t, 0.94, 0.99) });
    }
  });
})();
