/* Primero la enfermedad: el telefono del dueno guardado en cada cita produce las tres anomalias
 * (actualizacion, insercion, borrado). La cura: el dato vive una sola vez, en dueno. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('anomalias', {
    duracion: 5,
    // Pasos LOGICOS: 1) la tabla con el dato repetido, 2) actualizacion, 3) insercion,
    // 4) borrado, 5) la cura. Una anomalia por clic.
    pasos: [0.2, 0.33, 0.46, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var x0 = 60, y0 = 30, cw = [120, 210, 230, 120], ch = 44;
      var cab = ['id_cita', 'dueno', 'telefono', 'fecha'];
      var tel2 = t >= 0.28 ? '3159998877' : '3001112233';
      var filas = [['1', 'Ana Pérez', '3001112233', '02-03'], ['2', 'Ana Pérez', tel2, '09-03'], ['3', 'Luis Mora', '3104445566', '10-03']];
      var borrada = L.tramo(t, 0.5, 0.58);
      function celda(x, y, w, txt, fondo, color) {
        L.rectRed(ctx, x, y, w, ch, 0); L.rellena(ctx, fondo, L.tono(A, 0.5), 1);
        L.texto(ctx, txt, x + w / 2, y + 12, { tam: 18, color: color || m.tinta, alinear: 'center', letra: 'Consolas, monospace', peso: 600 });
      }
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        var x = x0;
        for (var j = 0; j < 4; j++) { L.rectRed(ctx, x, y0, cw[j], ch, 0); L.rellena(ctx, A, m.papel, 2); UJ.rotulo(ctx, lz, cab[j], x + cw[j] / 2, y0 + 11, { tam: 18, peso: 700, color: m.papel }); x += cw[j]; }
        for (var i = 0; i < 3; i++) {
          var a = i === 2 ? 1 - borrada : 1;
          UJ.alfa(ctx, a, function () {
            x = x0;
            for (var j = 0; j < 4; j++) {
              var mal = (j === 2 && i === 1 && t >= 0.28);
              celda(x, y0 + ch * (i + 1), cw[j], filas[i][j], mal ? L.tono(R, 0.8) : (j === 2 ? L.tono(m.sello || C, 0.75) : m.papel), mal ? R : null);
              x += cw[j];
            }
          });
        }
      });
      UJ.rotulo(ctx, lz, 'El teléfono del dueño se repite en cada cita', W / 2, 220, { tam: 19, visible: L.tramo(t, 0.08, 0.16) });
      var etiquetas = [
        ['Actualización', 'se cambia en una cita y no en la otra: dos verdades', 0.24],
        ['Inserción', 'un dueño sin cita no se puede registrar', 0.36],
        ['Borrado', 'se borra la última cita de Luis: su teléfono desaparece', 0.5]
      ];
      for (var k = 0; k < 3; k++) {
        UJ.alfa(ctx, L.tramo(t, etiquetas[k][2], etiquetas[k][2] + 0.06), function () {
          var y = 262 + k * 72;
          L.rectRed(ctx, 40, y, W - 80, 60, 10); L.rellena(ctx, L.tono(R, 0.9), R, 2);
          UJ.rotulo(ctx, lz, etiquetas[k][0], 60, y + 17, { tam: 20, peso: 800, color: R, alinear: 'left' });
          UJ.rotulo(ctx, lz, etiquetas[k][1], 230, y + 19, { tam: 17, alinear: 'left', ancho: 500 });
        });
      }
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.82), function () {
        L.rectRed(ctx, 40, 492, W - 80, 120, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'La cura (1FN → 3FN): cada dato vive una sola vez', W / 2, 504, { tam: 21, peso: 800, color: V, ancho: W - 120 });
        UJ.codigo(ctx, lz, 70, 548, W - 140, 'dueno(id_dueno, nombre, telefono) · cita(id_cita, id_dueno, fecha)', L.tramo(t, 0.78, 0.96), 17);
      });
    }
  });
})();
