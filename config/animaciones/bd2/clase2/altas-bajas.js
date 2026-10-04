/* El ciclo de vida de una cuenta: alta autorizada con su rol, cambio de funcion, baja el mismo
 * dia del retiro, y revision periodica de cuentas activas (3 a 6 meses, practica de gobierno).
 * Lo que evita: la cuenta huerfana y la cuenta compartida. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('altas-bajas', {
    duracion: 5,
    pasos: [0.5, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A, y = 150;
      L.trazo(ctx, [[60, y], [W - 60, y]], L.tramo(t, 0, 0.12), L.tono(m.tinta, 0.6), 5);
      var hitos = [[120, 'Alta', 'quién autoriza y con qué rol', V, 0.06],
                   [400, 'Cambio de función', 'se revoca un rol, se otorga otro', C, 0.2],
                   [680, 'Baja', 'el mismo día del retiro', R, 0.34]];
      for (var i = 0; i < 3; i++) {
        UJ.alfa(ctx, L.tramo(t, hitos[i][4], hitos[i][4] + 0.08), function () {
          L.circulo(ctx, hitos[i][0], y, 18); L.rellena(ctx, hitos[i][3], m.papel, 3);
          UJ.rotulo(ctx, lz, hitos[i][1], hitos[i][0], y - 66, { tam: 21, peso: 800, color: hitos[i][3], ancho: 240 });
          UJ.rotulo(ctx, lz, hitos[i][2], hitos[i][0], y + 30, { tam: 17, ancho: 250 });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.5), function () {
        ctx.setLineDash([8, 8]);
        L.trazo(ctx, [[120, y + 96], [120, y + 130], [680, y + 130], [680, y + 96]], 1, A, 3);
        ctx.setLineDash([]);
        UJ.rotulo(ctx, lz, 'revisión de cuentas activas cada 3 a 6 meses', W / 2, y + 140, { tam: 18, peso: 700, color: A, ancho: 600 });
      });
      var riesgos = [['Cuenta huérfana', 'se fue hace un año y la clave sigue viva'], ['Cuenta compartida', 'la auditoría no sabe quién fue']];
      for (var k = 0; k < 2; k++) {
        UJ.alfa(ctx, L.tramo(t, 0.54 + k * 0.12, 0.62 + k * 0.12), function () {
          var x = 40 + k * 370;
          L.rectRed(ctx, x, 360, 350, 110, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
          UJ.rotulo(ctx, lz, riesgos[k][0], x + 175, 374, { tam: 21, peso: 800, color: R });
          UJ.rotulo(ctx, lz, riesgos[k][1], x + 175, 412, { tam: 17, ancho: 330 });
        });
      }
      UJ.rotulo(ctx, lz, 'Vale porque fija responsables y plazos, no generalidades.', W / 2, 520,
                { tam: 20, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
