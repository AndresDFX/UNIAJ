/* Los cuatro terminos: objeto (lo que el motor guarda con nombre), esquema (contenedor con nombre:
 * public.cita), privilegio (permiso atomico sobre un objeto) y rol (paquete de privilegios). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('cuatro-terminos', {
    duracion: 5,
    pasos: [0.26, 0.5, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, S = m.sello || C;
      // Esquema
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.34), function () {
        L.rectRed(ctx, 30, 30, 420, 400, 18); L.rellena(ctx, L.tono(A, 0.94), A, 3);
        UJ.rotulo(ctx, lz, 'Esquema public', 50, 44, { tam: 22, peso: 800, color: A, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'nombre completo: public.cita', 50, 78, { tam: 17, alinear: 'left' });
      });
      // Objetos
      var obj = [['cita', 'tabla'], ['v_agenda', 'vista'], ['sp_agendar', 'procedimiento'], ['seq_cita', 'secuencia']];
      for (var i = 0; i < 4; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.02 + i * 0.05, 0.08 + i * 0.05), function () {
          var x = 60 + (i % 2) * 190, y = 130 + Math.floor(i / 2) * 140;
          L.rectRed(ctx, x, y, 170, 110, 12); L.rellena(ctx, m.papel, C, 2);
          L.texto(ctx, obj[i][0], x + 85, y + 26, { tam: 18, peso: 700, color: A, alinear: 'center', letra: 'Consolas, monospace' });
          UJ.rotulo(ctx, lz, obj[i][1], x + 85, y + 64, { tam: 16, color: L.tono(m.tinta, 0.2) });
        });
      }
      UJ.rotulo(ctx, lz, 'Objeto: lo que el motor guarda con nombre', 240, 446, { tam: 18, peso: 700, ancho: 420, visible: L.tramo(t, 0.14, 0.24) });
      // Privilegio
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.6), function () {
        L.rectRed(ctx, 500, 120, 270, 92, 14); L.rellena(ctx, L.tono(S, 0.75), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Privilegio', 635, 132, { tam: 22, peso: 800 });
        UJ.rotulo(ctx, lz, 'SELECT sobre cita', 635, 168, { tam: 17 });
        L.trazo(ctx, [[496, 140], [470, 116], [145, 116]], 1, L.tono(m.tinta, 0.3), 3); L.flecha(ctx, 145, 114, 145, 128, L.tono(m.tinta, 0.3), 3);
      });
      UJ.rotulo(ctx, lz, 'permiso atómico sobre un objeto', 635, 224, { tam: 16, ancho: 260, visible: L.tramo(t, 0.56, 0.64) });
      // Rol
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.86), function () {
        L.rectRed(ctx, 500, 300, 270, 130, 14); L.rellena(ctx, L.tono(C, 0.85), C, 3);
        UJ.rotulo(ctx, lz, 'Rol', 635, 312, { tam: 22, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'paquete de privilegios con nombre: recepcion', 635, 348, { tam: 17, ancho: 240 });
        L.flecha(ctx, 635, 296, 635, 236, L.tono(m.tinta, 0.3), 3);
      });
      UJ.rotulo(ctx, lz, 'Administrar: quién puede hacer qué sobre cada objeto, y dejar rastro.', W / 2, 520,
                { tam: 20, peso: 700, ancho: W - 60, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
