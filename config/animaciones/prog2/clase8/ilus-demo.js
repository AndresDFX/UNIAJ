/* Ilustracion: que observar: javadoc a HTML y pruebas rojo a verde */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var d = {"titulo": "Qué observar en la demo", "pasos": [["Bloque /** ... */ sobre el método", "@param · @return · @throws"], ["javadoc genera el HTML", "la página del contrato, sin abrir el código"], ["Las pruebas corren: barra roja", "una regla no se cumple", "mal"], ["Se corrige la regla: barra verde", "las mismas pruebas pasan", "bien"]], "fin": "Documentación y pruebas describen el mismo contrato"};
      UJ.rotulo(ctx, lz, d.titulo, W / 2, 14, { tam: 26, peso: 800, color: A, ancho: W - 40 });
      var n = d.pasos.length, alto = Math.min(96, (470 - (n - 1) * 22) / n), y0 = 66;
      for (var i = 0; i < n; i++) {
        var y = y0 + i * (alto + 22), p = d.pasos[i];
        var col = p[2] === 'mal' ? (m.malva || '#A02030') : p[2] === 'bien' ? (m.verde || A) : A;
        L.rectRed(ctx, 40, y, 70, alto, 14); L.rellena(ctx, col);
        UJ.rotulo(ctx, lz, String(i + 1), 75, y + alto / 2 - 16, { tam: 28, peso: 800, color: m.papel });
        L.rectRed(ctx, 120, y, W - 160, alto, 14); L.rellena(ctx, L.tono(col, 0.9), col, 2);
        UJ.rotulo(ctx, lz, p[0], 140, y + (p[1] ? alto / 2 - 30 : alto / 2 - 13), { tam: 21, peso: 800, alinear: 'left', ancho: W - 200 });
        if (p[1]) UJ.rotulo(ctx, lz, p[1], 140, y + alto / 2 + 4, { tam: 17, alinear: 'left', ancho: W - 200, color: L.tono(m.tinta, 0.1) });
        if (i < n - 1) L.flecha(ctx, 75, y + alto + 2, 75, y + alto + 20, L.tono(m.tinta, 0.4), 3, 1);
      }
      L.rectRed(ctx, 40, 560, W - 80, 62, 14); L.rellena(ctx, m.sello || C);
      UJ.rotulo(ctx, lz, d.fin, W / 2, 577, { tam: 20, peso: 800, ancho: W - 110 });
    }
  });
})();
