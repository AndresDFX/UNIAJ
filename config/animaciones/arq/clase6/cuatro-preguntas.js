/* Modelar amenazas es responder cuatro preguntas en orden. El vocabulario: activo (lo que vale
 * proteger) y amenaza (el evento indeseado). */
(function () {
  FP_ANIMADOR.registrar('cuatro-preguntas', {
    duracion: 5,
    // Pasos LOGICOS: 1) las cuatro preguntas, en orden, 2) el vocabulario: activo y amenaza,
    // 3) la regla de orden: primero lo que se protege, despues lo que puede pasarle.
    pasos: [0.46, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var q = ['¿Qué estamos construyendo?', '¿Qué puede salir mal?', '¿Qué hacemos al respecto?', '¿Lo hicimos bien?'];
      var e = [];
      for (var i = 0; i < 4; i++) {
        e.push({ tipo: 'caja', x: 30, y: 30 + i * 100, w: 460, h: 76, t: (i + 1) + ' · ' + q[i], color: i === 1 ? 'malva' : 'accion', r: 10, tam: 22, en: 0.02 + i * 0.1 });
        if (i < 3) e.push({ tipo: 'flecha', de: [260, 108 + i * 100], a: [260, 128 + i * 100], en: 0.08 + i * 0.1 });
      }
      e.push({ tipo: 'caja', x: 520, y: 40, w: 255, h: 150, t: 'Activo', s: 'lo que vale proteger: datos personales, token, disponibilidad', color: 'acento', tamSub: 17, en: 0.5 });
      e.push({ tipo: 'caja', x: 520, y: 220, w: 255, h: 150, t: 'Amenaza', s: 'el evento indeseado: un tercero lee la tabla de usuarios', color: 'malva', tamSub: 17, en: 0.6 });
      e.push({ tipo: 'texto', t: 'Primero se nombra lo que se protege; después, lo que puede pasarle.', x: 400, y: 470, tam: 22, ancho: 740, en: 0.84 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
