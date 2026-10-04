/* Incremento contra iteración: arriba el sistema gana piezas nuevas; abajo el mismo mockup
 * vuelve a la mesa y mejora con lo que pidió la veterinaria. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('iteracion-incremento', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, C = m.acento, W = lz.ancho;
      // ---- Incremento
      UJ.rotulo(ctx, lz, 'Incremento: se agrega una pieza nueva', 26, 20, { tam: 22, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0, 0.06) });
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.1), function () {
        L.rectRed(ctx, 26, 62, 748, 170, 14); L.rellena(ctx, L.tono(m.gris, 0.93), L.tono(m.gris, 0.4), 2);
        UJ.rotulo(ctx, lz, 'El sistema', 46, 74, { tam: 17, peso: 700, color: m.gris, alinear: 'left' });
      });
      function pieza(x, nombre, c, p) {
        if (p <= 0) return;
        var y = 110 + (1 - p) * -40;
        UJ.alfa(ctx, p, function () {
          L.rectRed(ctx, x, y, 220, 90, 12); L.rellena(ctx, L.tono(c, 0.85), c, 3);
          UJ.rotulo(ctx, lz, nombre, x + 110, y + 32, { tam: 20, peso: 800, color: L.tono(c, -0.3), ancho: 200 });
        });
      }
      pieza(50, 'Ficha del paciente', A, L.tramo(t, 0.1, 0.2, 'frena'));
      pieza(290, 'Historial', A, L.tramo(t, 0.24, 0.34, 'frena'));
      UJ.pildora(ctx, lz, 530, 136, '+ pieza nueva y utilizable', V, L.tramo(t, 0.3, 0.38), { tam: 17 });
      // ---- Iteración
      UJ.rotulo(ctx, lz, 'Iteración: se mejora lo que ya existe', 26, 262, { tam: 22, peso: 800, color: C, alinear: 'left', visible: L.tramo(t, 0.42, 0.48) });
      function mockup(x, y, titulo, campos, nuevos, c, a) {
        UJ.alfa(ctx, a, function () {
          var al = 52 + campos.length * 34;
          L.rectRed(ctx, x, y, 210, al, 10); L.rellena(ctx, m.papel, c, 2.5);
          UJ.rotulo(ctx, lz, titulo, x + 105, y + 12, { tam: 18, peso: 800, color: L.tono(c, -0.3) });
          for (var i = 0; i < campos.length; i++) {
            var fy = y + 46 + i * 34, nuevo = i >= campos.length - nuevos;
            L.rectRed(ctx, x + 12, fy, 186, 28, 5);
            L.rellena(ctx, nuevo ? L.tono(V, 0.8) : L.tono(m.gris, 0.9), nuevo ? V : L.tono(m.gris, 0.5), 1.5);
            UJ.rotulo(ctx, lz, campos[i], x + 22, fy + 5, { tam: 16, peso: nuevo ? 700 : 500, color: m.tinta, alinear: 'left' });
          }
        });
      }
      mockup(26, 312, 'Mockup ficha v1', ['Nombre', 'Especie', 'Dueño'], 0, C, L.tramo(t, 0.46, 0.53));
      var vb = L.tramo(t, 0.56, 0.64);
      UJ.flecha(ctx, lz, 240, 400, 310, 400, C, L.tramo(t, 0.54, 0.58));
      UJ.alfa(ctx, vb, function () {
        L.rectRed(ctx, 318, 300, 186, 66, 12); L.rellena(ctx, m.papel, m.malva, 2.5);
        ctx.beginPath(); ctx.moveTo(400, 365); ctx.lineTo(412, 382); ctx.lineTo(420, 365); ctx.closePath(); ctx.fillStyle = m.malva; ctx.fill();
        UJ.rotulo(ctx, lz, '«faltan alergias y foto»', 411, 310, { tam: 17, peso: 700, color: m.malva, ancho: 170 });
        UJ.monigote(ctx, lz, 411, 392, 82, 'la veterinaria', m.tinta, 1);
      });
      UJ.flecha(ctx, lz, 512, 400, 566, 400, C, L.tramo(t, 0.66, 0.7));
      mockup(568, 300, 'Mockup ficha v2', ['Nombre', 'Especie', 'Dueño', 'Alergias', 'Foto'], 2, C, L.tramo(t, 0.7, 0.8));
      UJ.rotulo(ctx, lz, 'Incremento agrega; iteración mejora.', W / 2, 562,
        { tam: 24, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
