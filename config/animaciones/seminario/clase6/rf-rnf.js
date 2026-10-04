/* Una misma frase de la clínica se parte en un requisito funcional y uno no funcional, y cada
 * uno se prueba distinto: el RF haciendo clic, el RNF intentando lo prohibido. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('rf-rnf', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.25, 0.65, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.rectRed(ctx, 130, 28, 540, 70, 14); L.rellena(ctx, L.tono(m.sello, 0.82), L.tono(m.sello, -0.2), 2.5);
        UJ.rotulo(ctx, lz, 'La necesidad', W / 2, 36, { tam: 17, peso: 700, color: L.tono(m.tinta, 0.3) });
        UJ.rotulo(ctx, lz, '«que la auxiliar pueda agendar sin llamarme»', W / 2, 60, { tam: 21, peso: 700, color: m.tinta, ancho: 520 });
      });
      UJ.flecha(ctx, lz, 340, 102, 210, 162, A, L.tramo(t, 0.27, 0.36));
      UJ.flecha(ctx, lz, 460, 102, 590, 162, R, L.tramo(t, 0.27, 0.36));
      function ficha(x, c, cod, fam, texto, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, 168, 360, 150, 14); L.rellena(ctx, L.tono(c, 0.9), c, 3);
          UJ.pildora(ctx, lz, x + 16, 182, cod, c, 1, { tam: 18, lleno: true });
          UJ.rotulo(ctx, lz, fam, x + 344, 190, { tam: 17, peso: 700, color: L.tono(c, -0.2), alinear: 'right' });
          UJ.rotulo(ctx, lz, texto, x + 180, 238, { tam: 19, peso: 600, color: m.tinta, ancho: 320 });
        });
      }
      ficha(26, A, 'RF-05', 'funcional', 'Registrar una cita: mascota, veterinario, fecha y hora', L.tramo(t, 0.36, 0.46));
      ficha(414, R, 'RNF-02', 'no funcional', 'Dos perfiles: la auxiliar crea citas pero no ve el diagnóstico', L.tramo(t, 0.48, 0.58));
      // Cómo se prueba cada uno
      var p1 = L.tramo(t, 0.68, 0.78), p2 = L.tramo(t, 0.82, 0.92);
      UJ.alfa(ctx, p1, function () {
        L.rectRed(ctx, 26, 360, 360, 120, 14); L.rellena(ctx, m.papel, A, 2);
        L.rectRed(ctx, 50, 390, 120, 40, 10); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'Guardar', 110, 400, { tam: 18, peso: 700, color: m.papel });
        ctx.beginPath(); ctx.moveTo(150, 415); ctx.lineTo(150, 445); ctx.lineTo(158, 437); ctx.lineTo(165, 450); ctx.lineTo(170, 447); ctx.lineTo(163, 434); ctx.lineTo(174, 433); ctx.closePath();
        L.rellena(ctx, m.papel, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'se prueba haciendo clic', 290, 400, { tam: 19, peso: 700, color: A, ancho: 170 });
      });
      UJ.alfa(ctx, p2, function () {
        L.rectRed(ctx, 414, 360, 360, 120, 14); L.rellena(ctx, m.papel, R, 2);
        UJ.rotulo(ctx, lz, 'auxiliar abre el diagnóstico', 520, 378, { tam: 17, peso: 600, color: m.tinta, ancho: 180 });
        UJ.sello(ctx, lz, 520, 446, 20, false, 1);
        UJ.rotulo(ctx, lz, 'se prueba intentando lo prohibido', 680, 390, { tam: 19, peso: 700, color: R, ancho: 170 });
      });
    }
  });
})();
