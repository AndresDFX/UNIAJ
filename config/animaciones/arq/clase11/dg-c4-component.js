/* Lo que dibuja el codigo «El C4 Component: por dentro de la API»: la app web arriba, la API
 * abierta (limite punteado) con sus cinco componentes, y fuera la base, la cola y el proveedor
 * de identidad. Las ocho relaciones, con protocolo solo donde el codigo lo declara. */
(function () {
  FP_ANIMADOR.registrar('dg-c4-component', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      C4.contenedor(ctx, lz, 40, 6, 190, 80, 'App web', 'React', 'Crea la reserva');
      C4.limiteContenedor(ctx, lz, 20, 120, 560, 395, 'API de turnos - Node.js', true);
      C4.componente(ctx, lz, 40, 140, 190, 70, 'Rutas', 'Express', 'Valida la peticion');
      C4.componente(ctx, lz, 370, 140, 190, 70, 'Token', 'JWT', 'Firma y expiracion');
      C4.componente(ctx, lz, 40, 280, 190, 70, 'Reglas', 'Node.js', 'Sin doble reserva');
      C4.componente(ctx, lz, 370, 280, 190, 70, 'Publicador', 'AMQP', 'Publica el aviso');
      C4.componente(ctx, lz, 40, 410, 190, 70, 'Repositorio', 'node-postgres', 'El SQL');
      C4.externo(ctx, lz, 590, 4, 200, 96, 'Proveedor de identidad', '');
      FP_LIENZO.texto(ctx, 'Emite tokens', 690, 70, { tam: 13, color: '#FFFFFF', alinear: 'center', letra: lz.letra });
      C4.cola(ctx, lz, 605, 280, 185, 70, 'Cola de avisos', 'RabbitMQ', 'Avisos');
      C4.baseDatos(ctx, lz, 25, 535, 220, 100, 'Base de turnos', 'PostgreSQL', 'Turnos');
      C4.rel(ctx, lz, 135, 88, 135, 138, 'POST /turnos', 'HTTPS/JSON', 75, 0);
      C4.rel(ctx, lz, 232, 175, 366, 175, 'Verifica el token', '', 0, 0);
      C4.rel(ctx, lz, 520, 138, 650, 102, 'Pide llaves publicas', 'HTTPS', -20, 4);
      C4.rel(ctx, lz, 135, 212, 135, 276, 'Pide reservar', '', 0, 0);
      C4.rel(ctx, lz, 232, 315, 366, 315, 'Pide avisar', '', 0, 0);
      C4.rel(ctx, lz, 562, 315, 601, 315, 'Publica aviso-de-turno', 'AMQP', 110, 50);
      C4.rel(ctx, lz, 135, 352, 135, 406, 'Guarda el turno', '', 0, 0);
      C4.rel(ctx, lz, 135, 482, 135, 531, 'INSERT del turno', 'TCP/SQL', 85, 0);
    }
  });
})();
