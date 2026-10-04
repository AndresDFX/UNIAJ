/* Seguridad y respaldo: la seguridad intenta que nada malo pase (roles y GRANT); el respaldo
 * asume que pasara. pg_dump respalda UNA base; los roles salen con pg_dumpall --globals-only. */
(function () {
  var L = FP_LIENZO;
  function escudo(ctx, x, y, s, color) {
    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + s * 0.5, y + s * 0.18); ctx.lineTo(x + s * 0.44, y + s * 0.7);
    ctx.quadraticCurveTo(x + s * 0.3, y + s * 0.95, x, y + s * 1.08);
    ctx.quadraticCurveTo(x - s * 0.3, y + s * 0.95, x - s * 0.44, y + s * 0.7); ctx.lineTo(x - s * 0.5, y + s * 0.18); ctx.closePath();
    ctx.fillStyle = color; ctx.fill();
  }
  function base(ctx, x, y, an, al, color, papel) {
    var e = al * 0.16;
    ctx.fillStyle = color; ctx.fillRect(x, y + e / 2, an, al - e);
    ctx.beginPath(); ctx.ellipse(x + an / 2, y + al - e / 2, an / 2, e / 2, 0, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.ellipse(x + an / 2, y + e / 2, an / 2, e / 2, 0, 0, Math.PI * 2); ctx.fillStyle = papel; ctx.fill();
    ctx.strokeStyle = color; ctx.lineWidth = 3; ctx.stroke();
  }
  FP_ANIMADOR.registrar('seguridad-respaldo', {
    duracion: 4.8,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      // Seguridad
      UJ.alfa(ctx, L.tramo(t, 0, 0.14), function () {
        escudo(ctx, 190, 40, 130, A);
        UJ.rotulo(ctx, lz, 'GRANT', 190, 100, { tam: 22, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, 'Seguridad', 190, 196, { tam: 26, peso: 800, color: A });
        UJ.rotulo(ctx, lz, 'que nada malo pase', 190, 232, { tam: 19 });
      });
      // Respaldo
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.3), function () {
        base(ctx, 540, 40, 110, 120, C, m.papel);
        UJ.rotulo(ctx, lz, 'Respaldo', 595, 196, { tam: 26, peso: 800, color: C });
        UJ.rotulo(ctx, lz, 'asume que pasará', 595, 232, { tam: 19 });
      });
      // Las dos copias
      UJ.codigo(ctx, lz, 24, 300, W - 48, 'pg_dump -Fc -d clinica -f clinica_AAAAMMDD.dump', L.tramo(t, 0.34, 0.5), 16);
      L.flecha(ctx, 400, 336, 400, 376, C, 4, L.tramo(t, 0.5, 0.56, 'frena'));
      UJ.caja(ctx, lz, 230, 380, 340, 58, 'una base: tablas y datos', null, C, L.tramo(t, 0.54, 0.62));
      UJ.codigo(ctx, lz, 24, 462, W - 48, 'pg_dumpall --globals-only -f roles.sql', L.tramo(t, 0.64, 0.78), 16);
      L.flecha(ctx, 400, 498, 400, 538, A, 4, L.tramo(t, 0.78, 0.84, 'frena'));
      UJ.caja(ctx, lz, 230, 542, 340, 58, 'los roles, que pg_dump no copia', null, A, L.tramo(t, 0.82, 0.92));
    }
  });
})();
