/* La matriz es la decision; el script es su traduccion. Objetos en filas, roles en columnas,
 * notacion S I U D E y guion. Sin celdas vacias y coherente con los GRANT: sin D si nadie la
 * recibio; los procedimientos van con E. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('matriz-decision', {
    duracion: 5,
    pasos: [0.42, 0.74, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var roles = ['admin_bd', 'recepcion', 'veterinario_rol', 'auditor'];
      var objs = [['cita', ['S I U D', 'S I U', 'S', 'S']], ['consulta', ['S I U D', '—', 'S I U', 'S']],
                  ['factura', ['S I U D', '—', '—', 'S']], ['sp_agendar_cita', ['E', 'E', '—', '—']]];
      var x0 = 200, cw = 140, y0 = 30, ch = 52;
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () {
        for (var j = 0; j < 4; j++) {
          L.rectRed(ctx, x0 + j * cw, y0, cw, ch, 0); L.rellena(ctx, C, m.papel, 2);
          UJ.rotulo(ctx, lz, roles[j], x0 + j * cw + cw / 2, y0 + 16, { tam: 16, peso: 700, color: m.papel });
        }
      });
      UJ.rotulo(ctx, lz, 'roles →', x0 - 14, y0 + 16, { tam: 16, alinear: 'right', color: C, visible: L.tramo(t, 0.04, 0.1) });
      for (var i = 0; i < 4; i++) {
        var y = y0 + ch * (i + 1);
        UJ.alfa(ctx, L.tramo(t, 0.06 + i * 0.05, 0.12 + i * 0.05), function () {
          L.rectRed(ctx, 30, y, 170, ch, 0); L.rellena(ctx, A, m.papel, 2);
          L.texto(ctx, objs[i][0], 115, y + 15, { tam: 17, peso: 700, color: m.papel, alinear: 'center', letra: 'Consolas, monospace' });
        });
        for (var j = 0; j < 4; j++) {
          var esE = i === 3 && objs[i][1][j] === 'E';
          UJ.alfa(ctx, L.tramo(t, 0.16 + (i * 4 + j) * 0.014, 0.2 + (i * 4 + j) * 0.014), function () {
            L.rectRed(ctx, x0 + j * cw, y, cw, ch, 0);
            L.rellena(ctx, esE && t >= 0.5 ? L.tono(m.sello || C, 0.6) : (i % 2 ? L.tono(A, 0.94) : m.papel), L.tono(A, 0.5), 1);
            L.texto(ctx, objs[i][1][j], x0 + j * cw + cw / 2, y + 14, { tam: 20, peso: 700, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
          });
        }
      }
      UJ.rotulo(ctx, lz, 'S SELECT · I INSERT · U UPDATE · D DELETE · E EXECUTE · — ninguno', W / 2, 300,
                { tam: 17, ancho: W - 40, visible: L.tramo(t, 0.34, 0.42) });
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.56), function () {
        L.rectRed(ctx, 30, 346, W - 60, 56, 10); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'El procedimiento va con E, nunca con S ni con I', W / 2, 361, { tam: 19, peso: 700 });
      });
      var reglas = [['Sin celdas vacías: cada objeto por cada rol', V], ['Coherente con los GRANT: ni una letra que no se otorgó', R]];
      for (var k = 0; k < 2; k++) {
        UJ.alfa(ctx, L.tramo(t, 0.76 + k * 0.1, 0.84 + k * 0.1), function () {
          L.rectRed(ctx, 30, 426 + k * 72, W - 60, 60, 10); L.rellena(ctx, L.tono(reglas[k][1], 0.9), reglas[k][1], 2);
          UJ.rotulo(ctx, lz, reglas[k][0], W / 2, 444 + k * 72, { tam: 19, peso: 700, ancho: W - 100 });
        });
      }
    }
  });
})();
