/* Partir una épica: los cortes por capa no sirven solos; las rebanadas verticales atraviesan
 * pantalla, lógica y datos y cada una deja algo usable. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('corte-vertical', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.2, 0.5, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Épicas y corte vertical', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var x0 = 150, an = 460, y0 = 124, h = 76;
      var capas = ['Pantalla', 'Lógica', 'Datos'], tonos = [0.75, 0.6, 0.45];
      var ap = L.tramo(t, 0.03, 0.15);
      UJ.alfa(ctx, ap, function () {
        for (var i = 0; i < 3; i++) {
          L.rectRed(ctx, x0, y0 + i * h, an, h, i === 0 ? 10 : 0); L.rellena(ctx, L.tono(m.sello, tonos[i]), L.tono(m.sello, -0.25), 2);
          UJ.rotulo(ctx, lz, capas[i], x0 - 14, y0 + i * h + 26, { tam: 20, peso: 700, alinear: 'right' });
        }
      });
      // Cortes horizontales: una historia por capa
      var hz = L.tramo(t, 0.22, 0.36), hzF = 1 - 0.55 * L.tramo(t, 0.52, 0.6);
      UJ.alfa(ctx, hzF, function () {
        UJ.alfa(ctx, 1 - L.tramo(t, 0.52, 0.58), function () { for (var i = 1; i < 3; i++) UJ.linea(ctx, x0 - 6, y0 + i * h, x0 + an + 6, y0 + i * h, R, 5, hz, true); });
        for (var j = 0; j < 3; j++) {
          var a = L.tramo(t, 0.3 + j * 0.04, 0.36 + j * 0.04);
          UJ.alfa(ctx, a, function () {
            L.texto(ctx, 'una historia', 628, y0 + j * h + 27, { tam: 17, peso: 700, color: R, letra: lz.letra });
          });
          UJ.sello(ctx, lz, 762, y0 + j * h + 38, 13, false, a);
        }
        UJ.alfa(ctx, L.tramo(t, 0.42, 0.48), function () {
          L.texto(ctx, 'Por capas: ninguna sirve sola', 628, y0 + 3 * h + 14, { tam: 18, peso: 800, color: R, ancho: 150, letra: lz.letra });
        });
      });
      // Cortes verticales: rebanadas
      var nombres = ['consultar historial', 'registrar atención', 'adjuntar laboratorio', 'filtrar por fechas'];
      var ra = an / 4;
      for (var k = 0; k < 4; k++) {
        (function (k) {
          var a = L.tramo(t, 0.56 + k * 0.08, 0.66 + k * 0.08, 'frena'), x = x0 + k * ra;
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, x + 6, y0 + 4, ra - 12, 3 * h - 8, 8); L.rellena(ctx, L.tono(V, 0.55, 0.45), V, 3);
            L.texto(ctx, nombres[k], x + ra / 2, y0 + 3 * h + 14, { tam: 17, peso: 700, color: L.tono(V, -0.3), alinear: 'center', ancho: ra - 10, letra: lz.letra });
          });
          UJ.sello(ctx, lz, x + ra / 2, y0 - 22, 15, true, a);
        })(k);
      }
      UJ.rotulo(ctx, lz, 'Rebanadas: cada una deja algo que el cliente puede usar', W / 2, 470,
                { tam: 20, peso: 700, color: L.tono(V, -0.3), ancho: W - 40, visible: L.tramo(t, 0.88, 0.95) });
      UJ.rotulo(ctx, lz, 'Cada historia atraviesa pantalla, lógica y datos', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
