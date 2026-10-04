/* Consistencia: valido es lo que las restricciones declaran. La atomicidad no la produce: el
 * mismo UPDATE confirmado completo deja stock en -7 si la tabla no declara CHECK (stock >= 0). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('consistencia-restriccion', {
    duracion: 4.8,
    // Pasos LOGICOS: 1) sin restriccion, el UPDATE deja -7 y confirma; 2) con CHECK, el mismo
    // UPDATE se rechaza; 3) la idea: atomicidad no es consistencia.
    pasos: [0.47, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.codigo(ctx, lz, 24, 20, W - 48, 'UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;', L.tramo(t, 0, 0.16), 17);
      // Sin restriccion
      UJ.rotulo(ctx, lz, 'Sin restricción', 200, 96, { tam: 24, peso: 800, color: R, visible: L.tramo(t, 0.16, 0.22) });
      var s = Math.round(L.mezcla(3, -7, L.tramo(t, 0.22, 0.38, 'suave')));
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.22), function () {
        L.rectRed(ctx, 60, 140, 280, 150, 16); L.rellena(ctx, s < 0 ? L.tono(R, 0.85) : L.tono(A, 0.92), s < 0 ? R : A, 3);
        UJ.rotulo(ctx, lz, 'stock', 200, 156, { tam: 20 });
        UJ.rotulo(ctx, lz, String(s), 200, 190, { tam: 64, peso: 800, color: s < 0 ? R : A });
      });
      UJ.rotulo(ctx, lz, 'COMMIT sin quejarse', 200, 306, { tam: 19, peso: 700, visible: L.tramo(t, 0.38, 0.44) });
      UJ.rotulo(ctx, lz, 'atómico, pero inválido', 200, 336, { tam: 19, color: R, visible: L.tramo(t, 0.4, 0.46) });
      // Con CHECK
      UJ.rotulo(ctx, lz, 'Con CHECK', 600, 96, { tam: 24, peso: 800, color: V, visible: L.tramo(t, 0.5, 0.56) });
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.58), function () {
        L.rectRed(ctx, 460, 140, 280, 150, 16); L.rellena(ctx, L.tono(A, 0.92), A, 3);
        UJ.rotulo(ctx, lz, 'stock', 600, 156, { tam: 20 });
        UJ.rotulo(ctx, lz, '3', 600, 190, { tam: 64, peso: 800, color: A });
      });
      UJ.sello(ctx, lz, 740, 140, 32, false, L.tramo(t, 0.6, 0.68));
      UJ.alfa(ctx, L.tramo(t, 0.62, 0.7), function () {
        UJ.codigo(ctx, lz, 440, 306, 330, 'stock INT CHECK (stock >= 0)', 1, 16);
      });
      UJ.rotulo(ctx, lz, 'el motor rechaza el UPDATE', 600, 360, { tam: 19, color: V, peso: 700, visible: L.tramo(t, 0.68, 0.76) });
      // La idea
      UJ.alfa(ctx, L.tramo(t, 0.8, 0.9), function () {
        L.rectRed(ctx, 40, 420, 720, 160, 16); L.rellena(ctx, L.tono(A, 0.94), A, 2);
        UJ.rotulo(ctx, lz, 'La atomicidad NO produce consistencia.', 400, 442, { tam: 24, peso: 800, color: A, ancho: 680 });
        UJ.rotulo(ctx, lz, 'Válido = lo que cumplen PK, FK, UNIQUE, NOT NULL, CHECK y triggers.', 400, 494, { tam: 19, ancho: 680 });
        UJ.rotulo(ctx, lz, 'Se declara una vez y vale para quien escriba después.', 400, 536, { tam: 19, ancho: 680 });
      });
    }
  });
})();
