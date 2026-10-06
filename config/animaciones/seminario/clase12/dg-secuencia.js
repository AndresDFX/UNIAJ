/* Lo que dibuja el codigo de «El diagrama de secuencia en Mermaid»: el actor y cuatro
 * participantes con sus lineas de vida y los diez mensajes numerados (autonumber); las
 * respuestas van punteadas. */
(function () {
  FP_ANIMADOR.registrar('dg-secuencia', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var X = { R: 70, UI: 225, S: 390, M: 555, C: 715 };
      var y0 = 20, yFin = 620;
      DG.participante(ctx, lz, X.R, y0, 120, 'Recepcionista', yFin, true);
      DG.participante(ctx, lz, X.UI, y0, 140, 'Pantalla Agendar', yFin);
      DG.participante(ctx, lz, X.S, y0, 140, 'ServicioCita', yFin);
      DG.participante(ctx, lz, X.M, y0, 150, 'RepositorioMascota', yFin);
      DG.participante(ctx, lz, X.C, y0, 140, 'RepositorioCita', yFin);
      var m = [['R', 'UI', 'solicita agendar'], ['UI', 'S', 'agendar(idMascota, fechaHora)'],
               ['S', 'M', 'estaActiva(idMascota)'], ['M', 'S', 'true', 1],
               ['S', 'C', 'existeEnFranja(idVet, fechaHora)'], ['C', 'S', 'false', 1],
               ['S', 'C', 'guardar(cita)'], ['C', 'S', 'idCita', 1],
               ['S', 'UI', 'PROGRAMADA (idCita)', 1], ['UI', 'R', 'confirmacion', 1]];
      m.forEach(function (k, i) { DG.mensaje(ctx, lz, X[k[0]], X[k[1]], 135 + i * 49, k[2], !!k[3], i + 1); });
    }
  });
})();
