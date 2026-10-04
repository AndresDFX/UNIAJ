/* El molde de PL/pgSQL: AS (no IS), el cuerpo es una cadena entre $proc$, punto y coma final
 * obligatorio y sin barra. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('molde-plpgsql', {
    duracion: 5,
    pasos: [0.35, 0.65, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      var lin = [
        'CREATE PROCEDURE sp_x(p_id INT)',
        'LANGUAGE plpgsql',
        'AS $proc$',
        'DECLARE',
        '  v_activa CHAR(1);',
        'BEGIN',
        "  RAISE NOTICE 'paso; ok';",
        'END;',
        '$proc$;'
      ];
      var x0 = 30, y0 = 24, an = 430, h = 40;
      L.rectRed(ctx, x0, y0, an, lin.length * h + 24, 12); L.rellena(ctx, L.tono(m.tinta, -0.55));
      for (var i = 0; i < lin.length; i++) {
        // fillText directo: L.texto parte por espacios y se come la sangria.
        var v = L.tramo(t, 0.02 + i * 0.03, 0.05 + i * 0.03);
        ctx.font = '500 19px Consolas, monospace'; ctx.fillStyle = '#E8F4FA';
        ctx.textAlign = 'left'; ctx.textBaseline = 'top';
        ctx.fillText(lin[i].slice(0, Math.round(lin[i].length * v)), x0 + 16, y0 + 14 + i * h);
      }
      var cu = L.tramo(t, 0.36, 0.46);
      UJ.alfa(ctx, cu, function () {
        L.rectRed(ctx, x0 + 6, y0 + 8 + 3 * h, an - 12, 5 * h, 8); L.rellena(ctx, L.tono(C, 0.2, 0.25), C, 3);
      });
      var nota = function (y, txt, col, a) {
        UJ.alfa(ctx, a, function () {
          L.flecha(ctx, 556, y + 14, x0 + an + 8, y + 14, col, 3, 1);
          L.rectRed(ctx, 560, y - 8, 220, 46, 10); L.rellena(ctx, L.tono(col, 0.9), col, 2);
          UJ.rotulo(ctx, lz, txt, 670, y + 3, { tam: 18, peso: 700, color: col, ancho: 210 });
        });
      };
      nota(y0 + 14 + 2 * h, 'AS, no IS', A, L.tramo(t, 0.26, 0.34));
      nota(y0 + 14 + 5 * h, 'cuerpo = una cadena', C, L.tramo(t, 0.46, 0.56));
      nota(y0 + 14 + 8 * h, '; final obligatorio', A, L.tramo(t, 0.66, 0.74));
      UJ.rotulo(ctx, lz, 'Entre $proc$ caben ; y comillas sin duplicarlas.', W / 2, 440, { tam: 20, ancho: W - 40, visible: L.tramo(t, 0.55, 0.65) });
      UJ.rotulo(ctx, lz, '$$ funciona igual; la etiqueta sirve para bloques anidados.', W / 2, 480, { tam: 18, ancho: W - 40, visible: L.tramo(t, 0.74, 0.82) });
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        UJ.codigo(ctx, lz, 150, 540, 60, '/', 1, 22);
        UJ.sello(ctx, lz, 250, 562, 22, false, 1);
        UJ.rotulo(ctx, lz, 'la barra de Oracle aquí es error', 290, 550, { tam: 19, color: R, alinear: 'left', ancho: 400 });
      });
    }
  });
})();
