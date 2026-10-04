/* Ilustracion: una linea base con el cronometro del celular. 10 clientes en hora pico,
 * tiempos que suman 140 min: promedio 14 min, escrito completo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-linea-celular', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde || A, S = m.sello || m.acento, W = lz.ancho;
      L.objetos.reloj(ctx, 60, 56, 36, m, 6);
      UJ.rotulo(ctx, lz, '1 · Hora pico: viernes 6-7 p. m.', 110, 40, { tam: 23, peso: 800, color: A, alinear: 'left' });
      UJ.rotulo(ctx, lz, '2 · Cronometrar 10 clientes (min)', 30, 112, { tam: 21, peso: 800, color: A, alinear: 'left' });
      var v = [9, 12, 18, 15, 11, 16, 20, 13, 10, 16], base = 330, esc = 8;
      for (var i = 0; i < 10; i++) {
        var x = 40 + i * 50, h = v[i] * esc;
        L.rectRed(ctx, x, base - h, 36, h, 4); L.rellena(ctx, L.tono(A, 0.45));
        UJ.rotulo(ctx, lz, String(v[i]), x + 18, base - h - 24, { tam: 18, peso: 700 });
      }
      ctx.save(); ctx.setLineDash([10, 8]);
      L.trazo(ctx, [[30, base - 14 * esc], [530, base - 14 * esc]], 1, L.tono(S, -0.4), 3);
      ctx.restore();
      L.rectRed(ctx, 570, 150, 210, 180, 16); L.rellena(ctx, L.tono(S, 0.55), L.tono(S, -0.35), 2);
      UJ.rotulo(ctx, lz, '3 · Promedio', 675, 164, { tam: 20, peso: 800 });
      UJ.rotulo(ctx, lz, '14 min', 675, 204, { tam: 42, peso: 800 });
      UJ.rotulo(ctx, lz, '140 ÷ 10', 675, 270, { tam: 20 });
      UJ.rotulo(ctx, lz, '4 · Escribirlo completo', 30, 360, { tam: 21, peso: 800, color: A, alinear: 'left' });
      L.rectRed(ctx, 30, 396, W - 60, 90, 14); L.rellena(ctx, m.papel, A, 3);
      UJ.rotulo(ctx, lz, '14 min de espera promedio · 10 clientes · viernes 6-7 p. m. · medido el 12/09', W / 2, 410, { tam: 20, peso: 700, ancho: W - 100 });
      L.rectRed(ctx, 30, 510, W - 60, 100, 14); L.rellena(ctx, L.tono(V, 0.88), V, 2);
      UJ.rotulo(ctx, lz, '5 · Al final del semestre: se mide igual y se compara', W / 2, 540, { tam: 21, peso: 800, color: L.tono(V, -0.3), ancho: W - 100 });
    }
  });
})();
