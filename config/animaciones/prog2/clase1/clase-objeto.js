/* Clase y objeto: la clase Mascota es el molde; new fabrica dos piezas con sus propios valores;
 * static totalMascotas existe una sola vez, pegado a la clase. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('clase-objeto', {
    duracion: 4.6,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, S = m.sello, W = lz.ancho;
      // La clase (molde)
      UJ.alfa(ctx, L.tramo(t, 0, 0.12), function () {
        L.rectRed(ctx, 30, 70, 280, 230, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
        L.rectRed(ctx, 30, 70, 280, 50, 14); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'class Mascota', 170, 82, { tam: 22, peso: 800, color: m.papel, letra: 'Consolas, monospace' });
        var f = ['String nombre;', 'String especie;', 'int edad;'];
        for (var i = 0; i < 3; i++) UJ.rotulo(ctx, lz, f[i], 54, 140 + i * 40, { tam: 20, alinear: 'left', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'el molde', 170, 262, { tam: 18, peso: 700, color: A });
      });
      UJ.rotulo(ctx, lz, 'La clase declara qué tiene toda mascota', 170, 20, { tam: 18, peso: 600, ancho: 290, color: A, visible: L.tramo(t, 0.1, 0.22) });
      // new -> dos objetos
      var objs = [['Luna', 'Canino', '3'], ['Michi', 'Felino', '5']];
      for (var k = 0; k < 2; k++) {
        var y = 40 + k * 180, t0 = 0.34 + k * 0.12;
        L.flecha(ctx, 314, 185, 470, y + 70, C, 4, L.tramo(t, t0, t0 + 0.08, 'frena'));
        UJ.rotulo(ctx, lz, 'new', k ? 400 : 380, k ? 252 : 105, { tam: 20, peso: 800, color: C, letra: 'Consolas, monospace', visible: L.tramo(t, t0, t0 + 0.04) });
        var b = L.tramo(t, t0 + 0.06, t0 + 0.14, 'frena');
        UJ.alfa(ctx, b, function () {
          L.rectRed(ctx, 476, y, 300, 140, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
          UJ.rotulo(ctx, lz, 'objeto · pieza ' + (k + 1), 626, y + 10, { tam: 17, peso: 700, color: V });
          UJ.rotulo(ctx, lz, 'nombre = "' + objs[k][0] + '"', 496, y + 42, { tam: 18, alinear: 'left', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, 'especie = "' + objs[k][1] + '"', 496, y + 72, { tam: 18, alinear: 'left', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, 'edad = ' + objs[k][2], 496, y + 102, { tam: 18, alinear: 'left', letra: 'Consolas, monospace' });
        });
      }
      UJ.rotulo(ctx, lz, 'Instanciar: cada objeto con sus propios valores', 626, 380, { tam: 18, peso: 600, ancho: 300, color: V, visible: L.tramo(t, 0.56, 0.64) });
      // static: una sola vez, en la clase
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.8, 'frena'), function () {
        L.rectRed(ctx, 30, 316, 280, 92, 14); L.rellena(ctx, L.tono(S, 0.7), L.tono(S, -0.4), 3);
        UJ.rotulo(ctx, lz, 'static int', 170, 326, { tam: 18, peso: 700, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'totalMascotas = 2', 170, 356, { tam: 20, peso: 800, letra: 'Consolas, monospace' });
      });
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.9), function () {
        L.rectRed(ctx, 30, 450, W - 60, 140, 14); L.rellena(ctx, L.tono(S, 0.88), L.tono(S, -0.3), 2);
        UJ.rotulo(ctx, lz, 'static = de la clase, no de cada objeto', W / 2, 466, { tam: 23, peso: 800 });
        UJ.rotulo(ctx, lz, 'Mascota.totalMascotas existe una vez,', W / 2, 510, { tam: 20, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'aunque haya 2 objetos o 2.000.', W / 2, 545, { tam: 20 });
      });
    }
  });
})();
