/* Los cuatro niveles del estandar SQL se definen por cuales de los tres fenomenos permiten. Un
 * nivel por paso, de menos a mas aislado. Las notas de cada fila dicen lo que hace PostgreSQL:
 * READ COMMITTED por omision, READ UNCOMMITTED se comporta como READ COMMITTED y su REPEATABLE
 * READ (foto de la transaccion) tampoco deja ver fantasmas. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('niveles-aislamiento', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      var x0 = 20, xc = [330, 490, 650], y0 = 30, h = 92;
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, x0, y0, W - 40, 70, 12); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'Nivel', 150, y0 + 22, { tam: 20, peso: 800, color: m.papel });
        var cab = ['lectura sucia', 'no repetible', 'fantasma'];
        for (var k = 0; k < 3; k++) UJ.rotulo(ctx, lz, cab[k], xc[k], y0 + 10, { tam: 18, peso: 800, color: m.papel, ancho: 140 });
      });
      var filas = [
        ['READ UNCOMMITTED', [1, 1, 1], 'PostgreSQL lo trata como READ COMMITTED'],
        ['READ COMMITTED', [0, 1, 1], 'por omisión en PostgreSQL'],
        ['REPEATABLE READ', [0, 0, 1], 'el estándar permite fantasmas; PostgreSQL no'],
        ['SERIALIZABLE', [0, 0, 0], 'como una tras otra; puede abortar: reintentar']
      ];
      var tiempos = [[0.08, 0.26], [0.32, 0.5], [0.57, 0.75], [0.82, 0.96]];
      for (var i = 0; i < 4; i++) {
        var f = filas[i], y = y0 + 80 + i * (h + 40);
        var a = L.tramo(t, tiempos[i][0], tiempos[i][1]);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x0, y, W - 40, h, 12); L.rellena(ctx, i === 1 ? L.tono(m.sello || C, 0.75) : L.tono(A, 0.93), L.tono(A, 0.5), 2);
          L.texto(ctx, f[0], 40, y + 12, { tam: 19, peso: 800, color: m.tinta, letra: 'Consolas, monospace', ancho: 240 });
          L.texto(ctx, f[2], 40, y + 42, { tam: 15, peso: 600, color: L.tono(m.tinta, 0.2), letra: lz.letra, ancho: 245 });
        });
        for (var k = 0; k < 3; k++) {
          UJ.alfa(ctx, a, function () {
            UJ.rotulo(ctx, lz, f[1][k] ? 'permite' : 'impide', xc[k], y + 60, { tam: 16, peso: 700, color: f[1][k] ? R : V });
          });
          UJ.sello(ctx, lz, xc[k], y + 32, 20, !f[1][k], L.tramo(t, tiempos[i][0] + 0.03 * (k + 1), tiempos[i][0] + 0.03 * (k + 1) + 0.08));
        }
      }
    }
  });
})();
