/* Lo que dibuja el codigo «El C4 Context en Mermaid»: las dos personas, el sistema como UNA
 * sola caja, los dos sistemas externos y las cinco relaciones con su protocolo. */
(function () {
  FP_ANIMADOR.registrar('dg-c4-context', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      C4.persona(ctx, lz, 150, 6, 'Cliente', 'Reserva turnos');
      C4.persona(ctx, lz, 650, 6, 'Barbero', 'Ve su agenda');
      C4.sistema(ctx, lz, 260, 250, 280, 100, 'App de turnos', 'Agenda turnos');
      C4.externo(ctx, lz, 20, 500, 240, 84, 'Correo transaccional', 'Envia correos');
      C4.externo(ctx, lz, 540, 500, 240, 84, 'Proveedor de identidad', 'Login');
      C4.rel(ctx, lz, 190, 112, 330, 246, 'Reserva un turno', 'HTTPS', 30, -10);
      C4.rel(ctx, lz, 610, 112, 470, 246, 'Consulta su agenda', 'HTTPS', -30, -10);
      C4.rel(ctx, lz, 470, 352, 620, 496, 'Valida identidad', 'OIDC/HTTPS', 40, -10);
      C4.rel(ctx, lz, 330, 352, 190, 496, 'Pide recordatorio', 'REST/HTTPS', -40, -10);
      C4.rel(ctx, lz, 70, 496, 120, 112, 'Entrega el recordatorio', 'SMTP', -8, 30);
      C4.marca(ctx, lz, 560, 250, 1, '');
      FP_LIENZO.texto(ctx, 'El sistema es una sola caja: por dentro no se ve', 400, 612,
        { tam: 15, peso: 700, color: '#333', alinear: 'center', letra: lz.letra });
      C4.marca(ctx, lz, 215, 621, 1, '');
    }
  });
})();
