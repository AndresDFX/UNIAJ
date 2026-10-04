/* Index Only Scan: si todas las columnas que pide la consulta estan en el indice, el motor no
 * toca la tabla. Si se agrega id_mascota, vuelve a ir a la tabla por cada fila; se recupera con
 * INCLUDE (id_mascota). Planes reales de la base sembrada (despues de VACUUM). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('index-only', {
    duracion: 5,
    // Pasos LOGICOS: 1) la consulta cabe entera en el indice: Index Only Scan; 2) se pide una
    // columna que no esta: vuelve a la tabla; 3) INCLUDE la guarda en las hojas y se recupera.
    pasos: [0.34, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var f2 = L.tramo(t, 0.36, 0.42), f3 = L.tramo(t, 0.7, 0.76);
      // 1 · la consulta y el indice que la cubre
      UJ.codigo(ctx, lz, 30, 22, W - 60, f2 >= 1 ? 'SELECT estado, fecha_hora, id_mascota FROM cita' : 'SELECT estado, fecha_hora FROM cita', L.tramo(t, 0, 0.08), 17);
      UJ.codigo(ctx, lz, 30, 66, W - 60, "WHERE estado = 'PROGRAMADA' AND fecha_hora >= '2026-03-01'", L.tramo(t, 0.06, 0.14), 17);
      UJ.caja(ctx, lz, 30, 140, 320, 120, f3 >= 1 ? 'idx_cita_cubridor' : 'idx_cita_estado_fecha',
              f3 >= 1 ? '(estado, fecha_hora) INCLUDE (id_mascota)' : '(estado, fecha_hora)', C, L.tramo(t, 0.14, 0.22));
      UJ.caja(ctx, lz, 470, 140, 300, 120, 'tabla cita', 'filas completas', A, L.tramo(t, 0.14, 0.22));
      // estado del plan: sin tabla (paso 1 y 3) o con tabla (paso 2)
      var conTabla = f2 >= 1 && f3 < 1;
      UJ.alfa(ctx, L.tramo(t, 0.22, 0.3), function () {
        L.rectRed(ctx, 30, 300, W - 60, 130, 14);
        L.rellena(ctx, L.tono(conTabla ? R : V, 0.9), conTabla ? R : V, 2);
        UJ.rotulo(ctx, lz, conTabla ? 'Bitmap Heap Scan on cita' : (f3 >= 1 ? 'Index Only Scan using idx_cita_cubridor' : 'Index Only Scan using idx_cita_estado_fecha'),
                  W / 2, 314, { tam: 20, peso: 800, color: conTabla ? R : V, ancho: W - 100 });
        UJ.rotulo(ctx, lz, conTabla ? 'id_mascota no está en el índice: va a la tabla por cada fila' : 'responde desde el índice, sin tocar la tabla (Heap Fetches: 0)',
                  W / 2, 356, { tam: 17, ancho: W - 100 });
        UJ.rotulo(ctx, lz, '13.187 filas', W / 2, 394, { tam: 16, peso: 700, color: L.tono(m.tinta, 0.3) });
      });
      if (conTabla) L.flecha(ctx, 354, 200, 466, 200, R, 4, 1);
      UJ.sello(ctx, lz, 410, 200, 24, true, L.tramo(t, 0.26, 0.32) * (conTabla ? 0 : 1));
      // 3 · la salida: INCLUDE
      UJ.alfa(ctx, f3, function () {
        L.rectRed(ctx, 30, 460, W - 60, 140, 14); L.rellena(ctx, L.tono(V, 0.88), V, 2);
        UJ.rotulo(ctx, lz, 'INCLUDE guarda la columna en las hojas sin usarla para ordenar', W / 2, 474, { tam: 19, peso: 800, color: V, ancho: W - 100 });
        L.texto(ctx, 'CREATE INDEX idx_cita_cubridor ON cita (estado, fecha_hora)', W / 2, 520, { tam: 15, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
        L.texto(ctx, 'INCLUDE (id_mascota);', W / 2, 548, { tam: 15, peso: 600, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
      });
    }
  });
})();
