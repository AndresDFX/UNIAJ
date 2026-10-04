/* Ilustracion: que observar en la demo. El Mascota[3] revienta con la cuarta ficha; el mismo
 * caso con la lista crece solo, size() sube con cada agregar y el id repetido se rechaza. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, R = m.malva, W = lz.ancho;
      var MONO = 'Consolas, monospace';
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });

      // 1. El arreglo fijo
      UJ.rotulo(ctx, lz, '1 · El arreglo fijo', 206, 60, { tam: 20, peso: 800, color: A });
      UJ.codigo(ctx, lz, 24, 96, 352, 'Mascota[] fichero = new Mascota[3];', 1, 15);
      var nom = ['Firulais', 'Michi', 'Rocky'];
      for (var i = 0; i < 3; i++) {
        var x = 30 + i * 88;
        L.rectRed(ctx, x, 144, 84, 56, 8); L.rellena(ctx, L.tono(V, 0.85), A, 2);
        UJ.rotulo(ctx, lz, nom[i], x + 42, 162, { tam: 17, peso: 700 });
        UJ.rotulo(ctx, lz, '[' + i + ']', x + 42, 204, { tam: 15, color: m.gris });
      }
      L.rectRed(ctx, 296, 150, 76, 44, 8); L.rellena(ctx, L.tono(R, 0.85), R, 2);
      UJ.rotulo(ctx, lz, 'Nieve', 334, 162, { tam: 17, peso: 700 });
      UJ.sello(ctx, lz, 366, 148, 16, false, 1);
      UJ.codigo(ctx, lz, 24, 236, 280, 'fichero[3] = new Mascota(…);', 1, 15);
      L.rectRed(ctx, 24, 280, 352, 38, 8); L.rellena(ctx, R);
      L.texto(ctx, 'ArrayIndexOutOfBoundsException', 200, 289, { tam: 17, peso: 700, color: m.papel, alinear: 'center', letra: MONO });
      L.rectRed(ctx, 24, 334, 352, 70, 8); L.rellena(ctx, L.tono(m.gris, 0.9), m.gris, 1);
      L.texto(ctx, 'No cabe la cuarta mascota:', 38, 344, { tam: 16, color: m.tinta, letra: MONO });
      L.texto(ctx, 'fichero.length = 3', 38, 372, { tam: 16, color: m.tinta, letra: MONO });
      UJ.rotulo(ctx, lz, 'length = 3 y no crece', 206, 424, { tam: 22, peso: 800, color: R });

      // 2. El mismo caso con la lista
      UJ.rotulo(ctx, lz, '2 · El mismo caso con ArrayList', 594, 60, { tam: 20, peso: 800, color: V });
      UJ.codigo(ctx, lz, 424, 96, 352, 'registro.agregar(m);', 1, 15);
      L.rectRed(ctx, 424, 140, 352, 34, 8); L.rellena(ctx, V);
      UJ.rotulo(ctx, lz, 'agregar…', 440, 146, { tam: 17, peso: 700, color: m.papel, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'size() después', 760, 146, { tam: 17, peso: 700, color: m.papel, alinear: 'right' });
      var filas = [['Firulais', '1'], ['Michi', '2'], ['Rocky', '3'], ['Nieve', '4'], ['Toby', '5'], ['M-001 otra vez', '5']];
      for (var k = 0; k < filas.length; k++) {
        var fy = 174 + k * 36, mala = k === filas.length - 1;
        L.rectRed(ctx, 424, fy, 352, 36, 0);
        L.rellena(ctx, mala ? L.tono(R, 0.88) : (k % 2 ? L.tono(V, 0.92) : m.papel), L.tono(V, 0.5), 1);
        L.texto(ctx, filas[k][0], 440, fy + 8, { tam: 17, peso: 600, color: mala ? R : m.tinta, letra: MONO });
        L.texto(ctx, filas[k][1], 744, fy + 7, { tam: 19, peso: 800, color: mala ? R : V, alinear: 'right', letra: MONO });
      }
      UJ.sello(ctx, lz, 690, 174 + 5 * 36 + 18, 13, false, 1);
      UJ.rotulo(ctx, lz, 'ID repetido: se rechaza', 594, 392, { tam: 16, peso: 700, color: R });
      UJ.rotulo(ctx, lz, 'size() = 5: creció sola', 594, 424, { tam: 22, peso: 800, color: V });

      // Lo que se lleva
      L.rectRed(ctx, 24, 486, W - 48, 120, 14); L.rellena(ctx, L.tono(A, 0.92), A, 2);
      UJ.rotulo(ctx, lz, 'Mismo caso, dos resultados:', W / 2, 502, { tam: 21, peso: 800, ancho: W - 80 });
      UJ.rotulo(ctx, lz, 'el arreglo revienta en la cuarta ficha; la lista crece', W / 2, 540, { tam: 19, ancho: W - 80 });
      UJ.rotulo(ctx, lz, 'y size() cuenta lo que guarda.', W / 2, 570, { tam: 19, ancho: W - 80 });
    }
  });
})();
