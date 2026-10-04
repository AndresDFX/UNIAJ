/* Modelar amenazas es responder cuatro preguntas en orden. El vocabulario: activo (lo que vale
 * proteger) y amenaza (el evento indeseado). */
(function () {
  FP_ANIMADOR.registrar('cuatro-preguntas', {
    duracion: 5,
    pasos: [0.5, 1],
    dibujar: function (ctx, t, lz) {
      var q = ['¿Qué estamos construyendo?', '¿Qué puede salir mal?', '¿Qué hacemos al respecto?', '¿Lo hicimos bien?'];
      var e = [];
      for (var i = 0; i < 4; i++) {
        e.push({ tipo: 'caja', x: 40, y: 20 + i * 92, w: 450, h: 76, t: (i + 1) + ' · ' + q[i], color: i === 1 ? 'malva' : 'accion', r: 10, tam: 22, en: 0.03 + i * 0.1 });
        if (i < 3) e.push({ tipo: 'flecha', de: [265, 98 + i * 92], a: [265, 110 + i * 92], en: 0.08 + i * 0.1 });
      }
      e.push({ tipo: 'caja', x: 520, y: 40, w: 250, h: 130, t: 'Activo', s: 'lo que vale proteger: datos personales, token, disponibilidad', color: 'acento', tamSub: 17, en: 0.55 });
      e.push({ tipo: 'caja', x: 520, y: 200, w: 250, h: 130, t: 'Amenaza', s: 'el evento indeseado: un tercero lee la tabla de usuarios', color: 'malva', tamSub: 17, en: 0.68 });
      e.push({ tipo: 'texto', t: 'Primero se nombra lo que se protege; después, lo que puede pasarle.', x: 400, y: 440, tam: 22, ancho: 740, en: 0.86 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
