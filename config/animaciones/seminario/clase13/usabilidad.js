/* Cuatro principios de usabilidad, cada uno con su mini pantalla: visibilidad del estado,
 * prevencion de errores, consistencia y reconocer antes que recordar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('usabilidad', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.25, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, T = m.tinta, G = m.gris, V = m.verde, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Cuatro principios de usabilidad', W / 2, 18, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      var pos = [[20, 66], [410, 66], [20, 340], [410, 340]], cw = 370, ch = 258;
      var tit = ['Visibilidad del estado', 'Prevención de errores', 'Consistencia', 'Reconocer antes que recordar'];
      var cols = [V, m.sello, A, C];

      function campo(x, y, w, txt, borde) {
        L.rectRed(ctx, x, y, w, 34, 6); L.rellena(ctx, m.papel, borde || L.tono(G, 0.2), 1.5);
        UJ.rotulo(ctx, lz, txt, x + 10, y + 8, { tam: 16, peso: 500, color: T, alinear: 'left' });
      }
      function boton(x, y, w, txt, c, apagado) {
        L.rectRed(ctx, x, y, w, 34, 7); L.rellena(ctx, apagado ? L.tono(G, 0.7) : c);
        UJ.rotulo(ctx, lz, txt, x + w / 2, y + 8, { tam: 16, peso: 800, color: apagado ? L.tono(G, -0.1) : m.papel });
      }
      var dib = [
        function (x, y) {
          L.rectRed(ctx, x + 20, y + 14, cw - 40, 40, 8); L.rellena(ctx, L.tono(V, 0.82), V, 2);
          UJ.rotulo(ctx, lz, '✓ Ficha guardada, código M-0421', x + cw / 2, y + 24, { tam: 17, peso: 700, color: L.tono(V, -0.4) });
          campo(x + 20, y + 74, cw - 40, 'Nombre: Rocky');
          boton(x + cw - 140, y + 130, 120, 'Guardar', V, true);
          UJ.rotulo(ctx, lz, 'deshabilitado: no se guarda dos veces', x + 20, y + 178, { tam: 16, peso: 600, color: L.tono(G, -0.35), alinear: 'left', ancho: cw - 40 });
        },
        function (x, y) {
          UJ.rotulo(ctx, lz, 'Fecha', x + 20, y + 10, { tam: 16, peso: 700, color: T, alinear: 'left' });
          for (var r = 0; r < 3; r++) for (var c = 0; c < 5; c++) {
            L.rectRed(ctx, x + 20 + c * 30, y + 36 + r * 28, 26, 24, 3);
            L.rellena(ctx, r === 1 && c === 2 ? L.tono(m.sello, 0.3) : L.tono(m.sello, 0.85), L.tono(m.sello, -0.2), 1);
          }
          UJ.rotulo(ctx, lz, 'Especie', x + 200, y + 10, { tam: 16, peso: 700, color: T, alinear: 'left' });
          var ops = ['Canino', 'Felino', 'Otro'];
          for (var k = 0; k < 3; k++) {
            L.rectRed(ctx, x + 200, y + 36 + k * 30, 140, 30, 0); L.rellena(ctx, k === 0 ? L.tono(m.sello, 0.6) : m.papel, L.tono(G, 0.3), 1);
            UJ.rotulo(ctx, lz, ops[k], x + 212, y + 41 + k * 30, { tam: 16, peso: 600, color: T, alinear: 'left' });
          }
          UJ.rotulo(ctx, lz, 'calendario y lista cerrada: no hay cómo escribir mal', x + 20, y + 140, { tam: 16, peso: 600, color: L.tono(G, -0.35), alinear: 'left', ancho: cw - 40 });
        },
        function (x, y) {
          for (var k = 0; k < 2; k++) {
            var px = x + 20 + k * 175;
            L.rectRed(ctx, px, y + 10, 155, 120, 8); L.rellena(ctx, m.papel, L.tono(G, 0.2), 1.5);
            UJ.rotulo(ctx, lz, k ? 'Cita' : 'Mascota', px + 12, y + 18, { tam: 16, peso: 700, color: T, alinear: 'left' });
            L.rectRed(ctx, px + 12, y + 44, 130, 14, 3); L.rellena(ctx, L.tono(G, 0.75));
            L.rectRed(ctx, px + 12, y + 64, 100, 14, 3); L.rellena(ctx, L.tono(G, 0.75));
            boton(px + 60, y + 88, 86, 'Guardar', A);
          }
          UJ.rotulo(ctx, lz, '«Guardar» siempre abajo a la derecha', x + 20, y + 150, { tam: 16, peso: 600, color: L.tono(G, -0.35), alinear: 'left', ancho: cw - 40 });
        },
        function (x, y) {
          UJ.rotulo(ctx, lz, 'Raza', x + 20, y + 10, { tam: 16, peso: 700, color: T, alinear: 'left' });
          campo(x + 20, y + 36, 130, 'código: 07', R);
          UJ.rayar(ctx, x + 26, y + 54, 104, R, 1);
          L.flecha(ctx, x + 160, y + 53, x + 192, y + 53, T, 2.5, 1);
          var ops = ['Criollo', 'Labrador', 'Siamés'];
          for (var k = 0; k < 3; k++) {
            L.rectRed(ctx, x + 200, y + 36 + k * 30, 140, 30, 0); L.rellena(ctx, k === 1 ? L.tono(C, 0.6) : m.papel, L.tono(G, 0.3), 1);
            UJ.rotulo(ctx, lz, ops[k], x + 212, y + 41 + k * 30, { tam: 16, peso: 600, color: T, alinear: 'left' });
          }
          UJ.rotulo(ctx, lz, 'elegir de una lista, no recordar códigos', x + 20, y + 140, { tam: 16, peso: 600, color: L.tono(G, -0.35), alinear: 'left', ancho: cw - 40 });
        }
      ];
      for (var i = 0; i < 4; i++) {
        (function (i) {
          var x = pos[i][0], y = pos[i][1], a = L.tramo(t, 0.03 + i * 0.25, 0.13 + i * 0.25);
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, x, y, cw, ch, 12); L.rellena(ctx, m.papel, cols[i], 2.5);
            L.rectRed(ctx, x, y, cw, 42, 12); L.rellena(ctx, cols[i]);
            L.rectRed(ctx, x, y + 30, cw, 12, 0); L.rellena(ctx, cols[i]);
            UJ.rotulo(ctx, lz, tit[i], x + cw / 2, y + 10, { tam: 19, peso: 800, color: i === 1 ? T : m.papel });
            dib[i](x, y + 52);
          });
        })(i);
      }
    }
  });
})();
