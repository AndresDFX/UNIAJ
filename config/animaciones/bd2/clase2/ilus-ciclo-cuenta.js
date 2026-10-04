/* Ilustracion: el ciclo de vida de una cuenta, cada fase con la sentencia que la ejecuta. Alta
 * (nace con un solo rol), cambio (se otorga el nuevo y se revoca el anterior), baja el mismo dia
 * (revocar, sin login, reasignar objetos), revision periodica y la prueba de que el permiso falta. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-ciclo-cuenta', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      var f = [
        ['1 · Alta', 'con un solo rol', ['CREATE ROLE ana_gomez LOGIN PASSWORD ...;', 'GRANT recepcion TO ana_gomez;'], V],
        ['2 · Cambio', 'no se acumula', ['GRANT auditor TO ana_gomez;', 'REVOKE recepcion FROM ana_gomez;'], C],
        ['3 · Baja', 'el mismo día', ['REVOKE recepcion FROM ana_gomez;', 'ALTER ROLE ana_gomez NOLOGIN;'], R],
        ['4 · Revisión', 'cada 3 a 6 meses', ['SELECT ... FROM', 'information_schema.role_table_grants;'], A],
        ['5 · Prueba', 'que el permiso NO está', ['SET ROLE recepcion; DELETE ...;', '-- permission denied'], L.tono(m.tinta, 0.2)]
      ];
      for (var i = 0; i < 5; i++) {
        var y = 14 + i * 104;
        L.rectRed(ctx, 20, y, 200, 92, 14); L.rellena(ctx, L.tono(f[i][3], 0.88), f[i][3], 3);
        UJ.rotulo(ctx, lz, f[i][0], 120, y + 14, { tam: 21, peso: 800, color: f[i][3] });
        UJ.rotulo(ctx, lz, f[i][1], 120, y + 52, { tam: 16, ancho: 180 });
        L.flecha(ctx, 224, y + 46, 246, y + 46, f[i][3], 3, 1);
        L.rectRed(ctx, 250, y + 6, 530, 80, 10); L.rellena(ctx, L.tono(m.tinta, -0.55));
        ctx.font = '500 15px Consolas, monospace'; ctx.fillStyle = '#E8F4FA'; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
        ctx.fillText(f[i][2][0], 264, y + 20);
        ctx.fillText(f[i][2][1], 264, y + 50);
        if (i < 4) L.flecha(ctx, 120, y + 92, 120, y + 104, L.tono(m.tinta, 0.4), 2, 1);
      }
      L.rectRed(ctx, 20, 538, W - 40, 88, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Antes de DROP ROLE: REASSIGN OWNED BY ana_gomez TO admin_bd', W / 2, 550, { tam: 18, peso: 700, ancho: W - 80 });
      UJ.rotulo(ctx, lz, 'Sin cuentas compartidas: la auditoría tiene que saber quién fue', W / 2, 584, { tam: 17, ancho: W - 80 });
    }
  });
})();
