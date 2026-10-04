/* Ilustracion: el script de la demo de transacciones en sus cinco bloques, con lo que cada uno
 * debe mostrar. Salidas reales de PGlite: 27.400; fotos 1|3|40|3 antes y despues del CALL que
 * falla; la factura viable sale por 112.000 con id 3 (el intento fallido consumio el 2). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo-orden', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El script de la demo, bloque por bloque', W / 2, 8, { tam: 23, peso: 800, color: A });
      var b = [
        ['0', 'Esquema y 6 insumos', 'el insumo 2 tiene 3 unidades: es el que se queda corto', L.tono(m.tinta, 0.3)],
        ['1', 'El procedimiento', 'leer en voz alta el guardia y el GET DIAGNOSTICS', A],
        ['2', 'El caso que funciona', 'factura por 27.400; stocks 1, 6 y 5 en 11, 58 y 5', V],
        ['3', 'Foto · CALL que falla · foto', '1 | 3 | 40 | 3 antes y después: nada quedó a medias', R],
        ['4', 'La función', 'true | false | true, sin ningún stock negativo', C]
      ];
      for (var i = 0; i < b.length; i++) {
        var y = 52 + i * 106;
        L.rectRed(ctx, 20, y, W - 40, 92, 14); L.rellena(ctx, L.tono(b[i][3], 0.92), b[i][3], i === 3 ? 4 : 2);
        L.circulo(ctx, 62, y + 46, 26); L.rellena(ctx, b[i][3]);
        UJ.rotulo(ctx, lz, b[i][0], 62, y + 32, { tam: 26, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, b[i][1], 104, y + 14, { tam: 20, peso: 800, color: L.tono(b[i][3], -0.25), alinear: 'left' });
        UJ.rotulo(ctx, lz, b[i][2], 104, y + 50, { tam: 16, alinear: 'left', ancho: W - 150 });
        if (i < b.length - 1) L.flecha(ctx, 62, y + 92, 62, y + 104, L.tono(m.tinta, 0.4), 3, 1);
      }
      UJ.rotulo(ctx, lz, 'El bloque 3 es la clase entera: si falta tiempo, se recorta el 4.', W / 2, 594, { tam: 18, peso: 800, color: R, ancho: W - 40 });
    }
  });
})();
