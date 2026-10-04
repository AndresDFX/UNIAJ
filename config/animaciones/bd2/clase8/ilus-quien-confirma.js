/* Ilustracion: quien confirma o deshace segun desde donde se llama el procedimiento. CALL de
 * nivel superior: es su propia transaccion y la excepcion propagada la deshace. CALL dentro de
 * un BEGIN o de un bloque con EXCEPTION: un COMMIT dentro del procedimiento da «invalid
 * transaction termination» (comprobado en PGlite). Conclusion: confirma el llamador. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-quien-confirma', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, '¿Quién confirma lo que hizo el procedimiento?', W / 2, 8, { tam: 23, peso: 800, color: A, ancho: W - 30 });
      // 1 · CALL suelto
      L.rectRed(ctx, 16, 52, W - 32, 196, 14); L.rellena(ctx, L.tono(V, 0.92), V, 2);
      UJ.rotulo(ctx, lz, '1 · CALL suelto, sin BEGIN', 32, 62, { tam: 18, peso: 800, color: V, alinear: 'left' });
      ctx.save(); ctx.setLineDash([10, 7]); L.rectRed(ctx, 32, 96, W - 64, 62, 10); ctx.strokeStyle = V; ctx.lineWidth = 3; ctx.stroke(); ctx.restore();
      UJ.codigo(ctx, lz, 48, 108, 460, 'CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]);', 1, 15);
      UJ.rotulo(ctx, lz, 'su propia transacción', 650, 114, { tam: 15, peso: 700, color: V });
      UJ.rotulo(ctx, lz, 'la excepción sale del CALL → se deshace todo: cabecera, líneas y stock', W / 2, 176, { tam: 16, peso: 700, ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'nadie escribió ROLLBACK', W / 2, 210, { tam: 15, color: L.tono(V, -0.3) });
      // 2 · dentro de una transaccion abierta
      L.rectRed(ctx, 16, 262, W - 32, 176, 14); L.rellena(ctx, L.tono(A, 0.93), A, 2);
      UJ.rotulo(ctx, lz, '2 · CALL dentro de BEGIN … COMMIT', 32, 272, { tam: 18, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 32, 306, 230, 'BEGIN;', 1, 15);
      UJ.codigo(ctx, lz, 32, 342, 230, '  CALL sp_…();', 1, 15);
      UJ.codigo(ctx, lz, 32, 378, 230, 'COMMIT;  -- decide aquí', 1, 15);
      UJ.rotulo(ctx, lz, 'un COMMIT dentro del procedimiento:', 520, 312, { tam: 16, ancho: 480 });
      L.texto(ctx, 'ERROR: invalid transaction termination', 520, 346, { tam: 15, peso: 700, color: R, alinear: 'center', letra: 'Consolas, monospace' });
      UJ.rotulo(ctx, lz, 'lo mismo dentro de un bloque con EXCEPTION', 520, 384, { tam: 15, ancho: 480 });
      // 3 · conclusion
      L.rectRed(ctx, 16, 452, W - 32, 168, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
      UJ.rotulo(ctx, lz, 'Quien confirma es uno solo: el llamador', W / 2, 466, { tam: 22, peso: 800, color: L.tono(C, -0.35), ancho: W - 60 });
      UJ.rotulo(ctx, lz, 'un procedimiento que confirma por su cuenta le quita al llamador la posibilidad de deshacer', W / 2, 508, { tam: 16, ancho: W - 80 });
      UJ.rotulo(ctx, lz, 'si se captura el error, se relanza con RAISE; nunca WHEN OTHERS THEN NULL', W / 2, 568, { tam: 16, peso: 700, color: R, ancho: W - 80 });
    }
  });
})();
