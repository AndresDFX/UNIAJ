/* Factory: la ventana pide crear("URGENCIA", "M-001"); la fabrica decide la subclase,
 * construye ConsultaUrgencia y la entrega como el tipo base Consulta. Un tipo que no existe
 * lanza IllegalArgumentException. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('factory-decide', {
    duracion: 4.8,
    pasos: [0.36, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, G = m.gris, W = lz.ancho;
      // Paso 1: el pedido y la decision
      UJ.caja(ctx, lz, 20, 20, 200, 80, 'Ventana', 'pide, no construye', A, L.tramo(t, 0, 0.06));
      L.flecha(ctx, 224, 60, 296, 60, A, 3, L.tramo(t, 0.04, 0.1));
      UJ.caja(ctx, lz, 300, 20, 300, 80, 'FabricaConsultas', 'concentra la decisión', C, L.tramo(t, 0.06, 0.12));
      UJ.codigo(ctx, lz, 20, 116, W - 40, 'Consulta c = FabricaConsultas.crear("URGENCIA", "M-001");', L.tramo(t, 0.08, 0.2), 16);
      var subs = [['ConsultaVacunacion', G], ['ConsultaControl', G], ['ConsultaUrgencia', R]];
      for (var i = 0; i < 3; i++) {
        var x = 20 + i * 260, el = i === 2;
        L.flecha(ctx, 450, 158, x + 120, 192, el ? R : L.tono(G, 0.4), el ? 4 : 2, L.tramo(t, 0.2, 0.26));
        UJ.caja(ctx, lz, x, 196, 240, 66, subs[i][0], el ? '45 min · $120.000' : 'duración y tarifa propias', el ? R : L.tono(G, -0.2), L.tramo(t, 0.22 + i * 0.02, 0.28 + i * 0.02) * (el ? 1 : 0.55));
      }
      UJ.rotulo(ctx, lz, 'La fábrica elige la subclase según el tipo pedido.', 20, 284, { tam: 20, peso: 600, alinear: 'left', visible: L.tramo(t, 0.28, 0.34) });
      // Paso 2: se entrega como el tipo base
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.48), function () {
        L.flecha(ctx, 640, 270, 420, 350, R, 3, L.tramo(t, 0.4, 0.48));
        L.rectRed(ctx, 20, 330, 400, 100, 16); L.rellena(ctx, L.tono(A, 0.9), A, 3);
        UJ.rotulo(ctx, lz, 'Consulta c', 40, 344, { tam: 24, peso: 800, alinear: 'left', color: A });
        UJ.rotulo(ctx, lz, 'tipo base para la ventana', 40, 378, { tam: 17, peso: 500, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'objeto real: ConsultaUrgencia', 40, 401, { tam: 17, peso: 700, alinear: 'left', color: R });
      });
      UJ.rotulo(ctx, lz, 'Las reglas de cada tipo no quedan regadas por la interfaz.', 440, 352, { tam: 18, peso: 600, alinear: 'left', ancho: 330, visible: L.tramo(t, 0.5, 0.62) });
      // Paso 3: un tipo que no existe
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.78), function () {
        UJ.codigo(ctx, lz, 20, 460, 640, 'FabricaConsultas.crear("PELUQUERIA", "M-001");', 1, 16);
      });
      UJ.sello(ctx, lz, 712, 477, 28, false, L.tramo(t, 0.78, 0.86));
      UJ.rotulo(ctx, lz, 'IllegalArgumentException', W / 2, 520, { tam: 24, peso: 800, color: R, visible: L.tramo(t, 0.84, 0.9) });
      UJ.rotulo(ctx, lz, 'El dato basura no llega a objeto.', W / 2, 560, { tam: 21, peso: 600, visible: L.tramo(t, 0.88, 0.97) });
    }
  });
})();
