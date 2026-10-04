/* Correccion y tiempo son ejes independientes. Se comprueba con SELECT COUNT(*) de cada version
 * en la misma corrida: conteos iguales -> optimizacion; distintos -> respuesta equivocada. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('mismo-resultado', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.codigo(ctx, lz, 40, 30, W - 80, 'SELECT COUNT(*) FROM ( …versión ANTES… ) a;', L.tramo(t, 0, 0.12), 18);
      UJ.codigo(ctx, lz, 40, 84, W - 80, 'SELECT COUNT(*) FROM ( …versión DESPUÉS… ) d;', L.tramo(t, 0.1, 0.22), 18);
      UJ.rotulo(ctx, lz, 'en la misma corrida', W / 2, 140, { tam: 18, peso: 600, color: L.tono(m.tinta, 0.3), visible: L.tramo(t, 0.2, 0.26) });
      function caso(x, a0, n1, n2, ok, tit, sub) {
        var c = ok ? V : R;
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.08), function () {
          L.rectRed(ctx, x, 186, 340, 290, 16); L.rellena(ctx, L.tono(c, 0.9), c, 3);
          UJ.rotulo(ctx, lz, 'ANTES', x + 90, 204, { tam: 18, peso: 700 });
          UJ.rotulo(ctx, lz, 'DESPUÉS', x + 250, 204, { tam: 18, peso: 700 });
          UJ.rotulo(ctx, lz, n1, x + 90, 236, { tam: 34, peso: 800, color: A });
          UJ.rotulo(ctx, lz, n2, x + 250, 236, { tam: 34, peso: 800, color: ok ? A : R });
          UJ.rotulo(ctx, lz, tit, x + 170, 370, { tam: 22, peso: 800, color: c, ancho: 310 });
          UJ.rotulo(ctx, lz, sub, x + 170, 410, { tam: 17, peso: 500, ancho: 310 });
        });
        UJ.sello(ctx, lz, x + 170, 320, 28, ok, L.tramo(t, a0 + 0.08, a0 + 0.14));
      }
      caso(40, 0.24, '150', '150', true, 'Es una optimización', 'mismo resultado, menos tiempo');
      caso(420, 0.58, '150', '148', false, 'Respuesta equivocada', 'no es una versión más rápida');
      UJ.rotulo(ctx, lz, 'Corrección y tiempo son ejes independientes.', W / 2, 530,
                { tam: 22, ancho: W - 40, color: A, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
