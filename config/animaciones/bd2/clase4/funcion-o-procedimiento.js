/* Funcion y procedimiento: la funcion DEVUELVE un valor que se usa en la consulta; el
 * procedimiento HACE un cambio y se llama con CALL. Dos columnas, el mismo ritmo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('funcion-o-procedimiento', {
    duracion: 4.6,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.37, 0.66, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // Funcion, a la izquierda
      UJ.rotulo(ctx, lz, 'FUNCIÓN · devuelve', 200, 18, { tam: 28, peso: 800, color: A });
      UJ.codigo(ctx, lz, 22, 64, 356, "SELECT fn_precio_consulta(…);", L.tramo(t, 0.02, 0.22), 15);
      L.flecha(ctx, 200, 108, 200, 168, A, 4, L.tramo(t, 0.22, 0.32, 'frena'));
      UJ.caja(ctx, lz, 70, 172, 260, 90, 'fn_precio_consulta', 'RETURNS NUMERIC', A, L.tramo(t, 0.25, 0.35));
      var v = L.tramo(t, 0.38, 0.6, 'suave');
      if (v > 0) {
        var vy = L.mezcla(262, 330, v);
        L.rectRed(ctx, 150, vy, 100, 40, 20); L.rellena(ctx, m.sello || C);
        UJ.rotulo(ctx, lz, '40000', 200, vy + 7, { tam: 22, peso: 800 });
      }
      UJ.alfa(ctx, L.tramo(t, 0.55, 0.65), function () {
        UJ.tabla(ctx, lz, 40, 390, 320, 'resultado', ['tarifa = 40000'], 1, A, 0);
      });
      // Procedimiento, a la derecha
      var X = W / 2 + 10;
      UJ.rotulo(ctx, lz, 'PROCEDIMIENTO · hace', X + 190, 18, { tam: 28, peso: 800, color: C });
      UJ.codigo(ctx, lz, X + 12, 64, 356, 'CALL sp_agendar_cita(1, 2, …);', L.tramo(t, 0.3, 0.48), 15);
      L.flecha(ctx, X + 190, 108, X + 190, 168, C, 4, L.tramo(t, 0.48, 0.58, 'frena'));
      UJ.caja(ctx, lz, X + 60, 172, 260, 90, 'sp_agendar_cita', 'valida y escribe', C, L.tramo(t, 0.5, 0.6));
      L.flecha(ctx, X + 190, 266, X + 190, 380, C, 4, L.tramo(t, 0.62, 0.72, 'frena'));
      UJ.tabla(ctx, lz, X + 30, 390, 320, 'cita', ['1 · Firulais · 09:00', '2 · Michi · 10:00'], 1 + L.tramo(t, 0.72, 0.82) , C, L.tramo(t, 0.72, 0.82) > 0.5 ? 1 : -1);
      UJ.rotulo(ctx, lz, 'Una se usa dentro de la consulta; el otro cambia los datos.', W / 2, 580,
                { tam: 21, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.82, 0.98) });
    }
  });
})();
