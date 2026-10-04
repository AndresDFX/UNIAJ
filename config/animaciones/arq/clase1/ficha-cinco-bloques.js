/* La ficha de dominio: cinco bloques rotulados, en el orden en que se llenan. Primero el
 * problema, despues quien usa el sistema y que hace, y al final el limite de lo que NO hace. */
(function () {
  FP_ANIMADOR.registrar('ficha-cinco-bloques', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 30, y: 30, w: 360, h: 140, t: '1 · DOMINIO', s: 'el problema de negocio, en una línea', tam: 24, tamSub: 19, en: 0.02 },
        { tipo: 'caja', x: 410, y: 30, w: 360, h: 140, t: '2 · PROBLEMA', s: 'quién sufre, cómo se resuelve hoy y una cifra', tam: 24, tamSub: 19, en: 0.14 },
        { tipo: 'caja', x: 30, y: 195, w: 360, h: 165, t: '3 · ACTORES', s: 'quién lo usa y qué espera · y los 2 o 3 sistemas externos', color: 'acento', tam: 24, tamSub: 19, en: 0.34 },
        { tipo: 'caja', x: 410, y: 195, w: 360, h: 165, t: '4 · CAPACIDADES', s: 'verbos de negocio: reservar, cancelar… nunca «login» ni «caché»', color: 'acento', tam: 24, tamSub: 19, en: 0.48 },
        { tipo: 'caja', x: 30, y: 385, w: 740, h: 120, t: '5 · FUERA DE ALCANCE', s: 'tres cosas que el sistema NO hará este semestre', color: 'malva', tam: 24, tamSub: 19, en: 0.7 },
        { tipo: 'texto', t: 'Los sistemas externos de la ficha son los System_Ext del diagrama.', x: 400, y: 545, tam: 22, ancho: 740, en: 0.86 }
      ]);
    }
  });
})();
