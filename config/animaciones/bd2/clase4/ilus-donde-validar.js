/* Ilustracion: donde vive cada validacion, como un arbol de decision de preguntas. La primera
 * respuesta «si» decide la capa: CHECK, UNIQUE/FK, trigger o aplicacion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-donde-validar', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, '¿Dónde vive esta regla?', W / 2, 14, { tam: 26, peso: 800, color: A });
      var filas = [
        ['¿Se decide mirando UNA fila?', 'CHECK', 'stock >= 0'],
        ['¿Relaciona filas o tablas?', 'UNIQUE / FK', 'un veterinario, una franja'],
        ['¿Necesita OTRA fila, OLD/NEW u otra tabla?', 'Trigger', 'auditar el cambio de estado'],
        ['¿La base no puede saberlo?', 'Aplicación', 'el formato del correo']
      ];
      for (var i = 0; i < filas.length; i++) {
        var y = 70 + i * 128;
        L.rectRed(ctx, 24, y, 380, 84, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, filas[i][0], 214, y + 16, { tam: 18, peso: 700, ancho: 350 });
        L.flecha(ctx, 410, y + 42, 470, y + 42, m.verde || A, 4, 1);
        UJ.rotulo(ctx, lz, 'sí', 440, y + 14, { tam: 15, peso: 700, color: m.verde || A });
        L.rectRed(ctx, 476, y, 300, 84, 14); L.rellena(ctx, m.sello || C, m.tinta, 2);
        UJ.rotulo(ctx, lz, filas[i][1], 626, y + 12, { tam: 22, peso: 800 });
        UJ.rotulo(ctx, lz, filas[i][2], 626, y + 48, { tam: 15, ancho: 280 });
        if (i < filas.length - 1) {
          L.flecha(ctx, 214, y + 86, 214, y + 126, L.tono(m.tinta, 0.4), 3, 1);
          UJ.rotulo(ctx, lz, 'no', 236, y + 96, { tam: 14, color: L.tono(m.tinta, 0.3) });
        }
      }
    }
  });
})();
