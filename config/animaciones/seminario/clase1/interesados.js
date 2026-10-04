/* Los interesados de la clínica quieren cosas distintas y a veces opuestas: decidir qué se
 * prioriza, y dejar escrito por qué, es el trabajo del análisis. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('interesados', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.45, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Cada interesado quiere algo distinto', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var act = [
        [140, 'Dueño de la clínica', 'quiere métricas', A],
        [400, 'Recepcionista', 'quiere agendar rápido', m.acento],
        [660, 'Veterinario', 'quiere el historial a la mano', m.verde]
      ];
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, 0.06 + i * 0.12, 0.16 + i * 0.12);
        var c = L.tono(act[i][3], -0.15);
        UJ.monigote(ctx, lz, act[i][0], 90, 110, null, c, a);
        UJ.rotulo(ctx, lz, act[i][1], act[i][0], 210, { tam: 19, peso: 800, color: c, ancho: 220, visible: a });
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, act[i][0] - 110, 250, 220, 64, 12); L.rellena(ctx, L.tono(act[i][3], 0.9), act[i][3], 2);
          var hh = L.texto(ctx, act[i][2], -9999, -9999, { tam: 18, peso: 600, letra: lz.letra, ancho: 200 });
          UJ.rotulo(ctx, lz, act[i][2], act[i][0], 282 - hh / 2, { tam: 18, peso: 600, ancho: 200 });
        });
      }
      // Conflicto dueño - recepcionista
      var p = L.tramo(t, 0.48, 0.62, 'frena');
      if (p > 0) {
        var y = 370, x1 = 140, x2 = 400;
        UJ.linea(ctx, x1, 318, x1, y, R, 3, Math.min(1, p * 3));
        UJ.linea(ctx, x2, 318, x2, y, R, 3, Math.min(1, p * 3));
        L.flecha(ctx, (x1 + x2) / 2, y, x1 + 4, y, R, 4, p);
        L.flecha(ctx, (x1 + x2) / 2, y, x2 - 4, y, R, 4, p);
        UJ.rayo(ctx, (x1 + x2) / 2 - 6, y - 30, 40, m.sello, L.tramo(t, 0.58, 0.64));
      }
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.72), function () {
        UJ.pildora(ctx, lz, 270, 400, 'más datos ⇄ registro más lento', R, 1, { centrar: true, tam: 19 });
      });

      UJ.alfa(ctx, L.tramo(t, 0.82, 0.96), function () {
        L.rectRed(ctx, 70, 500, W - 140, 64, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2.5);
        UJ.rotulo(ctx, lz, 'Decidir qué se prioriza y escribir por qué = análisis', W / 2, 518, { tam: 22, peso: 800, color: A, ancho: W - 170 });
      });
    }
  });
})();
