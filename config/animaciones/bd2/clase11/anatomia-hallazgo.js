/* La anatomia fija de un hallazgo util: artefacto, observacion verificable, impacto, accion y
 * responsable con fecha. Frente a la retroalimentacion inutil, que no dice que mirar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('anatomia-hallazgo', {
    duracion: 5,
    pasos: [0.22, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030';
      // Inutil
      UJ.alfa(ctx, L.tramo(t, 0, 0.1) * (1 - 0.6 * L.tramo(t, 0.24, 0.3)), function () {
        L.rectRed(ctx, 40, 20, 720, 70, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, '«El modelo está flojo, mejórenlo»', 380, 40, { tam: 23, peso: 700, color: R });
      });
      UJ.sello(ctx, lz, 720, 55, 22, false, L.tramo(t, 0.1, 0.18));
      // Util: cinco partes
      var partes = [['Artefacto', 'script DDL'], ['Observación', 'detalle_factura sin FOREIGN KEY a insumo'],
                    ['Impacto', 'se insertan detalles con insumos que no existen'],
                    ['Acción', 'agregar la FK y re-ejecutar el script desde cero'], ['Responsable y fecha', 'el autor · antes de la próxima sesión']];
      for (var i = 0; i < 5; i++) {
        var y = 116 + i * 82, a = L.tramo(t, 0.26 + i * 0.11, 0.34 + i * 0.11);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 40, y, 220, 68, 10); L.rellena(ctx, L.tono(A, 0.1 + i * 0.08));
          UJ.rotulo(ctx, lz, (i + 1) + ' · ' + partes[i][0], 150, y + 12, { tam: 19, peso: 800, color: m.papel, ancho: 200 });
          L.rectRed(ctx, 268, y, 492, 68, 10); L.rellena(ctx, L.tono(A, 0.92), A, 2);
          UJ.rotulo(ctx, lz, partes[i][1], 284, y + 12, { tam: 19, peso: 500, alinear: 'left', ancho: 460 });
        });
      }
      UJ.rotulo(ctx, lz, 'La diferencia es verificabilidad: se sabe cuándo está resuelto.', W / 2, 545,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
