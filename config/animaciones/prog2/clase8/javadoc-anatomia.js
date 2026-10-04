/* Anatomia de un bloque Javadoc: /** con la frase resumen encima del metodo; luego las etiquetas
 * @param, @return y @throws; al final, el editor lo muestra al pasar el cursor. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('javadoc-anatomia', {
    duracion: 4.8,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      var filas = [
        ['/**', 0], ['* Agenda una cita para una mascota activa.', 0],
        ['* @param idMascota id de la mascota', 1], ['* @param fecha día y hora de la cita', 1],
        ['* @return la cita creada', 1], ['* @throws IllegalStateException si está inactiva', 1],
        ['*/', 0], ['public Cita agendar(String idMascota, LocalDateTime fecha)', 0]
      ];
      var x0 = 20, y0 = 20, an = 446, al = 30;
      for (var i = 0; i < filas.length; i++) {
        var v = filas[i][1] ? L.tramo(t, 0.38 + (i - 2) * 0.05, 0.44 + (i - 2) * 0.05) : L.tramo(t, 0.02 + i * 0.02, 0.1 + i * 0.02);
        UJ.codigo(ctx, lz, x0, y0 + i * al, i === 7 ? W - 40 : an, filas[i][0], v, 15);
      }
      function nota(fila, frase, color, a) {
        UJ.alfa(ctx, a, function () {
          L.flecha(ctx, 506, y0 + fila * al + al / 2, 472, y0 + fila * al + al / 2, color, 3);
          UJ.rotulo(ctx, lz, frase, 514, y0 + fila * al + 5, { tam: 16, peso: 700, alinear: 'left', color: color });
        });
      }
      // Paso 1: el bloque y su resumen
      nota(0, '/** justo encima del método', A, L.tramo(t, 0.14, 0.2));
      nota(1, 'resumen corto, con punto final', A, L.tramo(t, 0.2, 0.26));
      // Paso 2: las etiquetas
      nota(2, '@param: qué recibe', C, L.tramo(t, 0.4, 0.44));
      nota(4, '@return: qué devuelve', C, L.tramo(t, 0.5, 0.54));
      nota(5, '@throws: cuándo falla', R, L.tramo(t, 0.55, 0.6));
      UJ.rotulo(ctx, lz, 'En la clase: @author y @version.', 514, y0 + 6 * al + 5, { tam: 16, peso: 500, alinear: 'left', visible: L.tramo(t, 0.58, 0.64) });
      // Paso 3: el editor lo muestra al pasar el cursor
      var a3 = L.tramo(t, 0.7, 0.76);
      UJ.alfa(ctx, a3, function () {
        UJ.codigo(ctx, lz, 20, 300, W - 40, 'Cita c = servicio.agendar(id, fecha);', 1, 16);
        // el puntero sobre agendar
        var px = 230, py = 322;
        ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(px, py + 22); ctx.lineTo(px + 6, py + 17); ctx.lineTo(px + 15, py + 18); ctx.closePath();
        ctx.fillStyle = m.papel; ctx.fill(); ctx.strokeStyle = m.tinta; ctx.lineWidth = 1.5; ctx.stroke();
      });
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.86), function () {
        L.rectRed(ctx, 200, 352, 560, 196, 10); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.5), 2);
        UJ.rotulo(ctx, lz, 'Cita agendar(String idMascota, LocalDateTime fecha)', 216, 364, { tam: 16, peso: 700, alinear: 'left', color: A, ancho: 530 });
        UJ.rotulo(ctx, lz, 'Agenda una cita para una mascota activa.', 216, 396, { tam: 17, peso: 500, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'Parámetros: idMascota – id de la mascota', 216, 432, { tam: 16, peso: 500, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'fecha – día y hora de la cita', 322, 456, { tam: 16, peso: 500, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'Devuelve: la cita creada', 216, 484, { tam: 16, peso: 500, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'Lanza: IllegalStateException – si está inactiva', 216, 512, { tam: 16, peso: 500, alinear: 'left', color: R });
      });
      UJ.rotulo(ctx, lz, 'El editor lo muestra al pasar el cursor;', 20, 566, { tam: 18, peso: 600, alinear: 'left', visible: L.tramo(t, 0.86, 0.93) });
      UJ.rotulo(ctx, lz, 'javadoc -d docs genera el sitio HTML.', 20, 594, { tam: 18, peso: 600, alinear: 'left', visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
