/* Ilustracion: dos datos locales. La matriz electrica (hidraulica; con El Nino entran las
 * termicas) y los residuos electronicos (Ley 1672 de 2013). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-colombia', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, S = m.sello || C, W = lz.ancho;
      function embalse(x, y, nivel) {
        L.rectRed(ctx, x, y, 90, 90, 8); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.4), 3);
        L.rectRed(ctx, x + 3, y + 90 - 84 * nivel, 84, 84 * nivel - 3, 4); L.rellena(ctx, L.tono(C, 0.3));
      }
      L.rectRed(ctx, 20, 16, 370, 440, 16); L.rellena(ctx, L.tono(A, 0.94), A, 2);
      UJ.rotulo(ctx, lz, '1 · La electricidad', 205, 30, { tam: 23, peso: 800, color: A });
      embalse(40, 90, 0.9);
      UJ.rotulo(ctx, lz, 'casi todo hidráulica: menos emisiones por kWh', 255, 92, { tam: 18, peso: 700, color: V, ancho: 230 });
      embalse(40, 260, 0.25);
      UJ.rotulo(ctx, lz, 'El Niño: entran las térmicas', 255, 250, { tam: 18, peso: 700, color: R, ancho: 230 });
      UJ.rotulo(ctx, lz, 'la misma app emite más, sin cambiar código', 255, 304, { tam: 17, ancho: 230 });
      UJ.rotulo(ctx, lz, 'Se usa el factor local', 205, 400, { tam: 20, peso: 800 });
      L.rectRed(ctx, 410, 16, 370, 440, 16); L.rellena(ctx, L.tono(V, 0.94), V, 2);
      UJ.rotulo(ctx, lz, '2 · Residuos (RAEE)', 595, 30, { tam: 23, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'Ley 1672 de 2013', 595, 76, { tam: 21, peso: 800 });
      UJ.caja(ctx, lz, 430, 116, 330, 80, 'Productor', 'ofrece puntos de recolección', V);
      UJ.caja(ctx, lz, 430, 210, 330, 80, 'Usuario', 'debe llevarlos allí', V);
      UJ.rotulo(ctx, lz, 'En el mundo:', 595, 310, { tam: 19, peso: 700 });
      L.rectRed(ctx, 430, 344, 90, 50, 6); L.rellena(ctx, V);
      L.rectRed(ctx, 520, 344, 240, 50, 6); L.rellena(ctx, L.tono(R, 0.7));
      UJ.rotulo(ctx, lz, 'la mayor parte no se recoge', 640, 404, { tam: 17, peso: 700, color: R, ancho: 240 });
      L.rectRed(ctx, 20, 476, W - 40, 144, 16); L.rellena(ctx, L.tono(S, 0.55), L.tono(S, -0.35), 2);
      UJ.rotulo(ctx, lz, 'La decisión más fuerte de su proyecto:', W / 2, 490, { tam: 21, peso: 800 });
      UJ.rotulo(ctx, lz, 'no obligar a cambiar de aparato', W / 2, 530, { tam: 22, peso: 700 });
      UJ.rotulo(ctx, lz, 'no mover datos que no hacen falta', W / 2, 570, { tam: 22, peso: 700 });
    }
  });
})();
