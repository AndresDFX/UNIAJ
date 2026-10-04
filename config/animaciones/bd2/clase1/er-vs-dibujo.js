/* Un dibujo son cajas unidas por lineas; un diagrama ER cumple cinco condiciones verificables.
 * Criterio: otra persona escribe el CREATE TABLE mirandolo, sin preguntar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('er-vs-dibujo', {
    duracion: 5,
    pasos: [0.2, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // El dibujo
      UJ.alfa(ctx, L.tramo(t, 0, 0.1), function () {
        UJ.rotulo(ctx, lz, 'Un dibujo', 150, 16, { tam: 22, peso: 800, color: R });
        L.rectRed(ctx, 40, 60, 100, 50, 6); L.rellena(ctx, m.papel, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Dueños', 90, 74, { tam: 17 });
        L.rectRed(ctx, 170, 60, 110, 50, 6); L.rellena(ctx, m.papel, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Mascotas', 225, 74, { tam: 17 });
        L.trazo(ctx, [[140, 85], [170, 85]], 1, m.tinta, 2);
        UJ.rotulo(ctx, lz, 'cajas + líneas', 160, 130, { tam: 17, color: L.tono(m.tinta, 0.3) });
      });
      UJ.sello(ctx, lz, 290, 40, 18, false, L.tramo(t, 0.12, 0.18));
      // El diagrama
      UJ.alfa(ctx, L.tramo(t, 0.22, 0.3), function () {
        UJ.rotulo(ctx, lz, 'Un diagrama ER', 570, 16, { tam: 22, peso: 800, color: V });
        L.rectRed(ctx, 360, 56, 190, 104, 6); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        L.texto(ctx, 'Dueno', 455, 62, { tam: 17, peso: 800, color: A, alinear: 'center', letra: lz.letra });
        L.texto(ctx, 'PK id_dueno INT', 372, 92, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
        L.texto(ctx, 'telefono VARCHAR(30)', 372, 118, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
        L.rectRed(ctx, 600, 56, 190, 104, 6); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        L.texto(ctx, 'Mascota', 695, 62, { tam: 17, peso: 800, color: A, alinear: 'center', letra: lz.letra });
        L.texto(ctx, 'PK id_mascota INT', 612, 92, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
        L.texto(ctx, 'FK id_dueno INT', 612, 118, { tam: 15, color: m.tinta, letra: 'Consolas, monospace' });
        L.trazo(ctx, [[550, 108], [600, 108]], 1, m.tinta, 2);
        L.texto(ctx, '1..1', 553, 84, { tam: 15, color: C, peso: 700 });
        L.texto(ctx, '0..N', 562, 116, { tam: 15, color: C, peso: 700 });
        UJ.rotulo(ctx, lz, 'posee', 575, 172, { tam: 16, peso: 700, color: C });
      });
      var cond = ['Entidades en singular, con su PK marcada', 'Cada atributo con tipo y longitud', 'Cada FK señalada: a qué entidad apunta',
                  'Cardinalidad en los dos extremos (mín. y máx.)', 'Cada relación con nombre verbal: Dueño posee Mascota'];
      for (var i = 0; i < 5; i++) {
        var a = L.tramo(t, 0.32 + i * 0.1, 0.4 + i * 0.1);
        UJ.alfa(ctx, a, function () {
          var y = 214 + i * 58;
          L.rectRed(ctx, 40, y, W - 80, 48, 10); L.rellena(ctx, L.tono(V, 0.9), V, 2);
          UJ.rotulo(ctx, lz, (i + 1) + ' · ' + cond[i], 90, y + 13, { tam: 18, peso: 600, alinear: 'left', ancho: W - 160 });
        });
        UJ.sello(ctx, lz, 66, 238 + i * 58, 13, true, a);
      }
      UJ.rotulo(ctx, lz, 'Prueba: otro escribe el CREATE TABLE mirándolo, sin preguntar.', W / 2, 520,
                { tam: 20, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
