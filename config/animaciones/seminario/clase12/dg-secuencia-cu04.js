/* Lo que dibuja el codigo de «Secuencia de CU-04 Agendar cita en sintaxis Mermaid»: el actor y
 * cuatro objetos con lineas de vida, los seis mensajes previos y el recuadro alt/else con los
 * dos desenlaces: hay horario libre o no lo hay. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dg-secuencia-cu04', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var X = { R: 62, UI: 215, CTRL: 375, REPM: 545, REPC: 712 };
      var y0 = 14, yFin = 628;
      DG.participante(ctx, lz, X.R, y0, 110, 'Recepcionista', yFin, true);
      DG.participante(ctx, lz, X.UI, y0, 140, ':PantallaAgenda', yFin);
      DG.participante(ctx, lz, X.CTRL, y0, 140, ':ControlAgenda', yFin);
      DG.participante(ctx, lz, X.REPM, y0, 160, ':RepositorioMascotas', yFin);
      DG.participante(ctx, lz, X.REPC, y0, 150, ':RepositorioCitas', yFin);
      var paso = 44, y = 118;
      function msg(a, b, txt, resp) { DG.mensaje(ctx, lz, X[a], X[b], y, txt, resp); y += paso; }
      msg('R', 'UI', 'solicitarAgendamiento(codigoMascota, fecha)');
      msg('UI', 'CTRL', 'agendarCita(codigoMascota, fecha, idVeterinario)');
      msg('CTRL', 'REPM', 'existePorCodigo(codigoMascota)');
      msg('REPM', 'CTRL', 'mascota', true);
      msg('CTRL', 'REPC', 'consultarDisponibilidad(idVeterinario, fecha)');
      msg('REPC', 'CTRL', 'horariosLibres', true);
      // Recuadro alt / else
      var ax = 150, aw = 640, ay = y - 24, ah = 4 * paso + 60;
      L.rectRed(ctx, ax, ay, aw, ah, 4); L.rellena(ctx, 'rgba(255,246,214,0.35)', '#B8860B', 2);
      L.rectRed(ctx, ax, ay, 46, 24, 0); L.rellena(ctx, '#B8860B');
      L.texto(ctx, 'alt', ax + 23, ay + 3, { tam: 15, peso: 800, color: '#FFF', alinear: 'center', letra: lz.letra });
      L.texto(ctx, '[hay horario libre]', ax + 56, ay + 4, { tam: 14, peso: 700, color: '#8A6400', letra: lz.letra });
      y += 22;
      msg('CTRL', 'REPC', 'guardarCita(cita)');
      msg('REPC', 'CTRL', 'idCita', true);
      msg('CTRL', 'UI', 'confirmacion(idCita)', true);
      var ye = y - 16;
      ctx.save(); ctx.setLineDash([8, 6]); L.trazo(ctx, [[ax, ye], [ax + aw, ye]], 1, '#B8860B', 2); ctx.restore();
      L.texto(ctx, '[no hay horario libre]', ax + 10, ye + 3, { tam: 14, peso: 700, color: '#8A6400', letra: lz.letra });
      y += 34;
      msg('CTRL', 'UI', 'alternativas(dia siguiente)', true);
    }
  });
})();
