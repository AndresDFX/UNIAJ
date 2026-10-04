/* Tablero Kanban con límite 2 en «Modelando»: la tercera tarjeta rebota hasta que otra termina.
 * La columna «Aprobado» tiene su política explícita. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('kanban-wip', {
    duracion: 5,
    // Pasos LOGICOS: 1) el tablero con limite 2 lleno; 2) la tercera tarjeta rebota; 3) una
    // termina y recien entonces entra la siguiente; 4) la politica explicita de «Aprobado».
    pasos: [0.3, 0.6, 0.88, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      function cx(i) { return 26 + i * 190; }
      var cols = ['Por hacer', 'Modelando', 'En revisión del cliente', 'Aprobado'];
      var ap = L.tramo(t, 0, 0.08);
      UJ.alfa(ctx, ap, function () {
        for (var i = 0; i < 4; i++) {
          L.rectRed(ctx, cx(i), 20, 178, 500, 12); L.rellena(ctx, L.tono(i === 1 ? A : m.gris, 0.92), L.tono(m.gris, 0.5), 2);
          UJ.rotulo(ctx, lz, cols[i], cx(i) + 89, (i === 1 || i === 2) ? 30 : 50, { tam: 19, peso: 800, color: i === 1 ? A : m.tinta, ancho: 160 });
          L.trazo(ctx, [[cx(i) + 10, 110], [cx(i) + 168, 110]], 1, L.tono(m.gris, 0.4), 2);
        }
      });
      UJ.pildora(ctx, lz, cx(1) + 89, 62, 'límite 2', R, ap, { tam: 16, centrar: true });
      function slot(k) { return 124 + k * 70; }
      function tarjeta(nombre, x, y, color) {
        L.rectRed(ctx, x, y, 158, 56, 8); L.rellena(ctx, m.papel, color, 2.5);
        L.rectRed(ctx, x, y, 8, 56, 4); L.rellena(ctx, color);
        var h = L.texto(ctx, nombre, -9999, -9999, { tam: 17, peso: 700, letra: lz.letra, ancho: 140 });
        UJ.rotulo(ctx, lz, nombre, x + 83, y + (56 - h) / 2 + 1, { tam: 17, peso: 700, color: m.tinta, ancho: 140 });
      }
      // A y B entran a Modelando; C espera
      var pa = L.tramo(t, 0.1, 0.2, 'suave'), pb = L.tramo(t, 0.16, 0.26, 'suave');
      var pa2 = L.tramo(t, 0.64, 0.74, 'suave');
      var xa = cx(0) + 10 + 190 * pa + 190 * pa2, ya = slot(0);
      var xb = cx(0) + 10 + 190 * pb, yb = slot(1);
      // C: intenta entrar y rebota (0.32-0.48), entra de verdad tras la salida de A (0.78-0.86)
      var ida = L.tramo(t, 0.32, 0.4, 'suave'), vuelta = L.tramo(t, 0.42, 0.5, 'suave');
      var entra = L.tramo(t, 0.78, 0.86, "suave");
      var xc = cx(0) + 10 + 110 * ida - 110 * vuelta + 190 * entra;
      var yc = slot(2) + (slot(0) - slot(2)) * entra;
      UJ.alfa(ctx, ap, function () {
        tarjeta('Registrar mascota', xa, ya, A);
        tarjeta('Agendar cita', xb, yb, A);
        tarjeta('Historial clínico', xc, yc, m.acento);
      });
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.44) * (1 - L.tramo(t, 0.76, 0.8)), function () {
        UJ.sello(ctx, lz, cx(1) + 89, slot(2) + 28, 24, false, 1);
        UJ.rotulo(ctx, lz, 'ya hay 2 en curso', cx(1) + 89, slot(2) + 62, { tam: 17, peso: 700, color: R });
      });
      UJ.alfa(ctx, L.tramo(t, 0.74, 0.78), function () {
        UJ.rotulo(ctx, lz, 'una terminó', cx(2) + 89, slot(0) + 66, { tam: 17, peso: 700, color: m.verde });
      });
      // Política explícita de Aprobado
      UJ.alfa(ctx, L.tramo(t, 0.89, 0.97), function () {
        L.rectRed(ctx, cx(3) + 10, 330, 158, 170, 10); L.rellena(ctx, L.tono(m.sello, 0.8), L.tono(m.sello, -0.2), 2);
        UJ.rotulo(ctx, lz, 'Política', cx(3) + 89, 342, { tam: 17, peso: 800, color: m.tinta });
        UJ.rotulo(ctx, lz, 'diagrama + mockup + visto bueno', cx(3) + 89, 374, { tam: 17, peso: 600, color: m.tinta, ancho: 140 });
      });
      UJ.rotulo(ctx, lz, 'Terminar antes de empezar.', W / 2, 556,
        { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0.82, 0.87) });
    }
  });
})();
