/* Lo que dibuja el codigo de «El plan de sprints en Mermaid (gantt)»: tres secciones, cinco
 * tareas de 7 dias encadenadas con `after`, sobre un eje de fechas dd/mm. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dg-gantt-sprints', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.rotulo(ctx, lz, 'Tres sprints de diseno de la clinica', 400, 40, { tam: 20, peso: 800 });
      var x0 = 300, x1 = 755, dias = 35, px = (x1 - x0) / dias, yTop = 110, fila = 70;
      var tareas = [['Modelo de dominio', 0], ['Casos de uso nucleo', 7], ['Secuencia de agendar', 14],
                    ['Wireframes principales', 21], ['Consolidacion paquete', 28]];
      var secc = [['Sprint 1', 0, 2, '#E3EEF8'], ['Sprint 2', 2, 2, '#F3ECF8'], ['Sprint 3', 4, 1, '#E2F2EA']];
      var cols = ['#095292', '#6A3D9A', '#1B7A4E'];
      secc.forEach(function (s, k) {
        L.rectRed(ctx, 20, yTop + s[1] * fila, 760, s[2] * fila, 0); L.rellena(ctx, s[3]);
        L.texto(ctx, s[0], 32, yTop + s[1] * fila + s[2] * fila / 2 - 10, { tam: 16, peso: 800, color: cols[k], letra: lz.letra });
      });
      var yEje = yTop + 5 * fila;
      for (var d = 0; d <= 35; d += 7) {
        var x = x0 + d * px;
        L.trazo(ctx, [[x, yTop], [x, yEje + 6]], 1, '#C9D6E2', 1.5);
        var dia = d < 30 ? (1 + d) : (d - 29), mes = d < 30 ? '09' : '10';
        UJ.rotulo(ctx, lz, (dia < 10 ? '0' : '') + dia + '/' + mes, x, yEje + 12, { tam: 14, peso: 600, color: '#555' });
      }
      tareas.forEach(function (tk, i) {
        var y = yTop + i * fila + 16, c = cols[i < 2 ? 0 : i < 4 ? 1 : 2];
        L.texto(ctx, tk[0], 290, y + 9, { tam: 15, peso: 600, color: '#1A2B3C', alinear: 'right', letra: lz.letra });
        L.rectRed(ctx, x0 + tk[1] * px, y, 7 * px - 2, 38, 6); L.rellena(ctx, c);
        UJ.rotulo(ctx, lz, '7d', x0 + tk[1] * px + 7 * px / 2, y + 9, { tam: 15, peso: 700, color: '#FFFFFF' });
      });
      UJ.rotulo(ctx, lz, 'Cada tarea empieza «after» la anterior: 01/09 → 05/10', 400, yEje + 50, { tam: 15, peso: 600, color: '#555' });
    }
  });
})();
