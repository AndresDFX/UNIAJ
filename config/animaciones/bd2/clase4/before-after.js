/* BEFORE o AFTER: la fila viaja de izquierda a derecha. Antes de escribirse pasa por BEFORE,
 * que decide lo que se guarda (NEW, NEW modificado o NULL = cancela en silencio); despues de
 * escrita pasa por AFTER, que solo registra. Para rechazar: RAISE EXCEPTION. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('before-after', {
    duracion: 4.8,
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, y = 190;
      // La via
      ctx.lineWidth = 6; ctx.strokeStyle = L.tono(m.tinta, 0.8); ctx.beginPath(); ctx.moveTo(40, y); ctx.lineTo(W - 40, y); ctx.stroke();
      UJ.caja(ctx, lz, 150, y - 70, 170, 140, 'BEFORE', 'decide qué se guarda', A, L.tramo(t, 0.0, 0.1));
      L.rectRed(ctx, 360, y - 36, 90, 72, 8); L.rellena(ctx, m.papel, m.tinta, 3);
      UJ.rotulo(ctx, lz, 'tabla', 405, y - 12, { tam: 18 });
      UJ.caja(ctx, lz, 490, y - 70, 170, 140, 'AFTER', 'solo registra', C, L.tramo(t, 0.05, 0.15));
      // La fila que viaja
      var x = L.claves(t, [[0, 40], [0.22, 190, 'frena'], [0.4, 190], [0.55, 380, 'suave'], [0.62, 380], [0.78, 560, 'suave'], [1, 560]]);
      L.rectRed(ctx, x, y - 18, 60, 36, 8); L.rellena(ctx, m.sello || C, m.tinta, 2);
      UJ.rotulo(ctx, lz, 'NEW', x + 30, y - 11, { tam: 17, peso: 800 });
      // Lo que puede retornar BEFORE
      var op = [['RETURN NEW', 'se guarda tal cual'], ['RETURN NEW cambiado', 'se guarda la versión cambiada'], ['RETURN NULL', 'se cancela en silencio']];
      for (var i = 0; i < 3; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.24 + i * 0.05, 0.32 + i * 0.05), function () {
          L.rectRed(ctx, 40, 300 + i * 58, 350, 48, 10);
          L.rellena(ctx, i === 2 ? L.tono(m.malva || '#A02030', 0.85) : L.tono(A, 0.9), i === 2 ? (m.malva || '#A02030') : A, 2);
          UJ.rotulo(ctx, lz, op[i][0], 56, 304 + i * 58, { tam: 17, peso: 800, alinear: 'left', color: i === 2 ? (m.malva || '#A02030') : A });
          UJ.rotulo(ctx, lz, op[i][1], 56, 326 + i * 58, { tam: 15, peso: 500, alinear: 'left' });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.76), function () {
        L.rectRed(ctx, 430, 300, 330, 106, 10); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'La fila ya está escrita:', 446, 314, { tam: 18, peso: 700, alinear: 'left', color: C });
        UJ.rotulo(ctx, lz, 'el retorno se ignora (RETURN NEW por convención).', 446, 340, { tam: 16, peso: 500, alinear: 'left', ancho: 300 });
      });
      UJ.rotulo(ctx, lz, 'Para rechazar: RAISE EXCEPTION, no RETURN NULL.', W / 2, 520,
                { tam: 23, ancho: W - 40, color: m.malva || '#A02030', visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
