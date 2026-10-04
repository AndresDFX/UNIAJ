/* Cada fase deja sus artefactos; las dos primeras producen los planos (esta asignatura) y
 * construccion y pruebas son la obra. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('artefactos-por-fase', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      var fases = ['Requisitos', 'Diseño', 'Construcción', 'Pruebas', 'Mantenimiento'];
      var arts = [['RF y RNF', 'glosario', 'reglas'], ['casos de uso', 'clases', 'wireframes'], ['el ejecutable'],
                  ['casos de prueba', 'evidencias'], ['el sistema en uso']];
      var colores = [A, A, m.acento, m.acento, m.gris];
      var x0 = 24, an = 144, gap = 8, yC = 190;
      UJ.rotulo(ctx, lz, 'Lo que deja cada fase', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 5; i++) {
        var x = x0 + i * (an + gap), c = colores[i];
        (function (i, x, c) {
          UJ.alfa(ctx, L.tramo(t, 0.04 + i * 0.05, 0.1 + i * 0.05), function () {
            L.rectRed(ctx, x, yC, an, 52, 10); L.rellena(ctx, c);
            UJ.rotulo(ctx, lz, fases[i], x + an / 2, yC + 15, { tam: 17, peso: 800, color: m.papel });
          });
          for (var k = 0; k < arts[i].length; k++) {
            var a0 = 0.18 + i * 0.05 + k * 0.03;
            (function (k) {
              UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.06), function () {
                var y = yC + 68 + k * 64;
                L.rectRed(ctx, x + 6, y, an - 12, 52, 8); L.rellena(ctx, L.tono(c, 0.9), L.tono(c, 0.4), 1.5);
                var h = L.texto(ctx, arts[i][k], -9999, -9999, { tam: 17, peso: 600, letra: lz.letra, ancho: an - 24 });
                UJ.rotulo(ctx, lz, arts[i][k], x + an / 2, y + 26 - h / 2, { tam: 17, peso: 600, ancho: an - 24 });
              });
            })(k);
          }
        })(i, x, c);
      }
      function llave(xa, xb, texto, color, p) {
        if (p <= 0) return;
        var y = 170;
        UJ.alfa(ctx, p, function () {
          L.trazo(ctx, [[xa, y], [xa, y - 22], [xb, y - 22], [xb, y]], 1, color, 3);
          L.trazo(ctx, [[(xa + xb) / 2, y - 22], [(xa + xb) / 2, y - 36]], 1, color, 3);
          UJ.rotulo(ctx, lz, texto, (xa + xb) / 2, y - 72, { tam: 20, peso: 800, color: color });
        });
      }
      llave(x0 + 4, x0 + 2 * an + gap - 4, 'los planos · esta asignatura', A, L.tramo(t, 0.52, 0.66));
      llave(x0 + 2 * (an + gap) + 4, x0 + 4 * an + 3 * gap - 4, 'la obra', m.acento, L.tramo(t, 0.77, 0.9));
    }
  });
})();
