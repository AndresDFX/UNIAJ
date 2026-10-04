/* Ilustracion: el depurador de VS Code en una pausa. Breakpoint condicional en el margen, la
 * linea donde se detuvo, los paneles Variables / Watch / Call Stack y las teclas para avanzar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-depurador', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', T = m.tinta, W = lz.ancho;
      var AMA = m.sello || '#F2C200', MONO = 'Consolas, monospace';
      function mono(txt, x, y, tam, color, alinear) {
        ctx.font = '500 ' + tam + 'px ' + MONO; ctx.fillStyle = color;
        ctx.textAlign = alinear || 'left'; ctx.textBaseline = 'top'; ctx.fillText(txt, x, y);
      }
      function punto(x, y, cond) {
        L.circulo(ctx, x, y, 8); L.rellena(ctx, R);
        if (cond) { ctx.fillStyle = m.papel; ctx.fillRect(x - 4, y - 3, 8, 2); ctx.fillRect(x - 4, y + 1, 8, 2); }
      }
      UJ.rotulo(ctx, lz, 'El depurador: pausa la ejecución y muestra el estado', W / 2, 14, { tam: 24, peso: 800, color: A });

      // Editor detenido en la linea 15
      L.rectRed(ctx, 20, 58, 450, 210, 10); L.rellena(ctx, L.tono(T, -0.55));
      L.rectRed(ctx, 20, 58, 450, 30, 10); L.rellena(ctx, L.tono(T, -0.3));
      mono('ServicioClinica.java', 36, 65, 15, '#C8D3DC');
      var cod = ['Mascota buscarPorId(String buscado) {', '  for (Mascota m : mascotas) {', '    String id = m.getId();',
                 '    if (id.equals(buscado))', '      return m;'];
      for (var i = 0; i < cod.length; i++) {
        var y = 96 + i * 32;
        if (i === 3) {
          ctx.fillStyle = L.tono(AMA, 0, 0.3); ctx.fillRect(22, y - 2, 446, 30);
          punto(32, y + 13, true);
          ctx.beginPath(); ctx.moveTo(44, y + 6); ctx.lineTo(54, y + 13); ctx.lineTo(44, y + 20); ctx.closePath();
          ctx.fillStyle = AMA; ctx.fill();
        }
        mono(String(12 + i), 76, y + 5, 15, '#7F8C99', 'right');
        mono(cod[i], 86, y + 4, 17, '#E8F4FA');
      }

      // Leyenda del margen
      punto(34, 293, false);
      UJ.rotulo(ctx, lz, 'Breakpoint: clic en el margen o F9', 52, 282, { tam: 18, alinear: 'left' });
      punto(34, 333, true);
      UJ.rotulo(ctx, lz, 'Condicional:', 52, 322, { tam: 18, peso: 700, alinear: 'left', color: R });
      UJ.codigo(ctx, lz, 172, 316, 214, 'id.equals("M009")', 1, 16);
      UJ.rotulo(ctx, lz, 'se detiene solo en el caso problemático', 52, 358, { tam: 17, alinear: 'left' });
      ctx.fillStyle = L.tono(AMA, 0, 0.45); ctx.fillRect(24, 396, 22, 20);
      UJ.rotulo(ctx, lz, 'F5 arranca y se pausa en esa línea', 52, 394, { tam: 17, alinear: 'left' });

      // Paneles del depurador
      function panel(x, y, titulo, filas, c) {
        var an = 290, cab = 36, fila = 34;
        L.rectRed(ctx, x, y, an, cab + filas.length * fila, 8); L.rellena(ctx, m.papel, L.tono(c, 0.5), 2);
        L.rectRed(ctx, x, y, an, cab, 8); L.rellena(ctx, c);
        UJ.rotulo(ctx, lz, titulo, x + 12, y + 8, { tam: 18, peso: 700, alinear: 'left', color: m.papel });
        for (var k = 0; k < filas.length; k++) mono(filas[k], x + 12, y + cab + 8 + k * fila, 17, T);
        return y + cab + filas.length * fila;
      }
      panel(490, 58, 'Variables · estado real', ['id = "M009"', 'buscado = "M009"'], A);
      panel(490, 176, 'Watch · una expresión', ['mascotas.size() = 12'], C);
      var fin = panel(490, 264, 'Call Stack · quién llamó', ['ServicioClinica.buscarPorId', 'ClinicaApp.buscarPorId'], L.tono(A, -0.3));
      UJ.rotulo(ctx, lz, 'arriba, el método detenido; debajo, el que lo llamó', 635, fin + 10, { tam: 16, ancho: 280 });

      // Teclas para avanzar
      UJ.rotulo(ctx, lz, 'Desde la pausa, se avanza con el teclado', 20, 446, { tam: 19, peso: 700, alinear: 'left', color: A });
      var teclas = [['F5', 'continúa al siguiente breakpoint'], ['F10', 'pasa a la línea siguiente'], ['F11', 'entra al método'], ['Mayús+F11', 'sale del método']];
      for (var k = 0; k < teclas.length; k++) {
        var x = 20 + k * 192;
        L.rectRed(ctx, x, 484, 176, 52, 10); L.rellena(ctx, L.tono(T, 0.6));
        L.rectRed(ctx, x, 480, 176, 50, 10); L.rellena(ctx, L.tono(T, 0.94), L.tono(T, 0.45), 2);
        UJ.rotulo(ctx, lz, teclas[k][0], x + 88, 491, { tam: 22, peso: 800 });
        UJ.rotulo(ctx, lz, teclas[k][1], x + 88, 548, { tam: 17, ancho: 170 });
      }
    }
  });
})();
