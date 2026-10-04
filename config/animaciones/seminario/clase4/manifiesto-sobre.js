/* Los cuatro valores del manifiesto ágil: lo de la izquierda pesa más, pero lo de la derecha
 * sigue visible y sigue valiendo. «Sobre», no «en vez de». */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('manifiesto-sobre', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      var filas = [
        ['Individuos e interacciones', 'procesos y herramientas'],
        ['Software funcionando', 'documentación exhaustiva'],
        ['Colaboración con el cliente', 'negociación contractual'],
        ['Respuesta ante el cambio', 'seguir un plan']
      ];
      UJ.rotulo(ctx, lz, 'El manifiesto ágil (2001)', W / 2, 26, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.08) });
      UJ.alfa(ctx, L.tramo(t, 0.05, 0.15), function () {
        UJ.rotulo(ctx, lz, 'se valora más', 188, 88, { tam: 18, peso: 700, color: A });
        UJ.rotulo(ctx, lz, 'sigue valiendo', 612, 88, { tam: 18, peso: 700, color: m.gris });
      });
      for (var i = 0; i < 4; i++) {
        var y = 130 + i * 98;
        var a = L.tramo(t, 0.1 + i * 0.045, 0.18 + i * 0.045);
        var b = L.tramo(t, 0.34 + i * 0.09, 0.44 + i * 0.09);
        (function (i, y, a, b) {
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, 26, y, 324, 70, 12); L.rellena(ctx, L.tono(A, 0.86), A, 3);
            UJ.rotulo(ctx, lz, filas[i][0], 188, y + 22, { tam: 20, peso: 800, color: L.tono(A, -0.3), ancho: 304 });
          });
          UJ.alfa(ctx, b, function () {
            UJ.pildora(ctx, lz, 400, y + 17, 'sobre', m.sello, 1, { tam: 17, centrar: true });
            L.rectRed(ctx, 450, y + 6, 324, 58, 12); L.rellena(ctx, L.tono(m.gris, 0.9), L.tono(m.gris, 0.4), 2);
            UJ.rotulo(ctx, lz, filas[i][1], 612, y + 22, { tam: 19, peso: 500, color: L.tono(m.tinta, 0.25), ancho: 304 });
          });
        })(i, y, a, b);
      }
      UJ.rotulo(ctx, lz, '«Sobre», no «en vez de»: lo de la derecha sigue valiendo.', W / 2, 560,
        { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.82, 1) });
    }
  });
})();
