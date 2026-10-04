/* Ilustracion: que observar en la demo — tres UPDATE dejan dos filas de auditoria, y el
 * trigger de stock rechaza el negativo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });
      // auditoria
      UJ.rotulo(ctx, lz, '1 · Auditoría', 200, 64, { tam: 20, peso: 800, color: A });
      for (var i = 0; i < 3; i++) UJ.codigo(ctx, lz, 24, 100 + i * 48, 352, 'UPDATE cita SET estado = …', 1, 15);
      L.flecha(ctx, 200, 248, 200, 292, A, 4, 1);
      UJ.tabla(ctx, lz, 40, 298, 320, 'audit_cita', ['pendiente → confirmada', 'confirmada → atendida'], 2, A, -1);
      UJ.rotulo(ctx, lz, '3 UPDATE → 2 filas', 200, 440, { tam: 22, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'el WHEN ignora el que no cambió', 200, 474, { tam: 16 });
      // stock
      UJ.rotulo(ctx, lz, '2 · Stock', 600, 64, { tam: 20, peso: 800, color: R });
      UJ.codigo(ctx, lz, 424, 100, 352, 'UPDATE insumo SET stock = stock - 10', 1, 15);
      L.flecha(ctx, 600, 148, 600, 190, R, 4, 1);
      L.rectRed(ctx, 470, 196, 260, 120, 16); L.rellena(ctx, L.tono(A, 0.92), A, 2);
      UJ.rotulo(ctx, lz, 'stock', 600, 210, { tam: 18 });
      UJ.rotulo(ctx, lz, '3', 600, 236, { tam: 50, peso: 800, color: A });
      UJ.sello(ctx, lz, 730, 196, 26, false, 1);
      UJ.rotulo(ctx, lz, 'el negativo se rechaza', 600, 340, { tam: 18, peso: 700, color: R });
      UJ.rotulo(ctx, lz, 'RAISE EXCEPTION', 600, 372, { tam: 16 });
    }
  });
})();
