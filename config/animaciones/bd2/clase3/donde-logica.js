/* Donde vive la logica: toda entrada pasa por el procedimiento; GRANT EXECUTE sin INSERT. A favor y en contra. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('donde-logica', {
    duracion: 5,
    pasos: [0.35, 0.65, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      var ent = ['aplicación', 'migración', 'consola admin'];
      for (var i = 0; i < 3; i++) {
        UJ.caja(ctx, lz, 20, 30 + i * 90, 220, 66, ent[i], null, C, L.tramo(t, 0.02 + i * 0.05, 0.08 + i * 0.05));
        L.flecha(ctx, 244, 63 + i * 90, 330, 155, C, 3, L.tramo(t, 0.16 + i * 0.03, 0.26 + i * 0.03, 'frena'));
      }
      UJ.caja(ctx, lz, 334, 110, 220, 90, 'sp_agendar_cita', 'la regla', A, L.tramo(t, 0.12, 0.2));
      L.flecha(ctx, 558, 155, 616, 155, A, 4, L.tramo(t, 0.26, 0.32));
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.32), function () { UJ.tabla(ctx, lz, 620, 132, 160, 'cita', [], 0, A); });
      UJ.rotulo(ctx, lz, 'La regla se cumple entre por donde se entre.', W / 2, 306, { tam: 20, ancho: W - 40, visible: L.tramo(t, 0.28, 0.35) });
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.46), function () {
        UJ.codigo(ctx, lz, 20, 350, 540, 'GRANT EXECUTE ON PROCEDURE sp_agendar_cita TO recepcion;', 1, 15);
        UJ.sello(ctx, lz, 590, 365, 18, true, 1);
      });
      UJ.alfa(ctx, L.tramo(t, 0.48, 0.58), function () {
        UJ.codigo(ctx, lz, 20, 396, 540, 'GRANT INSERT ON cita TO recepcion;', 1, 15);
        UJ.sello(ctx, lz, 590, 411, 18, false, 1);
        UJ.rotulo(ctx, lz, 'agenda, pero no escribe filas a mano', 700, 362, { tam: 16, ancho: 170 });
        UJ.rotulo(ctx, lz, 'Ojo: solo si el procedimiento es SECURITY DEFINER; si no, corre con los permisos de quien llama', W / 2, 432, { tam: 15, peso: 700, color: R, ancho: W - 40 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.68, 0.8), function () {
        L.rectRed(ctx, 20, 460, 370, 140, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'A favor', 205, 472, { tam: 20, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'una sola regla · permisos más finos · cierra la inyección', 205, 506, { tam: 17, ancho: 340 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.94), function () {
        L.rectRed(ctx, 410, 460, 370, 140, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'En contra', 595, 472, { tam: 20, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'se versiona peor: el .sql tiene que vivir en un repositorio', 595, 506, { tam: 17, ancho: 340 });
      });
    }
  });
})();
