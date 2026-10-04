/* STRIDE: seis categorias, y cada una niega una propiedad deseable. De ahi sale la distincion
 * que mas se confunde: autenticacion (quien eres) y autorizacion (que puedes hacer). */
(function () {
  FP_ANIMADOR.registrar('stride', {
    duracion: 5,
    // Pasos LOGICOS: 1) las seis categorias completas (que hace el atacante en cada una),
    // 2) la propiedad que niega cada una, las seis a la vez, 3) la distincion que sale de ahi:
    // spoofing niega la autenticacion y elevation la autorizacion, que no son lo mismo.
    // Antes: tres filas enteras por paso y la cuarta a medias.
    pasos: [0.4, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      var f = [['S', 'Spoofing', 'suplantar a otro', 'autenticación'],
               ['T', 'Tampering', 'alterar datos', 'integridad'],
               ['R', 'Repudiation', 'negar una acción', 'no repudio'],
               ['I', 'Information disclosure', 'exponer datos', 'confidencialidad'],
               ['D', 'Denial of service', 'tumbar el servicio', 'disponibilidad'],
               ['E', 'Elevation of privilege', 'ganar permisos', 'autorización']];
      var e = [{ tipo: 'texto', t: 'propiedad que niega', x: 667, y: 6, tam: 18, color: 'malva', en: 0.42 }];
      for (var i = 0; i < 6; i++) {
        var y = 36 + i * 86;
        e.push({ tipo: 'caja', x: 20, y: y, w: 70, h: 72, t: f[i][0], lleno: true, tam: 34, r: 10, en: 0.02 + i * 0.05 });
        e.push({ tipo: 'caja', x: 100, y: y, w: 370, h: 72, t: f[i][1], s: f[i][2], r: 10, tam: 21, tamSub: 17, en: 0.03 + i * 0.05 });
        e.push({ tipo: 'flecha', de: [478, y + 36], a: [548, y + 36], color: 'malva', en: 0.44 + i * 0.05 });
        e.push({ tipo: 'caja', x: 555, y: y + 6, w: 225, h: 60, t: f[i][3], color: 'acento', r: 10, tam: 20, en: 0.46 + i * 0.05 });
      }
      // Paso 3: las dos que mas se confunden, resaltadas sobre su caja.
      e.push({ tipo: 'caja', x: 555, y: 42, w: 225, h: 60, t: 'autenticación', color: 'accion', lleno: true, r: 10, tam: 20, en: 0.86 });
      e.push({ tipo: 'caja', x: 555, y: 42 + 5 * 86, w: 225, h: 60, t: 'autorización', color: 'accion', lleno: true, r: 10, tam: 20, en: 0.86 });
      e.push({ tipo: 'texto', t: 'Autenticación: demostrar quién eres · Autorización: qué puedes hacer', x: 400, y: 560, tam: 20, peso: 700, color: 'accion', ancho: 760, en: 0.88 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
