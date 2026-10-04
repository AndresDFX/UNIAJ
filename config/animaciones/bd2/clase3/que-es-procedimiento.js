/* Que es un procedimiento: GUARDADO en el catalogo del motor e INVOCADO con una sola linea que
 * dispara varias sentencias. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('que-es-procedimiento', {
    duracion: 4.8,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // Guardado
      UJ.rotulo(ctx, lz, 'GUARDADO', 200, 20, { tam: 30, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.14), function () {
        L.rectRed(ctx, 30, 70, 340, 250, 18); L.rellena(ctx, L.tono(A, 0.93), A, 3);
        UJ.rotulo(ctx, lz, 'Motor PostgreSQL', 200, 84, { tam: 22, peso: 700, color: A });
      });
      UJ.alfa(ctx, L.tramo(t, 0.08, 0.16), function () {
        UJ.tabla(ctx, lz, 50, 124, 300, 'catálogo (pg_proc)', ['sp_agendar_cita', 'sp_registrar_consulta'], L.mezcla(0, 2, L.tramo(t, 0.14, 0.3)), A, -1);
      });
      UJ.rotulo(ctx, lz, 'El fuente vive en el motor, no en el equipo de alguien.', 200, 340,
                { tam: 18, ancho: 340, visible: L.tramo(t, 0.28, 0.4) });
      // Invocado
      var X = W / 2 + 10;
      UJ.rotulo(ctx, lz, 'INVOCADO', X + 190, 20, { tam: 30, peso: 800, color: C, visible: L.tramo(t, 0.4, 0.46) });
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.44), function () {
        UJ.codigo(ctx, lz, X, 74, 380, 'CALL sp_agendar_cita(…);', L.tramo(t, 0.42, 0.55), 18);
      });
      var ss = ['SELECT · ¿mascota activa?', 'IF … RAISE EXCEPTION', 'INSERT INTO cita …'];
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, 0.55 + i * 0.06, 0.62 + i * 0.06, 'frena');
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, X + 10, 150 + i * 60, 360, 48, 10); L.rellena(ctx, L.tono(C, 0.9), C, 2);
          UJ.rotulo(ctx, lz, ss[i], X + 190, 162 + i * 60, { tam: 18, peso: 600 });
        });
      }
      L.flecha(ctx, X - 2, 100, X - 2, 330, C, 3, L.tramo(t, 0.55, 0.72));
      UJ.rotulo(ctx, lz, 'Una línea dispara varias sentencias.', X + 190, 340, { tam: 18, ancho: 360, visible: L.tramo(t, 0.7, 0.75) });
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.92), function () {
        L.rectRed(ctx, 40, 450, W - 80, 110, 16); L.rellena(ctx, L.tono(m.sello || C, 0.6), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'La regla de negocio queda escrita UNA vez', W / 2, 470, { tam: 24, peso: 800, ancho: W - 120 });
        UJ.rotulo(ctx, lz, 'y todos los que llaman pasan por ella.', W / 2, 512, { tam: 20, ancho: W - 120 });
      });
    }
  });
})();
