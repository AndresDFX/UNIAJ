/* Las cuatro senales de oro, cada una con su definicion operativa. Saturacion: que tan cerca esta
 * el recurso mas escaso de su limite; se suele alertar sobre el 70 u 80 % sostenido (convencion). */
(function () {
  FP_ANIMADOR.registrar('cuatro-senales', {
    duracion: 5,
    pasos: [0.25, 0.5, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 20, w: 370, h: 150, t: 'Latencia', s: 'cuánto tarda una petición · p95 en ms', en: 0.02 },
        { tipo: 'caja', x: 410, y: 20, w: 370, h: 150, t: 'Tráfico', s: 'cuánta demanda llega · peticiones por segundo', color: 'acento', en: 0.26 },
        { tipo: 'caja', x: 20, y: 190, w: 370, h: 150, t: 'Errores', s: 'qué fracción falla · % de respuestas 5xx', color: 'malva', en: 0.51 },
        { tipo: 'caja', x: 410, y: 190, w: 370, h: 150, t: 'Saturación', s: 'qué tan cerca del límite está el recurso más escaso', color: 'gris', en: 0.76 },
        { tipo: 'barra', x: 250, y: 400, w: 440, h: 36, valor: 0.78, t: 'CPU de la API', r: '78 %', color: 'malva', en: 0.8 },
        { tipo: 'linea', pts: [[250 + 440 * 0.7, 385], [250 + 440 * 0.7, 450]], color: 'tinta', grosor: 3, punteada: true, en: 0.84 },
        { tipo: 'texto', t: 'alerta sobre 70-80 % sostenido (convención, no ley)', x: 400, y: 475, tam: 20, ancho: 740, en: 0.88 }
      ]);
    }
  });
})();
