/* La politica de secretos en el pipeline: el valor vive en el almacen del repositorio y llega como
 * variable de entorno; el registro lo enmascara, pero enmascarar no impide la fuga. Y las corridas
 * de un pull_request desde un fork no reciben secretos. */
(function () {
  FP_ANIMADOR.registrar('secretos-enmascarados', {
    duracion: 5,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'cilindro', x: 20, y: 30, w: 200, h: 130, t: 'Secretos del repo', s: 'DEPLOY_TOKEN', color: 'accion', en: 0 },
        { tipo: 'flecha', de: [225, 95], a: [325, 95], r: 'variable de entorno', dy: 15, ancho: 95, en: 0.08 },
        { tipo: 'caja', x: 330, y: 40, w: 200, h: 110, t: 'Paso del job', s: 'env: TOKEN', color: 'acento', en: 0.12 },
        { tipo: 'flecha', de: [535, 95], a: [585, 95], en: 0.18 },
        { tipo: 'caja', x: 590, y: 40, w: 190, h: 110, t: 'Registro', s: 'TOKEN = ***', color: 'gris', en: 0.22 },
        { tipo: 'texto', t: 'Enmascarar no es impedir la fuga: un paso puede enviarlo a otro lado.', x: 400, y: 200, tam: 21, ancho: 740, color: 'malva', en: 0.38 },
        { tipo: 'texto', t: 'Para verificar que llegó: su longitud, nunca su valor.', x: 400, y: 260, tam: 21, ancho: 740, en: 0.48 },
        { tipo: 'caja', x: 40, y: 360, w: 280, h: 110, t: 'pull_request', s: 'desde un fork', color: 'gris', en: 0.68 },
        { tipo: 'flecha', de: [325, 415], a: [475, 415], r: 'sin secretos', dy: -32, color: 'malva', en: 0.72 },
        { tipo: 'caja', x: 480, y: 360, w: 280, h: 110, t: 'Paso del job', s: 'TOKEN vacío', color: 'malva', en: 0.76 },
        { tipo: 'texto', t: 'Validar un cambio externo no puede depender de credenciales.', x: 400, y: 530, tam: 22, ancho: 740, peso: 700, color: 'accion', en: 0.88 }
      ]);
    }
  });
})();
