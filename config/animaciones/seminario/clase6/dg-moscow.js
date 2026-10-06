/* Lo que dibuja el codigo de «La priorizacion MoSCoW en Mermaid»: cuatro subgrafos apilados
 * (Must, Should, Could, Wont) con los requisitos que caen en cada uno. */
(function () {
  FP_ANIMADOR.registrar('dg-moscow', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var g = [['Must - sin esto no hay producto', ['RF-01 Registrar mascota', 'RF-03 Agendar cita'], '#095292', '#E3EEF8'],
               ['Should - importante, hay alternativa manual', ['RF-07 Reporte mensual'], '#1B7A4E', '#E2F2EA'],
               ['Could - si sobra tiempo', ['RF-11 Exportar a Excel'], '#8A6400', '#FFF6D6'],
               ['Wont - fuera de este alcance', ['RF-15 App movil'], '#666666', '#EFEFEF']];
      var y = 20, h = 140, gap = 12;
      g.forEach(function (s, i) {
        var gy = y + i * (h + gap);
        DG.grupo(ctx, lz, 20, gy, 760, h, s[0], { tam: 17, color: s[2], borde: s[2], relleno: s[3] });
        var n = s[1].length, w = 300;
        s[1].forEach(function (rf, k) {
          var cx = n === 1 ? 400 : 220 + k * 360;
          DG.nodo(ctx, lz, cx, gy + 85, w, 56, rf, 'rect', { tam: 17, borde: s[2] });
        });
      });
      DG.marca(ctx, lz, 590, 3 * (h + gap) + 105, 1, 'Wont = no en esta version, no «nunca»', 170);
    }
  });
})();
