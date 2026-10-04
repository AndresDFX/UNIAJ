/* El catch vacio: el error se traga y reaparece despues como NullPointerException; que es manejar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('catch-vacio', {
    duracion: 4.5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.codigo(ctx, lz, 30, 24, 440, 'Mascota m = null;', L.tramo(t, 0, 0.06), 18);
      UJ.codigo(ctx, lz, 30, 64, 440, 'try { m = repo.buscar("M-001"); }', L.tramo(t, 0.04, 0.12), 18);
      UJ.codigo(ctx, lz, 30, 104, 440, 'catch (IOException e) { }', L.tramo(t, 0.1, 0.18), 18);
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.26), function () {
        L.rectRed(ctx, 258, 104, 60, 36, 6); ctx.strokeStyle = R; ctx.lineWidth = 3; ctx.stroke();
        UJ.rotulo(ctx, lz, 'vacío: el error se traga en silencio', 490, 108, { tam: 18, peso: 700, alinear: 'left', ancho: 290, color: R });
      });
      // Pantallas despues
      var pant = ['Pantalla 1', 'Pantalla 2', 'Pantalla 3'];
      for (var i = 0; i < 3; i++) {
        var x = 30 + i * 180;
        UJ.alfa(ctx, L.tramo(t, 0.32 + i * 0.06, 0.38 + i * 0.06), function () {
          L.rectRed(ctx, x, 190, 150, 90, 10); L.rellena(ctx, L.tono(A, 0.92), A, 2);
          UJ.rotulo(ctx, lz, pant[i], x + 75, 200, { tam: 18, peso: 700, color: A });
          UJ.rotulo(ctx, lz, i < 2 ? 'todo «bien»' : 'm.getNombre()', x + 75, 236, { tam: 16, ancho: 140 });
        });
        if (i < 2) { var a = L.tramo(t, 0.36 + i * 0.06, 0.4 + i * 0.06); if (a > 0) L.flecha(ctx, x + 152, 235, x + 178, 235, A, 3, a); }
      }
      UJ.rayo(ctx, 562, 190, 60, R, L.tramo(t, 0.5, 0.54));
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.6), function () {
        UJ.rotulo(ctx, lz, 'NullPointerException', 685, 200, { tam: 18, peso: 800, color: R, ancho: 190 });
        UJ.rotulo(ctx, lz, 'lejos de la causa', 685, 236, { tam: 16, ancho: 190 });
      });
      // Manejar de verdad
      UJ.rotulo(ctx, lz, 'Manejar es hacer al menos una de estas:', W / 2, 320, { tam: 21, peso: 800, color: V, visible: L.tramo(t, 0.64, 0.7) });
      var op = [['Informar', 'mensaje claro al usuario'], ['Registrar', 'dejar la traza en el log'], ['Valor documentado', 'p. ej. lista vacía, dicho en el método'], ['Relanzar', 'que la atrape quien sí sepa']];
      for (var k = 0; k < 4; k++) {
        var cx = 30 + (k % 2) * 380, cy = 362 + Math.floor(k / 2) * 110;
        UJ.alfa(ctx, L.tramo(t, 0.68 + k * 0.06, 0.74 + k * 0.06), function () {
          L.rectRed(ctx, cx, cy, 360, 94, 12); L.rellena(ctx, L.tono(V, 0.9), V, 2);
          UJ.rotulo(ctx, lz, op[k][0], cx + 180, cy + 14, { tam: 21, peso: 800, color: V });
          UJ.rotulo(ctx, lz, op[k][1], cx + 180, cy + 50, { tam: 17, ancho: 330 });
        });
      }
    }
  });
})();
