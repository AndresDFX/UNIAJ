/* La bateria de pruebas: cuatro CALL seguidos se cortan en el primer fallo; un bloque DO por caso
 * corre los cuatro y deja el veredicto en una tabla. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('bateria-do', {
    duracion: 5,
    pasos: [0.38, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      var gris = L.tono(m.tinta, 0.75);
      UJ.rotulo(ctx, lz, 'Cuatro CALL de un tiro', 200, 16, { tam: 24, peso: 800, color: R, visible: L.tramo(t, 0, 0.05) });
      var casos = ['CALL … positivo', 'CALL … inactiva', 'CALL … franja ocupada', 'CALL … no existe'];
      var corte = L.tramo(t, 0.2, 0.3);
      for (var i = 0; i < 4; i++) {
        var col = i === 0 ? A : (i === 1 ? R : (corte > 0.5 ? gris : C));
        UJ.caja(ctx, lz, 30, 64 + i * 74, 340, 58, casos[i], null, col, L.tramo(t, 0.04 + i * 0.03, 0.08 + i * 0.03));
      }
      UJ.sello(ctx, lz, 360, 64 + 74 + 29, 20, false, L.tramo(t, 0.18, 0.24));
      UJ.rotulo(ctx, lz, 'el fallo aborta: los demás no corren', 200, 368, { tam: 18, peso: 700, color: R, ancho: 340, visible: L.tramo(t, 0.26, 0.36) });
      // Un DO por caso
      var X = W / 2 + 10;
      UJ.rotulo(ctx, lz, 'Un bloque DO por caso', X + 190, 16, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0.38, 0.42) });
      for (var j = 0; j < 4; j++) {
        UJ.alfa(ctx, L.tramo(t, 0.42 + j * 0.04, 0.46 + j * 0.04), function () {
          L.rectRed(ctx, X, 64 + j * 74, 380, 58, 10); L.rellena(ctx, L.tono(m.tinta, -0.55));
          L.texto(ctx, 'DO $$ BEGIN CALL … EXCEPTION … END $$;', X + 12, 64 + j * 74 + 20, { tam: 15, color: '#E8F4FA', letra: 'Consolas, monospace' });
        });
      }
      UJ.rotulo(ctx, lz, 'se ejecuta una vez y no se guarda', X + 190, 368, { tam: 18, ancho: 360, visible: L.tramo(t, 0.62, 0.72) });
      // tabla de resultados
      var filas = ['1 · positivo     · ok    · ok    · t', '2 · inactiva     · error · error · t',
                   '3 · franja       · error · error · t', '4 · no existe    · error · error · t'];
      UJ.alfa(ctx, L.tramo(t, 0.75, 0.8), function () {
        UJ.tabla(ctx, lz, 60, 410, W - 120, 'resultado_prueba (caso · esperado · obtenido · paso)', filas, L.mezcla(0, 4, L.tramo(t, 0.78, 0.94)), A, -1);
      });
    }
  });
})();
