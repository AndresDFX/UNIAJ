/* El semaforo con seis artefactos esperados: verde, amarillo y rojo, cada uno con su umbral. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('semaforo', {
    duracion: 5,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, luces = [[m.verde || m.accion, 0.04], [m.sello || '#FFD000', 0.36], [m.malva || '#A02030', 0.68]];
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () {
        L.rectRed(ctx, 40, 30, 140, 470, 30); L.rellena(ctx, L.tono(m.tinta, 0.15));
      });
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, luces[i][1], luces[i][1] + 0.08);
        L.circulo(ctx, 110, 110 + i * 150, 55); L.rellena(ctx, a > 0 ? L.mezclaColor(L.tono(m.tinta, 0.4), luces[i][0], a) : L.tono(m.tinta, 0.4));
      }
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 220, y: 50, w: 560, h: 120, t: 'Verde', s: 'los seis artefactos y a lo sumo una cadena rota', color: 'verde', tam: 24, en: 0.06 },
        { tipo: 'caja', x: 220, y: 200, w: 560, h: 120, t: 'Amarillo', s: 'cinco de seis, o dos o tres cadenas rotas que se corrigen editando documentos', color: 'sello', tam: 24, en: 0.38 },
        { tipo: 'caja', x: 220, y: 350, w: 560, h: 120, t: 'Rojo', s: 'falta el C4 de Contenedores o el Despliegue, o no hay repositorio', color: 'malva', tam: 24, en: 0.7 },
        { tipo: 'texto', t: 'El umbral decide si el proyecto va a tiempo.', x: 400, y: 540, tam: 23, peso: 800, color: 'accion', ancho: 760, en: 0.88 }
      ]);
    }
  });
})();
