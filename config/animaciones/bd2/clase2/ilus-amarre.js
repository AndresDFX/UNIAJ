/* Ilustracion: como amarra la Clase 2 con las vecinas. De la Clase 1 vienen las tablas que hoy se
 * protegen; los roles de hoy se usan en la 3 (EXECUTE en vez de INSERT), en la 4 (auditoria con
 * current_user y respaldo de roles) y en la 12 (la cuenta de la aplicacion). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-amarre', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, S = m.sello || C;
      // Lo que llega
      L.rectRed(ctx, 24, 40, 230, 110, 14); L.rellena(ctx, L.tono(A, 0.88), A, 2);
      UJ.rotulo(ctx, lz, 'Clase 1', 139, 56, { tam: 22, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'las tablas y sus claves', 139, 96, { tam: 17, ancho: 210 });
      L.flecha(ctx, 260, 95, 300, 95, A, 4, 1);
      // Hoy
      L.rectRed(ctx, 306, 30, 200, 130, 16); L.rellena(ctx, S, m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Clase 2 · hoy', 406, 52, { tam: 21, peso: 800 });
      UJ.rotulo(ctx, lz, 'roles, GRANT y la matriz', 406, 92, { tam: 17, ancho: 180 });
      UJ.rotulo(ctx, lz, 'hoy se protegen', 139, 160, { tam: 16, color: L.tono(m.tinta, 0.3) });
      // Lo que sigue
      var sig = [
        ['Clase 3', 'EXECUTE sobre sp_agendar_cita en vez de INSERT sobre cita'],
        ['Clase 4', 'current_user en la auditoría · pg_dumpall respalda los roles'],
        ['Clase 12', 'la aplicación se conecta con una cuenta de servicio y su rol']
      ];
      L.trazo(ctx, [[406, 164], [406, 214], [60, 214], [60, 520]], 1, L.tono(C, 0.2), 3);
      for (var i = 0; i < 3; i++) {
        var y = 236 + i * 108;
        L.flecha(ctx, 60, y + 44, 96, y + 44, C, 3, 1);
        L.rectRed(ctx, 100, y, 170, 88, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, sig[i][0], 185, y + 28, { tam: 21, peso: 800, color: L.tono(C, -0.3) });
        L.rectRed(ctx, 286, y + 6, 494, 76, 12); L.rellena(ctx, m.papel, C, 2);
        UJ.rotulo(ctx, lz, sig[i][1], 533, y + 22, { tam: 17, ancho: 460 });
      }
      UJ.rotulo(ctx, lz, 'La matriz de hoy es la base de las tres clases que siguen.', W / 2, 580,
                { tam: 18, peso: 700, ancho: W - 40 });
    }
  });
})();
