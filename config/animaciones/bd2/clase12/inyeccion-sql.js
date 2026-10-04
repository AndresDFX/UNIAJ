/* Inyeccion SQL: la aplicacion pega lo que escribio el usuario dentro del texto de la consulta;
 * el motor no distingue que parte es del programador, y la condicion OR 1=1 devuelve toda la tabla. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('inyeccion-sql', {
    duracion: 5,
    pasos: [0.32, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      UJ.rotulo(ctx, lz, 'La aplicación concatena:', 30, 20, { tam: 21, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 58, 740, "sql = \"… WHERE nombre = '\" + entrada + \"'\"", L.tramo(t, 0, 0.16), 18);
      // El usuario escribe
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.24), function () {
        UJ.rotulo(ctx, lz, 'El usuario escribe:', 30, 140, { tam: 21, peso: 800, color: C, alinear: 'left' });
        L.rectRed(ctx, 250, 130, 320, 48, 8); L.rellena(ctx, m.papel, C, 3);
      });
      UJ.rotulo(ctx, lz, "' OR 1=1 --", 266, 142, { tam: 22, peso: 700, alinear: 'left', color: R, visible: L.tramo(t, 0.22, 0.32) });
      // Lo que recibe el motor
      UJ.rotulo(ctx, lz, 'El motor recibe un solo texto:', 30, 216, { tam: 21, peso: 800, color: A, alinear: 'left', visible: L.tramo(t, 0.34, 0.4) });
      UJ.alfa(ctx, L.tramo(t, 0.38, 0.44), function () {
        L.rectRed(ctx, 30, 254, 740, 52, 8); L.rellena(ctx, L.tono(m.tinta, -0.55));
        UJ.rotulo(ctx, lz, "WHERE nombre = ''", 46, 268, { tam: 20, alinear: 'left', color: '#E8F4FA' });
      });
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        L.rectRed(ctx, 250, 260, 230, 40, 6); L.rellena(ctx, L.tono(R, 0.3));
        UJ.rotulo(ctx, lz, 'OR 1=1', 365, 268, { tam: 20, peso: 800, color: '#FFFFFF' });
        UJ.rotulo(ctx, lz, "-- '", 500, 268, { tam: 20, alinear: 'left', color: '#9FB3BF' });
      });
      UJ.rotulo(ctx, lz, 'siempre verdadero', 365, 312, { tam: 17, peso: 700, color: R, visible: L.tramo(t, 0.5, 0.56) });
      UJ.rotulo(ctx, lz, 'comentario', 540, 312, { tam: 17, peso: 700, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.52, 0.58) });
      // Toda la tabla
      // La tabla no existe en pantalla hasta su paso: una tabla vacia anunciaria el final.
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.68), function () {
        UJ.tabla(ctx, lz, 30, 360, 420, 'mascota · las 8 filas', ['1 · Firulais', '2 · Luna', '3 · Rocky', '4 · Mishi  … y 4 más'], 1 + 3 * L.tramo(t, 0.68, 0.82), R, -1);
      });
      UJ.rotulo(ctx, lz, 'El dato se interpretó como código.', 620, 420, { tam: 22, peso: 800, color: R, ancho: 300, visible: L.tramo(t, 0.84, 0.96) });
    }
  });
})();
