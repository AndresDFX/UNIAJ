/* Lo que dibuja el codigo de «Lo que NO es una clase del dominio»: tres clases del dominio sin
 * compartimentos (Dueno, Mascota, Cita), sus dos asociaciones y la nota pegada a Mascota. */
(function () {
  FP_ANIMADOR.registrar('dg-no-es-clase', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var x = 120, w = 200, cx = x + w / 2, ys = [60, 270, 480];
      ['Dueno', 'Mascota', 'Cita'].forEach(function (n, i) { DG.clase(ctx, lz, x, ys[i], w, n, null, null); });
      var rots = ['posee', 'tiene'];
      for (var i = 0; i < 2; i++) {
        var a = ys[i] + 38, b = ys[i + 1];
        DG.flecha(ctx, lz, [[cx, a], [cx, b - 1]], { abierta: true, rotulo: rots[i], en: [cx, (a + b) / 2] });
        FP_LIENZO.texto(ctx, '1', cx + 12, a + 4, { tam: 17, peso: 800, color: '#333', letra: lz.letra });
        FP_LIENZO.texto(ctx, '0..*', cx + 12, b - 28, { tam: 17, peso: 800, color: '#333', letra: lz.letra });
      }
      DG.nota(ctx, lz, 430, 250, 240, 78, 'La nombra el cliente\ny tiene reglas');
      ctx.save(); ctx.setLineDash([5, 5]);
      FP_LIENZO.trazo(ctx, [[x + w, 289], [430, 289]], 1, '#C9B037', 2); ctx.restore();
    }
  });
})();
