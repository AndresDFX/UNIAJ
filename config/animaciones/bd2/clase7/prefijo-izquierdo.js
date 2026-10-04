/* Indice compuesto (estado, fecha_hora): las entradas se ordenan por estado y, dentro de cada
 * estado, por fecha. Sirve si el filtro empieza por la columna lider; solo por fecha, no. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('prefijo-izquierdo', {
    duracion: 5,
    // Pasos LOGICOS: 1) como se ordena el indice compuesto; 2) las dos consultas que empiezan
    // por la columna lider; 3) la que no, y la regla.
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var e = ['ATENDIDA · 03-02', 'ATENDIDA · 03-09', 'CANCELADA · 03-05', 'PROGRAMADA · 03-01', 'PROGRAMADA · 03-10', 'PROGRAMADA · 03-14'];
      var res = -1;
      if (t > 0.34 && t < 0.66) res = 4;
      UJ.alfa(ctx, L.tramo(t, 0, 0.12), function () {
        UJ.tabla(ctx, lz, 30, 30, 340, 'idx_cita_estado_fecha', e, 6, A, res);
      });
      // grupos
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.24), function () {
        ctx.strokeStyle = C; ctx.lineWidth = 4;
        [[0, 2], [2, 3], [3, 6]].forEach(function (g) {
          ctx.beginPath(); ctx.moveTo(380, 80 + g[0] * 40); ctx.lineTo(392, 80 + g[0] * 40); ctx.lineTo(392, 72 + g[1] * 40); ctx.lineTo(380, 72 + g[1] * 40); ctx.stroke();
        });
        UJ.rotulo(ctx, lz, '1.º por estado', 410, 90, { tam: 18, peso: 700, color: L.tono(C, -0.3), alinear: 'left' });
        UJ.rotulo(ctx, lz, '2.º por fecha, dentro de cada estado', 410, 200, { tam: 18, peso: 700, color: L.tono(C, -0.3), alinear: 'left', ancho: 360 });
      });
      var q = [["WHERE estado = 'PROGRAMADA' AND fecha_hora >= …", true, 0.34], ["WHERE estado = 'PROGRAMADA'", true, 0.46], ['WHERE fecha_hora >= …', false, 0.66]];
      for (var i = 0; i < 3; i++) {
        UJ.codigo(ctx, lz, 30, 360 + i * 60, 660, q[i][0], L.tramo(t, q[i][2], q[i][2] + 0.08), 17);
        UJ.sello(ctx, lz, 732, 377 + i * 60, 20, q[i][1], L.tramo(t, q[i][2] + 0.08, q[i][2] + 0.14));
      }
      UJ.rotulo(ctx, lz, 'sin búsqueda directa: PostgreSQL 18 puede «saltar» una vez por estado (skip scan)', W / 2, 546,
                { tam: 15, ancho: W - 60, color: L.tono(m.tinta, 0.2), visible: L.tramo(t, 0.8, 0.86) });
      UJ.rotulo(ctx, lz, 'Sin la columna líder no hay búsqueda directa en el índice.', W / 2, 590,
                { tam: 21, ancho: W - 40, color: R, visible: L.tramo(t, 0.88, 0.98) });
    }
  });
})();
