/* El modelo en V: cada nivel de especificacion a la izquierda tiene su nivel de prueba a la
 * derecha, y los dos nacen juntos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('modelo-v', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.42, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, W = lz.ancho;
      var an = 190, al = 56;
      var izq = [[30, 90, 'Requisitos'], [80, 185, 'Diseño de arquitectura'], [130, 280, 'Diseño detallado']];
      var der = [[580, 90, 'Pruebas de aceptación'], [530, 185, 'Pruebas de integración'], [480, 280, 'Pruebas unitarias']];
      function box(x, y, txt, c, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, an, al, 12); L.rellena(ctx, L.tono(c, 0.88), c, 2.5);
          var h = L.texto(ctx, txt, -9999, -9999, { tam: 18, peso: 700, letra: lz.letra, ancho: an - 16 });
          UJ.rotulo(ctx, lz, txt, x + an / 2, y + al / 2 - h / 2, { tam: 18, peso: 700, color: L.tono(c, -0.2), ancho: an - 16 });
        });
      }
      UJ.rotulo(ctx, lz, 'El modelo en V', W / 2, 12, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      for (var i = 0; i < 3; i++) {
        box(izq[i][0], izq[i][1], izq[i][2], A, L.tramo(t, 0.04 + i * 0.05, 0.09 + i * 0.05));
        if (i < 2) UJ.flecha(ctx, lz, izq[i][0] + 40, izq[i][1] + al, izq[i + 1][0] + 40, izq[i + 1][1], A, L.tramo(t, 0.08 + i * 0.05, 0.12 + i * 0.05));
      }
      UJ.flecha(ctx, lz, 170, 336, 300, 400, A, L.tramo(t, 0.18, 0.22));
      box(305, 380, 'Codificación', m.gris, L.tramo(t, 0.2, 0.25));
      UJ.flecha(ctx, lz, 500, 400, 630, 336, V, L.tramo(t, 0.24, 0.28));
      for (var j = 2; j >= 0; j--) {
        var k = 2 - j;
        box(der[j][0], der[j][1], der[j][2], V, L.tramo(t, 0.27 + k * 0.05, 0.32 + k * 0.05));
        if (j > 0) UJ.flecha(ctx, lz, der[j][0] + an - 40, der[j][1], der[j - 1][0] + an - 40, der[j - 1][1] + al, V, L.tramo(t, 0.3 + k * 0.05, 0.34 + k * 0.05));
      }
      // Emparejamientos
      for (var p = 0; p < 3; p++) {
        var y = izq[p][1] + al / 2;
        UJ.linea(ctx, izq[p][0] + an + 6, y, der[p][0] - 6, y, L.tono(m.tinta, 0.35), 2.5, L.tramo(t, 0.44 + p * 0.07, 0.52 + p * 0.07), true);
      }
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.8), function () {
        UJ.pildora(ctx, lz, 400, 54, 'RF-03 ↔ CP-ACEP-07: nacen juntos', m.sello, 1, { tam: 17, centrar: true, lleno: true });
        UJ.linea(ctx, 400, 88, 400, 114, L.tono(m.sello, -0.3), 2.5, 1);
      });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.96), function () {
        UJ.rotulo(ctx, lz, 'Verificar: ¿se construyó bien?', 24, 500, { tam: 21, peso: 700, color: A, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'Validar: ¿se construyó lo correcto?', W - 24, 540, { tam: 21, peso: 700, color: V, alinear: 'right' });
      });
    }
  });
})();
