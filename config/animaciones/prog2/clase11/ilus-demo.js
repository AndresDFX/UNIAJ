/* Ilustracion: comentario vago reescrito como accionable */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var R = m.malva || '#A02030', V = m.verde || A;
      var d = {"titulo": "Qué observar en la demo", "izq": ["Comentario vago", "«Este código es un desastre»", "No dice dónde", "No dice por qué importa", "No dice qué hacer"], "der": ["Comentario accionable", "Se aplica el checklist", "Dónde: archivo:línea", "Impacto: qué falla", "Sugerencia concreta"], "fin": "Se corre el programa, se revisa y se reescribe el comentario"};
      UJ.rotulo(ctx, lz, d.titulo, W / 2, 14, { tam: 26, peso: 800, color: A, ancho: W - 40 });
      var cols = d.neutro ? [[d.izq, A, 24], [d.der, C, 412]] : [[d.izq, R, 24], [d.der, V, 412]];
      for (var c = 0; c < 2; c++) {
        var col = cols[c][1], x = cols[c][2], k = cols[c][0];
        L.rectRed(ctx, x, 64, 364, 56, 12); L.rellena(ctx, col);
        UJ.rotulo(ctx, lz, k[0], x + 182, 78, { tam: 22, peso: 800, color: m.papel, ancho: 340 });
        var n = k.length - 1, alto = Math.min(92, (410 - (n - 1) * 14) / n);
        for (var i = 1; i <= n; i++) {
          var y = 134 + (i - 1) * (alto + 14);
          L.rectRed(ctx, x, y, 364, alto, 12); L.rellena(ctx, L.tono(col, 0.9), col, 2);
          var mono = k[i].charAt(0) === '`';
          UJ.rotulo(ctx, lz, mono ? k[i].slice(1) : k[i], x + 182, y + alto / 2 - (k[i].length > 34 ? 22 : 12),
                    { tam: mono ? 17 : 18, peso: 600, ancho: 336 });
        }
        if (!d.neutro) UJ.sello(ctx, lz, x + 340, 66, 20, c === 1, 1);
      }
      L.rectRed(ctx, 24, 560, W - 48, 62, 14); L.rellena(ctx, m.sello || C);
      UJ.rotulo(ctx, lz, d.fin, W / 2, 577, { tam: 20, peso: 800, ancho: W - 80 });
    }
  });
})();
