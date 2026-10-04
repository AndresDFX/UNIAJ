/* El trigger que impide. El mismo UPDATE dos veces sobre un insumo con 3 unidades: sin defensa
 * la base guarda un imposible (-7); con un trigger BEFORE que hace RAISE EXCEPTION el UPDATE se
 * rechaza y el stock sigue en 3. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('trigger-que-impide', {
    duracion: 4.8,
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.codigo(ctx, lz, 24, 20, W - 48, 'UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;', L.tramo(t, 0, 0.18), 17);
      // Sin defensa
      UJ.rotulo(ctx, lz, 'Sin defensa', 200, 100, { tam: 24, peso: 800, color: R, visible: L.tramo(t, 0.18, 0.24) });
      var stock1 = Math.round(L.mezcla(3, -7, L.tramo(t, 0.26, 0.44, 'suave')));
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.26), function () {
        L.rectRed(ctx, 60, 150, 280, 150, 16); L.rellena(ctx, stock1 < 0 ? L.tono(R, 0.85) : L.tono(A, 0.92), stock1 < 0 ? R : A, 3);
        UJ.rotulo(ctx, lz, 'stock', 200, 168, { tam: 20 });
        UJ.rotulo(ctx, lz, String(stock1), 200, 200, { tam: 64, peso: 800, color: stock1 < 0 ? R : A });
      });
      UJ.rotulo(ctx, lz, 'un imposible físico', 200, 318, { tam: 19, visible: L.tramo(t, 0.44, 0.52) });
      // Con trigger BEFORE
      UJ.rotulo(ctx, lz, 'Con trigger BEFORE', 600, 100, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0.52, 0.58) });
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.6), function () {
        L.rectRed(ctx, 460, 150, 280, 150, 16); L.rellena(ctx, L.tono(A, 0.92), A, 3);
        UJ.rotulo(ctx, lz, 'stock', 600, 168, { tam: 20 });
        UJ.rotulo(ctx, lz, '3', 600, 200, { tam: 64, peso: 800, color: A });
      });
      UJ.sello(ctx, lz, 740, 150, 34, false, L.tramo(t, 0.64, 0.72));
      UJ.alfa(ctx, L.tramo(t, 0.68, 0.76), function () {
        UJ.codigo(ctx, lz, 430, 330, 346, "RAISE EXCEPTION 'stock insuficiente';", 1, 15);
      });
      UJ.rotulo(ctx, lz, 'Si la regla cabe en un CHECK, va en un CHECK.', W / 2, 450, { tam: 21, ancho: W - 40, visible: L.tramo(t, 0.8, 0.9) });
      UJ.rotulo(ctx, lz, 'El trigger es para lo que mira otra fila u otra tabla.', W / 2, 490, { tam: 21, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
