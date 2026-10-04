/* De golpe vs por goteo: cuatro modulos a la vez fallan sin culpable; uno a uno, humo tras cada union. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('goteo-vs-golpe', {
    duracion: 4.5,
    pasos: [0.35, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      var mods = ['Modelo', 'Repositorio', 'Servicio', 'Interfaz'];
      UJ.rotulo(ctx, lz, 'De golpe', 200, 20, { tam: 24, peso: 800, color: R, visible: L.tramo(t, 0, 0.06) });
      UJ.rotulo(ctx, lz, 'Por goteo', 600, 20, { tam: 24, peso: 800, color: m.verde, visible: L.tramo(t, 0.38, 0.44) });
      var c = L.tramo(t, 0.06, 0.22, 'suave');
      for (var i = 0; i < 4; i++) {
        var x0 = 20 + (i % 2) * 200, y0 = 80 + Math.floor(i / 2) * 240;
        var xf = 60, yf = 110 + i * 62;
        UJ.caja(ctx, lz, x0 + (xf - x0) * c, y0 + (yf - y0) * c, 170, 52, mods[i], null, A, L.tramo(t, 0, 0.06));
      }
      UJ.rayo(ctx, 300, 170, 100, R, L.tramo(t, 0.22, 0.28));
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.32), function () {
        UJ.rotulo(ctx, lz, 'Falla… ¿cuál fue?', 200, 400, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, '4 sospechosos a la vez', 200, 436, { tam: 18 });
      });
      ctx.save(); ctx.strokeStyle = L.tono(m.tinta, 0.75); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(400, 60); ctx.lineTo(400, 500); ctx.stroke(); ctx.restore();
      for (var k = 0; k < 4; k++) {
        var y = 70 + k * 100, a = L.tramo(t, 0.4 + k * 0.08, 0.45 + k * 0.08);
        UJ.caja(ctx, lz, 460, y, 190, 60, '+ ' + mods[k], null, A, a);
        if (k > 0 && a > 0) L.flecha(ctx, 555, y - 36, 555, y - 4, A, 4, a);
        UJ.sello(ctx, lz, 700, y + 30, 22, true, L.tramo(t, 0.46 + k * 0.06, 0.5 + k * 0.06));
      }
      UJ.rotulo(ctx, lz, '✓ = guion de humo en verde', 600, 470, { tam: 18, peso: 700, color: m.verde, visible: L.tramo(t, 0.66, 0.72) });
      UJ.rotulo(ctx, lz, 'Si falla, el culpable es lo último que se unió.', W / 2, 550, { tam: 21, ancho: W - 40, visible: L.tramo(t, 0.8, 0.92) });
    }
  });
})();
