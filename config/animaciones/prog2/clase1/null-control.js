/* null y NullPointerException: la referencia es un control remoto; con televisor funciona,
 * sin televisor (null) apretar un boton lanza NullPointerException. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('null-control', {
    duracion: 4.6,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      function control(x, y, nombre, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, 80, 150, 20); L.rellena(ctx, L.tono(m.tinta, 0.2), m.tinta, 2);
          L.circulo(ctx, x + 40, y + 30, 13); L.rellena(ctx, R);
          for (var i = 0; i < 2; i++) for (var j = 0; j < 3; j++) { L.circulo(ctx, x + 24 + i * 32, y + 66 + j * 26, 8); L.rellena(ctx, L.tono(m.gris, 0.6)); }
          UJ.rotulo(ctx, lz, nombre, x + 40, y + 160, { tam: 24, peso: 800, letra: 'Consolas, monospace' });
        });
      }
      function tele(x, y, texto, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, 240, 150, 12); L.rellena(ctx, m.tinta);
          L.rectRed(ctx, x + 12, y + 12, 216, 126, 6); L.rellena(ctx, L.tono(V, 0.8));
          UJ.rotulo(ctx, lz, 'Mascota', x + 120, y + 30, { tam: 18, peso: 800, color: V });
          UJ.rotulo(ctx, lz, texto, x + 120, y + 64, { tam: 22, peso: 800 });
          L.rectRed(ctx, x + 100, y + 150, 40, 14, 2); L.rellena(ctx, m.tinta);
        });
      }
      // Fila 1: control con televisor
      UJ.rotulo(ctx, lz, 'Mascota m = buscar("M-001");', 30, 18, { tam: 18, alinear: 'left', letra: 'Consolas, monospace', visible: L.tramo(t, 0, 0.1) });
      control(60, 56, 'm', L.tramo(t, 0.04, 0.12));
      tele(420, 60, '"Luna"', L.tramo(t, 0.1, 0.18));
      L.flecha(ctx, 150, 130, 412, 130, A, 4, L.tramo(t, 0.14, 0.22, 'frena'));
      UJ.rotulo(ctx, lz, 'm.getNombre() → "Luna"', 280, 150, { tam: 18, peso: 700, color: V, visible: L.tramo(t, 0.2, 0.28) });
      // Fila 2: control sin televisor
      UJ.rotulo(ctx, lz, 'Mascota n = buscar("M-999");  // null', 30, 270, { tam: 18, alinear: 'left', letra: 'Consolas, monospace', visible: L.tramo(t, 0.34, 0.44) });
      control(60, 306, 'n', L.tramo(t, 0.36, 0.44));
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.5), function () {
        L.rectRed(ctx, 420, 310, 240, 150, 12); ctx.setLineDash([10, 8]); L.rellena(ctx, m.papel, m.gris, 3); ctx.setLineDash([]);
        UJ.rotulo(ctx, lz, 'null', 540, 350, { tam: 30, peso: 800, color: m.gris, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'ningún objeto', 540, 396, { tam: 18, color: m.gris });
      });
      L.flecha(ctx, 150, 380, 400, 380, m.gris, 3, L.tramo(t, 0.46, 0.54, 'frena'));
      // El clic sobre null
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.66), function () {
        UJ.codigo(ctx, lz, 170, 404, 220, 'n.getNombre()', 1, 18);
      });
      UJ.rayo(ctx, 690, 330, 90, R, L.tramo(t, 0.68, 0.72));
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        L.rectRed(ctx, 30, 500, W - 60, 56, 10); L.rellena(ctx, R);
        UJ.rotulo(ctx, lz, 'NullPointerException', W / 2, 512, { tam: 26, peso: 800, color: m.papel, letra: 'Consolas, monospace' });
      });
      UJ.rotulo(ctx, lz, 'Defensas: validar en el constructor · devolver listas vacías · leer el mensaje del error', W / 2, 576, { tam: 18, peso: 600, ancho: W - 60, visible: L.tramo(t, 0.84, 0.96) });
    }
  });
})();
