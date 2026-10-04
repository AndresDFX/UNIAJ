/* Baja logica: DELETE FROM mascota choca con las referencias y borra la historia; marcar
 * activa = 'N' conserva citas, consultas y facturas, y es reversible. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('baja-logica', {
    duracion: 5,
    pasos: [0.4, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // Izquierda: DELETE
      UJ.rotulo(ctx, lz, 'Borrado físico', 200, 20, { tam: 22, peso: 800, color: R, visible: L.tramo(t, 0, 0.06) });
      UJ.codigo(ctx, lz, 20, 60, 360, 'DELETE FROM mascota ...', L.tramo(t, 0.04, 0.14), 17);
      var hijos = ['citas', 'consultas', 'facturas'];
      for (var i = 0; i < 3; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.14 + i * 0.04, 0.2 + i * 0.04), function () {
          L.rectRed(ctx, 40 + i * 112, 200, 100, 46, 8); L.rellena(ctx, L.tono(C, 0.85), C, 2);
          UJ.rotulo(ctx, lz, hijos[i], 90 + i * 112, 212, { tam: 16, peso: 700 });
          L.flecha(ctx, 90 + i * 112, 196, 200, 150, L.tono(m.tinta, 0.4), 2);
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.12, 0.2), function () {
        L.rectRed(ctx, 120, 112, 160, 40, 8); L.rellena(ctx, m.papel, A, 2);
        UJ.rotulo(ctx, lz, 'Luna', 200, 120, { tam: 18, peso: 700, color: A });
      });
      UJ.sello(ctx, lz, 300, 132, 22, false, L.tramo(t, 0.26, 0.32));
      var malos = ['1 · la integridad lo impide', '2 · se pierde la historia', '3 · es irreversible'];
      for (var k = 0; k < 3; k++)
        UJ.rotulo(ctx, lz, malos[k], 30, 290 + k * 40, { tam: 18, peso: 600, alinear: 'left', color: R, visible: L.tramo(t, 0.28 + k * 0.03, 0.34 + k * 0.03) });
      // Derecha: UPDATE
      UJ.rotulo(ctx, lz, 'Baja lógica', 600, 20, { tam: 22, peso: 800, color: V, visible: L.tramo(t, 0.42, 0.48) });
      UJ.codigo(ctx, lz, 420, 60, 360, "UPDATE mascota SET activa = 'N'", L.tramo(t, 0.46, 0.56), 17);
      var act = t >= 0.62 ? "'N'" : "'S'";
      UJ.alfa(ctx, L.tramo(t, 0.5, 0.56), function () {
        L.rectRed(ctx, 480, 112, 240, 40, 8); L.rellena(ctx, t >= 0.62 ? L.tono(m.tinta, 0.85) : m.papel, A, 2);
        UJ.rotulo(ctx, lz, 'Luna · activa = ' + act, 600, 120, { tam: 18, peso: 700, color: A });
      });
      UJ.sello(ctx, lz, 750, 132, 20, true, L.tramo(t, 0.64, 0.7));
      var buenos = ['las referencias siguen válidas', 'historial y facturas intactos', "se revierte con activa = 'S'"];
      for (var j = 0; j < 3; j++)
        UJ.rotulo(ctx, lz, buenos[j], 430, 200 + j * 40, { tam: 18, peso: 600, alinear: 'left', color: V, visible: L.tramo(t, 0.66 + j * 0.03, 0.72 + j * 0.03) });
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.94), function () {
        L.rectRed(ctx, 40, 450, W - 80, 140, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.codigo(ctx, lz, 70, 466, W - 140, "activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N'))", 1, 18);
        UJ.rotulo(ctx, lz, "Las consultas del día filtran WHERE activa = 'S'", W / 2, 522, { tam: 18, peso: 600, ancho: W - 120 });
        UJ.rotulo(ctx, lz, 'Ojo: para la FK, la mascota inactiva sigue existiendo', W / 2, 554, { tam: 18, peso: 700, color: R, ancho: W - 120 });
      });
    }
  });
})();
