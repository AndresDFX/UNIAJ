/* La cadena de trazabilidad del semestre, de la entrevista al criterio de aceptación, y el
 * requisito huérfano que no llega a ningún caso de uso. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cadena-trazabilidad', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.45, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Trazabilidad: el hilo del semestre', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var es = [['Entrevista', 'quien lo pidió'], ['Requisito', 'clase 6'], ['Historia', 'clase 7'],
                ['Caso de uso', 'clase 9'], ['Pantalla', 'clase 13'], ['Criterio', 'de aceptación']];
      var bw = 200, bh = 76, gap = 50, x0 = 50, ys = [90, 230];
      function pos(i) { return [x0 + (i % 3) * (bw + gap), ys[Math.floor(i / 3)]]; }
      for (var i = 0; i < 6; i++) {
        var p = pos(i), s = 0.04 + i * 0.06, a = L.tramo(t, s, s + 0.05);
        var c = i === 0 ? m.gris : i === 5 ? m.verde : A;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, p[0], p[1], bw, bh, 12); L.rellena(ctx, L.tono(c, 0.88), c, 2.5);
          UJ.rotulo(ctx, lz, es[i][0], p[0] + bw / 2, p[1] + 12, { tam: 19, peso: 800, color: L.tono(c, -0.3), ancho: bw - 16 });
          UJ.rotulo(ctx, lz, es[i][1], p[0] + bw / 2, p[1] + 44, { tam: 16, peso: 600, color: L.tono(m.tinta, 0.2) });
        });
        if (i < 5) {
          var q = pos(i + 1), pa = L.tramo(t, s + 0.04, s + 0.07);
          if (i === 2) {
            // Del final de la fila 1 al comienzo de la fila 2
            if (pa > 0) {
              L.trazo(ctx, [[p[0] + bw / 2, p[1] + bh + 2], [p[0] + bw / 2, p[1] + bh + 32], [q[0] + bw / 2, p[1] + bh + 32]], Math.min(1, pa * 1.25), L.tono(m.tinta, 0.4), 3);
              if (pa >= 1) L.flecha(ctx, q[0] + bw / 2, p[1] + bh + 32, q[0] + bw / 2, q[1] - 3, L.tono(m.tinta, 0.4), 3, 1);
            }
          } else {
            L.flecha(ctx, p[0] + bw + 4, p[1] + bh / 2, q[0] - 4, q[1] + bh / 2, L.tono(m.tinta, 0.4), 3, pa);
          }
        }
      }

      // RF huerfano
      var ha = L.tramo(t, 0.48, 0.56);
      UJ.alfa(ctx, ha, function () {
        ctx.save(); ctx.setLineDash([8, 6]);
        L.rectRed(ctx, x0, 370, bw, bh, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2.5);
        ctx.restore();
        UJ.rotulo(ctx, lz, 'RF huérfano', x0 + bw / 2, 382, { tam: 19, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'ningún caso de uso', x0 + bw / 2, 414, { tam: 16, peso: 600, color: L.tono(m.tinta, 0.2) });
      });
      UJ.sello(ctx, lz, x0 + bw + 40, 408, 24, false, L.tramo(t, 0.56, 0.64));
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.72), function () {
        UJ.rotulo(ctx, lz, 'nadie lo necesita,', x0 + bw + 80, 382, { tam: 19, peso: 700, color: R, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'o nadie notó el hueco', x0 + bw + 80, 410, { tam: 19, peso: 700, color: R, alinear: 'left' });
      });

      UJ.alfa(ctx, L.tramo(t, 0.82, 0.96), function () {
        L.rectRed(ctx, 50, 490, W - 100, 70, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2.5);
        UJ.rotulo(ctx, lz, 'Todo RF llega a un caso de uso; todo caso de uso señala su RF.', W / 2, 512, { tam: 20, peso: 800, color: A, ancho: W - 130 });
      });
    }
  });
})();
