/* Ilustracion: el nombre del indice se lee en dos lugares, en el plan (el nodo de acceso por
 * indice) y en pg_indexes (indexdef, con el WHERE del parcial). Y el nombre que no es: el sufijo
 * va como la columna, _fecha_hora. Salidas reales de PGlite. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-nombre-en-plan', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      UJ.rotulo(ctx, lz, 'El nombre se lee en la salida, no en la pizarra', W / 2, 8, { tam: 23, peso: 800, color: A, ancho: W - 30 });
      // en el plan
      L.rectRed(ctx, 16, 50, W - 32, 196, 14); L.rellena(ctx, L.tono(A, 0.94), A, 2);
      UJ.rotulo(ctx, lz, '1 · En el plan, junto al nodo que usa el índice', 32, 60, { tam: 17, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 92, W - 60, 'Bitmap Heap Scan on cita  (rows=91)', 1, 15);
      UJ.codigo(ctx, lz, 30, 128, W - 60, '  ->  Bitmap Index Scan on idx_cita_programada_fecha', 1, 15);
      ctx.strokeStyle = m.sello || '#FFD000'; ctx.lineWidth = 3;
      L.rectRed(ctx, 262, 128, 214, 30, 6); ctx.stroke();
      UJ.rotulo(ctx, lz, 'en un servidor también puede salir como «Index Scan using <nombre>»: es el mismo acceso por índice', W / 2, 178, { tam: 15, ancho: W - 80 });
      // en pg_indexes
      L.rectRed(ctx, 16, 260, W - 32, 196, 14); L.rellena(ctx, L.tono(V, 0.92), V, 2);
      UJ.rotulo(ctx, lz, '2 · En pg_indexes: indexdef trae el CREATE INDEX completo', 32, 270, { tam: 17, peso: 800, color: V, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 302, W - 60, 'SELECT indexname, indexdef FROM pg_indexes', 1, 15);
      UJ.codigo(ctx, lz, 30, 338, W - 60, " WHERE tablename IN ('cita','mascota');", 1, 15);
      UJ.rotulo(ctx, lz, "… ON public.cita USING btree (fecha_hora) WHERE (estado = 'PROGRAMADA'::text)", W / 2, 386, { tam: 15, peso: 700, ancho: W - 70 });
      UJ.rotulo(ctx, lz, 'ese WHERE confirma que el índice se creó parcial', W / 2, 420, { tam: 15, color: L.tono(V, -0.3) });
      // el nombre que no es
      L.rectRed(ctx, 16, 470, 376, 150, 14); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      L.texto(ctx, 'idx_cita_fecha', 204, 500, { tam: 22, peso: 700, color: R, alinear: 'center', letra: 'Consolas, monospace' });
      UJ.sello(ctx, lz, 204, 572, 22, false, 1);
      L.rectRed(ctx, 408, 470, 376, 150, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
      L.texto(ctx, 'idx_cita_fecha_hora', 596, 500, { tam: 22, peso: 700, color: V, alinear: 'center', letra: 'Consolas, monospace' });
      UJ.rotulo(ctx, lz, 'el sufijo es el de la columna', 596, 534, { tam: 15 });
      UJ.sello(ctx, lz, 596, 584, 22, true, 1);
    }
  });
})();
