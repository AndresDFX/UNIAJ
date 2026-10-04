/* Ilustracion: que observar en la demo — dos ventanas abiertas a la vez; la mascota registrada en
 * la primera aparece en la segunda, porque las dos usan la unica instancia del repositorio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, S = m.sello || C, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });
      function ventana(x, y, an, al, titulo, color) {
        L.rectRed(ctx, x, y, an, al, 12); L.rellena(ctx, m.papel, color, 3);
        L.rectRed(ctx, x, y, an, 44, 12); L.rellena(ctx, color);
        ctx.fillStyle = color; ctx.fillRect(x, y + 30, an, 14);
        UJ.rotulo(ctx, lz, titulo, x + 16, y + 11, { tam: 19, peso: 800, alinear: 'left', color: m.papel });
      }
      function paso(n, x, y, frase, color) {
        L.circulo(ctx, x + 16, y + 14, 16); L.rellena(ctx, color);
        UJ.rotulo(ctx, lz, String(n), x + 16, y + 3, { tam: 20, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, frase, x + 42, y + 2, { tam: 19, peso: 700, alinear: 'left', color: color, ancho: 300 });
      }
      // Ventana 1: registro
      paso(1, 24, 60, 'Se registra Luna aquí', A);
      ventana(24, 100, 352, 250, 'Registro de mascotas', A);
      var campos = [['Nombre', 'Luna'], ['Especie', 'Gato']];
      for (var i = 0; i < 2; i++) {
        var y = 162 + i * 56;
        UJ.rotulo(ctx, lz, campos[i][0], 44, y + 8, { tam: 17, peso: 600, alinear: 'left' });
        L.rectRed(ctx, 140, y, 214, 38, 6); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.55), 2);
        L.texto(ctx, campos[i][1], 152, y + 9, { tam: 18, peso: 500, color: m.tinta, letra: 'Consolas, monospace' });
      }
      L.rectRed(ctx, 214, 284, 140, 42, 10); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'Registrar', 284, 294, { tam: 18, peso: 800, color: m.papel });
      // Ventana 2: citas
      paso(2, 424, 60, 'y aparece aquí, sin recargar nada', V);
      ventana(424, 100, 352, 250, 'Ventana de citas', C);
      UJ.tabla(ctx, lz, 444, 160, 312, 'mascotas', ['Michi', 'Rocky', 'Luna'], 3, C, 2);
      L.flecha(ctx, 380, 225, 420, 225, V, 4, 1);
      // La unica instancia
      L.flecha(ctx, 200, 354, 330, 420, A, 3, 1);
      L.flecha(ctx, 600, 354, 470, 420, C, 3, 1);
      L.rectRed(ctx, 200, 424, 400, 86, 16); L.rellena(ctx, L.tono(V, 0.88), V, 3);
      UJ.rotulo(ctx, lz, 'una sola instancia', W / 2, 436, { tam: 20, peso: 800, color: V });
      L.texto(ctx, 'RepositorioClinica.getInstancia()', W / 2, 470, { tam: 18, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
      UJ.rotulo(ctx, lz, 'Las dos ventanas leen y escriben en el mismo objeto.', W / 2, 534, { tam: 20, peso: 700, ancho: W - 40 });
      UJ.rotulo(ctx, lz, 'Comprobación: el mismo identityHashCode en las dos.', W / 2, 574, { tam: 17, peso: 600, color: L.tono(S, -0.45), ancho: W - 40 });
    }
  });
})();
