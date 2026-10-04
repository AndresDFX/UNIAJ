/* Una observacion accionable tiene cuatro partes: observacion, evidencia, impacto y accion con
 * fecha. «Mejorar el diagrama» no tiene ninguna. */
(function () {
  FP_ANIMADOR.registrar('retro-cuatro-partes', {
    duracion: 5,
    pasos: [0.2, 0.42, 0.64, 0.86, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 200, y: 10, w: 400, h: 70, t: '«Mejorar el diagrama»', color: 'gris', tam: 22, en: 0, sale: 0.2 },
        { tipo: 'tacha', x: 200, y: 10, w: 400, h: 70, en: 0.08, sale: 0.2 },
        { tipo: 'caja', x: 20, y: 100, w: 760, h: 95, t: '1 · Observación', s: 'el Despliegue llama «backend» a la API de turnos', en: 0.22 },
        { tipo: 'caja', x: 20, y: 205, w: 760, h: 95, t: '2 · Evidencia', s: 'el Containers dice «API de turnos»; el Despliegue, «backend»', color: 'acento', en: 0.44 },
        { tipo: 'caja', x: 20, y: 310, w: 760, h: 95, t: '3 · Impacto', s: 'en la sustentación parecen dos piezas distintas', color: 'malva', en: 0.66 },
        { tipo: 'caja', x: 20, y: 415, w: 760, h: 95, t: '4 · Acción con fecha', s: 'unificar el nombre antes de la próxima clase', color: 'accion', lleno: true, en: 0.88 },
        { tipo: 'texto', t: 'Tres hallazgos por proyecto como máximo, y cuál bloquea.', x: 400, y: 545, tam: 21, ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
