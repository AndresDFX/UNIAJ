/* Caso GitLab, enero de 2017: borrado del directorio de datos en el servidor equivocado (causa
 * proxima); los cinco mecanismos de respaldo y replicacion fallaban (causa raiz); se restauro una
 * copia de unas seis horas antes. Un respaldo que nunca se restauro no es un respaldo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('gitlab-2017', {
    duracion: 5,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.caja(ctx, lz, 30, 20, 340, 84, 'Problema de replicación', 'enero de 2017', A, L.tramo(t, 0, 0.08));
      L.flecha(ctx, 374, 62, 420, 62, m.tinta, 4, L.tramo(t, 0.08, 0.12, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.18), function () {
        L.rectRed(ctx, 424, 20, 346, 84, 10); L.rellena(ctx, L.tono(m.tinta, -0.55));
        UJ.rotulo(ctx, lz, 'borrado recursivo', 597, 32, { tam: 19, color: '#E8F4FA' });
        UJ.rotulo(ctx, lz, 'en el servidor equivocado', 597, 62, { tam: 19, color: '#FFB4B4' });
      });
      UJ.rotulo(ctx, lz, '≈ 300 GB eliminados · causa próxima', 597, 112, { tam: 17, peso: 800, color: R, visible: L.tramo(t, 0.18, 0.26) });
      // Los cinco mecanismos
      UJ.rotulo(ctx, lz, 'Al recuperar: los 5 mecanismos de respaldo fallaban', 30, 170, { tam: 21, peso: 800, color: C, alinear: 'left', ancho: 740, visible: L.tramo(t, 0.32, 0.36) });
      for (var i = 0; i < 5; i++) {
        var x = 40 + i * 150;
        UJ.alfa(ctx, L.tramo(t, 0.36 + i * 0.04, 0.42 + i * 0.04), function () {
          L.rectRed(ctx, x, 214, 130, 90, 12); L.rellena(ctx, L.tono(A, 0.88), A, 2);
          UJ.rotulo(ctx, lz, 'respaldo ' + (i + 1), x + 65, 228, { tam: 18, peso: 700, color: A });
        });
        UJ.sello(ctx, lz, x + 65, 280, 16, false, L.tramo(t, 0.44 + i * 0.03, 0.5 + i * 0.03));
      }
      UJ.rotulo(ctx, lz, 'volcado que fallaba en silencio · copias remotas vacías', W / 2, 318, { tam: 18, peso: 600, ancho: 740, visible: L.tramo(t, 0.56, 0.62) });
      // El desenlace
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.74), function () {
        L.rectRed(ctx, 30, 370, 740, 80, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'Se restauró una copia de ~6 h antes: esa ventana se perdió', 400, 396, { tam: 20, peso: 700, color: R, ancho: 700 });
      });
      UJ.rotulo(ctx, lz, 'El RPO no se declara: se demuestra restaurando.', W / 2, 500, { tam: 22, peso: 800, color: A, ancho: W - 40, visible: L.tramo(t, 0.8, 0.9) });
      UJ.rotulo(ctx, lz, 'Respaldo nunca restaurado ≠ respaldo.', W / 2, 560, { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
