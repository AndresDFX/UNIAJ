/* Encapsular es proteger una regla: con public activa, tres archivos la apagan sin rastro;
 * con private, quedan bloqueados y solo pasa inactivar(motivo), que guarda motivo y fecha. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('encapsular-regla', {
    duracion: 4.8,
    pasos: [0.36, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde, R = m.malva, W = lz.ancho;
      var priv = t >= 0.42, cierra = L.tramo(t, 0.4, 0.46);
      // El objeto
      L.rectRed(ctx, 430, 90, 340, 170, 14); L.rellena(ctx, L.tono(V, 0.9), V, 3);
      UJ.rotulo(ctx, lz, 'Mascota luna', 600, 102, { tam: 20, peso: 800, color: V });
      UJ.rotulo(ctx, lz, priv ? 'private boolean activa' : 'public boolean activa', 600, 146, { tam: 19, peso: 700, color: priv ? V : R, letra: 'Consolas, monospace' });
      var apagada = (t >= 0.2 && t < 0.42) || t >= 0.66;
      UJ.rotulo(ctx, lz, apagada ? '= false' : '= true', 600, 180, { tam: 22, peso: 800, color: apagada && t < 0.42 ? R : V, letra: 'Consolas, monospace' });
      if (priv) { L.rectRed(ctx, 426, 86, 348, 178, 16); ctx.lineWidth = 6 * cierra; ctx.strokeStyle = A; if (cierra > 0) ctx.stroke(); }
      // Archivos que escriben directo
      var arch = ['Agenda.java', 'Reporte.java', 'Main.java'];
      for (var i = 0; i < 3; i++) {
        var y = 40 + i * 90;
        UJ.alfa(ctx, L.tramo(t, 0.02 + i * 0.04, 0.08 + i * 0.04), function () {
          L.rectRed(ctx, 24, y, 190, 56, 10); L.rellena(ctx, L.tono(m.gris, 0.85), m.gris, 2);
          UJ.rotulo(ctx, lz, arch[i], 119, y + 15, { tam: 19, peso: 700, letra: 'Consolas, monospace' });
        });
        var col = priv ? L.tono(m.gris, 0.4) : R;
        L.flecha(ctx, 218, y + 28, 424, 175, col, 3, L.tramo(t, 0.1 + i * 0.04, 0.18 + i * 0.04, 'frena'));
        UJ.sello(ctx, lz, 320, y + 28 + (147 - y) * 0.495, 18, false, L.tramo(t, 0.44 + i * 0.03, 0.5 + i * 0.03));
      }
      UJ.rotulo(ctx, lz, 'luna.activa = false;  ¿quién fue, y por qué?', W / 2, 300, { tam: 21, peso: 700, color: R, ancho: W - 40, visible: L.tramo(t, 0.22, 0.32) * (1 - L.tramo(t, 0.4, 0.42)) });
      // La unica puerta
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.6), function () {
        L.rectRed(ctx, 24, 330, 190, 56, 10); L.rellena(ctx, L.tono(m.gris, 0.85), m.gris, 2);
        UJ.rotulo(ctx, lz, 'Recepción.java', 119, 345, { tam: 19, peso: 700, letra: 'Consolas, monospace' });
        L.rectRed(ctx, 430, 320, 340, 76, 12); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'inactivar(motivo)', 600, 330, { tam: 22, peso: 800, color: m.papel, letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'la única puerta', 600, 362, { tam: 17, color: m.papel });
      });
      L.flecha(ctx, 218, 358, 424, 358, A, 4, L.tramo(t, 0.58, 0.64, 'frena'));
      L.flecha(ctx, 600, 318, 600, 268, A, 4, L.tramo(t, 0.62, 0.66, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.7), function () {
        L.rectRed(ctx, 430, 410, 340, 70, 10); L.rellena(ctx, L.tono(m.sello, 0.7), L.tono(m.sello, -0.4), 2);
        UJ.rotulo(ctx, lz, 'motivo: "traslado"', 450, 418, { tam: 18, alinear: 'left', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'fecha: 2026-10-03', 450, 446, { tam: 18, alinear: 'left', letra: 'Consolas, monospace' });
      });
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.9), function () {
        L.rectRed(ctx, 24, 500, W - 48, 116, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Un solo lugar donde la regla puede romperse.', W / 2, 514, { tam: 22, peso: 800, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'Getters y setters para todo no es encapsular:', W / 2, 554, { tam: 19, ancho: W - 80 });
        UJ.rotulo(ctx, lz, 'se exponen operaciones del dominio.', W / 2, 582, { tam: 19, ancho: W - 80 });
      });
    }
  });
})();
