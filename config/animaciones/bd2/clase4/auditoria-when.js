/* La auditoria y el WHEN: tres UPDATE llegan; el tercero deja el estado que ya tenia y el
 * WHEN (OLD.estado IS DISTINCT FROM NEW.estado) no lo deja pasar: tres UPDATE, DOS filas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('auditoria-when', {
    duracion: 5,
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var ups = [['pendiente', 'confirmada', true], ['confirmada', 'atendida', true], ['atendida', 'atendida', false]];
      // El filtro
      L.rectRed(ctx, 330, 40, 120, 330, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
      UJ.rotulo(ctx, lz, 'WHEN', 390, 60, { tam: 24, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'OLD.estado IS DISTINCT FROM NEW.estado', 390, 100, { tam: 16, ancho: 110, color: m.tinta });
      var filas = [];
      for (var i = 0; i < 3; i++) {
        var t0 = 0.05 + i * 0.22, u = ups[i], y = 70 + i * 100;
        var x = L.claves(t, [[t0, -280], [t0 + 0.1, 30, 'frena'], [t0 + 0.13, 30], [t0 + 0.2, u[2] ? 480 : 40, 'suave']]);
        if (t >= t0) {
          L.rectRed(ctx, x, y, 270, 60, 10); L.rellena(ctx, m.papel, u[2] ? C : R, 3);
          UJ.rotulo(ctx, lz, 'UPDATE ' + (i + 1), x + 14, y + 6, { tam: 17, peso: 800, alinear: 'left', color: u[2] ? C : R });
          UJ.rotulo(ctx, lz, u[0] + ' → ' + u[1], x + 14, y + 32, { tam: 16, peso: 500, alinear: 'left' });
        }
        if (!u[2]) UJ.sello(ctx, lz, 310, y + 30, 26, false, L.tramo(t, t0 + 0.18, t0 + 0.24));
        if (u[2] && t > t0 + 0.2) filas.push(u[0] + ' → ' + u[1]);
      }
      UJ.tabla(ctx, lz, 470, 420, 310, 'audit_cita', ['pendiente → confirmada', 'confirmada → atendida'], filas.length, A, -1);
      UJ.rotulo(ctx, lz, '3 UPDATE → 2 filas', 200, 470, { tam: 30, peso: 800, color: A, visible: L.tramo(t, 0.82, 0.9) });
      UJ.rotulo(ctx, lz, 'El que no cambia nada no se audita.', 200, 520, { tam: 19, ancho: 360, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
