/* Integracion continua, definida operativamente: cada cambio que se sube se construye y se prueba
 * solo, y el resultado vuelve en minutos. El valor esta en ese intervalo corto, no en el robot. */
(function () {
  FP_ANIMADOR.registrar('ci-ciclo', {
    duracion: 5,
    // Pasos LOGICOS: 1) el problema (cada quien en su rama, todo choca al integrar), 2) cada push
    // se construye y se prueba solo y sale verde o rojo, 3) ese resultado vuelve en minutos: el
    // valor es el intervalo. El paso 2 cierra cuando ya se ven los dos sellos completos.
    pasos: [0.3, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: '«En mi máquina funciona»', x: 400, y: 20, tam: 26, peso: 800, color: 'malva', en: 0, sale: 0.3 },
        { tipo: 'caja', x: 40, y: 80, w: 200, h: 100, t: 'Ana', s: 'su rama, 3 semanas', color: 'gris', en: 0.04, sale: 0.3 },
        { tipo: 'caja', x: 300, y: 80, w: 200, h: 100, t: 'Luis', s: 'su rama, 3 semanas', color: 'gris', en: 0.08, sale: 0.3 },
        { tipo: 'caja', x: 560, y: 80, w: 200, h: 100, t: 'Integrar', s: 'todo choca el último día', color: 'malva', en: 0.16, sale: 0.3 },
        { tipo: 'caja', x: 30, y: 230, w: 160, h: 100, t: 'push', s: 'cada cambio', en: 0.36 },
        { tipo: 'flecha', de: [195, 280], a: [235, 280], en: 0.4 },
        { tipo: 'caja', x: 240, y: 230, w: 160, h: 100, t: 'construir', s: 'automático', color: 'acento', en: 0.44 },
        { tipo: 'flecha', de: [405, 280], a: [445, 280], en: 0.48 },
        { tipo: 'caja', x: 450, y: 230, w: 160, h: 100, t: 'probar', s: 'automático', color: 'acento', en: 0.52 },
        { tipo: 'flecha', de: [615, 280], a: [655, 280], en: 0.56 },
        { tipo: 'sello', x: 700, y: 250, r: 26, ok: true, en: 0.6 },
        { tipo: 'sello', x: 700, y: 315, r: 26, ok: false, en: 0.62 },
        { tipo: 'linea', pts: [[700, 350], [700, 420], [110, 420], [110, 335]], color: 'accion', en: 0.74 },
        { tipo: 'chip', x: 400, y: 400, t: 'resultado en minutos', color: 'accion', en: 0.8 },
        { tipo: 'texto', t: 'El valor no es la automatización: es el intervalo de retroalimentación.', x: 400, y: 500, tam: 23, peso: 700, ancho: 740, en: 0.9 }
      ]);
    }
  });
})();
