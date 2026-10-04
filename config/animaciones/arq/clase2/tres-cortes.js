/* IaaS, PaaS y SaaS: la misma pila en tres columnas; la linea del proveedor sube. Debajo de la
 * linea administra el proveedor; encima, el cliente. Aun en SaaS, los datos y los usuarios
 * (quien entra y con que permiso) siguen siendo del cliente. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('tres-cortes', {
    duracion: 5,
    pasos: [0.3, 0.6, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, capas = ['Infraestructura', 'Virtualización', 'Sistema operativo', 'Runtime', 'Aplicación', 'Datos y usuarios'];
      var modelos = [['IaaS', 2, 0.05], ['PaaS', 4, 0.32], ['SaaS', 5, 0.62]];
      for (var k = 0; k < 3; k++) {
        var x = 30 + k * 260, a = L.tramo(t, modelos[k][2], modelos[k][2] + 0.1), corte = modelos[k][1];
        if (a <= 0) continue;
        UJ.alfa(ctx, a, function () {
          UJ.rotulo(ctx, lz, modelos[k][0], x + 115, 20, { tam: 30, peso: 800, color: m.accion });
          for (var i = 0; i < capas.length; i++) {
            var y = 480 - i * 70, prov = i < corte;
            var c = prov ? m.acento : m.sello;
            L.rectRed(ctx, x, y, 230, 60, 10); L.rellena(ctx, L.tono(c, prov ? 0.55 : 0.35), c, 2);
            UJ.rotulo(ctx, lz, capas[i], x + 115, y + 17, { tam: 19, peso: 700, color: m.tinta, ancho: 220 });
          }
          var yl = 480 - corte * 70 + 65;
          ctx.setLineDash([10, 6]); L.trazo(ctx, [[x - 8, yl], [x + 238, yl]], L.tramo(t, modelos[k][2] + 0.06, modelos[k][2] + 0.16), m.malva || '#A02030', 4); ctx.setLineDash([]);
        });
      }
      UJ.escena(ctx, t, lz, [
        { tipo: 'chip', x: 220, y: 575, t: 'administra el proveedor', color: 'acento', tinta: true, en: 0.88 },
        { tipo: 'chip', x: 560, y: 575, t: 'administra usted', color: 'sello', tinta: true, en: 0.9 }
      ]);
    }
  });
})();
