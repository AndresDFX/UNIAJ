/* Lo que cuesta un mismo cambio segun cuanto se haya construido encima, y por que congelar un
 * requisito incierto sale caro: el cliente descubre lo que quiere al ver el grafico. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('costo-del-cambio', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.45, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      var etiquetas = ['en requisitos', 'con diseño', 'con código', 'con datos migrados'];
      var alto = [14, 60, 130, 230], base = 370, an = 130, paso = 180, x0 = 55;
      UJ.rotulo(ctx, lz, 'El mismo cambio, cada vez más caro', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      L.trazo(ctx, [[30, base], [W - 30, base]], L.tramo(t, 0.02, 0.1), L.tono(m.tinta, 0.5), 3);
      for (var i = 0; i < 4; i++) {
        var x = x0 + i * paso, a0 = 0.08 + i * 0.08;
        UJ.rotulo(ctx, lz, etiquetas[i], x + an / 2, base + 10, { tam: 18, peso: 700, ancho: 170, visible: L.tramo(t, a0, a0 + 0.04) });
        var h = alto[i] * L.tramo(t, a0 + 0.02, a0 + 0.08, 'frena');
        if (h > 0) { L.rectRed(ctx, x, base - h, an, h, 8); L.rellena(ctx, L.mezclaColor(L.tono(A, 0.35), R, i / 3)); }
      }
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.42), function () {
        UJ.rotulo(ctx, lz, 'cambiar una frase', x0 + an / 2, base - alto[0] - 30, { tam: 17, peso: 700, color: A });
        UJ.rotulo(ctx, lz, 'semanas', x0 + 3 * paso + an / 2, base - alto[3] - 30, { tam: 18, peso: 800, color: R });
      });
      // El ejemplo
      UJ.alfa(ctx, L.tramo(t, 0.47, 0.55), function () {
        L.rectRed(ctx, 24, 440, 330, 72, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, '«quiero ver cuántos pacientes atendemos»', 189, 452, { tam: 17, peso: 700, color: A, ancho: 300 });
      });
      UJ.flecha(ctx, lz, 362, 476, 434, 476, m.gris, L.tramo(t, 0.56, 0.62));
      UJ.rotulo(ctx, lz, 'al ver el gráfico:', 611, 410, { tam: 17, peso: 700, color: m.gris, visible: L.tramo(t, 0.58, 0.64) });
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.72), function () {
        L.rectRed(ctx, 446, 440, 330, 72, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, '«por especie, por veterinario, por mes»', 611, 452, { tam: 17, peso: 700, color: R, ancho: 300 });
      });
      UJ.rotulo(ctx, lz, 'Congelar un requisito incierto es congelar una suposición.', W / 2, 570,
                { tam: 22, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
