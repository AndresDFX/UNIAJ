/* Ausencia de estado: si la sesion vive en la memoria de la instancia 1 y el balanceador manda la
 * siguiente peticion a la 2, el usuario es expulsado. La solucion es sacar el estado del proceso. */
(function () {
  FP_ANIMADOR.registrar('sesion-en-memoria', {
    duracion: 5,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'persona', x: 400, y: 10, tam: 56, t: 'usuario', color: 'accion', en: 0 },
        { tipo: 'caja', x: 300, y: 100, w: 200, h: 60, t: 'Balanceador', lleno: true, tam: 20, en: 0.02 },
        { tipo: 'caja', x: 80, y: 230, w: 240, h: 120, t: 'Instancia 1', s: 'sesión en memoria', color: 'acento', en: 0.04 },
        { tipo: 'caja', x: 480, y: 230, w: 240, h: 120, t: 'Instancia 2', s: 'no conoce la sesión', color: 'gris', en: 0.06 },
        { tipo: 'flecha', de: [360, 165], a: [210, 225], r: '1 · login', dx: -40, dy: -10, en: 0.1 },
        { tipo: 'flecha', de: [440, 165], a: [590, 225], r: '2 · ver mis turnos', dx: 110, dy: -30, ancho: 180, color: 'malva', en: 0.32 },
        { tipo: 'chip', x: 680, y: 362, t: '401 · sesión perdida', color: 'malva', en: 0.4 },
        { tipo: 'cilindro', x: 280, y: 440, w: 240, h: 120, t: 'Almacén de sesiones', s: 'fuera del proceso', color: 'accion', en: 0.62 },
        { tipo: 'flecha', de: [240, 352], a: [320, 445], en: 0.66 },
        { tipo: 'flecha', de: [560, 352], a: [480, 445], en: 0.68 },
        { tipo: 'texto', t: 'Cualquier instancia atiende a cualquier usuario.', x: 400, y: 590, tam: 22, peso: 800, color: 'accion', ancho: 760, en: 0.84 }
      ]);
    }
  });
})();
