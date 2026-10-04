/* Cambiar el esquema sin romper: nunca en su lugar. Ejemplo: registrar la fecha en que una mascota
 * se inactivo. Expandir, escribir en ambos lados, rellenar por lotes, mover lecturas y contraer.
 * A la derecha, en cada fase, si la aplicacion vieja y la nueva siguen funcionando: conviven. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('expandir-contraer', {
    duracion: 5,
    // Pasos LOGICOS: una fase por clic (cinco) y la regla al final. En cada fase se ve completa
    // su fila y si las dos versiones de la aplicacion siguen andando.
    pasos: [0.16, 0.32, 0.48, 0.64, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var gris = L.tono(m.tinta, 0.45);
      UJ.rotulo(ctx, lz, 'Agregar fecha_inactivacion a mascota sin romper nada', 20, 8, { tam: 19, peso: 800, color: A, alinear: 'left', ancho: 580 });
      UJ.rotulo(ctx, lz, 'app vieja', 645, 44, { tam: 15, peso: 800, color: L.tono(m.tinta, 0.2) });
      UJ.rotulo(ctx, lz, 'app nueva', 735, 44, { tam: 15, peso: 800, color: L.tono(m.tinta, 0.2) });
      var fases = [
        ['1 · Expandir', 'ADD COLUMN fecha_inactivacion DATE (admite nulos)', 1, 0],
        ['2 · Escribir en ambos lados', 'sp_inactivar_mascota llena activa y la fecha', 1, 1],
        ['3 · Rellenar el histórico', 'UPDATE por lotes, nunca uno gigante que bloquee', 1, 1],
        ['4 · Mover las lecturas', 'reportes y pantallas leen la columna nueva', 1, 1],
        ['5 · Contraer', 'si la fecha reemplaza a activa: borrar activa cuando nadie la lea', -1, 1]
      ];
      var ini = [0.02, 0.18, 0.34, 0.5, 0.66];
      for (var i = 0; i < 5; i++) {
        var f = fases[i], y = 72 + i * 84, a = L.tramo(t, ini[i], ini[i] + 0.08);
        UJ.alfa(ctx, a, function () {
          var col = i === 4 ? C : A;
          L.rectRed(ctx, 20, y, 570, 74, 12); L.rellena(ctx, L.tono(col, 0.9), col, 2);
          UJ.rotulo(ctx, lz, f[0], 36, y + 8, { tam: 20, peso: 800, alinear: 'left', color: i === 4 ? L.tono(C, -0.3) : A });
          UJ.rotulo(ctx, lz, f[1], 36, y + 42, { tam: 15, peso: 500, alinear: 'left', ancho: 540 });
        });
        var b = L.tramo(t, ini[i] + 0.08, ini[i] + 0.12);
        var marcas = [[645, f[2]], [735, f[3]]];
        for (var k = 0; k < 2; k++) {
          var mx = marcas[k][0], v = marcas[k][1];
          if (v === 1) UJ.sello(ctx, lz, mx, y + 37, 17, true, b);
          else UJ.alfa(ctx, b, function () {
            L.trazo(ctx, [[mx - 14, y + 37], [mx + 14, y + 37]], 1, gris, 4);
            UJ.rotulo(ctx, lz, v === 0 ? 'aún no' : 'retirada', mx, y + 50, { tam: 13, peso: 700, color: gris });
          });
        }
      }
      // La regla
      UJ.rotulo(ctx, lz, 'Nunca se cambia en su lugar: se expande, se migra y se contrae.', W / 2, 508,
                { tam: 20, peso: 800, ancho: W - 40, visible: L.tramo(t, 0.82, 0.9) });
      UJ.rotulo(ctx, lz, 'Con procedimientos igual: un parámetro nuevo al final con DEFAULT no rompe; cambiar el orden o el tipo sí, y entonces se publica sp_agendar_cita_v2.', W / 2, 552,
                { tam: 15, ancho: W - 60, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
