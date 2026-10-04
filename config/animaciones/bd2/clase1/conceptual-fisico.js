/* Nivel conceptual (entidades y relaciones con vocabulario de negocio) y nivel fisico (tablas con
 * columnas tipadas, restricciones y claves): dos vistas del mismo modelo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('conceptual-fisico', {
    duracion: 4.5,
    pasos: [0.34, 0.74, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'NIVEL CONCEPTUAL · vocabulario de negocio', W / 2, 20, { tam: 18, peso: 800, color: C, visible: L.tramo(t, 0, 0.08) });
      UJ.caja(ctx, lz, 90, 62, 200, 76, 'Dueño', null, C, L.tramo(t, 0.04, 0.12));
      UJ.caja(ctx, lz, 510, 62, 200, 76, 'Mascota', null, C, L.tramo(t, 0.1, 0.18));
      L.flecha(ctx, 296, 100, 504, 100, L.tono(C, -0.2), 4, L.tramo(t, 0.16, 0.26));
      UJ.rotulo(ctx, lz, 'posee', 400, 66, { tam: 20, peso: 700, color: L.tono(C, -0.3), visible: L.tramo(t, 0.22, 0.3) });
      UJ.rotulo(ctx, lz, 'NIVEL FÍSICO · tablas, tipos, restricciones, claves', W / 2, 186, { tam: 18, peso: 800, color: A, visible: L.tramo(t, 0.38, 0.46) });
      var n = L.tramo(t, 0.42, 0.68) * 3.2;
      if (n > 0) {
        UJ.tabla(ctx, lz, 24, 222, 370, 'dueno', ['id_dueno SERIAL PK', 'nombre VARCHAR(80)', 'telefono VARCHAR(30) NOT NULL'], n, A);
        UJ.tabla(ctx, lz, 406, 222, 370, 'mascota', ['id_mascota SERIAL PK', 'nombre VARCHAR(60)', 'id_dueno INT FK → dueno'], n, A);
      }
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.9), function () {
        ctx.setLineDash([8, 8]);
        L.flecha(ctx, 190, 142, 190, 178, L.tono(m.tinta, 0.4), 3);
        L.flecha(ctx, 610, 142, 610, 178, L.tono(m.tinta, 0.4), 3);
        ctx.setLineDash([]);
        L.rectRed(ctx, 60, 470, W - 120, 110, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Dos vistas del MISMO modelo', W / 2, 486, { tam: 25, peso: 800 });
        UJ.rotulo(ctx, lz, 'diagrama ER (conceptual) · CREATE TABLE (físico)', W / 2, 530, { tam: 19, ancho: W - 160 });
      });
    }
  });
})();
