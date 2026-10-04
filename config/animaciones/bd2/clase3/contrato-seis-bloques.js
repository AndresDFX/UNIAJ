/* El contrato del procedimiento: seis bloques, cada uno responde una pregunta de quien lo llama sin abrirlo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('contrato-seis-bloques', {
    duracion: 5,
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Para quien LLAMA sin abrir el código', W / 2, 14, { tam: 24, peso: 800, color: A, visible: L.tramo(t, 0, 0.05) });
      var b = [
        ['1 · Firma exacta', '¿cómo se declara?'],
        ['2 · Ejemplo de llamada', '¿cómo se invoca?'],
        ['3 · Precondiciones', '¿qué debe ser verdad antes?'],
        ['4 · Postcondiciones', '¿qué queda? si falla, NADA'],
        ['5 · Tabla de errores', 'el mensaje literal'],
        ['6 · Decisión de diseño', '¿por qué aborta?']
      ];
      for (var i = 0; i < 6; i++) {
        var col = i % 2 ? 1 : 0, fil = Math.floor(i / 2);
        var x = 30 + col * 380, y = 70 + fil * 150;
        var ini = [0.06, 0.18, 0.38, 0.5, 0.72, 0.84][i];
        UJ.caja(ctx, lz, x, y, 360, 120, b[i][0], b[i][1], i === 5 ? C : A, L.tramo(t, ini, ini + 0.1));
      }
      UJ.rotulo(ctx, lz, 'Errores y batería de pruebas: el mismo texto, palabra por palabra.', W / 2, 540,
                { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
