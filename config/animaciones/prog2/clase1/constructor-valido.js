/* El constructor: el objeto nace valido. new con nombre vacio -> el constructor lanza y no
 * hay objeto; new con datos completos -> el objeto nace en el monton. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('constructor-valido', {
    duracion: 4.8,
    pasos: [0.36, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      // El constructor, en el centro
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        L.rectRed(ctx, 220, 150, 360, 150, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
        UJ.rotulo(ctx, lz, 'Mascota(nombre, especie, edad)', 400, 162, { tam: 19, peso: 800, color: A, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'if (nombre vacío)', 240, 206, { tam: 17, alinear: 'left', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, '  throw new IllegalArgumentException', 240, 232, { tam: 15, alinear: 'left', letra: 'Consolas, monospace', color: R });
        UJ.rotulo(ctx, lz, 'this.nombre = nombre; …', 240, 262, { tam: 17, alinear: 'left', letra: 'Consolas, monospace' });
      });
      // Intento 1: nombre vacio
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.08) * (1 - L.tramo(t, 0.4, 0.46) * 0.6), function () {
        UJ.codigo(ctx, lz, 24, 30, 460, 'new Mascota("", "Canino", 3)', L.tramo(t, 0.04, 0.14), 18);
      });
      L.flecha(ctx, 254, 70, 300, 146, R, 4, L.tramo(t, 0.14, 0.2, 'frena'));
      UJ.rayo(ctx, 600, 160, 70, R, L.tramo(t, 0.22, 0.26));
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.3), function () {
        L.rectRed(ctx, 520, 40, 256, 90, 12); L.rellena(ctx, L.tono(R, 0.88), R, 3);
        UJ.rotulo(ctx, lz, 'lanza la excepción', 648, 52, { tam: 19, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'no existe una Mascota sin nombre', 648, 80, { tam: 16, ancho: 230 });
      });
      // Intento 2: datos validos
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.44), function () {
        UJ.codigo(ctx, lz, 24, 330, 460, 'new Mascota("Luna", "Canino", 3)', L.tramo(t, 0.4, 0.5), 18);
      });
      L.flecha(ctx, 254, 328, 330, 304, V, 4, L.tramo(t, 0.5, 0.54, 'frena'));
      L.flecha(ctx, 490, 304, 560, 380, V, 4, L.tramo(t, 0.54, 0.58, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.64, 'frena'), function () {
        L.rectRed(ctx, 520, 384, 256, 110, 14); L.rellena(ctx, L.tono(V, 0.86), V, 3);
        UJ.rotulo(ctx, lz, 'objeto en el montón', 648, 394, { tam: 17, peso: 700, color: V });
        UJ.rotulo(ctx, lz, '"Luna" · "Canino" · 3', 648, 430, { tam: 18, peso: 800, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'nace válido', 648, 460, { tam: 17, color: V });
      });
      UJ.sello(ctx, lz, 500, 450, 24, true, L.tramo(t, 0.6, 0.66));
      // Reglas
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.82), function () {
        L.rectRed(ctx, 24, 400, 430, 216, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        var r = ['Se llama igual que la clase', 'No declara tipo de retorno', 'Corre una sola vez, al crear', 'new reserva memoria y lo llama', 'Con parámetros, el constructor vacío por defecto desaparece'];
        for (var i = 0; i < r.length; i++) UJ.rotulo(ctx, lz, '· ' + r[i], 44, 414 + i * 33, { tam: 19, alinear: 'left', ancho: 400, peso: i >= 4 ? 700 : 500, color: i >= 4 ? A : m.tinta });
      });
    }
  });
})();
