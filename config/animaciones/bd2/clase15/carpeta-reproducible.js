/* Reproducible: una carpeta con archivos numerados en el orden exacto de ejecucion. El orden es
 * una dependencia real: la FK necesita su tabla, el disparador necesita su tabla. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('carpeta-reproducible', {
    duracion: 5,
    pasos: [0.5, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var arch = ['00_LEEME.txt', '01_ddl.sql', '02_datos_prueba.sql', '03_roles.sql', '04_procedimientos.sql',
                  '05_funciones.sql', '06_triggers.sql', '07_optimizacion.sql', '08_pruebas.sql'];
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () {
        L.rectRed(ctx, 30, 14, 120, 26, 6); L.rellena(ctx, L.tono(C, 0.5));
        L.rectRed(ctx, 30, 30, 360, 520, 12); L.rellena(ctx, L.tono(C, 0.9), C, 2);
      });
      for (var i = 0; i < 9; i++) {
        var y = 46 + i * 55;
        UJ.alfa(ctx, L.tramo(t, 0.06 + i * 0.045, 0.1 + i * 0.045), function () {
          L.rectRed(ctx, 50, y, 320, 44, 8); L.rellena(ctx, m.papel, A, 2);
          UJ.rotulo(ctx, lz, arch[i], 66, y + 12, { tam: 18, peso: 600, alinear: 'left', letra: 'Consolas, monospace' });
        });
      }
      // Dependencias
      UJ.rotulo(ctx, lz, 'El orden es dependencia', 600, 40, { tam: 22, peso: 800, color: A, visible: L.tramo(t, 0.52, 0.58) });
      UJ.caja(ctx, lz, 440, 90, 330, 120, 'FOREIGN KEY', 'no se crea antes que la tabla a la que apunta', A, L.tramo(t, 0.56, 0.64));
      L.trazo(ctx, [[436, 150], [400, 150], [400, 123], [374, 123]], L.tramo(t, 0.62, 0.7), A, 3);
      UJ.caja(ctx, lz, 440, 250, 330, 120, 'Trigger', 'no se puede crear si su tabla no existe', C, L.tramo(t, 0.66, 0.74));
      L.trazo(ctx, [[436, 310], [400, 310], [400, 398], [374, 398]], L.tramo(t, 0.72, 0.8), C, 3);
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.92), function () {
        L.rectRed(ctx, 440, 410, 330, 140, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, 'Un tercero, sin hablar con el autor, llega a la misma base', 605, 452, { tam: 19, peso: 700, ancho: 300 });
      });
    }
  });
})();
