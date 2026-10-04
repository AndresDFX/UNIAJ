/* Separacion de funciones con la factura: si una cuenta emite y borra, se cobra y desaparece el
 * registro. Separando, emitir es INSERT de un rol y anular es UPDATE de estado de otro, con rastro. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('separacion-funciones', {
    duracion: 5,
    pasos: [0.42, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // Una sola cuenta
      UJ.rotulo(ctx, lz, 'Una sola cuenta', 200, 16, { tam: 22, peso: 800, color: R, visible: L.tramo(t, 0, 0.06) });
      UJ.caja(ctx, lz, 110, 60, 180, 70, 'cuenta X', null, R, L.tramo(t, 0, 0.08));
      UJ.codigo(ctx, lz, 30, 160, 340, 'INSERT factura  -- cobra', L.tramo(t, 0.08, 0.18), 17);
      UJ.codigo(ctx, lz, 30, 220, 340, 'DELETE factura  -- la borra', L.tramo(t, 0.2, 0.3), 17);
      var f = 1 - L.tramo(t, 0.3, 0.38);
      UJ.alfa(ctx, L.tramo(t, 0.12, 0.18) * f, function () {
        L.rectRed(ctx, 150, 290, 100, 120, 6); L.rellena(ctx, m.papel, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'factura', 200, 336, { tam: 17 });
      });
      UJ.rotulo(ctx, lz, 'sin evidencia de que existió', 200, 420, { tam: 18, peso: 700, color: R, visible: L.tramo(t, 0.34, 0.42) });
      // Separada
      UJ.rotulo(ctx, lz, 'Funciones separadas', 600, 16, { tam: 22, peso: 800, color: V, visible: L.tramo(t, 0.44, 0.5) });
      UJ.caja(ctx, lz, 420, 60, 165, 70, 'rol emite', null, A, L.tramo(t, 0.46, 0.52));
      UJ.caja(ctx, lz, 605, 60, 165, 70, 'rol anula', null, C, L.tramo(t, 0.5, 0.56));
      UJ.codigo(ctx, lz, 420, 160, 350, 'INSERT factura', L.tramo(t, 0.54, 0.62), 17);
      UJ.codigo(ctx, lz, 420, 220, 350, "UPDATE estado = 'ANULADA'", L.tramo(t, 0.62, 0.7), 17);
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        L.rectRed(ctx, 450, 290, 290, 120, 6); L.rellena(ctx, m.papel, V, 2);
        UJ.rotulo(ctx, lz, 'factura ANULADA', 595, 300, { tam: 18, peso: 700, color: V });
        UJ.rotulo(ctx, lz, 'queda: fecha · usuario · motivo', 595, 344, { tam: 17, ancho: 260 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.86, 0.96), function () {
        L.rectRed(ctx, 40, 470, W - 80, 120, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Nadie completa solo un proceso sensible', W / 2, 484, { tam: 22, peso: 800, ancho: W - 120 });
        UJ.rotulo(ctx, lz, 'quien diseña el esquema no opera datos · quien audita solo lee', W / 2, 530, { tam: 17, ancho: W - 120 });
      });
    }
  });
})();
