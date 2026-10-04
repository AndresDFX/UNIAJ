/* Dos patologias con nombre propio. Scope creep: se cuenta contra la linea base de la Clase 1 y se
 * responde con una lista de aparcamiento. Teatro de microservicios: cajas separadas en el diagrama
 * que en el repositorio son un modulo de la misma API. */
(function () {
  FP_ANIMADOR.registrar('dos-patologias', {
    duracion: 5,
    pasos: [0.45, 1],
    dibujar: function (ctx, t, lz) {
      var e = [{ tipo: 'texto', t: 'Scope creep', x: 30, y: 14, tam: 24, peso: 800, alinear: 'left', color: 'malva', en: 0 }];
      for (var i = 0; i < 9; i++) {
        e.push({ tipo: 'caja', x: 30 + i * 52, y: 70, w: 44, h: 44, t: '', color: i < 4 ? 'accion' : 'malva', lleno: true, r: 8, en: 0.04 + i * 0.025 });
      }
      e.push({ tipo: 'texto', t: 'Clase 1: 4 capacidades · hoy: 9', x: 30, y: 130, tam: 20, alinear: 'left', en: 0.28 });
      e.push({ tipo: 'caja', x: 520, y: 50, w: 260, h: 110, t: 'Lista de aparcamiento', s: 'candidatas a v2', color: 'acento', tam: 20, en: 0.36 });
      e.push({ tipo: 'texto', t: 'Teatro de microservicios', x: 30, y: 240, tam: 24, peso: 800, alinear: 'left', color: 'malva', en: 0.48 });
      e.push({ tipo: 'caja', x: 30, y: 290, w: 220, h: 90, t: 'Servicio de autenticación', tam: 19, en: 0.52 });
      e.push({ tipo: 'caja', x: 280, y: 290, w: 220, h: 90, t: 'API de turnos', tam: 19, en: 0.55 });
      e.push({ tipo: 'texto', t: 'en el diagrama', x: 265, y: 395, tam: 18, color: 'gris', en: 0.56 });
      e.push({ tipo: 'marco', x: 540, y: 270, w: 240, h: 150, t: 'en el repositorio', color: 'malva', en: 0.62 });
      e.push({ tipo: 'caja', x: 560, y: 320, w: 200, h: 80, t: 'módulo auth', s: 'dentro de la misma API', color: 'malva', tam: 19, tamSub: 15, en: 0.66 });
      e.push({ tipo: 'texto', t: '¿Se despliega solo? ¿Tiene sus datos? ¿Falla sin tumbar a los demás? ¿Cambia a su propio ritmo?', x: 400, y: 470, tam: 20, ancho: 740, en: 0.78 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
