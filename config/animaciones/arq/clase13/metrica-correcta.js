/* Elegir la metrica: la CPU es la equivocada para una API que espera a la base. Con el pool agotado,
 * la latencia sube a 3 s y la CPU sigue en 20 %: el umbral de 70 % nunca se cruza. Para el worker, la
 * metrica natural es la longitud de la cola. */
(function () {
  FP_ANIMADOR.registrar('metrica-correcta', {
    duracion: 5,
    pasos: [0.45, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'API con el pool de conexiones agotado', x: 30, y: 14, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0 },
        { tipo: 'barra', x: 230, y: 70, w: 500, h: 36, valor: 0.2, t: 'CPU', r: '20 %', color: 'accion', en: 0.04, tam: 20 },
        { tipo: 'linea', pts: [[230 + 500 * 0.7, 55], [230 + 500 * 0.7, 120]], color: 'malva', grosor: 3, punteada: true, en: 0.1 },
        { tipo: 'texto', t: 'umbral 70 %: nunca se cruza', x: 580, y: 125, tam: 18, color: 'malva', ancho: 260, en: 0.14 },
        { tipo: 'barra', x: 230, y: 175, w: 500, h: 36, valor: 1, t: 'latencia p95', color: 'malva', en: 0.22, tam: 20 },
        { tipo: 'texto', t: '3 s', x: 742, y: 180, tam: 20, peso: 800, alinear: 'left', color: 'malva', en: 0.3 },
        { tipo: 'chip', x: 400, y: 240, t: 'el autoescalado no hace nada mientras los usuarios esperan', color: 'malva', en: 0.34 },
        { tipo: 'caja', x: 30, y: 320, w: 360, h: 110, t: 'API', s: 'latencia p95 o peticiones por segundo por instancia', en: 0.5 },
        { tipo: 'caja', x: 410, y: 320, w: 360, h: 110, t: 'Worker de avisos', s: 'mensajes esperando en la cola', color: 'acento', en: 0.6 },
        { tipo: 'texto', t: 'La métrica correcta mide el recurso que se agota primero: el cuello de botella.', x: 400, y: 480, tam: 22, ancho: 740, peso: 700, color: 'accion', en: 0.8 }
      ]);
    }
  });
})();
