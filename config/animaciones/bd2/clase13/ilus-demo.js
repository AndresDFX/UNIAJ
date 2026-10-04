/* Ilustracion: el analisis guiado de punta a punta, sobre un caso que no es el de la practica
 * (Capital One): contexto, que fallo, causa raiz, impacto, leccion accionable y cambio en la base. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.rotulo(ctx, lz, 'Un caso de punta a punta (Capital One, 2019)', W / 2, 8, { tam: 24, peso: 800, color: A });
      var filas = [
        ['Contexto', 'banco con datos de clientes en almacenamiento en la nube', A],
        ['Qué falló', 'cortafuegos mal configurado → credenciales de un rol de servicio', A],
        ['Causa raíz', 'ese rol podía leer todos los buckets: privilegio excesivo', C],
        ['Impacto', '≈ 100 millones de personas en EE. UU. · multa de 80 millones de dólares', R],
        ['Lección accionable', 'cada rol con solo los permisos de su tarea, revisados cada mes contra la matriz', V],
        ['Cambio en la base', 'la aplicación entra con su propio rol: GRANT EXECUTE sí, SELECT directo no', V]
      ];
      for (var i = 0; i < filas.length; i++) {
        var y = 52 + i * 96, col = filas[i][2];
        L.rectRed(ctx, 30, y, 210, 76, 12); L.rellena(ctx, col);
        UJ.rotulo(ctx, lz, (i + 1) + ' · ' + filas[i][0], 135, y + 14, { tam: 18, peso: 800, color: m.papel, ancho: 190 });
        L.rectRed(ctx, 250, y, 520, 76, 12); L.rellena(ctx, L.tono(col, 0.9), col, 2);
        UJ.rotulo(ctx, lz, filas[i][1], 266, y + 12, { tam: 17, peso: 600, alinear: 'left', ancho: 490 });
        if (i < filas.length - 1) L.flecha(ctx, 135, y + 78, 135, y + 94, L.tono(m.tinta, 0.3), 3, 1);
      }
    }
  });
})();
