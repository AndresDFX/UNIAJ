/* Ilustracion: las siete razones por las que un indice que existe no se usa, como lista de
 * revision con su ejemplo de la base de la clase. Abajo, el orden en que se revisa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-siete-razones', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El índice existe y el plan no lo usa: ¿por qué?', W / 2, 8, { tam: 23, peso: 800, color: A, ancho: W - 30 });
      var r = [
        ['Tabla pequeña', 'dueno: 20 páginas, leerlas de corrido gana'],
        ['Predicado no sargable', 'UPPER(nombre) = …, EXTRACT(YEAR FROM …)'],
        ['Selectividad mala', "activa = 'S' deja pasar el 94 % de mascota"],
        ['Estadísticas viejas', 'faltó ANALYZE después de cargar o de crear'],
        ['Sin la columna líder', '(estado, fecha_hora) con un filtro solo de fecha'],
        ['OR entre columnas', 'cada lado necesitaría su propio índice'],
        ['Tipo u orden distinto', 'el valor comparado no es del tipo de la columna']
      ];
      for (var i = 0; i < r.length; i++) {
        var y = 52 + i * 72;
        L.rectRed(ctx, 20, y, W - 40, 64, 12); L.rellena(ctx, i % 2 ? m.papel : L.tono(A, 0.94), L.tono(A, 0.6), 2);
        L.circulo(ctx, 52, y + 32, 20); L.rellena(ctx, i === 3 ? R : A);
        UJ.rotulo(ctx, lz, String(i + 1), 52, y + 19, { tam: 20, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, r[i][0], 86, y + 9, { tam: 19, peso: 800, color: i === 3 ? R : L.tono(A, -0.2), alinear: 'left' });
        UJ.rotulo(ctx, lz, r[i][1], 86, y + 36, { tam: 15, alinear: 'left', ancho: W - 130 });
      }
      L.rectRed(ctx, 20, 560, W - 40, 66, 12); L.rellena(ctx, L.tono(C, 0.88), C, 2);
      UJ.rotulo(ctx, lz, 'Con 30.010 citas el volumen ya no es excusa. Se revisa en orden:', W / 2, 568, { tam: 16, peso: 700, ancho: W - 70 });
      UJ.rotulo(ctx, lz, 'ANALYZE → columna líder → predicado sargable', W / 2, 596, { tam: 17, peso: 800, color: L.tono(C, -0.35) });
    }
  });
})();
