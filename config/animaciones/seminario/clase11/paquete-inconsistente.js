/* Un paquete de diseño puede tener cada documento correcto por separado y aun asi fallar como
 * conjunto: el requisito que ningun caso de uso ni ninguna clase recoge. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('paquete-inconsistente', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Tres documentos, un solo paquete', W / 2, 22, { tam: 26, peso: 800, color: m.accion, visible: L.tramo(t, 0, 0.06) });
      var docs = [
        ['Requisitos', ['RF-07', 'recordatorio de cita']],
        ['Casos de uso', ['(ningún caso de', 'recordatorio)']],
        ['Clases', ['(ninguna clase', 'Notificación)']]
      ];
      var xs = [30, 290, 550], an = 220, y = 90;
      for (var i = 0; i < 3; i++) {
        UJ.tarjeta(ctx, lz, xs[i], y, an, docs[i][0], docs[i][1], m.accion, L.tramo(t, 0.04 + i * 0.07, 0.1 + i * 0.07), undefined, { tam: 19, alto: 130 });
        UJ.sello(ctx, lz, xs[i] + an / 2, 262, 26, true, L.tramo(t, 0.26 + i * 0.03, 0.32 + i * 0.03));
      }
      UJ.rotulo(ctx, lz, 'cada uno, revisado solo: correcto', W / 2, 302, { tam: 19, peso: 700, color: m.verde, visible: L.tramo(t, 0.32, 0.4) });

      // Los enlaces entre documentos no cierran
      var yL = 360, p = L.tramo(t, 0.44, 0.56);
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.46), function () {
        L.circulo(ctx, 140, yL, 8); L.rellena(ctx, m.accion);
        L.circulo(ctx, 400, yL, 8); L.rellena(ctx, m.gris);
        L.circulo(ctx, 660, yL, 8); L.rellena(ctx, m.gris);
      });
      UJ.linea(ctx, 150, yL, 250, yL, m.malva, 3, p);
      UJ.linea(ctx, 410, yL, 510, yL, m.malva, 3, p);
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.62), function () {
        UJ.rayo(ctx, 262, yL - 22, 44, m.malva, 1);
        UJ.rayo(ctx, 522, yL - 22, 44, m.malva, 1);
        UJ.rotulo(ctx, lz, '¿qué caso lo cumple?', 270, yL + 30, { tam: 17, peso: 600, color: m.malva });
        UJ.rotulo(ctx, lz, '¿qué clase lo envía?', 530, yL + 30, { tam: 17, peso: 600, color: m.malva });
      });

      UJ.sello(ctx, lz, W / 2, 470, 40, false, L.tramo(t, 0.76, 0.84));
      UJ.rotulo(ctx, lz, 'El conjunto falla', W / 2, 525, { tam: 24, peso: 800, color: m.malva, visible: L.tramo(t, 0.82, 0.9) });
      UJ.rotulo(ctx, lz, 'Se audita el paquete, no cada documento', W / 2, 570,
        { tam: 21, peso: 700, color: m.tinta, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
