/* Un contrato son cuatro datos por flecha: la interaccion de negocio, quien llama a quien, con
 * que verbo y ruta, y el error de negocio que puede devolver (el 409 de la franja ocupada). */
(function () {
  FP_ANIMADOR.registrar('contrato-cuatro-datos', {
    duracion: 5,
    // Pasos LOGICOS: un dato del contrato por clic, sobre la flecha que negocia.
    // 1) la flecha y la interaccion de negocio, 2) quien llama a quien, 3) verbo y ruta (y su
    // nota: si es asincrono, el nombre del evento), 4) el error de negocio, el 409.
    pasos: [0.26, 0.42, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1) La flecha y lo que se negocia por ella
        { tipo: 'caja', x: 30, y: 60, w: 210, h: 120, t: 'App web', s: 'React', en: 0 },
        { tipo: 'caja', x: 560, y: 60, w: 210, h: 120, t: 'API de turnos', s: 'Node.js', en: 0.02 },
        { tipo: 'flecha', de: [245, 120], a: [555, 120], grosor: 4, en: 0.05 },
        { tipo: 'caja', x: 40, y: 240, w: 350, h: 110, t: '1 · Interacción', s: 'Reservar turno', color: 'accion', tam: 22, tamSub: 20, en: 0.12 },
        // 2) Quien llama a quien
        { tipo: 'caja', x: 410, y: 240, w: 350, h: 110, t: '2 · Quién llama a quién', s: 'App web → API de turnos', color: 'accion', tam: 22, tamSub: 20, en: 0.3 },
        // 3) Verbo y ruta
        { tipo: 'caja', x: 40, y: 370, w: 350, h: 110, t: '3 · Verbo y ruta', s: 'POST /turnos', color: 'acento', tam: 22, tamSub: 20, en: 0.46 },
        { tipo: 'texto', t: 'Si es asíncrono: el nombre del evento.', x: 215, y: 494, tam: 19, ancho: 350, color: 'acento', en: 0.54 },
        // 4) El error de negocio
        { tipo: 'caja', x: 410, y: 370, w: 350, h: 110, t: '4 · Error de negocio', s: '409 · la franja ya está ocupada', color: 'malva', tam: 22, tamSub: 20, en: 0.7 },
        { tipo: 'texto', t: 'Una respuesta prevista, parte del diseño.', x: 585, y: 494, tam: 19, ancho: 350, color: 'malva', en: 0.78 }
      ]);
    }
  });
})();
