/* Deuda técnica: una decisión de dos minutos que se salta en la semana 1 se cobra con
 * intereses en la semana 4, cuando dos documentos ya se contradicen. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('deuda-intereses', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, G = m.gris, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'La deuda técnica cobra intereses', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });

      // Semana 1
      UJ.pildora(ctx, lz, 30, 100, 'Semana 1', A, L.tramo(t, 0.04, 0.1), { lleno: true, tam: 18 });
      var gris = L.tramo(t, 0.2, 0.28);
      var c1 = L.mezclaColor(A, G, gris);
      UJ.alfa(ctx, L.tramo(t, 0.06, 0.14), function () {
        ctx.save(); ctx.globalAlpha *= 1 - 0.45 * gris;
        L.rectRed(ctx, 180, 80, 420, 86, 12); L.rellena(ctx, L.tono(c1, 0.9), c1, 2.5);
        UJ.rotulo(ctx, lz, '¿Puede existir una Mascota sin Dueño?', 390, 94, { tam: 20, peso: 700, ancho: 400 });
        UJ.rotulo(ctx, lz, 'decidirlo: 2 minutos', 390, 128, { tam: 18, peso: 600, color: L.tono(c1, -0.2) });
        ctx.restore();
      });
      UJ.alfa(ctx, L.tramo(t, 0.22, 0.28), function () {
        UJ.pildora(ctx, lz, 690, 106, 'se salta', G, 1, { centrar: true, tam: 18, lleno: true });
      });

      // Semana 4: contradiccion
      UJ.pildora(ctx, lz, 30, 230, 'Semana 4', R, L.tramo(t, 0.32, 0.38), { lleno: true, tam: 18 });
      function doc(x, tit, txt, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, 210, 260, 104, 10); L.rellena(ctx, m.papel, R, 2.5);
          UJ.rotulo(ctx, lz, tit, x + 130, 222, { tam: 19, peso: 800, color: R });
          UJ.rotulo(ctx, lz, txt, x + 130, 254, { tam: 18, peso: 600, ancho: 236 });
        });
      }
      doc(180, 'Pantalla', 'pide el dueño primero', L.tramo(t, 0.36, 0.44));
      doc(510, 'Caso de uso', 'la mascota se registra sola', L.tramo(t, 0.44, 0.52));
      UJ.rayo(ctx, 472, 226, 70, m.sello, L.tramo(t, 0.52, 0.58));
      UJ.rotulo(ctx, lz, 'se contradicen', 475, 322, { tam: 18, peso: 700, color: R, visible: L.tramo(t, 0.54, 0.6) });

      // Factura de intereses
      var items = ['decidir (lo mismo de antes)', 'ajustar 2 documentos', 'avisar al equipo', 'rehacer un wireframe'];
      var fa = L.tramo(t, 0.64, 0.7);
      UJ.tarjeta(ctx, lz, 180, 360, 440, 'Factura de intereses', items, R, fa, L.tramo(t, 0.68, 0.88) * 4, { tam: 18 });

      UJ.rotulo(ctx, lz, 'El interés de una decisión que costaba dos minutos.', W / 2, 575,
                { tam: 22, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
