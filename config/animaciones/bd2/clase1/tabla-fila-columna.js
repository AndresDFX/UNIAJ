/* El vocabulario minimo: la tabla (relacion) guarda entidades de un solo tipo; la fila es una
 * instancia concreta; la columna es un atributo con su dominio de valores legales. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('tabla-fila-columna', {
    duracion: 4.5,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      var cols = ['id_mascota', 'nombre', 'especie', 'id_dueno'];
      var filas = [['1', 'Luna', 'Canino', '1'], ['2', 'Michi', 'Felino', '2'], ['3', 'Kiwi', 'Ave', '1']];
      var x0 = 70, y0 = 90, cw = 165, ch = 48;
      var a = L.tramo(t, 0, 0.12);
      UJ.alfa(ctx, a, function () {
        UJ.rotulo(ctx, lz, 'mascota', x0, 40, { tam: 26, peso: 800, color: A, alinear: 'left' });
        for (var j = 0; j < 4; j++) {
          L.rectRed(ctx, x0 + j * cw, y0, cw, ch, 0); L.rellena(ctx, A, m.papel, 2);
          UJ.rotulo(ctx, lz, cols[j], x0 + j * cw + cw / 2, y0 + 13, { tam: 18, peso: 700, color: m.papel });
        }
      });
      for (var i = 0; i < 3; i++) {
        var ai = L.tramo(t, 0.06 + i * 0.05, 0.14 + i * 0.05);
        UJ.alfa(ctx, ai, function () {
          for (var j = 0; j < 4; j++) {
            L.rectRed(ctx, x0 + j * cw, y0 + ch * (i + 1), cw, ch, 0);
            L.rellena(ctx, i % 2 ? L.tono(A, 0.93) : m.papel, L.tono(A, 0.5), 1);
            L.texto(ctx, filas[i][j], x0 + j * cw + cw / 2, y0 + ch * (i + 1) + 13, { tam: 19, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
          }
        });
      }
      UJ.rotulo(ctx, lz, 'Tabla (relación): solo mascotas, nada más.', W / 2, 310, { tam: 21, ancho: W - 60, visible: L.tramo(t, 0.2, 0.3) });
      // Fila
      var af = L.tramo(t, 0.34, 0.44);
      UJ.alfa(ctx, af, function () {
        ctx.lineWidth = 5; ctx.strokeStyle = m.sello || C;
        L.rectRed(ctx, x0 - 6, y0 + ch - 4, cw * 4 + 12, ch + 8, 8); ctx.stroke();
        L.rectRed(ctx, 40, 370, 340, 100, 12); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'Fila = una instancia', 210, 386, { tam: 22, peso: 800 });
        UJ.rotulo(ctx, lz, 'la perra Luna, y solo ella', 210, 424, { tam: 18, ancho: 310 });
      });
      // Columna y dominio
      var ac = L.tramo(t, 0.68, 0.78);
      UJ.alfa(ctx, ac, function () {
        ctx.lineWidth = 5; ctx.strokeStyle = C;
        L.rectRed(ctx, x0 + 2 * cw - 4, y0 - 6, cw + 8, ch * 4 + 12, 8); ctx.stroke();
        L.rectRed(ctx, 420, 370, 340, 100, 12); L.rellena(ctx, L.tono(C, 0.85), C, 2);
        UJ.rotulo(ctx, lz, 'Columna = atributo', 590, 386, { tam: 22, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'con un dominio de valores legales', 590, 424, { tam: 18, ancho: 310 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.82, 0.94), function () {
        L.rectRed(ctx, 100, 500, W - 200, 56, 28); L.rellena(ctx, m.papel, C, 2);
        UJ.rotulo(ctx, lz, 'especie ∈ { Canino · Felino · Ave · Otro }', W / 2, 514, { tam: 21, peso: 700, color: L.tono(C, -0.3) });
      });
    }
  });
})();
