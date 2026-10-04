/* Los controles gratuitos en tres familias, y por que se valida en el servidor: el cliente esta
 * bajo control del atacante, que llama la API con curl y se salta el formulario. */
(function () {
  FP_ANIMADOR.registrar('validar-en-servidor', {
    duracion: 5,
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 20, w: 240, h: 120, t: 'Identidad', s: 'token y rol con mínimo privilegio', tamSub: 17, en: 0.02 },
        { tipo: 'caja', x: 280, y: 20, w: 240, h: 120, t: 'Red', s: 'solo el punto de entrada es público', color: 'acento', tamSub: 17, en: 0.08 },
        { tipo: 'caja', x: 540, y: 20, w: 240, h: 120, t: 'Aplicación', s: 'validar entradas y limitar la tasa', color: 'malva', tamSub: 17, en: 0.14 },
        { tipo: 'persona', x: 90, y: 210, tam: 64, t: 'Usuario', color: 'accion', en: 0.32 },
        { tipo: 'caja', x: 200, y: 215, w: 220, h: 80, t: 'Formulario', s: 'valida en el navegador', tam: 20, tamSub: 15, color: 'gris', en: 0.36 },
        { tipo: 'flecha', de: [425, 255], a: [565, 300], en: 0.4 },
        { tipo: 'caja', x: 570, y: 260, w: 210, h: 130, t: 'API', s: 'valida OTRA vez', lleno: true, tam: 24, en: 0.44 },
        { tipo: 'persona', x: 90, y: 400, tam: 64, t: 'Atacante', color: 'malva', en: 0.56 },
        { tipo: 'caja', x: 200, y: 410, w: 220, h: 70, t: 'curl', color: 'malva', tam: 22, en: 0.6 },
        { tipo: 'flecha', de: [425, 445], a: [565, 360], r: 'se salta el formulario', dx: 75, dy: 45, ancho: 200, color: 'malva', en: 0.64 },
        { tipo: 'texto', t: 'La validación del navegador es comodidad; la del servidor, seguridad.', x: 400, y: 560, tam: 21, ancho: 760, en: 0.86 }
      ]);
    }
  });
})();
