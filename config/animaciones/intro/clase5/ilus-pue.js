/* Ilustracion: el PUE con numeros. 1.600 kWh totales, 1.000 llegan a los servidores. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-pue', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', V = m.verde || A, S = m.sello || m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Total del día: 1.600 kWh', W / 2, 20, { tam: 26, peso: 800, color: A });
      L.rectRed(ctx, 40, 70, 450, 120, 8); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'servidores: 1.000 kWh', 265, 96, { tam: 24, peso: 800, color: m.papel });
      UJ.rotulo(ctx, lz, 'computan', 265, 136, { tam: 20, color: m.papel });
      L.rectRed(ctx, 490, 70, 270, 120, 8); L.rellena(ctx, L.tono(R, 0.75), R, 2);
      UJ.rotulo(ctx, lz, '600 kWh', 625, 86, { tam: 24, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'enfriar, iluminar, pérdidas', 625, 122, { tam: 18, ancho: 250 });
      L.rectRed(ctx, 110, 220, 580, 90, 16); L.rellena(ctx, L.tono(S, 0.55), L.tono(S, -0.35), 2);
      UJ.rotulo(ctx, lz, 'PUE = 1.600 ÷ 1.000 = 1,6', W / 2, 242, { tam: 34, peso: 800 });
      // Escala 1,0 a 2,0
      L.rectRed(ctx, 100, 420, 600, 8, 4); L.rellena(ctx, L.tono(m.tinta, 0.6));
      var px = 100 + 600 * 0.6;
      L.circulo(ctx, 100, 424, 14); L.rellena(ctx, V);
      L.circulo(ctx, 700, 424, 14); L.rellena(ctx, R);
      ctx.beginPath(); ctx.moveTo(px, 410); ctx.lineTo(px - 16, 380); ctx.lineTo(px + 16, 380); ctx.closePath(); ctx.fillStyle = A; ctx.fill();
      UJ.rotulo(ctx, lz, '1,6 · este centro', px, 346, { tam: 20, peso: 800, color: A });
      UJ.rotulo(ctx, lz, '1,0 · perfecto: todo computa', 160, 450, { tam: 19, peso: 700, color: V, ancho: 260 });
      UJ.rotulo(ctx, lz, '2,0 · la mitad no computa', 650, 450, { tam: 19, peso: 700, color: R, ancho: 260 });
      UJ.rotulo(ctx, lz, 'Más bajo = desperdicia menos', W / 2, 560, { tam: 24, peso: 800 });
    }
  });
})();
