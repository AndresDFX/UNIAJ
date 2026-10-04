/* Ilustracion: el mismo servidor de 64 GB repartido de dos maneras. Con virtualizacion, unas
 * decenas de maquinas virtuales de 2 GB, cada una con su SO invitado; con contenedores, cientos
 * de procesos aislados sobre un solo kernel. Mismo problema (aprovechar el servidor), otro costo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-de-donde-viene', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, S = m.sello || C, R = m.malva || '#A02030',
          G = m.gris || '#666666', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un servidor de 64 GB, dos formas de repartirlo', W / 2, 14, { tam: 24, peso: 800, color: A });

      // Leyenda
      L.rectRed(ctx, 230, 62, 22, 22, 4); L.rellena(ctx, R);
      UJ.rotulo(ctx, lz, 'SO invitado', 260, 62, { tam: 16, alinear: 'left' });
      L.rectRed(ctx, 420, 62, 22, 22, 4); L.rellena(ctx, S, L.tono(m.tinta, 0.5), 1);
      UJ.rotulo(ctx, lz, 'aplicación', 450, 62, { tam: 16, alinear: 'left' });

      function columna(x0, titulo, base, cuenta, notas) {
        L.rectRed(ctx, x0, 100, 364, 400, 16); L.rellena(ctx, L.tono(A, 0.95), L.tono(A, 0.6), 2);
        UJ.rotulo(ctx, lz, titulo, x0 + 182, 112, { tam: 22, peso: 800, color: A });
        L.rectRed(ctx, x0 + 14, 368, 336, 40, 10); L.rellena(ctx, C);
        UJ.rotulo(ctx, lz, base, x0 + 182, 378, { tam: 17, peso: 700, color: m.papel });
        L.rectRed(ctx, x0 + 14, 414, 336, 40, 10); L.rellena(ctx, G);
        UJ.rotulo(ctx, lz, 'Hardware · 64 GB de memoria', x0 + 182, 424, { tam: 17, peso: 700, color: m.papel });
        UJ.rotulo(ctx, lz, cuenta, x0 + 182, 464, { tam: 19, peso: 800, color: A });
        for (var k = 0; k < notas.length; k++) {
          UJ.escena(ctx, 1, lz, [{ tipo: 'chip', x: x0 + 182, y: 516 + k * 40, t: notas[k], color: k ? 'acento' : 'accion', tam: 16 }]);
        }
      }

      // Virtualizacion: 30 maquinas virtuales de 2 GB, cada una con su SO
      columna(24, 'Virtualización', 'Hipervisor', 'unas decenas de VM de 2 GB', ['cada VM con su SO', 'aislamiento fuerte · pesa GB']);
      for (var i = 0; i < 30; i++) {
        var cx = 24 + 22 + (i % 6) * 54, cy = 152 + Math.floor(i / 6) * 42;
        L.rectRed(ctx, cx, cy, 48, 36, 5); L.rellena(ctx, S, L.tono(m.tinta, 0.5), 1);
        L.rectRed(ctx, cx, cy + 20, 48, 16, 4); L.rellena(ctx, R);
      }

      // Contenedores: cientos de procesos sobre un kernel
      columna(412, 'Contenedores', 'SO anfitrión · un solo kernel', 'cientos de contenedores', ['sin SO propio', 'kernel compartido · pesa MB']);
      for (var j = 0; j < 240; j++) {
        var px = 412 + 22 + (j % 20) * 16.2, py = 152 + Math.floor(j / 20) * 17.5;
        L.rectRed(ctx, px, py, 13, 14, 2); L.rellena(ctx, S, L.tono(m.tinta, 0.5), 0.8);
      }

      UJ.rotulo(ctx, lz, 'Mismo problema: aprovechar mejor el servidor.', W / 2, 600, { tam: 19, peso: 700 });
    }
  });
})();
