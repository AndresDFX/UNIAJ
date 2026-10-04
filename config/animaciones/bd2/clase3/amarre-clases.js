/* Lo de hoy no es una isla: que deja cada clase vecina y que retoma despues. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('amarre-clases', {
    duracion: 4.8,
    pasos: [0.45, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var c = [
        ['Clase 1', 'esquema · baja lógica · franja única', A],
        ['Clase 2', 'roles: EXECUTE, no INSERT', A],
        ['Clase 3 · hoy', 'procedimientos almacenados', m.sello || C],
        ['Clase 4', 'función y triggers: ¿CHECK, trigger o app?', C],
        ['Clase 8', '¿quién confirma la transacción?', C],
        ['Clase 12', 'la aplicación los consume', C]
      ];
      var tt = [0.02, 0.12, 0.24, 0.48, 0.62, 0.76];
      for (var i = 0; i < 6; i++) {
        var y = 20 + i * 100, a = L.tramo(t, tt[i], tt[i] + 0.1);
        if (i > 0) L.flecha(ctx, 120, y - 30, 120, y - 4, L.tono(m.tinta, 0.4), 3, a);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 20, y, 200, 66, 12); L.rellena(ctx, i === 2 ? c[i][2] : L.tono(c[i][2], 0.85), c[i][2], 3);
          UJ.rotulo(ctx, lz, c[i][0], 120, y + 20, { tam: 21, peso: 800, color: i === 2 ? m.tinta : c[i][2] });
          UJ.rotulo(ctx, lz, c[i][1], 240, y + 20, { tam: 20, alinear: 'left', ancho: 540 });
        });
      }
    }
  });
})();
