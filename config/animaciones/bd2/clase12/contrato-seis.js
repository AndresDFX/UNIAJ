/* El contrato de un procedimiento y sus seis partes: firma, precondiciones, efecto, errores,
 * idempotencia y version. Mucho mas que el nombre del procedimiento. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('contrato-seis', {
    duracion: 5,
    pasos: [0.36, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.codigo(ctx, lz, 30, 16, 740, 'sp_agendar_cita( … )   ← solo el nombre no es contrato', L.tramo(t, 0, 0.12), 18);
      var partes = [['1 · Firma', 'parámetros: tipo y IN / OUT / IN OUT'], ['2 · Precondiciones', 'lo que debe ser cierto antes'],
                    ['3 · Efecto', 'qué queda distinto después'], ['4 · Errores', 'cada código y su significado'],
                    ['5 · Idempotencia', '¿dos llamadas = una?'], ['6 · Versión', 'cambiar sin romper']];
      for (var i = 0; i < 6; i++) {
        var col = i % 2, fila = Math.floor(i / 2), x = 30 + col * 380, y = 90 + fila * 140;
        var a = i < 3 ? L.tramo(t, 0.14 + i * 0.07, 0.22 + i * 0.07) : L.tramo(t, 0.4 + (i - 3) * 0.1, 0.48 + (i - 3) * 0.1);
        UJ.caja(ctx, lz, x, y, 360, 116, partes[i][0], partes[i][1], i < 3 ? A : C, a);
      }
      UJ.rotulo(ctx, lz, 'Las dos partes lo respetan: aplicación y base.', W / 2, 540,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
