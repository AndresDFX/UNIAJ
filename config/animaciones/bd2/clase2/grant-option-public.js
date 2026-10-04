/* WITH GRANT OPTION: el privilegio se reotorga en cadena y el REVOKE exige CASCADE. PUBLIC: todos
 * los roles, existentes y futuros; se limpia con REVOKE ALL ... FROM PUBLIC. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('grant-option-public', {
    duracion: 5,
    // Pasos LOGICOS: 1) la cadena de reotorgamientos, 2) el REVOKE que exige CASCADE, 3) PUBLIC
    // entrega el historial a todos, 4) como se limpia.
    pasos: [0.28, 0.54, 0.88, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.rotulo(ctx, lz, 'WITH GRANT OPTION', 30, 16, { tam: 22, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0, 0.05) });
      var nodos = [['admin', 80], ['rol_a', 280], ['rol_b', 480], ['rol_c', 680]];
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, 0.04 + i * 0.06, 0.1 + i * 0.06);
        var cortado = i > 0 && t >= 0.36;
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, nodos[i][1], 100, 40); L.rellena(ctx, cortado ? L.tono(R, 0.8) : L.tono(A, 0.85), cortado ? R : A, 3);
          L.texto(ctx, nodos[i][0], nodos[i][1], 90, { tam: 16, peso: 700, color: cortado ? R : A, alinear: 'center', letra: 'Consolas, monospace' });
          if (i > 0) L.flecha(ctx, nodos[i - 1][1] + 42, 100, nodos[i][1] - 44, 100, L.tono(m.tinta, 0.4), 3);
        });
      }
      UJ.rotulo(ctx, lz, 'cada uno lo reotorga: el admin pierde el control', W / 2, 156, { tam: 18, visible: L.tramo(t, 0.18, 0.26) });
      UJ.codigo(ctx, lz, 30, 196, W - 60, 'REVOKE SELECT ON consulta FROM rol_a CASCADE;', L.tramo(t, 0.3, 0.38), 18);
      UJ.rotulo(ctx, lz, 'sin CASCADE el motor lo rechaza: toca más de lo pedido', W / 2, 250, { tam: 18, peso: 600, color: R, ancho: W - 60, visible: L.tramo(t, 0.4, 0.5) });
      // PUBLIC
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.64), function () {
        L.trazo(ctx, [[30, 296], [W - 30, 296]], 1, L.tono(m.tinta, 0.8), 1);
        UJ.rotulo(ctx, lz, 'PUBLIC', 30, 310, { tam: 22, peso: 800, color: R, alinear: 'left' });
        UJ.rotulo(ctx, lz, '= todos los roles, de hoy y de mañana', 140, 314, { tam: 18, alinear: 'left' });
      });
      UJ.codigo(ctx, lz, 30, 360, W - 60, 'GRANT SELECT ON consulta TO PUBLIC;', L.tramo(t, 0.62, 0.7), 18);
      for (var p = 0; p < 9; p++) {
        UJ.alfa(ctx, L.tramo(t, 0.7 + p * 0.015, 0.74 + p * 0.015), function () {
          var x = 90 + p * 75, y = 450;
          L.circulo(ctx, x, y - 10, 10); L.rellena(ctx, p === 8 ? L.tono(R, 0.5) : L.tono(m.tinta, 0.35));
          L.rectRed(ctx, x - 13, y + 2, 26, 20, 7); L.rellena(ctx, p === 8 ? L.tono(R, 0.5) : L.tono(m.tinta, 0.35));
        });
      }
      UJ.rotulo(ctx, lz, 'el historial, para cualquiera que se conecte', W / 2, 484, { tam: 18, color: R, visible: L.tramo(t, 0.82, 0.88) });
      UJ.codigo(ctx, lz, 30, 530, W - 60, 'REVOKE ALL ON consulta FROM PUBLIC;', L.tramo(t, 0.88, 0.98), 18);
    }
  });
})();
