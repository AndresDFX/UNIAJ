/* Las cinco piezas del autoescalado, con la politica de ejemplo: metrica CPU promedio, umbral 70 %,
 * sostenido 5 min, enfriamiento 5 min, minimo 2 y maximo 6. Y la reduccion asimetrica (30 %) para
 * no oscilar. */
(function () {
  FP_ANIMADOR.registrar('cinco-piezas-autoescalado', {
    duracion: 5,
    pasos: [0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var p = [['1 · Métrica', 'CPU promedio de la API'], ['2 · Umbral', '70 %'], ['3 · Periodo', 'sostenido 5 min'],
               ['4 · Enfriamiento', '5 min sin actuar'], ['5 · Rango', 'mínimo 2 · máximo 6']];
      var e = [];
      for (var i = 0; i < 5; i++) {
        e.push({ tipo: 'caja', x: 20, y: 20 + i * 86, w: 260, h: 72, t: p[i][0], lleno: true, r: 10, tam: 21, en: 0.03 + i * 0.1 });
        e.push({ tipo: 'caja', x: 290, y: 20 + i * 86, w: 490, h: 72, t: p[i][1], r: 10, tam: 22, en: 0.06 + i * 0.1 });
      }
      e.push({ tipo: 'texto', t: 'El máximo es el techo de costo: sin él, la factura escala sola.', x: 400, y: 460, tam: 21, ancho: 760, color: 'malva', en: 0.58 });
      e.push({ tipo: 'chip', x: 240, y: 520, t: 'sale al 70 %', color: 'accion', en: 0.82 });
      e.push({ tipo: 'chip', x: 560, y: 520, t: 'entra al 30 %, más despacio', color: 'acento', en: 0.86 });
      e.push({ tipo: 'texto', t: 'Umbrales asimétricos: si no, oscila (flapping).', x: 400, y: 590, tam: 20, ancho: 760, en: 0.9 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
