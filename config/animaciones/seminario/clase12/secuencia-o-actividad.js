/* Cual diagrama dibujar segun la duda: responsabilidades de un caso de uso (secuencia) u orden,
 * decisiones y paralelos de un proceso (actividad). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('secuencia-o-actividad', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.45, 0.9, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, T = m.tinta, G = m.gris, W = lz.ancho;
      UJ.rotulo(ctx, lz, '¿Secuencia o actividad?', W / 2, 18, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });

      function pregunta(y, texto, a, c) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 24, y, 290, 150, 14); L.rellena(ctx, L.tono(c, 0.88), c, 2.5);
          var h = L.texto(ctx, texto, -9999, -9999, { tam: 21, peso: 700, letra: lz.letra, ancho: 250 });
          UJ.rotulo(ctx, lz, texto, 169, y + 75 - h / 2, { tam: 21, peso: 700, color: L.tono(c, -0.3), ancho: 250 });
        });
      }
      function marco(x, y, w, h, a) {
        UJ.alfa(ctx, a, function () { L.rectRed(ctx, x, y, w, h, 12); L.rellena(ctx, m.papel, L.tono(G, 0.3), 2); });
      }

      // Fila 1: secuencia
      var y1 = 78;
      pregunta(y1, '¿Quién se encarga y con quién habla?', L.tramo(t, 0.05, 0.12), A);
      L.flecha(ctx, 322, y1 + 75, 380, y1 + 75, A, 3, L.tramo(t, 0.13, 0.18));
      var a1 = L.tramo(t, 0.18, 0.24);
      marco(392, y1, 384, 150, a1);
      UJ.alfa(ctx, a1, function () {
        var px = [460, 584, 708];
        for (var i = 0; i < 3; i++) {
          L.rectRed(ctx, px[i] - 46, y1 + 14, 92, 26, 5); L.rellena(ctx, L.tono(A, 0.85), A, 2);
          UJ.linea(ctx, px[i], y1 + 40, px[i], y1 + 138, L.tono(G, 0.2), 2, 1, true);
        }
      });
      L.flecha(ctx, 464, y1 + 64, 580, y1 + 64, A, 2.5, L.tramo(t, 0.24, 0.28));
      L.flecha(ctx, 588, y1 + 88, 704, y1 + 88, A, 2.5, L.tramo(t, 0.28, 0.32));
      UJ.flecha(ctx, lz, 704, y1 + 112, 588, y1 + 112, L.tono(T, 0.3), L.tramo(t, 0.32, 0.36), null, { punteada: true, grosor: 2 });
      UJ.flecha(ctx, lz, 580, y1 + 130, 464, y1 + 130, L.tono(T, 0.3), L.tramo(t, 0.35, 0.39), null, { punteada: true, grosor: 2 });
      UJ.rotulo(ctx, lz, 'Secuencia · un caso de uso (agendar cita)', 584, y1 + 162,
                { tam: 18, peso: 700, color: A, visible: L.tramo(t, 0.38, 0.45) });

      // Fila 2: actividad
      var y2 = 320;
      pregunta(y2, '¿En qué orden, quién decide, qué va en paralelo?', L.tramo(t, 0.5, 0.57), C);
      L.flecha(ctx, 322, y2 + 75, 380, y2 + 75, C, 3, L.tramo(t, 0.57, 0.62));
      var a2 = L.tramo(t, 0.62, 0.68);
      marco(392, y2, 384, 150, a2);
      var cc = L.tono(C, -0.2);
      UJ.alfa(ctx, a2, function () {
        L.circulo(ctx, 418, y2 + 75, 9); L.rellena(ctx, T);
      });
      L.flecha(ctx, 428, y2 + 75, 448, y2 + 75, T, 2, L.tramo(t, 0.66, 0.68));
      UJ.alfa(ctx, L.tramo(t, 0.67, 0.71), function () {
        L.rectRed(ctx, 450, y2 + 60, 70, 30, 14); L.rellena(ctx, L.tono(C, 0.85), C, 2);
      });
      L.flecha(ctx, 520, y2 + 75, 538, y2 + 75, T, 2, L.tramo(t, 0.7, 0.72));
      UJ.alfa(ctx, L.tramo(t, 0.71, 0.75), function () {
        ctx.beginPath(); ctx.moveTo(560, y2 + 55); ctx.lineTo(580, y2 + 75); ctx.lineTo(560, y2 + 95); ctx.lineTo(540, y2 + 75); ctx.closePath();
        L.rellena(ctx, L.tono(m.sello, 0.6), L.tono(m.sello, -0.4), 2);
      });
      L.flecha(ctx, 580, y2 + 75, 606, y2 + 75, T, 2, L.tramo(t, 0.74, 0.76));
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.8), function () {
        L.rectRed(ctx, 608, y2 + 30, 7, 90, 2); L.rellena(ctx, T);
        L.rectRed(ctx, 632, y2 + 26, 76, 30, 14); L.rellena(ctx, L.tono(C, 0.85), C, 2);
        L.rectRed(ctx, 632, y2 + 94, 76, 30, 14); L.rellena(ctx, L.tono(C, 0.85), C, 2);
        L.flecha(ctx, 615, y2 + 41, 630, y2 + 41, T, 2, 1);
        L.flecha(ctx, 615, y2 + 109, 630, y2 + 109, T, 2, 1);
        L.rectRed(ctx, 726, y2 + 30, 7, 90, 2); L.rellena(ctx, T);
        L.flecha(ctx, 708, y2 + 41, 724, y2 + 41, T, 2, 1);
        L.flecha(ctx, 708, y2 + 109, 724, y2 + 109, T, 2, 1);
        L.circulo(ctx, 754, y2 + 75, 10); L.rellena(ctx, m.papel, T, 2.5);
        L.circulo(ctx, 754, y2 + 75, 5); L.rellena(ctx, T);
        L.flecha(ctx, 733, y2 + 75, 742, y2 + 75, T, 2, 1);
      });
      UJ.rotulo(ctx, lz, 'Actividad · un proceso (de la puerta a la factura)', 584, y2 + 162,
                { tam: 18, peso: 700, color: cc, visible: L.tramo(t, 0.82, 0.9) });

      UJ.rotulo(ctx, lz, 'La duda que se quiere resolver elige el diagrama.', W / 2, 568,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
