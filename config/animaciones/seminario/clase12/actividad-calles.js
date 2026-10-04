/* Diagrama de actividades con calles: la atencion completa en la clinica, de la llegada a la
 * factura, con una decision y dos tareas en paralelo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('actividad-calles', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.32, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, T = m.tinta, R = m.malva, V = m.verde, G = m.gris, W = lz.ancho;
      var calles = ['Propietario', 'Recepcionista', 'Veterinario', 'Sistema'];
      var x0 = 20, an = 190, top = 56, base = 616;
      var cx = function (i) { return x0 + an * i + an / 2; };
      UJ.rotulo(ctx, lz, 'Actividades: de la puerta a la factura', W / 2, 14, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      UJ.alfa(ctx, L.tramo(t, 0.02, 0.1), function () {
        for (var i = 0; i < 4; i++) {
          L.rectRed(ctx, x0 + an * i, top, an, base - top, 0); L.rellena(ctx, i % 2 ? L.tono(A, 0.95) : m.papel, L.tono(G, 0.5), 1.5);
          L.rectRed(ctx, x0 + an * i, top, an, 38, 0); L.rellena(ctx, L.tono(A, 0.8), L.tono(G, 0.5), 1.5);
          UJ.rotulo(ctx, lz, calles[i], cx(i), top + 9, { tam: 18, peso: 800, color: L.tono(A, -0.3) });
        }
      });
      function accion(i, y, texto, a, c) {
        UJ.alfa(ctx, a, function () {
          var w = 160, h = 54; c = c || A;
          L.rectRed(ctx, cx(i) - w / 2, y, w, h, 20); L.rellena(ctx, L.tono(c, 0.86), c, 2.5);
          var hh = L.texto(ctx, texto, -9999, -9999, { tam: 17, peso: 700, letra: lz.letra, ancho: w - 10 });
          UJ.rotulo(ctx, lz, texto, cx(i), y + h / 2 - hh / 2, { tam: 17, peso: 700, color: L.tono(c, -0.3), ancho: w - 10 });
        });
      }
      var cl = L.tono(T, 0.15);
      // Paso 1: inicio, llegada, verificacion
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.14), function () { L.circulo(ctx, cx(0), 118, 11); L.rellena(ctx, T); });
      L.flecha(ctx, cx(0), 130, cx(0), 144, cl, 2.5, L.tramo(t, 0.13, 0.16));
      accion(0, 146, 'llega con la mascota', L.tramo(t, 0.15, 0.2));
      L.flecha(ctx, cx(0) + 79, 184, cx(1) - 79, 222, cl, 2.5, L.tramo(t, 0.2, 0.24));
      accion(1, 210, 'verifica la cita', L.tramo(t, 0.24, 0.3));
      // Paso 2: decision
      var ry = 316, rr = 26;
      L.flecha(ctx, cx(1), 266, cx(1), ry - rr - 2, cl, 2.5, L.tramo(t, 0.33, 0.36));
      UJ.alfa(ctx, L.tramo(t, 0.35, 0.4), function () {
        ctx.beginPath(); ctx.moveTo(cx(1), ry - rr); ctx.lineTo(cx(1) + rr, ry); ctx.lineTo(cx(1), ry + rr); ctx.lineTo(cx(1) - rr, ry); ctx.closePath();
        L.rellena(ctx, L.tono(m.sello, 0.6), L.tono(m.sello, -0.4), 2.5);
      });
      L.flecha(ctx, cx(1), ry + rr, cx(1), 380, R, 2.5, L.tramo(t, 0.4, 0.44));
      UJ.alfa(ctx, L.tramo(t, 0.42, 0.46), function () {
        UJ.rotulo(ctx, lz, '[sin cita]', cx(1) - 10, 346, { tam: 16, peso: 700, color: R, alinear: 'right' });
      });
      accion(1, 382, 'reagendar', L.tramo(t, 0.44, 0.49), R);
      L.flecha(ctx, cx(1) + rr, ry, cx(2) - 81, ry, V, 2.5, L.tramo(t, 0.48, 0.52));
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.54), function () {
        UJ.rotulo(ctx, lz, '[con cita]', (cx(1) + rr + cx(2) - 81) / 2 - 2, ry + 8, { tam: 16, peso: 700, color: V });
      });
      accion(2, ry - 27, 'atiende', L.tramo(t, 0.52, 0.57), V);
      L.flecha(ctx, cx(2), ry + 27, cx(2), 380, cl, 2.5, L.tramo(t, 0.57, 0.6));
      accion(2, 382, 'registra la consulta', L.tramo(t, 0.59, 0.64));
      // Paso 3: bifurcacion en paralelo y union
      L.flecha(ctx, cx(2), 438, cx(2), 446, cl, 2.5, L.tramo(t, 0.68, 0.71));
      var bx1 = cx(1) - 40, bx2 = cx(3) + 40;
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.74), function () {
        L.rectRed(ctx, bx1, 448, bx2 - bx1, 8, 2); L.rellena(ctx, T);
      });
      L.flecha(ctx, cx(1), 456, cx(1), 476, cl, 2.5, L.tramo(t, 0.74, 0.77));
      L.flecha(ctx, cx(3), 456, cx(3), 476, cl, 2.5, L.tramo(t, 0.74, 0.77));
      accion(1, 478, 'facturación', L.tramo(t, 0.77, 0.82));
      accion(3, 478, 'programar control', L.tramo(t, 0.77, 0.82));
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.86), function () {
        UJ.rotulo(ctx, lz, 'en paralelo', cx(2), 494, { tam: 17, peso: 800, color: L.tono(A, -0.2) });
      });
      L.flecha(ctx, cx(1), 534, cx(1), 546, cl, 2.5, L.tramo(t, 0.86, 0.89));
      L.flecha(ctx, cx(3), 534, cx(3), 546, cl, 2.5, L.tramo(t, 0.86, 0.89));
      UJ.alfa(ctx, L.tramo(t, 0.88, 0.92), function () {
        L.rectRed(ctx, bx1, 548, bx2 - bx1, 8, 2); L.rellena(ctx, T);
      });
      L.flecha(ctx, cx(2), 556, cx(2), 576, cl, 2.5, L.tramo(t, 0.92, 0.95));
      UJ.alfa(ctx, L.tramo(t, 0.94, 0.98), function () {
        L.circulo(ctx, cx(2), 592, 13); L.rellena(ctx, m.papel, T, 3);
        L.circulo(ctx, cx(2), 592, 7); L.rellena(ctx, T);
      });
    }
  });
})();
