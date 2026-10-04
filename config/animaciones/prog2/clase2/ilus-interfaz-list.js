/* Ilustracion: la interfaz List. La declaracion pieza por pieza (List<Mascota> es el contrato,
 * new ArrayList<>() la clase que lo cumple), los metodos de toda la clase, el generico que
 * frena un String al compilar y contains/indexOf que comparan con equals. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-interfaz-list', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, Y = m.sello, W = lz.ancho;
      var MONO = 'Consolas, monospace';
      UJ.rotulo(ctx, lz, 'Contrato a la izquierda, clase a la derecha', W / 2, 12, { tam: 25, peso: 800, color: A });

      // La declaracion, con color por pieza (como en el editor)
      var tam = 24, bx = 24, by = 56, ban = W - 48, bal = 48;
      L.rectRed(ctx, bx, by, ban, bal, 8); L.rellena(ctx, L.tono(m.tinta, -0.55));
      var partes = [['List', '#9CDCFE'], ['<Mascota>', Y], [' mascotas = ', '#E8F4FA'],
                    ['new ArrayList<>()', '#7FD99A'], [';', '#E8F4FA']];
      ctx.font = '500 ' + tam + 'px ' + MONO; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      var x = bx + 18, cortes = [];
      for (var i = 0; i < partes.length; i++) {
        ctx.fillStyle = partes[i][1]; ctx.fillText(partes[i][0], x, by + 12);
        var w = ctx.measureText(partes[i][0]).width; cortes.push([x, x + w]); x += w;
      }
      function llave(x1, x2, color, texto) {
        var y = by + bal + 8;
        ctx.strokeStyle = color; ctx.lineWidth = 3; ctx.lineCap = 'round';
        ctx.beginPath(); ctx.moveTo(x1, y - 4); ctx.lineTo(x1, y + 4); ctx.lineTo(x2, y + 4); ctx.lineTo(x2, y - 4); ctx.stroke();
        UJ.rotulo(ctx, lz, texto, (x1 + x2) / 2, y + 12, { tam: 18, peso: 800, color: color });
      }
      llave(cortes[0][0], cortes[1][1], A, 'interfaz: el contrato');
      llave(cortes[3][0], cortes[3][1], V, 'clase: la implementación');

      // Los metodos del contrato
      UJ.rotulo(ctx, lz, 'Lo que promete List (y se usa toda la clase)', W / 2, 160, { tam: 18, peso: 700, color: m.tinta });
      var metodos = [
        ['add(m)', 'agrega al final', A], ['set(i, m)', 'reemplaza la posición i', A],
        ['get(i)', 'lee la posición i', A], ['isEmpty()', '¿está vacía?', A],
        ['size()', 'cuántos hay', A], ['contains(m)', '¿está? · usa equals', C],
        ['remove(i) / remove(m)', 'saca uno', A], ['indexOf(m)', 'posición o -1 · equals', C]
      ];
      for (var k = 0; k < metodos.length; k++) {
        var cx = k % 2 ? 408 : 24, cy = 192 + Math.floor(k / 2) * 50, c = metodos[k][2];
        L.rectRed(ctx, cx, cy, 368, 42, 10); L.rellena(ctx, L.tono(c, 0.9), c, 2);
        L.texto(ctx, metodos[k][0], cx + 14, cy + 10, { tam: 18, peso: 700, color: c === A ? A : L.tono(c, -0.35), letra: MONO });
        L.texto(ctx, metodos[k][1], cx + 354, cy + 11, { tam: 16, peso: 600, color: m.tinta, alinear: 'right', letra: lz.letra });
      }

      // El generico: el error sale al compilar
      L.rectRed(ctx, 24, 404, 368, 216, 14); L.rellena(ctx, L.tono(R, 0.94), R, 2);
      L.rectRed(ctx, 40, 416, 112, 32, 8); L.rellena(ctx, Y);
      L.texto(ctx, '<Mascota>', 96, 421, { tam: 18, peso: 700, color: m.tinta, alinear: 'center', letra: MONO });
      UJ.rotulo(ctx, lz, 'el genérico', 160, 420, { tam: 19, peso: 800, color: m.tinta, alinear: 'left' });
      UJ.codigo(ctx, lz, 40, 466, 290, 'mascotas.add("Luna");', 1, 18);
      UJ.sello(ctx, lz, 360, 484, 20, false, 1);
      UJ.rotulo(ctx, lz, 'un String no es una Mascota', 208, 520, { tam: 18, peso: 600, ancho: 340 });
      UJ.rotulo(ctx, lz, 'error al compilar,', 208, 552, { tam: 19, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'no al ejecutar', 208, 580, { tam: 19, peso: 800, color: R });

      // contains / indexOf comparan con equals
      L.rectRed(ctx, 408, 404, 368, 216, 14); L.rellena(ctx, L.tono(C, 0.92), C, 2);
      UJ.rotulo(ctx, lz, 'contains e indexOf usan equals', 592, 418, { tam: 19, peso: 800, color: L.tono(C, -0.4) });
      for (var j = 0; j < 2; j++) {
        var fx = j ? 612 : 424;
        L.rectRed(ctx, fx, 454, 148, 58, 10); L.rellena(ctx, m.papel, A, 2);
        UJ.rotulo(ctx, lz, 'M-001 · Luna', fx + 74, 460, { tam: 17, peso: 700 });
        UJ.rotulo(ctx, lz, 'objeto ' + (j + 1), fx + 74, 486, { tam: 15, color: m.gris });
      }
      UJ.rotulo(ctx, lz, '≠', 592, 464, { tam: 32, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'sin equals propio, son distintos', 592, 522, { tam: 17, peso: 600 });
      UJ.rotulo(ctx, lz, 'por eso se busca por id, recorriendo:', 592, 548, { tam: 16 });
      UJ.codigo(ctx, lz, 424, 574, 336, 'm.getId().equalsIgnoreCase(id)', 1, 16);
    }
  });
})();
