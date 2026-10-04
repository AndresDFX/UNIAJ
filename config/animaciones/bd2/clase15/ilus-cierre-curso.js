/* Ilustracion: el cierre del curso. Lo que el estudiante produjo en el semestre es el contenido de
 * las tareas de un primer empleo; en produccion cambia el volumen y el costo de un error, no la
 * sintaxis. Y la autoevaluacion con una consigna concreta. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-cierre-curso', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.rotulo(ctx, lz, 'Lo que hiciste es el trabajo de un primer empleo', W / 2, 8, { tam: 24, peso: 800, color: A });
      var hechos = ['ER justificado', 'DDL con restricciones', 'Matriz de privilegios', 'Procedimientos con errores',
                    'Triggers de auditoría', 'Plan de ejecución leído', 'Contrato de operaciones'];
      for (var i = 0; i < hechos.length; i++) {
        var y = 54 + i * 54;
        L.rectRed(ctx, 30, y, 330, 44, 10); L.rellena(ctx, L.tono(A, 0.9), A, 2);
        UJ.rotulo(ctx, lz, hechos[i], 195, y + 10, { tam: 18, peso: 700, color: A });
        L.trazo(ctx, [[362, y + 22], [400, y + 22], [400, 240], [430, 240]], 1, L.tono(A, 0.5), 2);
      }
      L.flecha(ctx, 400, 240, 440, 240, A, 4, 1);
      L.rectRed(ctx, 444, 150, 326, 180, 16); L.rellena(ctx, L.tono(V, 0.88), V, 3);
      UJ.rotulo(ctx, lz, 'Tareas del primer año', 607, 168, { tam: 21, peso: 800, color: L.tono(V, -0.3) });
      UJ.rotulo(ctx, lz, 'desarrollador de bases de datos o administrador junior', 607, 212, { tam: 18, peso: 600, ancho: 290 });
      L.rectRed(ctx, 444, 344, 326, 70, 12); L.rellena(ctx, L.tono(C, 0.9), C, 2);
      UJ.rotulo(ctx, lz, 'Leer un plan y decidir si un índice sobra se paga', 607, 354, { tam: 16, peso: 700, ancho: 300 });
      // Lo que cambia en produccion
      L.rectRed(ctx, 30, 448, 740, 70, 12); L.rellena(ctx, L.tono(A, 0.9), A, 2);
      UJ.rotulo(ctx, lz, 'En producción cambian el volumen y el costo de un error; la sintaxis es la misma.', W / 2, 460, { tam: 18, peso: 700, ancho: 700 });
      // Autoevaluacion
      L.rectRed(ctx, 30, 534, 740, 86, 12); L.rellena(ctx, L.tono(m.sello || C, 0.6), m.tinta, 1);
      UJ.rotulo(ctx, lz, 'Autoevaluación: ¿qué decisión de modelado te costó más revertir, y en qué clase te diste cuenta de que estaba mal?', W / 2, 546, { tam: 17, peso: 700, ancho: 700 });
    }
  });
})();
