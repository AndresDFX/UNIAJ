/* Ilustracion: la firma de fn_precio_consulta, pieza por pieza. RETURNS NUMERIC (se llama desde
 * una consulta) y no RETURNS TRIGGER; IMMUTABLE = misma entrada, misma salida, sin leer tablas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-firma-funcion', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'La firma decide todo lo demás', W / 2, 18, { tam: 26, peso: 800, color: A });
      var piezas = [
        ['CREATE FUNCTION', 'fn_precio_consulta', A],
        ['parámetros', '(p_especie TEXT, p_urgencia BOOLEAN)', C],
        ['devuelve', 'RETURNS NUMERIC', m.verde || A],
        ['volatilidad', 'IMMUTABLE', A]
      ];
      for (var i = 0; i < piezas.length; i++) {
        var y = 78 + i * 92;
        L.rectRed(ctx, 30, y, 210, 70, 12); L.rellena(ctx, L.tono(piezas[i][2], 0.88), piezas[i][2], 2);
        UJ.rotulo(ctx, lz, piezas[i][0], 135, y + 22, { tam: 19, peso: 700, color: piezas[i][2] });
        UJ.codigo(ctx, lz, 260, y + 14, 510, piezas[i][1], 1, 17);
      }
      // RETURNS TRIGGER tachado
      L.rectRed(ctx, 30, 452, 360, 92, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
      UJ.rotulo(ctx, lz, 'RETURNS TRIGGER', 210, 466, { tam: 21, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'solo para la función de un trigger', 210, 500, { tam: 16 });
      UJ.sello(ctx, lz, 390, 456, 22, false, 1);
      L.rectRed(ctx, 410, 452, 360, 92, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
      UJ.rotulo(ctx, lz, 'IMMUTABLE', 590, 466, { tam: 21, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'misma entrada → misma salida, sin leer tablas', 590, 500, { tam: 15, ancho: 330 });
      UJ.rotulo(ctx, lz, 'Se llama desde una consulta: SELECT …, fn_precio_consulta(especie, FALSE)', W / 2, 580,
                { tam: 17, ancho: W - 40, peso: 600 });
    }
  });
})();
