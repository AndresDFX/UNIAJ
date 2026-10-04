/* Ilustracion: que observar en la demo de la Clase 2. Uno: con SET ROLE recepcion el DELETE
 * responde permission denied. Dos: information_schema muestra la matriz real. Tres: la vista
 * entrega la agenda sin el email del dueno. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });
      // 1 · el permiso que falta
      UJ.rotulo(ctx, lz, '1 · El permiso que falta, falla', 30, 60, { tam: 20, peso: 800, color: R, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 96, W - 60, 'SET ROLE recepcion;  DELETE FROM cita WHERE id_cita = 1;', 1, 15);
      UJ.rotulo(ctx, lz, 'ERROR: permission denied for table cita', 46, 136, { tam: 17, peso: 700, color: R, alinear: 'left' });
      UJ.sello(ctx, lz, W - 54, 146, 16, false, 1);
      // 2 · la matriz real
      UJ.rotulo(ctx, lz, '2 · La matriz sale del motor', 30, 188, { tam: 20, peso: 800, color: A, alinear: 'left' });
      UJ.tabla(ctx, lz, 30, 222, W - 60, 'role_table_grants', ['recepcion · cita · INSERT', 'recepcion · cita · SELECT', 'recepcion · cita · UPDATE'], 3, A, -1);
      UJ.rotulo(ctx, lz, 'ninguna fila con DELETE', W - 40, 230, { tam: 16, peso: 700, color: m.papel, alinear: 'right' });
      // 3 · la vista
      UJ.rotulo(ctx, lz, '3 · La vista recorta', 30, 404, { tam: 20, peso: 800, color: V, alinear: 'left' });
      var cols = ['id_cita', 'fecha_hora', 'dueno', 'telefono', 'email'];
      for (var j = 0; j < 5; j++) {
        var x = 30 + j * 148, fuera = j === 4;
        L.rectRed(ctx, x, 440, 144, 44, 6); L.rellena(ctx, fuera ? L.tono(m.tinta, 0.88) : L.tono(V, 0.85), fuera ? L.tono(m.tinta, 0.6) : V, 2);
        L.texto(ctx, cols[j], x + 72, 452, { tam: 16, peso: 700, color: fuera ? L.tono(m.tinta, 0.55) : m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
      }
      L.trazo(ctx, [[30 + 4 * 148 + 10, 448], [30 + 5 * 148 - 14, 478]], 1, R, 3);
      UJ.rotulo(ctx, lz, 'v_agenda_recepcion: 9 citas (sin la CANCELADA) y sin email', W / 2, 500, { tam: 18, ancho: W - 60 });
      L.rectRed(ctx, 30, 548, W - 60, 64, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Cada línea que debe fallar se ejecuta sola, y después RESET ROLE', W / 2, 568, { tam: 18, peso: 700, ancho: W - 80 });
    }
  });
})();
