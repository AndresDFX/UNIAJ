/* Scope creep con su sintoma cuantificable: el numero de entidades. Seis minimas, rango sano de
 * seis a nueve; quince no es ir adelantado, es el mismo esfuerzo en el doble de superficie. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('scope-creep', {
    duracion: 5,
    pasos: [0.36, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var x0 = 40, paso = 46, yb = 300, alto = 70;
      UJ.rotulo(ctx, lz, 'Número de entidades', W / 2, 30, { tam: 26, peso: 800, color: A });
      // zona sana 6..9
      UJ.alfa(ctx, L.tramo(t, 0.2, 0.3), function () {
        L.rectRed(ctx, x0 + 5 * paso, yb - 30, 4 * paso, alto + 60, 10); L.rellena(ctx, L.tono(V, 0.82), V, 2);
        UJ.rotulo(ctx, lz, 'rango sano: 6 a 9', x0 + 7 * paso, yb - 72, { tam: 19, peso: 800, color: V });
      });
      var n = L.claves(t, [[0, 0], [0.18, 6, 'frena'], [0.4, 6], [0.42, 7], [0.78, 15, 'suave']]);
      for (var i = 0; i < 15; i++) {
        var a = Math.max(0, Math.min(1, n - i));
        if (a <= 0) continue;
        var col = i < 6 ? A : i < 9 ? L.tono(A, 0.25) : R;
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x0 + i * paso + 4, yb, paso - 8, alto, 6); L.rellena(ctx, L.tono(col, 0.3), col, 2);
        });
      }
      UJ.rotulo(ctx, lz, '6 mínimas', x0 + 3 * paso, yb + alto + 14, { tam: 18, peso: 700, color: A, visible: L.tramo(t, 0.16, 0.22) });
      var extras = ['proveedores', 'multialmacén', 'portal de dueños', 'notificaciones'];
      for (var k = 0; k < 4; k++)
        UJ.rotulo(ctx, lz, '+ ' + extras[k], 560, 412 + k * 28, { tam: 18, peso: 600, color: R, alinear: 'left', visible: L.tramo(t, 0.46 + k * 0.08, 0.52 + k * 0.08) });
      UJ.rotulo(ctx, lz, '15', x0 + 14.5 * paso, yb + alto + 14, { tam: 22, peso: 800, color: R, visible: L.tramo(t, 0.74, 0.78) });
      UJ.rotulo(ctx, lz, 'Nadie decidió agregarlo y nada se quitó a cambio.', 40, 412, { tam: 19, alinear: 'left', ancho: 480, visible: L.tramo(t, 0.5, 0.7) });
      UJ.rotulo(ctx, lz, 'Mismo esfuerzo, el doble de superficie.', W / 2, 538,
                { tam: 23, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.82, 0.9) });
      UJ.rotulo(ctx, lz, 'Acción: las que sobran pasan a «alcance futuro» del informe, con su porqué.', W / 2, 584,
                { tam: 17, peso: 600, color: V, ancho: W - 40, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
