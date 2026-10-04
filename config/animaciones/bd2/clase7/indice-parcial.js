/* Indice parcial: el WHERE es parte de la DEFINICION y decide que filas entran. Completo: 30.010
 * entradas; parcial PROGRAMADA: 18.187 (61 %), cuatro de cada diez menos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('indice-parcial', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, V = m.verde || A;
      UJ.codigo(ctx, lz, 30, 26, W - 60, 'CREATE INDEX idx_cita_programada_fecha', L.tramo(t, 0, 0.08), 17);
      UJ.codigo(ctx, lz, 30, 70, W - 60, "ON cita (fecha_hora) WHERE estado = 'PROGRAMADA';", L.tramo(t, 0.06, 0.16), 17);
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.28), function () {
        L.rectRed(ctx, 30, 126, W - 60, 70, 12); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'Ese WHERE no es el de la consulta:', W / 2, 134, { tam: 19, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'es parte de la definición y decide qué filas entran', W / 2, 162, { tam: 17, ancho: W - 100 });
      });
      function barra(y, nom, n, f, col, a0) {
        var p = L.tramo(t, a0 + 0.04, a0 + 0.16, 'suave');
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.06), function () {
          UJ.rotulo(ctx, lz, nom, 30, y, { tam: 18, peso: 700, alinear: 'left' });
          L.rectRed(ctx, 30, y + 30, 600 * f * Math.max(p, 0.01), 50, 8); L.rellena(ctx, col);
          UJ.rotulo(ctx, lz, n, 30 + 600 * f + 70, y + 42, { tam: 22, peso: 800, color: A, visible: p });
        });
      }
      barra(230, 'índice completo sobre fecha_hora', '30.010', 1, L.tono(A, 0.35), 0.38);
      barra(340, 'índice parcial: solo PROGRAMADA', '18.187', 18187 / 30010, V, 0.5);
      UJ.rotulo(ctx, lz, 'cuatro de cada diez entradas menos', W / 2, 446, { tam: 20, peso: 800, color: V, visible: L.tramo(t, 0.64, 0.7) });
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.86), function () {
        L.rectRed(ctx, 30, 490, W - 60, 100, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Menos disco, menos memoria y menos trabajo al escribir', W / 2, 502, { tam: 19, peso: 700, ancho: W - 100 });
        UJ.rotulo(ctx, lz, "Se usa si la consulta trae la misma condición: estado = 'PROGRAMADA'", W / 2, 540, { tam: 17, ancho: W - 100 });
      });
    }
  });
})();
