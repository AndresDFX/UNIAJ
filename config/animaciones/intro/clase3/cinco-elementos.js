/* Los cinco elementos de un sistema: entradas -> proceso -> salidas, la retroalimentacion que
 * vuelve, y la frontera que decide que queda dentro. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cinco-elementos', {
    duracion: 5,
    pasos: [0.4, 0.65, 0.88, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, S = m.sello || C, W = lz.ancho;
      var y = 200;
      UJ.caja(ctx, lz, 30, y, 190, 110, 'ENTRADAS', 'datos, dinero, personas', C, L.tramo(t, 0, 0.1));
      L.flecha(ctx, 222, y + 55, 290, y + 55, L.tono(m.tinta, 0.3), 4, L.tramo(t, 0.1, 0.16));
      UJ.caja(ctx, lz, 300, y, 200, 110, 'PROCESO', 'aquí vive el software', A, L.tramo(t, 0.14, 0.24));
      L.flecha(ctx, 502, y + 55, 572, y + 55, L.tono(m.tinta, 0.3), 4, L.tramo(t, 0.24, 0.3));
      UJ.caja(ctx, lz, 580, y, 190, 110, 'SALIDAS', 'decisiones, servicio', V, L.tramo(t, 0.28, 0.38));
      // Retroalimentacion
      var r = L.tramo(t, 0.42, 0.6, 'suave');
      if (r > 0) {
        var p = L.trazo(ctx, [[675, y + 112], [675, y + 190], [125, y + 190], [125, y + 114]], r, L.tono(S, -0.3), 4);
        if (r > 0.97) L.flecha(ctx, 125, y + 150, 125, y + 114, L.tono(S, -0.3), 4, 1);
        UJ.rotulo(ctx, lz, 'RETROALIMENTACIÓN: la salida vuelve y corrige', W / 2, y + 200, { tam: 21, peso: 700, color: L.tono(S, -0.4), visible: L.tramo(t, 0.55, 0.64) });
      }
      // Frontera
      var f = L.tramo(t, 0.68, 0.84);
      if (f > 0) {
        ctx.save(); ctx.setLineDash([14, 10]);
        L.trazo(ctx, [[14, 120], [786, 120], [786, 450], [14, 450], [14, 120]], f, m.tinta, 3);
        ctx.restore();
        UJ.rotulo(ctx, lz, 'FRONTERA · qué queda dentro', W / 2, 78, { tam: 24, peso: 800, visible: L.tramo(t, 0.78, 0.86) });
      }
      UJ.rotulo(ctx, lz, 'El software es solo una parte del proceso.', W / 2, 520, { tam: 24, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
