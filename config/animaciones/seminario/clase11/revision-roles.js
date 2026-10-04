/* La revision entre pares: tres roles con su regla, la ficha de un hallazgo y lo que no es un
 * hallazgo (una opinion). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('revision-roles', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.34, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Revisión entre pares', W / 2, 18, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var roles = [['Autor', 'escucha en silencio'], ['Revisor', 'solo hechos observables'], ['Moderador', 'tiempo y registro']];
      for (var i = 0; i < 3; i++) {
        var x = 30 + i * 255;
        UJ.tarjeta(ctx, lz, x, 66, 230, roles[i][0], [roles[i][1]], i === 1 ? m.acento : A,
          L.tramo(t, 0.04 + i * 0.08, 0.12 + i * 0.08), undefined, { tam: 18, alto: 90 });
      }

      // Ficha del hallazgo
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.42), function () {
        UJ.rotulo(ctx, lz, 'Ficha de hallazgo', W / 2, 184, { tam: 21, peso: 800, color: A });
      });
      var campos = [['Ubicación', 'diagrama de clases'], ['Inconsistencia', 'Consulta no se relaciona con Veterinario'], ['Severidad', 'mayor']];
      for (var k = 0; k < 3; k++) {
        (function (k) {
          var y = 222 + k * 52;
          UJ.alfa(ctx, L.tramo(t, 0.4 + k * 0.08, 0.46 + k * 0.08), function () {
            L.rectRed(ctx, 60, y, 190, 46, 0); L.rellena(ctx, L.tono(A, 0.82), A, 1.5);
            L.rectRed(ctx, 250, y, 490, 46, 0); L.rellena(ctx, m.papel, A, 1.5);
            UJ.rotulo(ctx, lz, campos[k][0], 76, y + 12, { tam: 18, peso: 800, color: L.tono(A, -0.2), alinear: 'left' });
            UJ.rotulo(ctx, lz, campos[k][1], 266, y + 12, { tam: 18, peso: 600, alinear: 'left', ancho: 460,
              color: k === 2 ? m.malva : m.tinta });
          });
        })(k);
      }

      // Una opinion no es hallazgo
      var a3 = L.tramo(t, 0.74, 0.82);
      UJ.alfa(ctx, a3, function () {
        L.rectRed(ctx, 200, 420, 260, 64, 32); L.rellena(ctx, L.tono(m.gris, 0.86), m.gris, 2);
        UJ.rotulo(ctx, lz, '«No me gusta»', 330, 438, { tam: 22, peso: 700, color: m.tinta });
      });
      UJ.sello(ctx, lz, 500, 452, 28, false, L.tramo(t, 0.82, 0.88));
      UJ.rotulo(ctx, lz, 'opinión, no hallazgo', 540, 440, { tam: 20, peso: 800, color: m.malva, alinear: 'left', visible: L.tramo(t, 0.86, 0.94) });
      UJ.rotulo(ctx, lz, 'Un hallazgo dice dónde, qué y cuánto pesa', W / 2, 560,
        { tam: 22, peso: 700, color: A, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
