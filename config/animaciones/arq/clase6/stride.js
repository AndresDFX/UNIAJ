/* STRIDE: seis categorias, y cada una niega una propiedad deseable. */
(function () {
  FP_ANIMADOR.registrar('stride', {
    duracion: 5,
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var f = [['S', 'Spoofing', 'suplantar a otro', 'autenticación'],
               ['T', 'Tampering', 'alterar datos', 'integridad'],
               ['R', 'Repudiation', 'negar una acción', 'no repudio'],
               ['I', 'Information disclosure', 'exponer datos', 'confidencialidad'],
               ['D', 'Denial of service', 'tumbar el servicio', 'disponibilidad'],
               ['E', 'Elevation of privilege', 'ganar permisos', 'autorización']];
      var e = [{ tipo: 'texto', t: 'niega →', x: 560, y: 4, tam: 20, color: 'malva', en: 0.1 }];
      for (var i = 0; i < 6; i++) {
        var y = 40 + i * 92, en = 0.04 + i * 0.12;
        e.push({ tipo: 'caja', x: 20, y: y, w: 70, h: 76, t: f[i][0], lleno: true, tam: 34, r: 10, en: en });
        e.push({ tipo: 'caja', x: 100, y: y, w: 370, h: 76, t: f[i][1], s: f[i][2], r: 10, tam: 21, tamSub: 17, en: en + 0.02 });
        e.push({ tipo: 'flecha', de: [478, y + 38], a: [548, y + 38], color: 'malva', en: en + 0.04 });
        e.push({ tipo: 'caja', x: 555, y: y + 8, w: 225, h: 60, t: f[i][3], color: 'acento', r: 10, tam: 20, en: en + 0.06 });
      }
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
