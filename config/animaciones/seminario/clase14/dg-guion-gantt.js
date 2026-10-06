/* Lo que dibuja el codigo de «El guion cronometrado de la sustentacion»: un gantt de 12 minutos
 * con los siete bloques encadenados y su duracion; el de decisiones, marcado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dg-guion-gantt', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.rotulo(ctx, lz, 'Sustentacion - 12 minutos', 400, 24, { tam: 21, peso: 800 });
      var x0 = 250, x1 = 780, px = (x1 - x0) / 720, yTop = 80, fila = 62;
      var b = [['Problema', 0, 90], ['Alcance', 90, 90], ['Requisitos', 180, 120], ['Modelo UML', 300, 120],
               ['Prototipo en vivo', 420, 120], ['Decisiones defendidas', 540, 120], ['Riesgos y cierre', 660, 60]];
      L.rectRed(ctx, 20, yTop, 760, 7 * fila, 0); L.rellena(ctx, '#F3F6FA');
      L.texto(ctx, 'Guion', 32, yTop + 8, { tam: 15, peso: 800, color: '#095292', letra: lz.letra });
      var yEje = yTop + 7 * fila;
      for (var s = 0; s <= 720; s += 120) {
        var x = x0 + s * px;
        L.trazo(ctx, [[x, yTop], [x, yEje + 6]], 1, '#C9D6E2', 1.5);
        UJ.rotulo(ctx, lz, (s / 60 < 10 ? '0' : '') + (s / 60) + ':00', x, yEje + 12, { tam: 14, peso: 600, color: '#555' });
      }
      b.forEach(function (k, i) {
        var y = yTop + i * fila + 12, dec = i === 5, c = dec ? '#A02030' : '#095292';
        L.texto(ctx, k[0], 240, y + 10, { tam: 16, peso: dec ? 800 : 600, color: dec ? c : '#1A2B3C', alinear: 'right', letra: lz.letra });
        L.rectRed(ctx, x0 + k[1] * px, y, k[2] * px - 2, 38, 6); L.rellena(ctx, c);
        var d = k[2] % 60 ? k[2] + 's' : (k[2] / 60) + 'm';
        UJ.rotulo(ctx, lz, d, x0 + k[1] * px + k[2] * px / 2, y + 9, { tam: 15, peso: 700, color: '#FFFFFF' });
      });
      DG.marca(ctx, lz, 40, yEje + 75, 1, 'Sin cronometro, el bloque de decisiones —el que mas pesa— se queda sin tiempo', 700);
    }
  });
})();
