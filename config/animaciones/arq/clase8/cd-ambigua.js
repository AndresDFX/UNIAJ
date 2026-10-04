/* La sigla CD es ambigua. Entrega continua: el artefacto queda listo y una persona decide salir a
 * produccion. Despliegue continuo: ese ultimo paso tambien es automatico. CI valida; CD entrega
 * o despliega. */
(function () {
  FP_ANIMADOR.registrar('cd-ambigua', {
    duracion: 5,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      function fila(y, en) {
        return [
          { tipo: 'caja', x: 20, y: y, w: 150, h: 80, t: 'construir', tam: 20, color: 'acento', en: en },
          { tipo: 'flecha', de: [173, y + 40], a: [197, y + 40], en: en + 0.02 },
          { tipo: 'caja', x: 200, y: y, w: 150, h: 80, t: 'probar', tam: 20, color: 'acento', en: en + 0.03 },
          { tipo: 'flecha', de: [353, y + 40], a: [377, y + 40], en: en + 0.05 },
          { tipo: 'caja', x: 380, y: y, w: 170, h: 80, t: 'listo para desplegar', tam: 18, en: en + 0.06 }
        ];
      }
      var e = [{ tipo: 'chip', x: 280, y: 20, t: 'CI = construir y probar cada cambio', color: 'acento', en: 0 }];
      e.push({ tipo: 'texto', t: 'Entrega continua', x: 20, y: 80, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0.32 });
      e = e.concat(fila(120, 0.34));
      e.push({ tipo: 'persona', x: 610, y: 115, tam: 50, t: 'decide', color: 'sello', en: 0.44 });
      e.push({ tipo: 'flecha', de: [645, 160], a: [690, 160], en: 0.46 });
      e.push({ tipo: 'caja', x: 695, y: 120, w: 95, h: 80, t: 'prod', tam: 20, color: 'malva', lleno: true, en: 0.48 });
      e.push({ tipo: 'texto', t: 'Despliegue continuo', x: 20, y: 280, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0.66 });
      e = e.concat(fila(320, 0.68));
      e.push({ tipo: 'flecha', de: [555, 360], a: [690, 360], r: 'automático', dy: -30, en: 0.76 });
      e.push({ tipo: 'caja', x: 695, y: 320, w: 95, h: 80, t: 'prod', tam: 20, color: 'malva', lleno: true, en: 0.78 });
      e.push({ tipo: 'texto', t: 'Comparten la sigla CD y no son lo mismo. En el curso: CI real y despliegue SIMULADO.', x: 400, y: 470, tam: 22, ancho: 740, en: 0.88 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
