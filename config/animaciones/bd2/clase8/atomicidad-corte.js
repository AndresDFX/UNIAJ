/* Atomicidad: se aplica completa o no se aplica. La facturacion avanza tres sentencias y se cae
 * la red antes de la segunda linea. Sin atomicidad queda una factura a medias; con atomicidad el
 * motor deshace todo al detectar que la sesion murio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('atomicidad-corte', {
    duracion: 5,
    pasos: [0.42, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      var pasos = ['INSERT factura', 'INSERT línea 1', 'UPDATE stock insumo 1', 'línea 2 ...'];
      var y = 120, xs = [110, 300, 490, 690];
      L.trazo(ctx, [[40, y], [W - 40, y]], L.tramo(t, 0, 0.1), L.tono(m.tinta, 0.6), 4);
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, 0.06 + i * 0.07, 0.12 + i * 0.07);
        var ok = i < 3, c = ok ? A : L.tono(m.tinta, 0.5);
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, xs[i], y, 12); L.rellena(ctx, c, m.papel, 3);
          UJ.rotulo(ctx, lz, pasos[i], xs[i], y + 24, { tam: 17, peso: 700, color: c, ancho: 170 });
        });
      }
      UJ.rayo(ctx, 595, 30, 70, R, L.tramo(t, 0.3, 0.36));
      UJ.rotulo(ctx, lz, 'se cae la red', 650, 46, { tam: 18, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0.32, 0.4) });
      // Sin atomicidad
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        L.rectRed(ctx, 30, 230, 360, 300, 16); L.rellena(ctx, L.tono(R, 0.92), R, 2);
        UJ.rotulo(ctx, lz, 'Sin atomicidad', 210, 246, { tam: 24, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'factura: queda', 210, 300, { tam: 19 });
        UJ.rotulo(ctx, lz, 'línea 1: queda', 210, 336, { tam: 19 });
        UJ.rotulo(ctx, lz, 'stock insumo 1: descontado', 210, 372, { tam: 19, ancho: 330 });
        UJ.rotulo(ctx, lz, 'línea 2: nunca llegó', 210, 408, { tam: 19 });
      });
      UJ.rotulo(ctx, lz, 'factura a medias: descuadre', 210, 462, { tam: 20, peso: 800, color: R, ancho: 330, visible: L.tramo(t, 0.56, 0.66) });
      // Con atomicidad
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.82), function () {
        L.rectRed(ctx, 410, 230, 360, 300, 16); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'Con atomicidad', 590, 246, { tam: 24, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'la sesión murió sin COMMIT:', 590, 300, { tam: 19, ancho: 330 });
        UJ.rotulo(ctx, lz, 'el motor deshace todo solo', 590, 336, { tam: 19, peso: 700, ancho: 330 });
        UJ.rotulo(ctx, lz, '0 facturas · 0 líneas', 590, 390, { tam: 19, ancho: 330 });
        UJ.rotulo(ctx, lz, 'stock intacto', 590, 426, { tam: 19, ancho: 330 });
      });
      UJ.sello(ctx, lz, 590, 482, 26, true, L.tramo(t, 0.84, 0.92));
      UJ.rotulo(ctx, lz, 'Completa o nada: sin estados intermedios.', W / 2, 570, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
