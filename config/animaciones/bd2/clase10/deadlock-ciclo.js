/* Deadlock: facturacion bloquea Factura y espera Insumo; devolucion bloquea Insumo y espera
 * Factura. El motor ve el ciclo en su grafo de esperas, elige una victima y la aborta (40P01 en
 * PostgreSQL). Prevencion: todos los procedimientos acceden en el mismo orden. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('deadlock-ciclo', {
    duracion: 5,
    pasos: [0.42, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      var victima = L.tramo(t, 0.5, 0.6);
      // Filas
      UJ.caja(ctx, lz, 300, 30, 200, 80, 'Factura', 'fila', m.tinta, L.tramo(t, 0, 0.06));
      UJ.caja(ctx, lz, 300, 260, 200, 80, 'Insumo', 'fila', m.tinta, L.tramo(t, 0, 0.06));
      // Transacciones
      UJ.caja(ctx, lz, 20, 145, 220, 80, 'Facturación', 'Factura → Insumo', A, L.tramo(t, 0.06, 0.12));
      UJ.alfa(ctx, 1 - 0.7 * victima, function () {
        UJ.caja(ctx, lz, 560, 145, 220, 80, 'Devolución', 'Insumo → Factura', C, L.tramo(t, 0.06, 0.12));
      });
      // Tiene (solido) y espera (punteado)
      L.flecha(ctx, 180, 143, 298, 80, A, 4, L.tramo(t, 0.12, 0.18));
      UJ.rotulo(ctx, lz, 'tiene', 210, 86, { tam: 17, peso: 700, color: A, visible: L.tramo(t, 0.16, 0.2) });
      UJ.alfa(ctx, 1 - victima, function () {
        L.flecha(ctx, 620, 228, 502, 300, C, 4, L.tramo(t, 0.18, 0.24));
        UJ.rotulo(ctx, lz, 'tiene', 600, 290, { tam: 17, peso: 700, color: C, visible: L.tramo(t, 0.22, 0.26) });
        ctx.save(); ctx.setLineDash([10, 8]);
        L.flecha(ctx, 620, 143, 502, 80, C, 3, L.tramo(t, 0.3, 0.36));
        ctx.restore();
        UJ.rotulo(ctx, lz, 'espera', 600, 86, { tam: 17, peso: 700, color: C, visible: L.tramo(t, 0.34, 0.38) });
      });
      // La espera de Facturacion: cuando la victima cae, deja de esperar y obtiene la fila.
      UJ.alfa(ctx, 1 - L.tramo(t, 0.6, 0.66), function () {
        ctx.save(); ctx.setLineDash([10, 8]);
        L.flecha(ctx, 180, 228, 298, 300, A, 3, L.tramo(t, 0.24, 0.3));
        ctx.restore();
        UJ.rotulo(ctx, lz, 'espera', 200, 290, { tam: 17, peso: 700, color: A, visible: L.tramo(t, 0.28, 0.32) });
      });
      L.flecha(ctx, 180, 228, 298, 300, A, 4, L.tramo(t, 0.6, 0.66));
      UJ.rotulo(ctx, lz, 'la obtiene y termina', 130, 300, { tam: 16, peso: 800, color: V, visible: L.tramo(t, 0.64, 0.7) });
      UJ.rotulo(ctx, lz, 'ciclo: ninguna avanza', 400, 172, { tam: 18, peso: 800, color: R, visible: L.tramo(t, 0.36, 0.42) * (1 - victima) });
      // Victima
      UJ.sello(ctx, lz, 760, 150, 26, false, L.tramo(t, 0.46, 0.54));
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.6), function () {
        L.rectRed(ctx, 30, 370, 740, 80, 14); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'El motor elige una víctima y la aborta', 400, 380, { tam: 20, peso: 800, color: R, ancho: 700 });
        UJ.rotulo(ctx, lz, 'PostgreSQL 40P01 · Oracle ORA-00060 · MySQL 1213 → la aplicación reintenta', 400, 414, { tam: 17, ancho: 720 });
      });
      // Prevencion
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.86), function () {
        L.rectRed(ctx, 30, 470, 740, 130, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, 'Prevención: siempre el mismo orden', 400, 484, { tam: 22, peso: 800, color: V, ancho: 700 });
        UJ.rotulo(ctx, lz, 'todos los procedimientos: Factura antes que Insumo', 400, 528, { tam: 19, ancho: 700 });
        UJ.rotulo(ctx, lz, 'sin orden cruzado no hay ciclo', 400, 562, { tam: 18, ancho: 700 });
      });
    }
  });
})();
