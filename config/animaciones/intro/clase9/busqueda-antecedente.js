/* La busqueda de un antecedente como embudo: pregunta, terminos, sitios, filtro y ficha. En el
 * filtro se descarta el blog sin autor y se queda la tesis. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('busqueda-antecedente', {
    duracion: 5,
    // Pasos LOGICOS: uno por paso de la busqueda (pregunta, terminos, sitios, filtro, ficha).
    pasos: [0.16, 0.36, 0.56, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var et = [['1 · Pregunta', '¿cómo manejan los turnos los negocios pequeños?'],
        ['2 · Términos', '«turnos virtuales» · «gestión de filas»'],
        ['3 · Sitios', 'Google Scholar · repositorios · apps existentes']];
      var t0 = [0.02, 0.2, 0.4];
      for (var i = 0; i < 3; i++) {
        var ind = i * 40, y = 20 + i * 104;
        UJ.alfa(ctx, L.tramo(t, t0[i], t0[i] + 0.1), function () {
          L.rectRed(ctx, 30 + ind, y, W - 60 - ind * 2, 88, 14); L.rellena(ctx, L.tono(A, 0.9 - i * 0.05), A, 3);
          UJ.rotulo(ctx, lz, et[i][0], W / 2, y + 10, { tam: 23, peso: 800, color: A });
          UJ.rotulo(ctx, lz, et[i][1], W / 2, y + 48, { tam: 19, ancho: W - 120 - ind * 2 });
        });
      }
      // 4 · Filtro
      UJ.rotulo(ctx, lz, '4 · Filtro', W / 2, 340, { tam: 23, peso: 800, color: A, visible: L.tramo(t, 0.6, 0.65) });
      UJ.caja(ctx, lz, 130, 380, 250, 70, 'blog sin autor', null, R, L.tramo(t, 0.61, 0.68));
      UJ.caja(ctx, lz, 420, 380, 250, 70, 'tesis de 2021', null, V, L.tramo(t, 0.63, 0.7));
      UJ.sello(ctx, lz, 375, 385, 22, false, L.tramo(t, 0.69, 0.74));
      UJ.sello(ctx, lz, 665, 385, 22, true, L.tramo(t, 0.71, 0.76));
      // 5 · Ficha
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.92), function () {
        L.rectRed(ctx, 160, 480, 480, 130, 14); L.rellena(ctx, L.tono(V, 0.9), V, 3);
        UJ.rotulo(ctx, lz, '5 · Ficha', W / 2, 492, { tam: 23, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'autor · año · enlace · qué hace · qué le falta', W / 2, 530, { tam: 19, ancho: 440 });
        UJ.rotulo(ctx, lz, 'le falta: «exige instalar una app»', W / 2, 572, { tam: 18, peso: 700, ancho: 440 });
      });
    }
  });
})();
