/* El ensayo del pitch: 5 a 8 minutos son 700 a 1000 palabras, siete u ocho ideas. El guion se
 * escribe por presupuesto de tiempo, y se presentan decisiones con su trade-off. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pitch-presupuesto', {
    duracion: 5,
    pasos: [0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca;
      var b = [['Problema', 45, 'gris'], ['Context', 60, 'accion'], ['Containers y decisiones', 90, 'accion'], ['Seguridad y despliegue', 60, 'acento'],
               ['Pipeline y métricas', 45, 'acento'], ['Costos y escala', 45, 'malva'], ['Cierre', 30, 'gris']];
      var e = [{ tipo: 'texto', t: 'Presupuesto de tiempo, en segundos', x: 400, y: 14, tam: 23, peso: 800, color: 'accion', en: 0 }];
      for (var i = 0; i < b.length; i++) {
        e.push({ tipo: 'barra', x: 300, y: 70 + i * 56, w: 420, h: 34, valor: b[i][1] / 90, t: b[i][0], r: b[i][1] + ' s', color: b[i][2], en: 0.04 + i * 0.07, tam: 19 });
      }
      e.push({ tipo: 'texto', t: 'Total ≈ 6 min 15 s, dentro de 5 a 8', x: 400, y: 470, tam: 21, ancho: 740, en: 0.56 });
      e.push({ tipo: 'texto', t: '«Elegimos base gestionada aunque cuesta el doble, porque no podemos garantizar respaldos manuales.»', x: 400, y: 520, tam: 20, ancho: 740, color: 'accion', en: 0.66 });
      e.push({ tipo: 'texto', t: 'Decisión + trade-off, no un recorrido por las cajas.', x: 400, y: 595, tam: 21, peso: 800, color: 'malva', ancho: 740, en: 0.82 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
