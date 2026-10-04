/* Probar que un privilegio falta: SET ROLE cambia con que permisos se evalua lo que se escribe;
 * las lineas que deben fallar se ejecutan una por una; RESET ROLE devuelve al propietario. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('set-role-prueba', {
    duracion: 5,
    // Pasos LOGICOS: 1) SET ROLE y lo que si tiene, 2) lo que no tiene falla, 3) RESET ROLE y la
    // regla de ejecutar una por una.
    pasos: [0.33, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.codigo(ctx, lz, 30, 30, W - 60, 'SET ROLE recepcion;', L.tramo(t, 0, 0.08), 19);
      UJ.rotulo(ctx, lz, '→ los permisos ahora son los de recepcion', 50, 80, { tam: 18, alinear: 'left', color: L.tono(C, -0.3), visible: L.tramo(t, 0.08, 0.16) });
      UJ.codigo(ctx, lz, 30, 130, W - 140, 'SELECT * FROM cita;', L.tramo(t, 0.18, 0.26), 19);
      UJ.sello(ctx, lz, W - 70, 150, 22, true, L.tramo(t, 0.26, 0.32));
      UJ.codigo(ctx, lz, 30, 210, W - 140, 'SELECT * FROM consulta;', L.tramo(t, 0.34, 0.42), 19);
      UJ.sello(ctx, lz, W - 70, 230, 22, false, L.tramo(t, 0.44, 0.5));
      UJ.rotulo(ctx, lz, 'ERROR: permission denied for table consulta', 50, 266, { tam: 18, peso: 700, alinear: 'left', color: R, visible: L.tramo(t, 0.48, 0.56) });
      UJ.codigo(ctx, lz, 30, 310, W - 140, 'DELETE FROM cita WHERE id_cita = 1;', L.tramo(t, 0.56, 0.64), 19);
      UJ.sello(ctx, lz, W - 70, 330, 22, false, L.tramo(t, 0.64, 0.7));
      UJ.codigo(ctx, lz, 30, 400, W - 60, 'RESET ROLE;', L.tramo(t, 0.74, 0.8), 19);
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.92), function () {
        L.rectRed(ctx, 30, 470, W - 60, 130, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Las líneas que deben fallar, una por una', W / 2, 484, { tam: 21, peso: 800, ancho: W - 100 });
        UJ.rotulo(ctx, lz, 'un ejecutor que aborta al primer error se lleva las siguientes', W / 2, 526, { tam: 17, ancho: W - 120 });
      });
    }
  });
})();
