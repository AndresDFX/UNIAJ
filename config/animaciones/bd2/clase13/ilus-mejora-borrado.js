/* Ilustracion: del caso a la mejora. Dos controles distintos: el trigger BEFORE DELETE que archiva
 * cada fila (permite volver) y la consulta que compara lo esperado con lo restaurado (demuestra
 * que se volvio completo). Hacen falta los dos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-mejora-borrado', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.rotulo(ctx, lz, 'Dos controles distintos, y hacen falta los dos', W / 2, 8, { tam: 24, peso: 800, color: A });
      // 1. Archivo
      UJ.rotulo(ctx, lz, '1 · Archivar antes de borrar', 205, 52, { tam: 20, peso: 800, color: C });
      UJ.codigo(ctx, lz, 30, 88, 350, 'DELETE FROM tarifa;', 1, 17);
      UJ.rotulo(ctx, lz, 'el error humano sigue siendo posible', 205, 128, { tam: 15, peso: 600, color: R });
      L.flecha(ctx, 205, 152, 205, 176, m.tinta, 3, 1);
      UJ.caja(ctx, lz, 40, 180, 330, 84, 'BEFORE DELETE', 'copia OLD y devuelve OLD', C, 1);
      L.flecha(ctx, 205, 268, 205, 292, m.tinta, 3, 1);
      UJ.tabla(ctx, lz, 40, 296, 330, 'tarifa_borrada', ['CANINO · 45000.00', 'FELINO · 40000.00', 'OTRA · 35000.00'], 3, C, -1);
      L.rectRed(ctx, 40, 476, 330, 44, 10); L.rellena(ctx, L.tono(C, 0.85), C, 2);
      UJ.rotulo(ctx, lz, 'permite volver', 205, 486, { tam: 19, peso: 800, color: L.tono(C, -0.35) });
      // 2. Comprobacion
      UJ.rotulo(ctx, lz, '2 · Comprobar lo restaurado', 595, 52, { tam: 20, peso: 800, color: V });
      UJ.tabla(ctx, lz, 430, 88, 330, 'registro_respaldo', ['tarifa · 3 filas'], 1, A, -1);
      UJ.caja(ctx, lz, 430, 196, 330, 84, 'COUNT(*) de tarifa', 'después de restaurar: 3', A, 1);
      L.flecha(ctx, 595, 284, 595, 310, m.tinta, 3, 1);
      L.rectRed(ctx, 430, 314, 330, 60, 10); L.rellena(ctx, L.tono(m.tinta, -0.55));
      ctx.font = '600 17px Consolas, monospace'; ctx.fillStyle = '#E8F4FA'; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('CASE WHEN 3 = 3', 446, 324);
      ctx.fillText("THEN 'RESTAURACION OK' …", 446, 348);
      L.flecha(ctx, 595, 378, 595, 404, m.tinta, 3, 1);
      L.rectRed(ctx, 450, 408, 290, 50, 25); L.rellena(ctx, L.tono(V, 0.75), V, 2);
      UJ.rotulo(ctx, lz, 'RESTAURACION OK', 595, 420, { tam: 19, peso: 800, color: L.tono(V, -0.35) });
      L.rectRed(ctx, 430, 476, 330, 44, 10); L.rellena(ctx, L.tono(V, 0.85), V, 2);
      UJ.rotulo(ctx, lz, 'demuestra que se volvió completo', 595, 486, { tam: 18, peso: 800, color: L.tono(V, -0.35) });
      // Cierre
      UJ.rotulo(ctx, lz, 'Lo que le faltó a GitLab: comprobar restaurando.', W / 2, 560, { tam: 21, peso: 700, ancho: W - 40 });
    }
  });
})();
