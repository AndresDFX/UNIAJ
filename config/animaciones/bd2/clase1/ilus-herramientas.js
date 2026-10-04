/* Ilustracion: las herramientas del dia, en el orden en que se usan, y lo que demuestra cada una.
 * Boceto (pensar) -> PostgreSQL en el navegador (el DDL corre y el error es real) -> visor Mermaid
 * (el texto erDiagram se dibuja). La fuente de verdad es el archivo .sql, no la pestana. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-herramientas', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Tres herramientas, tres preguntas', W / 2, 12, { tam: 25, peso: 800, color: A });
      var h = [
        ['draw.io · Excalidraw', '¿cómo es el modelo?', 'cajas y relaciones a mano alzada', C],
        ['DB Fiddle (PostgreSQL)', '¿el DDL corre?', 'CREATE TABLE, INSERT y el error real del motor', A],
        ['Visor Mermaid', '¿el diagrama se dibuja?', 'el texto erDiagram, renderizado', V]
      ];
      for (var i = 0; i < 3; i++) {
        var y = 62 + i * 140;
        L.rectRed(ctx, 30, y, 300, 108, 14); L.rellena(ctx, L.tono(h[i][3], 0.88), h[i][3], 3);
        UJ.rotulo(ctx, lz, h[i][0], 180, y + 18, { tam: 20, peso: 800, color: h[i][3], ancho: 280 });
        UJ.rotulo(ctx, lz, h[i][1], 180, y + 60, { tam: 19, peso: 600, ancho: 280 });
        UJ.rotulo(ctx, lz, h[i][2], 350, i === 1 ? y + 6 : y + 40, { tam: 18, alinear: 'left', ancho: 420 });
        if (i < 2) L.flecha(ctx, 180, y + 112, 180, y + 136, L.tono(m.tinta, 0.4), 3, 1);
      }
      // Lo que se ve en vivo con PostgreSQL
      UJ.codigo(ctx, lz, 350, 240, 420, 'VALUES (999, ...)  -- no existe', 1, 15);
      UJ.rotulo(ctx, lz, 'ERROR: violates foreign key constraint', 360, 280, { tam: 15, peso: 700, color: R, alinear: 'left', ancho: 410 });
      // Regla
      L.rectRed(ctx, 30, 488, W - 60, 112, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Fuente de verdad: el archivo .sql de la carpeta', W / 2, 502, { tam: 22, peso: 800, ancho: W - 100 });
      UJ.rotulo(ctx, lz, 'DB Fiddle no guarda nada: si el esquema se reconstruye pegando el .sql, vas bien', W / 2, 542, { tam: 18, ancho: W - 100 });
    }
  });
})();
