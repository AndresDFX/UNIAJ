/* Ordenes de magnitud de costo (referencia, no tarifa): lo que cobra por existir (instancia,
 * balanceador) contra lo que cobra por uso (objetos, trafico de salida). */
(function () {
  FP_ANIMADOR.registrar('ordenes-magnitud', {
    duracion: 5,
    pasos: [0.45, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Cobra por existir · al mes', x: 30, y: 14, tam: 23, peso: 800, alinear: 'left', color: 'malva', en: 0 },
        { tipo: 'barra', x: 290, y: 70, w: 400, h: 40, valor: 0.9, t: 'Instancia 2 vCPU · 4 GB', r: 'US$ 25-40', color: 'malva', en: 0.06, tam: 19 },
        { tipo: 'barra', x: 290, y: 130, w: 400, h: 40, valor: 0.55, t: 'Balanceador', r: 'US$ 18-25', color: 'malva', en: 0.14, tam: 19 },
        { tipo: 'texto', t: 'aunque haya cero tráfico', x: 400, y: 190, tam: 20, color: 'malva', en: 0.24 },
        { tipo: 'texto', t: 'Cobra por uso · por GB', x: 30, y: 270, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0.48 },
        { tipo: 'barra', x: 290, y: 330, w: 400, h: 40, valor: 0.025, t: 'Objetos (al mes)', r: 'US$ 0.02-0.03', color: 'accion', en: 0.54, tam: 19 },
        { tipo: 'barra', x: 290, y: 390, w: 400, h: 40, valor: 0.1, t: 'Tráfico de salida', r: 'US$ 0.08-0.12', color: 'accion', en: 0.62, tam: 19 },
        { tipo: 'texto', t: 'Guardar es casi gratis; lo que sale hacia internet, no.', x: 400, y: 470, tam: 22, ancho: 740, en: 0.8 },
        { tipo: 'texto', t: 'Órdenes de magnitud, no la tarifa de un proveedor.', x: 400, y: 545, tam: 20, ancho: 740, color: 'gris', en: 0.9 }
      ]);
    }
  });
})();
