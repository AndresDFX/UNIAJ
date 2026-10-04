/* Sin factura real, se estima con una escala ordinal de tres niveles, componente por componente:
 * ordena (uno cuesta mas que otro) pero no mide distancias. Lo que importa es el driver de cada uno. */
(function () {
  FP_ANIMADOR.registrar('escala-ordinal', {
    duracion: 5,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var f = [['Base de datos', 'Alto', 'malva', 'encendida todo el mes'],
               ['API', 'Medio', 'sello', 'horas de instancia encendida'],
               ['Frontend estático', 'Bajo', 'accion', 'almacenamiento y tráfico'],
               ['Notificaciones', 'Bajo', 'accion', 'función serverless, poco volumen']];
      var e = [
        { tipo: 'caja', x: 20, y: 20, w: 270, h: 56, t: 'Componente', lleno: true, r: 8, tam: 20, en: 0 },
        { tipo: 'caja', x: 300, y: 20, w: 160, h: 56, t: 'Nivel', lleno: true, r: 8, tam: 20, en: 0.02 },
        { tipo: 'caja', x: 470, y: 20, w: 310, h: 56, t: 'Driver de costo', lleno: true, color: 'acento', r: 8, tam: 20, en: 0.04 }
      ];
      for (var i = 0; i < 4; i++) {
        var y = 90 + i * 84;
        e.push({ tipo: 'caja', x: 20, y: y, w: 270, h: 70, t: f[i][0], r: 8, tam: 20, en: 0.08 + i * 0.07 });
        e.push({ tipo: 'chip', x: 380, y: y + 18, t: f[i][1], w: 120, color: f[i][2], tinta: f[i][2] === 'sello', en: 0.1 + i * 0.07 });
        e.push({ tipo: 'caja', x: 470, y: y, w: 310, h: 70, t: f[i][3], color: 'acento', r: 8, tam: 19, en: 0.44 + i * 0.07 });
      }
      e.push({ tipo: 'texto', t: 'Ordena, pero no mide distancias: «Alto» no dice cuánto más.', x: 400, y: 450, tam: 22, ancho: 740, en: 0.8 });
      e.push({ tipo: 'texto', t: 'Alcanza para lo que importa: el driver de cada componente.', x: 400, y: 530, tam: 22, peso: 800, color: 'accion', ancho: 740, en: 0.9 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
