/* De gasto de capital a gasto operativo medido: en un centro de datos propio se compra por
 * adelantado; en la nube se paga por segundo de computo, y cada decision de diseno mueve la factura. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('capex-opex', {
    duracion: 5,
    pasos: [0.4, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, e = [
        { tipo: 'texto', t: 'Centro de datos propio · gasto de capital', x: 30, y: 14, tam: 23, peso: 800, alinear: 'left', color: 'malva', en: 0 },
        { tipo: 'linea', pts: [[40, 250], [760, 250]], color: 'gris', grosor: 2, en: 0 },
        { tipo: 'texto', t: 'se compra todo el primer día', x: 220, y: 70, tam: 20, alinear: 'left', ancho: 300, en: 0.2 },
        { tipo: 'texto', t: 'Nube · gasto operativo medido', x: 30, y: 320, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0.42 },
        { tipo: 'linea', pts: [[40, 560], [760, 560]], color: 'gris', grosor: 2, en: 0.42 },
        { tipo: 'texto', t: 'se paga lo que se usa, por segundo', x: 400, y: 370, tam: 20, ancho: 400, en: 0.7 },
        { tipo: 'texto', t: 'El cambio no es contable: es de arquitectura.', x: 400, y: 590, tam: 22, peso: 800, color: 'accion', ancho: 760, en: 0.9 }
      ];
      UJ.escena(ctx, t, lz, e);
      // Una barra alta al inicio contra muchas barras pequenas que siguen a la demanda.
      var a = L.tramo(t, 0.06, 0.2, 'frena');
      if (a > 0) { L.rectRed(ctx, 60, 250 - 170 * a, 120, 170 * a, 4); L.rellena(ctx, L.tono(m.malva || '#A02030', 0.2)); }
      var dem = [0.2, 0.25, 0.3, 0.5, 0.9, 0.7, 0.4, 0.3, 0.35, 0.6, 0.95, 0.8, 0.45, 0.3, 0.25, 0.2, 0.3, 0.5];
      for (var i = 0; i < dem.length; i++) {
        var b = L.tramo(t, 0.46 + i * 0.012, 0.52 + i * 0.012, 'frena');
        if (b <= 0) continue;
        var h = 140 * dem[i] * b;
        L.rectRed(ctx, 60 + i * 38, 560 - h, 28, h, 3); L.rellena(ctx, L.tono(m.accion, 0.15));
      }
    }
  });
})();
