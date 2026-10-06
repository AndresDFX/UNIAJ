/* Lo que dibuja el sequenceDiagram «El presupuesto de latencia del camino critico»: cinco
 * participantes con su linea de vida, los seis mensajes numerados (autonumber), cada nota con
 * su costo y las dos notas que abarcan todo. La escritura (150 ms) se marca: es el cuello. */
(function () {
  var X = { N: 70, E: 215, A: 365, D: 520, Q: 690 };
  FP_ANIMADOR.registrar('dg-latencia', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var k;
      for (k in X) MF.vida(ctx, X[k], 52, 600);
      MF.participante(ctx, lz, X.N, 6, 120, 'Navegador');
      MF.participante(ctx, lz, X.E, 6, 120, 'Edge TLS');
      MF.participante(ctx, lz, X.A, 6, 140, 'API de turnos');
      MF.participante(ctx, lz, X.D, 6, 140, 'Base de turnos');
      MF.participante(ctx, lz, X.Q, 6, 140, 'Cola de avisos');
      MF.nota(ctx, lz, 20, 62, 760, 30, 'Objetivo p95 de POST /turnos 300 ms', { tam: 15 });
      MF.mensaje(ctx, lz, X.N, X.E, 132, 'POST /turnos', { n: 1 });
      MF.nota(ctx, lz, X.E + 8, 142, 130, 30, 'TLS y proxy - 20 ms');
      MF.mensaje(ctx, lz, X.E, X.A, 212, 'POST /turnos interno en 8080', { n: 2, tam: 12, cx: 300 });
      MF.nota(ctx, lz, X.A + 8, 222, 140, 30, 'Token y franja - 30 ms');
      MF.mensaje(ctx, lz, X.A, X.D, 292, 'SELECT de la franja', { n: 3 });
      MF.nota(ctx, lz, X.D + 8, 302, 178, 30, 'Lectura por indice - 40 ms', { tam: 12 });
      MF.mensaje(ctx, lz, X.A, X.D, 372, 'INSERT del turno y commit', { n: 4, tam: 13, cx: 450 });
      MF.nota(ctx, lz, X.D + 8, 382, 178, 30, 'Escritura y commit - 150 ms', { borde: '#C0392B', tam: 12 });
      MF.mensaje(ctx, lz, X.A, X.Q, 452, 'Publica aviso-de-turno', { n: 5 });
      MF.nota(ctx, lz, X.Q - 75, 462, 150, 30, 'Publicacion - 10 ms');
      MF.mensaje(ctx, lz, X.A, X.N, 532, '201 Created', { n: 6, respuesta: true });
      MF.nota(ctx, lz, 20, 556, 760, 30, 'Suma 250 ms - margen 50 ms', { tam: 15 });
      C4.marca(ctx, lz, X.D + 205, 397, 1, '');
      FP_LIENZO.texto(ctx, 'Cuello de botella: la escritura se lleva 150 de los 250 ms', 420, 608,
        { tam: 14, peso: 700, color: '#333', alinear: 'center', letra: lz.letra });
      C4.marca(ctx, lz, 212, 617, 1, '');
    }
  });
})();
