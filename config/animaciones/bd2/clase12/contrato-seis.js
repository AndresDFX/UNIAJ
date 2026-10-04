/* El contrato de un procedimiento y sus seis partes: firma, precondiciones, efecto, errores,
 * idempotencia y version. Paso 1: lo que la llamada necesita y hace (1-3); paso 2: lo que puede
 * salir mal y como evoluciona (4-6); paso 3: quien lo respeta y el ejemplo de la idempotencia. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('contrato-seis', {
    duracion: 5,
    pasos: [0.36, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.codigo(ctx, lz, 30, 16, 740, 'sp_agendar_cita( … )   ← solo el nombre no es contrato', L.tramo(t, 0, 0.12), 18);
      var partes = [['1 · Firma', 'parámetros con tipo (IN / OUT / INOUT) y lo que devuelve'], ['2 · Precondiciones', 'lo que debe ser cierto antes'],
                    ['3 · Efecto', 'qué queda distinto después'], ['4 · Errores', 'cada código y su significado'],
                    ['5 · Idempotencia', '¿dos llamadas = una?'], ['6 · Versión', 'cambiar sin romper']];
      for (var i = 0; i < 6; i++) {
        var col = i % 2, fila = Math.floor(i / 2), x = 30 + col * 380, y = 90 + fila * 140;
        var a = i < 3 ? L.tramo(t, 0.14 + i * 0.07, 0.22 + i * 0.07) : L.tramo(t, 0.4 + (i - 3) * 0.1, 0.48 + (i - 3) * 0.1);
        UJ.caja(ctx, lz, x, y, 360, 116, partes[i][0], partes[i][1], i < 3 ? A : C, a);
      }
      UJ.rotulo(ctx, lz, 'Las dos partes lo respetan: aplicación y base.', W / 2, 508,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.82, 0.9) });
      UJ.rotulo(ctx, lz, 'Agendar no es idempotente: un doble clic crea dos citas, salvo que un UNIQUE lo impida.', W / 2, 556,
                { tam: 17, peso: 600, color: L.tono(m.tinta, 0.2), ancho: W - 60, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
