/* Ilustracion: un patron es nombre + problema + forma de resolverlo (no una libreria que se
 * importa), y el catalogo GoF en sus tres familias, con los dos de hoy resaltados. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-que-es-patron', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, S = m.sello || C, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un patrón = nombre + problema + solución', W / 2, 12, { tam: 26, peso: 800, color: A });
      // Las tres partes, con Singleton de ejemplo
      var partes = [
        ['NOMBRE', 'Singleton', 'dicho en una palabra', A],
        ['PROBLEMA', 'una sola instancia', 'que todos alcancen', C],
        ['SOLUCIÓN', 'constructor private', '+ getInstancia()', V]
      ];
      for (var i = 0; i < 3; i++) {
        var x = 24 + i * 262;
        L.rectRed(ctx, x, 62, 228, 112, 14); L.rellena(ctx, L.tono(partes[i][3], 0.9), partes[i][3], 2);
        UJ.rotulo(ctx, lz, partes[i][0], x + 114, 72, { tam: 16, peso: 800, color: partes[i][3] });
        UJ.rotulo(ctx, lz, partes[i][1], x + 114, 100, { tam: 21, peso: 800 });
        UJ.rotulo(ctx, lz, partes[i][2], x + 114, 134, { tam: 16 });
        if (i < 2) UJ.rotulo(ctx, lz, '+', x + 245, 100, { tam: 30, peso: 800, color: L.tono(m.tinta, 0.3) });
      }
      // No es una libreria
      UJ.codigo(ctx, lz, 24, 196, 260, 'import Singleton;', 1, 17);
      UJ.sello(ctx, lz, 314, 213, 20, false, 1);
      UJ.rotulo(ctx, lz, 'no se importa: se aplica al diseño', 350, 202, { tam: 20, peso: 700, alinear: 'left', color: R });
      // Catalogo GoF
      L.rectRed(ctx, 280, 262, 240, 48, 12); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'Catálogo GoF', W / 2, 273, { tam: 22, peso: 800, color: m.papel });
      var fam = [
        ['Creacionales', 'cómo se crean', ['Singleton', 'Factory', 'Builder']],
        ['Estructurales', 'cómo se componen', ['Adapter', 'Decorator', 'Facade']],
        ['De comportamiento', 'cómo se comunican', ['Observer', 'Strategy']]
      ];
      for (var f = 0; f < 3; f++) {
        var cx = 140 + f * 260, x0 = cx - 116;
        L.trazo(ctx, [[W / 2, 310], [W / 2, 326], [cx, 326], [cx, 344]], 1, L.tono(A, 0.3), 3);
        L.rectRed(ctx, x0, 344, 232, 66, 12); L.rellena(ctx, L.tono(A, 0.88), A, 2);
        UJ.rotulo(ctx, lz, fam[f][0], cx, 352, { tam: 19, peso: 800, color: A });
        UJ.rotulo(ctx, lz, fam[f][1], cx, 380, { tam: 16 });
        for (var k = 0; k < fam[f][2].length; k++) {
          var y = 426 + k * 50, hoy = f === 0 && k < 2;
          L.rectRed(ctx, x0 + 16, y, 200, 40, 20);
          L.rellena(ctx, hoy ? S : m.papel, hoy ? L.tono(S, -0.35) : L.tono(m.tinta, 0.6), 2);
          UJ.rotulo(ctx, lz, fam[f][2][k], cx, y + 9, { tam: 18, peso: hoy ? 800 : 500 });
        }
      }
      UJ.rotulo(ctx, lz, 'Hoy: Singleton y Factory, con criterio y no por coleccionarlos.', W / 2, 592,
                { tam: 18, peso: 700, color: L.tono(S, -0.45), ancho: W - 40 });
    }
  });
})();
