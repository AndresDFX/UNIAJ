/* Ilustracion: donde estuvo el cuello de botella. En los 40-50 era la maquina; en los 60 pasa a
 * ser coordinar a cientos de personas; en 1968 se propone tratarlo con metodo: ingenieria de
 * software. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-cuello-botella', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      var col = [
        { x: 140, ano: 'Años 40 y 50', c: A, que: 'la máquina', sub: 'programan una persona o unas pocas' },
        { x: 400, ano: 'Años 60', c: R, que: 'coordinar a la gente', sub: 'cientos de personas, años de trabajo' },
        { x: 660, ano: '1968 · OTAN', c: V, que: '«ingeniería de software»', sub: 'método, no talento individual' }
      ];
      for (var i = 0; i < 3; i++) {
        var k = col[i];
        L.rectRed(ctx, k.x - 115, 16, 230, 50, 25); L.rellena(ctx, k.c);
        UJ.rotulo(ctx, lz, k.ano, k.x, 28, { tam: 23, peso: 800, color: m.papel });
        if (i < 2) L.flecha(ctx, k.x + 120, 41, k.x + 140, 41, L.tono(m.tinta, 0.4), 4, 1);
      }
      // Iconos: un chip, una multitud, un documento con metodo
      var x0 = 95, y0 = 105;
      L.rectRed(ctx, x0, y0, 90, 90, 10); L.rellena(ctx, L.tono(A, 0.2), A, 3);
      L.rectRed(ctx, x0 + 22, y0 + 22, 46, 46, 6); L.rellena(ctx, L.tono(A, 0.75));
      for (var p = 0; p < 4; p++) {
        var d = 14 + p * 20;
        L.rectRed(ctx, x0 + d, y0 - 14, 6, 14, 1); L.rellena(ctx, A);
        L.rectRed(ctx, x0 + d, y0 + 90, 6, 14, 1); L.rellena(ctx, A);
        L.rectRed(ctx, x0 - 14, y0 + d, 14, 6, 1); L.rellena(ctx, A);
        L.rectRed(ctx, x0 + 90, y0 + d, 14, 6, 1); L.rellena(ctx, A);
      }
      for (var f = 0; f < 3; f++) for (var c = 0; c < 6; c++) {
        var px = 320 + c * 32, py = 100 + f * 46;
        L.circulo(ctx, px, py, 9); L.rellena(ctx, L.tono(R, 0.3));
        L.rectRed(ctx, px - 11, py + 11, 22, 24, 8); L.rellena(ctx, L.tono(R, 0.55));
      }
      L.objetos.documento(ctx, 615, 92, 90, m, 1);
      // Donde estaba el cuello de botella
      for (var j = 0; j < 3; j++) {
        var q = col[j];
        L.rectRed(ctx, q.x - 125, 260, 250, 130, 14); L.rellena(ctx, L.tono(q.c, 0.9), q.c, 3);
        UJ.rotulo(ctx, lz, j < 2 ? 'Cuello de botella:' : 'Nace el nombre', q.x, 274, { tam: 19, peso: 600 });
        UJ.rotulo(ctx, lz, q.que, q.x, 308, { tam: 23, peso: 800, color: q.c, ancho: 230 });
        UJ.rotulo(ctx, lz, q.sub, q.x, 414, { tam: 19, ancho: 240 });
      }
      // Los tres casos que lo hicieron visible, bajo los años 60
      L.rectRed(ctx, 275, 470, 250, 66, 12); L.rellena(ctx, L.tono(R, 0.85), R, 2);
      UJ.rotulo(ctx, lz, 'SABRE · Apollo · OS/360', 400, 476, { tam: 18, peso: 800, color: R, ancho: 240 });
      UJ.rotulo(ctx, lz, 'tarde y sobre presupuesto', 400, 504, { tam: 17, ancho: 240 });
      L.rectRed(ctx, 20, 556, W - 40, 64, 16); L.rellena(ctx, L.tono(A, 0.9), A, 2);
      UJ.rotulo(ctx, lz, 'La disciplina nace de admitir que el trabajo se hacía mal', W / 2, 574, { tam: 21, peso: 800, color: A, ancho: W - 80 });
    }
  });
})();
