/* El semaforo de una esquina descompuesto: proposito y frontera, actores, una entrada seguida
 * (el peaton que espera 90 s) y la retroalimentacion que casi nunca existe. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('semaforo', {
    duracion: 5,
    pasos: [0.28, 0.52, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      function semaforo(x, y, s, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, 56 * s, 150 * s, 12 * s); L.rellena(ctx, L.tono(m.tinta, -0.3));
          var cols = [R, m.sello || '#FFD000', V];
          for (var i = 0; i < 3; i++) { L.circulo(ctx, x + 28 * s, y + (28 + i * 47) * s, 17 * s); L.rellena(ctx, i === 0 ? cols[i] : L.tono(cols[i], 0.55)); }
        });
      }
      // 1-2: proposito y frontera
      semaforo(240, 120, 1, L.tramo(t, 0, 0.08));
      UJ.rotulo(ctx, lz, 'Propósito: cruzar sin chocar y sin esperar de más', W / 2, 20, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.04, 0.14) });
      var f = L.tramo(t, 0.12, 0.24);
      if (f > 0) {
        ctx.save(); ctx.setLineDash([12, 9]);
        L.trazo(ctx, [[60, 80], [540, 80], [540, 420], [60, 420], [60, 80]], f, m.tinta, 3);
        ctx.restore();
        UJ.rotulo(ctx, lz, 'frontera: la esquina', 300, 384, { tam: 19, peso: 700, visible: L.tramo(t, 0.2, 0.26) });
      }
      semaforo(660, 150, 0.7, L.tramo(t, 0.18, 0.26));
      UJ.rotulo(ctx, lz, 'el de al lado: fuera, pero influye', 680, 270, { tam: 17, ancho: 200, visible: L.tramo(t, 0.2, 0.28) });
      // 3: actores
      var act = ['conductores', 'peatones', 'agente de tránsito', 'el vecino que aguanta el ruido'];
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, 0.3 + i * 0.04, 0.36 + i * 0.04), y = 112 + i * 64;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 330, y, 196, 52, 26); L.rellena(ctx, L.tono(C, 0.85), C, 2);
          UJ.rotulo(ctx, lz, act[i], 428, y + 6 + (act[i].length > 20 ? 0 : 9), { tam: 17, peso: 700, ancho: 180 });
        });
      }
      // 4: una entrada seguida
      UJ.alfa(ctx, L.tramo(t, 0.54, 0.64), function () {
        L.objetos.reloj(ctx, 130, 520, 46, m, L.mezcla(0, 1.5, L.tramo(t, 0.56, 0.72)));
        UJ.rotulo(ctx, lz, 'Un peatón a las 6 p. m. espera 90 s. ¿Es mucho?', 200, 492, { tam: 21, peso: 600, alinear: 'left', ancho: 560 });
      });
      // 5: retroalimentacion
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.9), function () {
        L.rectRed(ctx, 200, 560, 570, 60, 12); L.rellena(ctx, L.tono(R, 0.88), R, 2);
        UJ.rotulo(ctx, lz, '¿Se entera del trancón? Casi nunca: repite su ciclo.', 485, 575, { tam: 20, peso: 700, color: R, ancho: 550 });
      });
    }
  });
})();
