/* Sin roles: doce cuentas por diez objetos, cientos de GRANT, y un cambio de regla obliga a tocar
 * doce cuentas. Con rol: se define una vez, doce GRANT rol TO usuario, y un REVOKE corrige a todos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('rol-aritmetica', {
    duracion: 5,
    pasos: [0.4, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      function persona(x, y, col) { L.circulo(ctx, x, y - 9, 8); L.rellena(ctx, col); L.rectRed(ctx, x - 10, y, 20, 16, 6); L.rellena(ctx, col); }
      // Sin roles
      UJ.rotulo(ctx, lz, 'Cuenta por cuenta', 200, 16, { tam: 22, peso: 800, color: R, visible: L.tramo(t, 0, 0.06) });
      for (var j = 0; j < 10; j++) UJ.alfa(ctx, L.tramo(t, 0.04, 0.1), function () {
        L.rectRed(ctx, 30 + j * 34, 60, 28, 28, 4); L.rellena(ctx, L.tono(A, 0.85), A, 1);
      });
      for (var i = 0; i < 12; i++) {
        var a = L.tramo(t, 0.08 + i * 0.015, 0.14 + i * 0.015);
        UJ.alfa(ctx, a, function () {
          var x = 44 + (i % 6) * 60, y = 220 + Math.floor(i / 6) * 60;
          persona(x, y, L.tono(m.tinta, 0.3));
          for (var k = 0; k < 10; k += 3) L.trazo(ctx, [[x, y - 20], [44 + k * 34, 90]], 1, L.tono(R, 0.6), 1);
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.28, 0.36), function () {
        L.rectRed(ctx, 30, 330, 350, 90, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'cientos de GRANT', 205, 342, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'un cambio de regla = tocar 12 cuentas', 205, 380, { tam: 17, ancho: 320 });
      });
      // Con rol
      UJ.rotulo(ctx, lz, 'Con un rol', 600, 16, { tam: 22, peso: 800, color: V, visible: L.tramo(t, 0.42, 0.48) });
      for (var q = 0; q < 10; q++) UJ.alfa(ctx, L.tramo(t, 0.44, 0.5), function () {
        L.rectRed(ctx, 430 + q * 34, 60, 28, 28, 4); L.rellena(ctx, L.tono(A, 0.85), A, 1);
      });
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.58), function () {
        L.rectRed(ctx, 520, 130, 160, 50, 25); L.rellena(ctx, C);
        UJ.rotulo(ctx, lz, 'recepcion', 600, 142, { tam: 20, peso: 800, color: m.papel });
        L.flecha(ctx, 600, 126, 600, 94, C, 3);
      });
      for (var p = 0; p < 12; p++) {
        UJ.alfa(ctx, L.tramo(t, 0.58 + p * 0.01, 0.64 + p * 0.01), function () {
          var x = 444 + (p % 6) * 60, y = 240 + Math.floor(p / 6) * 50;
          persona(x, y, L.tono(m.tinta, 0.3));
          L.trazo(ctx, [[x, y - 20], [600, 182]], 1, L.tono(C, 0.4), 1);
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        L.rectRed(ctx, 420, 330, 350, 90, 12); L.rellena(ctx, L.tono(V, 0.9), V, 2);
        UJ.rotulo(ctx, lz, '1 definición + 12 GRANT', 595, 342, { tam: 22, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'GRANT recepcion TO usuario', 595, 380, { tam: 17 });
      });
      UJ.codigo(ctx, lz, 60, 470, W - 120, 'REVOKE ... FROM recepcion;  -- los 12 quedan corregidos', L.tramo(t, 0.82, 0.96), 18);
      UJ.rotulo(ctx, lz, 'Rol: paquete de privilegios con nombre', W / 2, 540, { tam: 20, peso: 700, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
