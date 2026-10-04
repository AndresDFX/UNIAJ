/* En PostgreSQL usuario y rol son lo mismo: CREATE USER es CREATE ROLE con LOGIN. El rol sin
 * LOGIN es un paquete de permisos; la persona con LOGIN lo recibe. Nombre veterinario_rol: por
 * legibilidad, no porque el motor lo exija. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('login-nologin', {
    duracion: 5,
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.codigo(ctx, lz, 40, 30, 340, 'CREATE USER ana_gomez;', L.tramo(t, 0, 0.08), 18);
      UJ.rotulo(ctx, lz, '=', W / 2, 34, { tam: 30, peso: 800, visible: L.tramo(t, 0.1, 0.14) });
      UJ.codigo(ctx, lz, 420, 30, 340, 'CREATE ROLE ana_gomez LOGIN;', L.tramo(t, 0.14, 0.24), 18);
      UJ.rotulo(ctx, lz, 'CREATE USER es un alias: el mismo objeto', W / 2, 90, { tam: 18, visible: L.tramo(t, 0.2, 0.28) });
      // Dos roles
      UJ.alfa(ctx, L.tramo(t, 0.32, 0.42), function () {
        L.rectRed(ctx, 40, 150, 330, 190, 16); L.rellena(ctx, L.tono(C, 0.88), C, 3);
        UJ.rotulo(ctx, lz, 'recepcion', 205, 164, { tam: 24, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'NOLOGIN', 205, 202, { tam: 20, peso: 700 });
        UJ.rotulo(ctx, lz, 'paquete de permisos: nadie se conecta con él', 205, 240, { tam: 17, ancho: 290 });
        L.rectRed(ctx, 430, 150, 330, 190, 16); L.rellena(ctx, L.tono(A, 0.9), A, 3);
        UJ.rotulo(ctx, lz, 'ana_gomez', 595, 164, { tam: 24, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'LOGIN', 595, 202, { tam: 20, peso: 700 });
        UJ.rotulo(ctx, lz, 'puede iniciar sesión: lo llamamos usuario', 595, 240, { tam: 17, ancho: 290 });
      });
      L.flecha(ctx, 374, 300, 426, 300, C, 4, L.tramo(t, 0.5, 0.58));
      UJ.codigo(ctx, lz, 160, 366, 480, 'GRANT recepcion TO ana_gomez;', L.tramo(t, 0.54, 0.66), 18);
      // Convencion de nombre
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.86), function () {
        L.rectRed(ctx, 40, 440, W - 80, 150, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'veterinario_rol, no veterinario', W / 2, 452, { tam: 22, peso: 800 });
        L.texto(ctx, 'GRANT SELECT ON cita TO veterinario_rol;', W / 2, 496, { tam: 17, color: A, alinear: 'center', letra: 'Consolas, monospace', peso: 700 });
        UJ.rotulo(ctx, lz, 'Convención de legibilidad: el motor no lo exige (roles y tablas no chocan)', W / 2, 532, { tam: 16, ancho: W - 140 });
      });
    }
  });
})();
