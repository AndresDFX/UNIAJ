/* Funcional frente a no funcional, y la diferencia entre un deseo («que sea rápido») y un
 * requisito que alguien puede comprobar con un número. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('deseo-o-requisito', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.28, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, '¿Deseo o requisito?', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      UJ.pildora(ctx, lz, W / 2, 80, 'Funcional = QUÉ hace', A, L.tramo(t, 0.05, 0.13), { centrar: true, tam: 20 });
      UJ.pildora(ctx, lz, W / 2, 132, 'No funcional = CÓMO se comporta', m.acento, L.tramo(t, 0.14, 0.22), { centrar: true, tam: 20 });

      // Deseo
      var x = 60, an = 480;
      UJ.alfa(ctx, L.tramo(t, 0.3, 0.38), function () {
        L.rectRed(ctx, x, 210, an, 80, 12); L.rellena(ctx, L.tono(m.gris, 0.85), m.gris, 2.5);
        UJ.rotulo(ctx, lz, '«El sistema debe ser rápido»', x + an / 2, 236, { tam: 21, peso: 700, ancho: an - 30 });
      });
      UJ.sello(ctx, lz, x + an + 70, 250, 30, false, L.tramo(t, 0.4, 0.5));
      UJ.rotulo(ctx, lz, 'deseo: nadie lo puede comprobar', x + 20, 302, { tam: 19, peso: 700, color: m.malva, alinear: 'left', visible: L.tramo(t, 0.48, 0.58) });

      // Requisito
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.72), function () {
        L.rectRed(ctx, x, 360, an, 100, 12); L.rellena(ctx, L.tono(m.verde, 0.88), m.verde, 2.5);
        UJ.rotulo(ctx, lz, '«Responde en menos de 2 s con 50 usuarios simultáneos»', x + an / 2, 382, { tam: 21, peso: 700, ancho: an - 40 });
      });
      UJ.sello(ctx, lz, x + an + 70, 410, 30, true, L.tramo(t, 0.74, 0.84));
      UJ.rotulo(ctx, lz, 'requisito: alguien se sienta a comprobarlo', x + 20, 472, { tam: 19, peso: 700, color: m.verde, alinear: 'left', visible: L.tramo(t, 0.82, 0.94) });

      UJ.rotulo(ctx, lz, 'Si no tiene número, no se puede probar.', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
