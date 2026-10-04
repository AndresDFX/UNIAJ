/* Ilustracion: que observar en la demo de la Clase 1. Uno: la FK rechaza la cita de una mascota
 * que no existe y no inserta nada. Dos: el mismo modelo en tres formas (boceto, DDL, erDiagram)
 * con los mismos nombres. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });
      // 1 · la FK en vivo
      UJ.rotulo(ctx, lz, '1 · La FK, en vivo', 30, 62, { tam: 21, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 100, W - 60, 'INSERT INTO cita (...) VALUES (1, ...);    -- mascota 1 existe', 1, 15);
      UJ.sello(ctx, lz, W - 50, 115, 16, true, 1);
      UJ.codigo(ctx, lz, 30, 146, W - 60, 'INSERT INTO cita (...) VALUES (999, ...);  -- no existe', 1, 15);
      UJ.sello(ctx, lz, W - 50, 161, 16, false, 1);
      UJ.rotulo(ctx, lz, 'ERROR: insert or update on table "cita" violates foreign key constraint', W / 2, 196,
                { tam: 16, peso: 700, color: R, ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'SELECT COUNT(*) FROM cita lo confirma: la cita con 999 no entró', W / 2, 226, { tam: 17, ancho: W - 60 });
      // 2 · un modelo, tres formas
      UJ.rotulo(ctx, lz, '2 · Un modelo, tres formas, los mismos nombres', 30, 280, { tam: 21, peso: 800, color: C, alinear: 'left' });
      var f = [['Boceto', 'mascota → dueno', C], ['DDL', 'id_dueno INT REFERENCES dueno', A], ['erDiagram', 'dueno ||--o{ mascota', V]];
      for (var i = 0; i < 3; i++) {
        var x = 30 + i * 252;
        L.rectRed(ctx, x, 322, 236, 120, 12); L.rellena(ctx, L.tono(f[i][2], 0.9), f[i][2], 2);
        UJ.rotulo(ctx, lz, f[i][0], x + 118, 334, { tam: 20, peso: 800, color: f[i][2] });
        L.texto(ctx, f[i][1], x + 118, 378, { tam: 15, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace', ancho: 220 });
        if (i < 2) UJ.rotulo(ctx, lz, '=', x + 244, 362, { tam: 26, peso: 800, color: L.tono(m.tinta, 0.3) });
      }
      L.rectRed(ctx, 30, 476, W - 60, 110, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Si un nombre cambia entre las tres,', W / 2, 492, { tam: 21, peso: 800, ancho: W - 100 });
      UJ.rotulo(ctx, lz, 'ya no son el mismo modelo', W / 2, 530, { tam: 21, peso: 800, ancho: W - 100 });
    }
  });
})();
