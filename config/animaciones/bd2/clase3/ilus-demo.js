/* Ilustracion: que observar en la demo de la Clase 3. El CALL valido inserta (COUNT 10 -> 11), los
 * invalidos abortan con su mensaje literal y no dejan nada, y el procedimiento queda guardado en el
 * motor (pg_get_functiondef lo devuelve aunque se cierre la pestana). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });
      var c = [
        ["CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00');", 'cita creada', true],
        ["CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-21 08:00');", 'ERROR: la mascota 3 esta inactiva', false],
        ["CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-22 08:00');", 'ERROR: la mascota 99 no existe', false]
      ];
      UJ.rotulo(ctx, lz, '1 · El válido escribe; los inválidos abortan con su mensaje', 24, 60, { tam: 19, peso: 800, color: A, alinear: 'left', ancho: W - 40 });
      for (var i = 0; i < 3; i++) {
        var y = 96 + i * 76;
        UJ.codigo(ctx, lz, 24, y, W - 96, c[i][0], 1, 14);
        UJ.sello(ctx, lz, W - 44, y + 14, 15, c[i][2], 1);
        UJ.rotulo(ctx, lz, c[i][1], 40, y + 36, { tam: 15, peso: 700, color: c[i][2] ? V : R, alinear: 'left' });
      }
      // conteo
      UJ.rotulo(ctx, lz, '2 · El conteo lo prueba', 24, 330, { tam: 19, peso: 800, color: C, alinear: 'left' });
      L.rectRed(ctx, 24, 364, 360, 110, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
      UJ.rotulo(ctx, lz, 'SELECT COUNT(*) FROM cita;', 204, 374, { tam: 15, peso: 700 });
      UJ.rotulo(ctx, lz, '10  →  11', 204, 408, { tam: 34, peso: 800, color: L.tono(C, -0.3) });
      UJ.rotulo(ctx, lz, 'los que fallan no dejan filas', 204, 450, { tam: 15 });
      // guardado
      UJ.rotulo(ctx, lz, '3 · Queda guardado', 416, 330, { tam: 19, peso: 800, color: V, alinear: 'left' });
      L.rectRed(ctx, 416, 364, 360, 110, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
      UJ.rotulo(ctx, lz, "pg_get_functiondef('sp_agendar_cita'::regproc)", 596, 376, { tam: 13, peso: 700, ancho: 340 });
      UJ.rotulo(ctx, lz, 'devuelve la definición completa: cerrar la pestaña no lo borra', 596, 412, { tam: 15, ancho: 330 });
      L.rectRed(ctx, 24, 506, W - 48, 100, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Crear el procedimiento no es evidencia de nada:', W / 2, 522, { tam: 20, peso: 800, ancho: W - 80 });
      UJ.rotulo(ctx, lz, 'la evidencia es el CALL corriendo', W / 2, 558, { tam: 20, peso: 800, ancho: W - 80 });
    }
  });
})();
