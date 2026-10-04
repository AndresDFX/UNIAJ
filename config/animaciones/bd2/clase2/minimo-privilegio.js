/* Minimo privilegio: cada rol recibe exactamente lo que su funcion necesita. Recepcion no lee
 * consulta (historial sensible); veterinario_rol lee cita y mascota y documenta consulta (S, I, U);
 * admin_bd sostiene el DDL. DELETE no aparece en ningun rol operativo: se marca, no se borra. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('minimo-privilegio', {
    duracion: 5,
    pasos: [0.3, 0.58, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var tablas = ['cita', 'mascota', 'consulta'], x0 = 230, cw = 180, y0 = 40, ch = 70;
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () {
        for (var j = 0; j < 3; j++) {
          L.rectRed(ctx, x0 + j * cw, y0, cw, 50, 0); L.rellena(ctx, A, m.papel, 2);
          L.texto(ctx, tablas[j], x0 + j * cw + cw / 2, y0 + 13, { tam: 19, peso: 700, color: m.papel, alinear: 'center', letra: 'Consolas, monospace' });
        }
      });
      var roles = [['recepcion', ['S I U', 'S', '—'], 0.04], ['veterinario_rol', ['S', 'S', 'S I U'], 0.32], ['admin_bd', ['todo + DDL', 'todo + DDL', 'todo + DDL'], 0.6]];
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, roles[i][2], roles[i][2] + 0.08), y = y0 + 50 + i * ch;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 30, y, 200, ch, 0); L.rellena(ctx, L.tono(C, 0.85), m.papel, 2);
          L.texto(ctx, roles[i][0], 130, y + 24, { tam: 17, peso: 700, color: L.tono(C, -0.35), alinear: 'center', letra: 'Consolas, monospace' });
          for (var j = 0; j < 3; j++) {
            var vacia = roles[i][1][j] === '—';
            L.rectRed(ctx, x0 + j * cw, y, cw, ch, 0); L.rellena(ctx, vacia ? L.tono(R, 0.9) : m.papel, L.tono(A, 0.5), 1);
            L.texto(ctx, roles[i][1][j], x0 + j * cw + cw / 2, y + 22, { tam: 20, peso: 700, color: vacia ? R : m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
          }
        });
      }
      var notas = [['recepcion no lee consulta: historial sensible que su trabajo no requiere', 0.14, R],
                   ['veterinario_rol documenta la atención: S, I, U sobre consulta', 0.42, C],
                   ['admin_bd: el único con privilegios amplios', 0.7, A]];
      for (var k = 0; k < 3; k++)
        UJ.rotulo(ctx, lz, notas[k][0], 40, 320 + k * 46, { tam: 18, peso: 600, alinear: 'left', ancho: W - 80, color: L.tono(notas[k][2], -0.2), visible: L.tramo(t, notas[k][1], notas[k][1] + 0.1) });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.96), function () {
        L.rectRed(ctx, 40, 480, W - 80, 110, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Ningún rol operativo tiene DELETE', W / 2, 494, { tam: 23, peso: 800 });
        UJ.rotulo(ctx, lz, "se marca: estado = 'CANCELADA' · activa = 'N'", W / 2, 538, { tam: 18 });
      });
    }
  });
})();
