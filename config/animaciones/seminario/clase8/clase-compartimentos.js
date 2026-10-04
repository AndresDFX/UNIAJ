/* La clase Mascota se arma en sus tres compartimentos con su notación anotada; las clases
 * técnicas (MascotaDAO, ConexionBD) no entran en el modelo de dominio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('clase-compartimentos', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.32, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho, MONO = 'Consolas, monospace';
      UJ.rotulo(ctx, lz, 'La clase: tres compartimentos', W / 2, 20, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var x = 240, an = 300, y = 76;
      var a1 = L.tramo(t, 0.04, 0.12), a2 = L.tramo(t, 0.12, 0.28), a3 = L.tramo(t, 0.36, 0.44);
      // Nombre
      UJ.alfa(ctx, a1, function () {
        L.rectRed(ctx, x, y, an, 50, 0); L.rellena(ctx, L.tono(A, 0.8), A, 3);
        UJ.rotulo(ctx, lz, 'Mascota', x + an / 2, y + 12, { tam: 24, peso: 800, color: L.tono(A, -0.3) });
      });
      // Atributos
      var attrs = ['-codigo: String', '-nombre: String', '-fechaNacimiento: Date'];
      UJ.alfa(ctx, a1, function () { L.rectRed(ctx, x, y + 50, an, 120, 0); L.rellena(ctx, m.papel, A, 3); });
      for (var i = 0; i < 3; i++) {
        UJ.alfa(ctx, Math.max(0, Math.min(1, a2 * 3 - i)), function () {
          L.texto(ctx, attrs[i], x + 14, y + 62 + i * 36, { tam: 20, peso: 500, color: m.tinta, letra: MONO });
        });
      }
      // Metodo
      UJ.alfa(ctx, a1, function () { L.rectRed(ctx, x, y + 170, an, 52, 0); L.rellena(ctx, m.papel, A, 3); });
      UJ.alfa(ctx, a3, function () {
        L.texto(ctx, '+calcularEdad(): int', x + 14, y + 184, { tam: 20, peso: 500, color: m.tinta, letra: MONO });
      });
      // Anotaciones
      var C = L.tono(m.sello, -0.4);
      function nota(txt, tx, ty, ax, ay, bx, by, a, al) {
        UJ.alfa(ctx, a, function () {
          L.texto(ctx, txt, tx, ty, { tam: 18, peso: 700, color: C, alinear: al || 'left', letra: lz.letra });
        });
        if (a > 0) UJ.flecha(ctx, lz, ax, ay, bx, by, C, a, null, { grosor: 2.5 });
      }
      nota('nombre en singular', 580, y + 14, 574, y + 25, 545, y + 25, L.tramo(t, 0.46, 0.52));
      nota('- privado', 196, y + 70, 200, y + 80, 250, y + 74, L.tramo(t, 0.5, 0.56), 'right');
      nota('+ público', 196, y + 184, 200, y + 194, 250, y + 196, L.tramo(t, 0.52, 0.58), 'right');
      nota('tipo', 580, y + 132, 574, y + 143, 508, y + 143, L.tramo(t, 0.56, 0.62));
      nota('retorno', 580, y + 184, 574, y + 195, 482, y + 195, L.tramo(t, 0.6, 0.66));
      // Lo que no es del dominio
      var d = L.tramo(t, 0.72, 0.82), s = L.tramo(t, 0.82, 0.9);
      UJ.caja(ctx, lz, 150, 360, 220, 64, 'MascotaDAO', null, m.gris, d);
      UJ.caja(ctx, lz, 430, 360, 220, 64, 'ConexionBD', null, m.gris, d);
      UJ.sello(ctx, lz, 150 + 220, 360, 18, false, s);
      UJ.sello(ctx, lz, 430 + 220, 360, 18, false, s);
      UJ.rotulo(ctx, lz, 'no son del dominio', W / 2, 440, { tam: 20, peso: 800, color: R, visible: s });
      UJ.rotulo(ctx, lz, 'Modelo de dominio: solo conceptos del negocio', W / 2, 545,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
