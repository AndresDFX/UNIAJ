/* Ilustracion: que observar en la demo del checkpoint. A la izquierda lo que se EJECUTA (las
 * consultas al catalogo y las dos llamadas al procedimiento), a la derecha lo que se ESCRIBE: un
 * hallazgo con sus cinco partes. Cada hallazgo sale de una ejecucion, no de una opinion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 8, { tam: 26, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'Se ejecuta', 200, 52, { tam: 21, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'Se escribe', 610, 52, { tam: 21, peso: 800, color: C });
      var filas = [
        ['tablas del esquema', 'están todas'],
        ['tablas sin PK', '0 filas'],
        ['claves foráneas', '7 relaciones'],
        ['rutinas y triggers', 'existen de verdad'],
        ['CALL caso válido', 'cita insertada'],
        ['CALL caso inválido', 'mensaje de negocio']
      ];
      for (var i = 0; i < filas.length; i++) {
        var y = 92 + i * 80, col = i < 4 ? A : V;
        L.rectRed(ctx, 20, y, 370, 66, 10); L.rellena(ctx, L.tono(col, 0.9), col, 2);
        UJ.rotulo(ctx, lz, filas[i][0], 36, y + 8, { tam: 18, peso: 800, color: col, alinear: 'left', ancho: 340 });
        UJ.rotulo(ctx, lz, '→ ' + filas[i][1], 36, y + 36, { tam: 16, alinear: 'left', ancho: 340 });
      }
      L.flecha(ctx, 396, 330, 436, 330, C, 5, 1);
      // El hallazgo
      L.rectRed(ctx, 440, 92, 340, 466, 14); L.rellena(ctx, m.papel, C, 3);
      var partes = [['Artefacto', 'script DDL'], ['Observación', 'detalle_factura sin FK a insumo'],
                    ['Impacto', 'detalles con insumos que no existen'], ['Acción', 'agregar la FK y re-ejecutar desde cero'],
                    ['Responsable y fecha', 'el autor · antes de la próxima sesión']];
      for (var k = 0; k < 5; k++) {
        var yy = 108 + k * 88;
        UJ.rotulo(ctx, lz, (k + 1) + ' · ' + partes[k][0], 458, yy, { tam: 17, peso: 800, color: L.tono(C, -0.3), alinear: 'left', ancho: 310 });
        UJ.rotulo(ctx, lz, partes[k][1], 458, yy + 28, { tam: 16, alinear: 'left', ancho: 310 });
        if (k < 4) { L.rectRed(ctx, 458, yy + 70, 300, 2, 1); L.rellena(ctx, L.tono(C, 0.6)); }
      }
      UJ.rotulo(ctx, lz, 'Cada hallazgo sale de una ejecución, no de lo que el autor dice.', W / 2, 584,
                { tam: 18, peso: 700, color: R, ancho: W - 40 });
    }
  });
})();
