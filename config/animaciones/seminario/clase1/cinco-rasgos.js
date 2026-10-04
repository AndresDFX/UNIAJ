/* Los cinco rasgos de un documento usable, comprobados contra una frase de relleno (falla
 * todos) y contra un requisito numerado (los cumple todos). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cinco-rasgos', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Cinco rasgos de un documento usable', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var rasgos = ['Tiene lector y pregunta', 'Verificable', 'Trazable', 'Fechado y versionado', 'Accionable'];
      var x0 = 24, w0 = 330, x1 = 366, w1 = 196, x2 = 574, w2 = 202;
      var hy = 76, hh = 126, ry = hy + hh + 10, rh = 58;

      function cabecera(x, w, tit, ej, color, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, hy, w, hh, 12); L.rellena(ctx, L.tono(color, 0.9), color, 2.5);
          UJ.rotulo(ctx, lz, tit, x + w / 2, hy + 10, { tam: 20, peso: 800, color: L.tono(color, -0.2) });
          UJ.rotulo(ctx, lz, ej, x + w / 2, hy + 42, { tam: 16, peso: 600, ancho: w - 20 });
        });
      }
      for (var i = 0; i < 5; i++) {
        var y = ry + i * rh, a = L.tramo(t, 0.04 + i * 0.045, 0.1 + i * 0.045);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x0, y, w0, rh - 8, 10); L.rellena(ctx, L.tono(A, 0.9), A, 2);
          UJ.rotulo(ctx, lz, (i + 1) + '. ' + rasgos[i], x0 + 16, y + 14, { tam: 19, peso: 700, color: L.tono(A, -0.2), alinear: 'left' });
        });
        UJ.alfa(ctx, L.tramo(t, 0.04 + i * 0.045, 0.1 + i * 0.045) * 0.6, function () {
          L.rectRed(ctx, x1, y, w1, rh - 8, 10); L.rellena(ctx, L.tono(m.gris, 0.94));
          L.rectRed(ctx, x2, y, w2, rh - 8, 10); L.rellena(ctx, L.tono(m.gris, 0.94));
        });
        UJ.sello(ctx, lz, x1 + w1 / 2, y + (rh - 8) / 2, 18, false, L.tramo(t, 0.4 + i * 0.045, 0.46 + i * 0.045));
        UJ.sello(ctx, lz, x2 + w2 / 2, y + (rh - 8) / 2, 18, true, L.tramo(t, 0.72 + i * 0.045, 0.78 + i * 0.045));
      }
      cabecera(x1, w1, 'De relleno', '«el sistema debe ser amigable e intuitivo»', R, L.tramo(t, 0.32, 0.4));
      cabecera(x2, w2, 'Usable', '«RF-012 registrar mascota con cinco datos y dueño asociado»', V, L.tramo(t, 0.66, 0.72));
    }
  });
})();
