/* Del programa en linea recta al evento: main -> a() -> b() -> fin; luego setVisible(true)
 * arranca el EDT, que toma los eventos de la cola (clic, tecla) y avisa al listener registrado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('edt-eventos', {
    duracion: 5,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Antes: en línea recta', 40, 20, { tam: 20, peso: 700, color: A, alinear: 'left' });
      var pasos = ['main()', 'a()', 'b()', 'fin'];
      for (var i = 0; i < 4; i++) {
        var a = L.tramo(t, 0.03 + i * 0.05, 0.08 + i * 0.05);
        UJ.caja(ctx, lz, 40 + i * 190, 60, 140, 56, pasos[i], null, i === 3 ? (m.gris || m.tinta) : A, a);
        if (i > 0) UJ.alfa(ctx, a, function () { L.flecha(ctx, 40 + (i - 1) * 190 + 144, 88, 40 + i * 190 - 6, 88, m.tinta, 3, 1); });
      }
      UJ.rotulo(ctx, lz, 'main llama, el otro método llama… y el programa termina.', 40, 130, { tam: 17, alinear: 'left', ancho: 720, visible: L.tramo(t, 0.22, 0.28) });
      // EDT
      UJ.alfa(ctx, L.tramo(t, 0.33, 0.36), function () {
        ctx.strokeStyle = L.tono(m.tinta, 0.75); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(20, 170); ctx.lineTo(W - 20, 170); ctx.stroke();
      });
      UJ.rotulo(ctx, lz, 'Con setVisible(true) arranca el EDT', 40, 186, { tam: 20, peso: 700, color: C, alinear: 'left', visible: L.tramo(t, 0.34, 0.4) });
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.44), function () {
        L.rectRed(ctx, 40, 250, 380, 84, 12); L.rellena(ctx, L.tono(S, 0.88), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'cola de eventos', 230, 342, { tam: 17, peso: 700 });
        L.circulo(ctx, 580, 292, 66); L.rellena(ctx, L.tono(C, 0.85), C, 4);
        UJ.rotulo(ctx, lz, 'EDT', 580, 262, { tam: 28, peso: 800, color: C });
        UJ.rotulo(ctx, lz, 'espera acciones', 580, 300, { tam: 15 });
        L.flecha(ctx, 424, 292, 510, 292, m.tinta, 3, 1);
      });
      // listener
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.78), function () {
        L.flecha(ctx, 580, 362, 580, 420, m.tinta, 3, 1);
        L.rectRed(ctx, 400, 426, 360, 100, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'listener registrado en el botón', 580, 500, { tam: 17, peso: 700, color: V });
      });
      // eventos en la cola; el primero (a la derecha) viaja al EDT y luego al listener
      var ev = ['tecla', 'clic', 'clic'];
      for (var k = 0; k < 3; k++) {
        var en = L.tramo(t, 0.44 + k * 0.05, 0.5 + k * 0.05, 'frena');
        if (en <= 0) continue;
        var x = L.mezcla(-110, 56 + k * 120, en), y = 270;
        if (k === 2) {
          var v1 = L.tramo(t, 0.7, 0.78, 'suave'), v2 = L.tramo(t, 0.8, 0.88, 'suave');
          x = L.mezcla(L.mezcla(x, 530, v1), 420, v2); y = L.mezcla(L.mezcla(y, 270, v1), 446, v2);
        }
        L.rectRed(ctx, x, y, 100, 44, 10); L.rellena(ctx, k === 2 ? L.tono(R, 0.82) : L.tono(A, 0.85), k === 2 ? R : A, 2);
        UJ.rotulo(ctx, lz, ev[k], x + 50, y + 11, { tam: 18, peso: 700 });
      }
      UJ.rotulo(ctx, lz, '→ actionPerformed(e)', 640, 456, { tam: 19, peso: 700, color: V, visible: L.tramo(t, 0.86, 0.9) });
      UJ.rotulo(ctx, lz, 'Su código no se llama desde main: queda registrado y lo dispara el usuario.', W / 2, 570, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
