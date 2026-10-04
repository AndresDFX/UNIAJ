/* Q&A de modelado: ¿que pasa si un dueno tiene dos mascotas llamadas Pelusa? Nada: la identidad la
 * da id_mascota. Si se quisiera prohibir, UNIQUE (id_dueno, nombre) rechaza la segunda. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dos-pelusa', {
    duracion: 4.8,
    pasos: [0.4, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.rotulo(ctx, lz, '¿Dos mascotas llamadas Pelusa?', W / 2, 16, { tam: 26, peso: 800, color: A });
      UJ.tabla(ctx, lz, 60, 70, 460, 'mascota', ['id_mascota 7 · dueño 3 · Pelusa', 'id_mascota 9 · dueño 3 · Pelusa'], L.claves(t, [[0.04, 0], [0.2, 2]]), A, -1);
      UJ.sello(ctx, lz, 580, 140, 26, true, L.tramo(t, 0.24, 0.32));
      UJ.rotulo(ctx, lz, 'la identidad la da id_mascota, no el nombre', W / 2, 200, { tam: 20, peso: 700, ancho: 700, visible: L.tramo(t, 0.28, 0.38) });
      // Si se quisiera prohibir
      UJ.rotulo(ctx, lz, 'Si se quisiera prohibirlo:', 60, 270, { tam: 21, peso: 800, color: C, alinear: 'left', visible: L.tramo(t, 0.42, 0.46) });
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.44 + 0.02), function () { UJ.codigo(ctx, lz, 60, 310, 680, 'UNIQUE (id_dueno, nombre)', L.tramo(t, 0.44, 0.56), 19); });
      UJ.tabla(ctx, lz, 60, 390, 460, 'mascota', ['id_mascota 7 · dueño 3 · Pelusa', 'id_mascota 9 · dueño 3 · Pelusa'], 1 + L.tramo(t, 0.58, 0.64), C, -1);
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.72), function () {
        ctx.strokeStyle = R; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(70, 496); ctx.lineTo(510, 496); ctx.stroke();
      });
      UJ.sello(ctx, lz, 580, 496, 26, false, L.tramo(t, 0.66, 0.74));
      UJ.rotulo(ctx, lz, 'Decisión que se defiende en cualquiera de los dos sentidos.', W / 2, 560,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
