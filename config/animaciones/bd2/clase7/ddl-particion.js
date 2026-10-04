/* El DDL: la tabla particionada por rango y sus dos particiones. Trampa 1: la PK debe incluir la
 * columna de particion. Trampa 2: el rango es cerrado abajo y abierto arriba (el TO de una es el
 * FROM de la siguiente). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ddl-particion', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.35, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var lin = ['CREATE TABLE cita_part ( …,', '  PRIMARY KEY (id_cita, fecha_hora)', ') PARTITION BY RANGE (fecha_hora);',
                 'CREATE TABLE cita_2025 PARTITION OF cita_part', "  FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');",
                 'CREATE TABLE cita_2026 PARTITION OF cita_part', "  FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');"];
      for (var i = 0; i < lin.length; i++) UJ.codigo(ctx, lz, 20, 20 + i * 40, W - 40, lin[i], L.tramo(t, i * 0.04, 0.05 + i * 0.04), 15);
      // trampa 1
      var a1 = L.tramo(t, 0.36, 0.44);
      UJ.alfa(ctx, a1, function () {
        ctx.strokeStyle = R; ctx.lineWidth = 3; L.rectRed(ctx, 16, 58, W - 32, 34, 6); ctx.stroke();
        L.rectRed(ctx, 20, 320, 370, 170, 14); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'Trampa 1', 205, 332, { tam: 21, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'la clave primaria DEBE incluir la columna de partición', 205, 368, { tam: 17, ancho: 330 });
        L.texto(ctx, 'PRIMARY KEY (id_cita) a secas: error', 205, 440, { tam: 15, peso: 700, color: R, alinear: 'center', letra: 'Consolas, monospace', ancho: 350 });
      });
      // trampa 2
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        ctx.strokeStyle = C; ctx.lineWidth = 3;
        L.rectRed(ctx, 16, 178, W - 32, 34, 6); ctx.stroke(); L.rectRed(ctx, 16, 258, W - 32, 34, 6); ctx.stroke();
        L.rectRed(ctx, 410, 320, 370, 170, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'Trampa 2', 595, 332, { tam: 21, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'FROM incluye, TO excluye: el TO de una es el FROM de la siguiente', 595, 368, { tam: 17, ancho: 330 });
      });
      UJ.rotulo(ctx, lz, 'Sin huecos y sin solapes entre particiones.', W / 2, 540, { tam: 21, ancho: W - 40, color: V, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
