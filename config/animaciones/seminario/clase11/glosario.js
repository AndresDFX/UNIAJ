/* El glosario canonico: cuatro nombres para lo mismo se reducen a uno, y dos palabras que
 * parecen sinonimos (cita y consulta) quedan separadas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('glosario', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.28, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un término, un significado', W / 2, 20, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var pal = [['Dueño', 'en Requisitos'], ['Propietario', 'en Casos de uso'], ['Cliente', 'en Clases'], ['Responsable', 'en Pantallas']];
      var x = 40, an = 250, al = 58;
      for (var i = 0; i < 4; i++) {
        var y = 76 + i * 72, canon = i === 1;
        var a = L.tramo(t, 0.04 + i * 0.05, 0.1 + i * 0.05);
        var gris = !canon && t >= 0.5;
        (function (y, canon, gris, w) {
          UJ.alfa(ctx, a, function () {
            var c = gris ? m.gris : A;
            L.rectRed(ctx, x, y, an, al, 12); L.rellena(ctx, L.tono(c, 0.9), c, 2);
            UJ.rotulo(ctx, lz, w[0], x + 16, y + 6, { tam: 21, peso: 800, color: c, alinear: 'left' });
            UJ.rotulo(ctx, lz, w[1], x + 16, y + 33, { tam: 16, peso: 500, color: m.tinta, alinear: 'left' });
            if (gris) UJ.rayar(ctx, x + 12, y + 20, UJ.medir(ctx, lz, w[0], 21, 800) + 8, m.malva, L.tramo(t, 0.5, 0.58));
          });
        })(y, canon, gris, pal[i]);
        UJ.flecha(ctx, lz, x + an + 6, y + al / 2, 466, 200, canon ? m.verde : m.gris, L.tramo(t, 0.32 + i * 0.03, 0.42 + i * 0.03), null, { grosor: 2.5 });
      }
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () {
        L.rectRed(ctx, 470, 160, 290, 80, 14); L.rellena(ctx, L.tono(m.verde, 0.86), m.verde, 3);
        UJ.rotulo(ctx, lz, 'Propietario', 615, 170, { tam: 24, peso: 800, color: L.tono(m.verde, -0.3) });
        UJ.rotulo(ctx, lz, 'término canónico', 615, 204, { tam: 17, peso: 600, color: m.tinta });
      });
      UJ.rotulo(ctx, lz, 'los demás: prohibidos', 615, 262, { tam: 19, peso: 700, color: m.malva, visible: L.tramo(t, 0.54, 0.62) });

      // Pareja peligrosa
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.72), function () {
        UJ.linea(ctx, 40, 382, W - 40, 382, L.tono(m.gris, 0.5), 2, 1, true);
        UJ.rotulo(ctx, lz, 'Parecen lo mismo y no lo son', W / 2, 396, { tam: 20, peso: 700, color: m.malva });
      });
      function def(xx, t1, t2, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, xx, 440, 320, 84, 14); L.rellena(ctx, L.tono(m.acento, 0.88), m.acento, 2.5);
          UJ.rotulo(ctx, lz, t1, xx + 160, 452, { tam: 22, peso: 800, color: L.tono(m.acento, -0.35) });
          UJ.rotulo(ctx, lz, t2, xx + 160, 486, { tam: 18, peso: 600, color: m.tinta, ancho: 300 });
        });
      }
      def(40, 'Cita', 'reserva futura', L.tramo(t, 0.72, 0.8));
      def(440, 'Consulta', 'atención ya realizada', L.tramo(t, 0.78, 0.86));
      UJ.rotulo(ctx, lz, '≠', W / 2, 458, { tam: 44, peso: 800, color: m.malva, visible: L.tramo(t, 0.86, 0.92) });
      UJ.rotulo(ctx, lz, 'El glosario manda sobre todos los documentos', W / 2, 562,
        { tam: 21, peso: 700, color: m.tinta, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
