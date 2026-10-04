/* El paquete documental de un proyecto tradicional: cuatro documentos con cabecera de control
 * y la solicitud de cambio que mide su impacto en alcance, tiempo y costo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('paquete-tradicional', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.33, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      var docs = ['ERS (IEEE 830 / ISO 29148)', 'Documento de diseño', 'Matriz de trazabilidad', 'Acta de aprobación'];
      var cab = ['versión', 'fecha', 'autor', 'aprobador'];
      var an = 172, al = 214, y0 = 76;
      UJ.rotulo(ctx, lz, 'El paquete de un proyecto tradicional', W / 2, 20, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 4; i++) {
        var x = 24 + i * 190, a0 = 0.04 + i * 0.06;
        (function (x, i, a0) {
          UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.06), function () {
            ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x + an - 28, y0); ctx.lineTo(x + an, y0 + 28); ctx.lineTo(x + an, y0 + al); ctx.lineTo(x, y0 + al); ctx.closePath();
            L.rellena(ctx, m.papel, A, 2.5);
            UJ.rotulo(ctx, lz, docs[i], x + an / 2 - 6, y0 + 14, { tam: 18, peso: 800, color: A, ancho: an - 40 });
          });
          // Cabecera de control que llega desde arriba
          var c0 = 0.34 + i * 0.06, q = L.tramo(t, c0, c0 + 0.08, 'frena');
          if (q > 0) UJ.alfa(ctx, q, function () {
            var y = y0 + 100 - (1 - q) * 40;
            L.rectRed(ctx, x + 10, y, an - 20, 104, 8); L.rellena(ctx, L.tono(m.sello, 0.75), L.tono(m.sello, -0.2), 1.5);
            for (var k = 0; k < 4; k++) L.texto(ctx, cab[k] + ': ____', x + 22, y + 8 + k * 23, { tam: 16, peso: 600, color: m.tinta, letra: lz.letra });
          });
        })(x, i, a0);
      }
      // Solicitud de cambio
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.7), function () {
        L.rectRed(ctx, 250, 326, 300, 50, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2.5);
        UJ.rotulo(ctx, lz, 'Solicitud de cambio', 400, 338, { tam: 20, peso: 800, color: R });
      });
      var imp = [[130, 'alcance'], [400, 'tiempo'], [670, 'costo']];
      for (var j = 0; j < 3; j++) {
        var b0 = 0.7 + j * 0.05;
        UJ.flecha(ctx, lz, 400, 378, imp[j][0], 444, R, L.tramo(t, b0, b0 + 0.05));
        UJ.pildora(ctx, lz, imp[j][0], 450, imp[j][1], R, L.tramo(t, b0 + 0.04, b0 + 0.08), { tam: 18, centrar: true });
      }
      UJ.alfa(ctx, L.tramo(t, 0.86, 0.9), function () {
        UJ.rotulo(ctx, lz, 'impacto que se evalúa antes de aprobar', W / 2, 500, { tam: 17, peso: 600, color: m.gris });
      });
      UJ.rotulo(ctx, lz, 'La documentación es buena parte de lo contratado.', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
