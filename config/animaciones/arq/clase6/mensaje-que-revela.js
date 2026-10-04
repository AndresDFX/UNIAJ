/* PII y una de las tres amenazas de information disclosure: el mensaje de error que revela
 * informacion permite enumerar cuentas validas; el mensaje generico no dice nada. */
(function () {
  FP_ANIMADOR.registrar('mensaje-que-revela', {
    duracion: 5,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'PII: nombre, correo, teléfono, documento', x: 400, y: 14, tam: 22, peso: 700, color: 'accion', ancho: 760, en: 0 },
        { tipo: 'caja', x: 30, y: 80, w: 340, h: 70, t: 'ana@correo.com  ·  ••••', color: 'gris', r: 8, tam: 20, en: 0.06 },
        { tipo: 'caja', x: 30, y: 160, w: 340, h: 70, t: 'zzz@correo.com  ·  ••••', color: 'gris', r: 8, tam: 20, en: 0.1 },
        { tipo: 'caja', x: 430, y: 80, w: 340, h: 70, t: '«contraseña incorrecta»', color: 'malva', r: 8, tam: 20, en: 0.16 },
        { tipo: 'caja', x: 430, y: 160, w: 340, h: 70, t: '«ese correo no existe»', color: 'malva', r: 8, tam: 20, en: 0.2 },
        { tipo: 'flecha', de: [372, 115], a: [426, 115], color: 'malva', en: 0.16 },
        { tipo: 'flecha', de: [372, 195], a: [426, 195], color: 'malva', en: 0.2 },
        { tipo: 'chip', x: 400, y: 255, t: 'ya sé que ana@correo.com tiene cuenta', color: 'malva', en: 0.3 },
        { tipo: 'caja', x: 30, y: 350, w: 340, h: 70, t: 'ana@correo.com  ·  ••••', color: 'gris', r: 8, tam: 20, en: 0.44 },
        { tipo: 'caja', x: 30, y: 430, w: 340, h: 70, t: 'zzz@correo.com  ·  ••••', color: 'gris', r: 8, tam: 20, en: 0.46 },
        { tipo: 'caja', x: 430, y: 350, w: 340, h: 70, t: '«credenciales inválidas»', color: 'accion', r: 8, tam: 20, en: 0.52 },
        { tipo: 'caja', x: 430, y: 430, w: 340, h: 70, t: '«credenciales inválidas»', color: 'accion', r: 8, tam: 20, en: 0.54 },
        { tipo: 'flecha', de: [372, 385], a: [426, 385], en: 0.52 },
        { tipo: 'flecha', de: [372, 465], a: [426, 465], en: 0.54 },
        { tipo: 'chip', x: 400, y: 525, t: 'no dice cuál cuenta existe', color: 'accion', en: 0.62 },
        { tipo: 'texto', t: 'Y las contraseñas no se guardan: se guarda su hash.', x: 400, y: 592, tam: 21, ancho: 760, en: 0.84 }
      ]);
    }
  });
})();
