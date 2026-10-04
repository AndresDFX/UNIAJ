/* La clave foranea: el motor se niega a guardar una referencia inventada (mascota 999) y, sin
 * clausula ON DELETE, el borrado del padre referenciado es restrictivo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('fk-restrictiva', {
    duracion: 5,
    pasos: [0.22, 0.56, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var n = L.tramo(t, 0, 0.12) * 3;
      UJ.tabla(ctx, lz, 30, 30, 300, 'mascota', ['id_mascota = 1', 'id_mascota = 2'], n, A);
      UJ.tabla(ctx, lz, 470, 30, 300, 'cita', ['id_mascota → 1', 'id_mascota → 2'], n, C);
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.2), function () {
        L.flecha(ctx, 466, 96, 334, 96, L.tono(m.tinta, 0.3), 3);
        L.flecha(ctx, 466, 136, 334, 136, L.tono(m.tinta, 0.3), 3);
        UJ.rotulo(ctx, lz, 'FK', 400, 62, { tam: 18, peso: 800, color: C });
      });
      // Referencia inventada
      UJ.codigo(ctx, lz, 30, 210, W - 60, "INSERT INTO cita (id_mascota, ...) VALUES (999, ...);", L.tramo(t, 0.24, 0.34), 18);
      var x = L.claves(t, [[0.34, 620], [0.42, 350, 'frena']]);
      if (t >= 0.34) {
        L.rectRed(ctx, x, 270, 120, 40, 8); L.rellena(ctx, L.tono(R, 0.8), R, 2);
        UJ.rotulo(ctx, lz, '999', x + 60, 278, { tam: 18, peso: 800, color: R });
      }
      UJ.sello(ctx, lz, 300, 290, 22, false, L.tramo(t, 0.42, 0.48));
      UJ.rotulo(ctx, lz, 'ERROR: … violates foreign key constraint "cita_id_mascota_fkey"', W / 2, 330,
                { tam: 18, peso: 700, color: R, ancho: W - 60, visible: L.tramo(t, 0.44, 0.54) });
      // Borrado del padre
      UJ.codigo(ctx, lz, 30, 390, W - 60, 'DELETE FROM mascota WHERE id_mascota = 1;', L.tramo(t, 0.6, 0.7), 18);
      UJ.sello(ctx, lz, 60, 470, 22, false, L.tramo(t, 0.72, 0.78));
      UJ.rotulo(ctx, lz, 'Rechazado: hay citas que la referencian', 96, 456, { tam: 20, peso: 700, alinear: 'left', color: R, visible: L.tramo(t, 0.74, 0.82) });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.96), function () {
        L.rectRed(ctx, 60, 520, W - 120, 84, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Sin ON DELETE, el estándar es restrictivo', W / 2, 532, { tam: 21, peso: 800 });
        UJ.rotulo(ctx, lz, 'regla del estándar SQL, no convención', W / 2, 568, { tam: 17 });
      });
    }
  });
})();
