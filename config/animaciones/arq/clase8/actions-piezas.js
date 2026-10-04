/* GitHub Actions en cinco palabras: el workflow (un YAML en .github/workflows) se dispara con un
 * evento; corre jobs; cada job corre en un runner (maquina virtual limpia que se destruye al
 * terminar) y es una lista de steps. */
(function () {
  FP_ANIMADOR.registrar('actions-piezas', {
    duracion: 5,
    pasos: [0.28, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'chip', x: 140, y: 20, t: 'evento: on push', color: 'malva', en: 0 },
        { tipo: 'flecha', de: [140, 56], a: [140, 96], color: 'malva', en: 0.06 },
        { tipo: 'marco', x: 20, y: 100, w: 760, h: 440, t: 'workflow · .github/workflows/ci.yml', color: 'accion', en: 0.1 },
        { tipo: 'marco', x: 60, y: 160, w: 680, h: 330, t: 'runner · máquina virtual limpia (ubuntu-latest)', color: 'acento', en: 0.32 },
        { tipo: 'marco', x: 100, y: 220, w: 600, h: 240, t: 'job · construir-y-probar', color: 'accion', en: 0.4 },
        { tipo: 'caja', x: 140, y: 280, w: 520, h: 46, t: 'step · checkout', r: 8, tam: 19, en: 0.62 },
        { tipo: 'caja', x: 140, y: 334, w: 520, h: 46, t: 'step · npm ci y docker build', r: 8, tam: 19, en: 0.68 },
        { tipo: 'caja', x: 140, y: 388, w: 520, h: 46, t: 'step · npm test', r: 8, tam: 19, en: 0.74 },
        { tipo: 'texto', t: 'Al terminar, el runner se destruye: nada queda «de la vez anterior».', x: 400, y: 565, tam: 21, ancho: 760, en: 0.88 }
      ]);
    }
  });
})();
