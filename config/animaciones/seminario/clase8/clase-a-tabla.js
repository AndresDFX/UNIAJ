/* Del diagrama de clases a la base de datos: la clase da la tabla, la asociación 1 a 0..* da la
 * llave foránea y un muchos a muchos da una tabla intermedia. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('clase-a-tabla', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.32, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, T = m.tinta, W = lz.ancho, MONO = 'Consolas, monospace';
      // Clase Mascota
      var a = L.tramo(t, 0, 0.1);
      UJ.alfa(ctx, a, function () {
        L.rectRed(ctx, 40, 30, 250, 44, 0); L.rellena(ctx, L.tono(A, 0.8), A, 3);
        UJ.rotulo(ctx, lz, 'Mascota', 165, 39, { tam: 22, peso: 800, color: L.tono(A, -0.3) });
        L.rectRed(ctx, 40, 74, 250, 140, 0); L.rellena(ctx, m.papel, A, 3);
        var at = ['-codigo: String', '-nombre: String', '-especie: String', '-fechaNacimiento: Date'];
        for (var i = 0; i < 4; i++) L.texto(ctx, at[i], 52, 84 + i * 32, { tam: 18, peso: 500, color: T, letra: MONO });
      });
      // Tabla mascota
      var filas = ['codigo (PK)', 'nombre', 'especie', 'fecha_nacimiento', 'documento_dueno (FK)'];
      var nt = L.tramo(t, 0.14, 0.28) * 4 + L.tramo(t, 0.52, 0.6);
      if (t > 0.12) UJ.tabla(ctx, lz, 470, 30, 300, 'mascota', filas, nt, V, t > 0.6 ? 4 : undefined);
      UJ.flecha(ctx, lz, 300, 120, 456, 120, A, L.tramo(t, 0.1, 0.16), 'clase → tabla', { tam: 17 });
      // Asociacion
      var d = L.tramo(t, 0.36, 0.44);
      UJ.caja(ctx, lz, 40, 320, 250, 50, 'Dueño', null, A, d);
      UJ.alfa(ctx, d, function () {
        L.trazo(ctx, [[165, 214], [165, 320]], 1, T, 3);
        UJ.rotulo(ctx, lz, '0..*', 178, 222, { tam: 19, peso: 800, color: R, alinear: 'left' });
        UJ.rotulo(ctx, lz, '1', 178, 290, { tam: 19, peso: 800, color: R, alinear: 'left' });
      });
      UJ.flecha(ctx, lz, 172, 266, 462, 266, R, L.tramo(t, 0.46, 0.54), 'llave foránea', { tam: 17, dy: -30 });
      // Muchos a muchos
      var mm = L.tramo(t, 0.68, 0.76);
      UJ.caja(ctx, lz, 40, 430, 70, 50, 'A', null, A, mm);
      UJ.caja(ctx, lz, 220, 430, 70, 50, 'B', null, A, mm);
      UJ.alfa(ctx, mm, function () {
        L.trazo(ctx, [[110, 455], [220, 455]], 1, T, 3);
        UJ.rotulo(ctx, lz, '*', 124, 424, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, '*', 206, 424, { tam: 22, peso: 800, color: R });
      });
      UJ.flecha(ctx, lz, 300, 455, 420, 455, A, L.tramo(t, 0.76, 0.82));
      var ti = L.tramo(t, 0.8, 0.88);
      UJ.caja(ctx, lz, 430, 430, 70, 50, 'a', null, V, ti);
      UJ.caja(ctx, lz, 560, 430, 100, 50, 'a_b', null, R, ti);
      UJ.caja(ctx, lz, 710, 430, 60, 50, 'b', null, V, ti);
      UJ.alfa(ctx, ti, function () {
        L.trazo(ctx, [[500, 455], [560, 455]], 1, T, 3);
        L.trazo(ctx, [[660, 455], [710, 455]], 1, T, 3);
        UJ.rotulo(ctx, lz, 'tabla intermedia', 610, 490, { tam: 18, peso: 800, color: R });
      });
      UJ.rotulo(ctx, lz, 'Del diagrama salen el diccionario de datos y las tablas', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
