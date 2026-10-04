/* El ciclo de Scrum: tres roles, el camino del Product Backlog al Sprint con su Diaria, y el
 * Incremento que pasa por Revisión y Retrospectiva antes de volver a empezar. */
(function () {
  var L = FP_LIENZO;
  function bloque(ctx, lz, x, y, an, al, titulo, sub, c, a) {
    UJ.alfa(ctx, a, function () {
      L.rectRed(ctx, x, y, an, al, 12); L.rellena(ctx, L.tono(c, 0.88), c, 2.5);
      var h = L.texto(ctx, titulo, -9999, -9999, { tam: 19, peso: 800, letra: lz.letra, ancho: an - 16 });
      var hs = sub ? L.texto(ctx, sub, -9999, -9999, { tam: 16, peso: 500, letra: lz.letra, ancho: an - 16 }) + 4 : 0;
      var y0 = y + (al - h - hs) / 2;
      UJ.rotulo(ctx, lz, titulo, x + an / 2, y0, { tam: 19, peso: 800, color: L.tono(c, -0.3), ancho: an - 16 });
      if (sub) UJ.rotulo(ctx, lz, sub, x + an / 2, y0 + h + 4, { tam: 16, peso: 500, color: lz.marca.tinta, ancho: an - 16 });
    });
  }
  FP_ANIMADOR.registrar('ciclo-scrum', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.28, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Scrum: roles, eventos y artefactos', W / 2, 18, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      // Roles
      var roles = [['Product Owner', 'qué y en qué orden'], ['Scrum Master', 'facilita, no es el jefe'], ['Equipo', 'cómo']];
      for (var i = 0; i < 3; i++) {
        bloque(ctx, lz, 26 + i * 254, 62, 240, 74, roles[i][0], roles[i][1], m.malva, L.tramo(t, 0.06 + i * 0.06, 0.14 + i * 0.06));
      }
      // Camino al sprint
      var a1 = L.tramo(t, 0.3, 0.37), a2 = L.tramo(t, 0.38, 0.45), a3 = L.tramo(t, 0.46, 0.53), a4 = L.tramo(t, 0.54, 0.62);
      bloque(ctx, lz, 26, 215, 150, 110, 'Product Backlog', 'la lista de todo', A, a1);
      UJ.flecha(ctx, lz, 178, 270, 202, 270, A, a2);
      bloque(ctx, lz, 204, 235, 150, 70, 'Planificación', null, C, a2);
      UJ.flecha(ctx, lz, 356, 270, 378, 270, A, a3);
      bloque(ctx, lz, 380, 225, 168, 90, 'Sprint Backlog', 'lo de este sprint', A, a3);
      UJ.flecha(ctx, lz, 550, 270, 576, 270, A, a4);
      UJ.alfa(ctx, a4, function () {
        L.circulo(ctx, 680, 270, 100); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'Sprint', 680, 192, { tam: 22, peso: 800, color: L.tono(V, -0.35) });
        UJ.rotulo(ctx, lz, '1 a 4 semanas', 680, 220, { tam: 17, peso: 600, color: m.tinta });
        var g = (t * 6) % 1;
        L.circulo(ctx, 680, 280, 22); L.rellena(ctx, m.papel, V, 3);
        L.flecha(ctx, 680 + 22 * Math.cos(g * 6.28), 280 + 22 * Math.sin(g * 6.28),
          680 + 22 * Math.cos(g * 6.28 + 0.6), 280 + 22 * Math.sin(g * 6.28 + 0.6), V, 3, 1);
        UJ.rotulo(ctx, lz, 'Diaria · 15 min', 680, 312, { tam: 16, peso: 700, color: L.tono(V, -0.35) });
      });
      // Del incremento de vuelta al backlog
      var b1 = L.tramo(t, 0.66, 0.74), b2 = L.tramo(t, 0.74, 0.82), b3 = L.tramo(t, 0.82, 0.9), b4 = L.tramo(t, 0.9, 0.97);
      UJ.flecha(ctx, lz, 680, 372, 680, 418, V, b1);
      bloque(ctx, lz, 560, 420, 214, 84, 'Incremento', 'cumple la Definición de Terminado', V, b1);
      UJ.flecha(ctx, lz, 558, 462, 532, 462, A, b2);
      bloque(ctx, lz, 316, 420, 214, 84, 'Revisión', 'con el cliente', C, b2);
      UJ.flecha(ctx, lz, 314, 462, 288, 462, A, b3);
      bloque(ctx, lz, 26, 420, 260, 84, 'Retrospectiva', 'mejorar cómo se trabaja', C, b3);
      UJ.flecha(ctx, lz, 101, 418, 101, 330, A, b4);
      UJ.alfa(ctx, b4, function () {
        UJ.rotulo(ctx, lz, 'vuelve', 112, 362, { tam: 17, peso: 700, color: A, alinear: 'left' });
      });
      UJ.rotulo(ctx, lz, 'Cada sprint termina en algo que el cliente puede ver.', W / 2, 560,
        { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
