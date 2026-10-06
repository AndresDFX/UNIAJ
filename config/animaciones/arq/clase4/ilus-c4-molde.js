/* Lo que dibuja el molde C4Container de la app de turnos: el cliente, los cuatro contenedores
 * dentro del limite del sistema, el correo externo fuera, y cada relacion con su protocolo. */
(function () {
  FP_ANIMADOR.registrar('ilus-c4-molde', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      C4.persona(ctx, lz, 400, 4, 'Cliente', 'Reserva sus turnos');
      C4.limite(ctx, lz, 20, 150, 560, 470, 'App de turnos');
      C4.contenedor(ctx, lz, 160, 180, 280, 88, 'App web', 'React', 'Reserva');
      C4.contenedor(ctx, lz, 160, 330, 280, 88, 'API de turnos', 'Node.js', 'Valida');
      C4.baseDatos(ctx, lz, 40, 470, 220, 110, 'Base de turnos', 'PostgreSQL', '');
      C4.contenedor(ctx, lz, 320, 480, 230, 88, 'Worker', 'cola', 'Avisos');
      C4.externo(ctx, lz, 610, 490, 175, 76, 'Correo', 'Entrega el correo');
      C4.rel(ctx, lz, 380, 110, 320, 178, 'Reserva un turno', 'HTTPS', 70, 0);
      C4.rel(ctx, lz, 300, 270, 300, 326, 'POST /turnos', 'HTTPS/JSON', 80, 0);
      C4.rel(ctx, lz, 230, 420, 160, 468, 'INSERT / SELECT', 'TCP/SQL', -55, -6);
      C4.rel(ctx, lz, 370, 420, 430, 476, 'Publica aviso', 'evento (AMQP)', 80, -6);
      C4.rel(ctx, lz, 552, 524, 606, 524, 'Envia', 'REST/HTTPS', 0, -52);
    }
  });
})();
