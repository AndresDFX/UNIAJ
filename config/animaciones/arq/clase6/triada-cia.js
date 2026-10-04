/* Asegurar un sistema es preservar tres propiedades: confidencialidad, integridad y
 * disponibilidad. Cada una con un ejemplo en una app de turnos. */
(function () {
  FP_ANIMADOR.registrar('triada-cia', {
    duracion: 5,
    // Pasos LOGICOS: 1) confidencialidad con su ejemplo, 2) integridad con su ejemplo (primer
    // lado del triangulo), 3) disponibilidad con su ejemplo: el triangulo se cierra y es la
    // triada CIA, 4) la conclusion. El triangulo crece con cada propiedad, no se anticipa.
    pasos: [0.2, 0.46, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var P = [[400, 80], [170, 440], [630, 440]], gris = 'rgba(173,173,173,1)';
      UJ.escena(ctx, t, lz, [
        // lados del triangulo, detras de las cajas
        { tipo: 'linea', pts: [P[0], P[1]], color: gris, grosor: 4, en: 0.24 },
        { tipo: 'linea', pts: [P[1], P[2], P[0]], color: gris, grosor: 4, en: 0.52 },
        { tipo: 'caja', x: 250, y: 20, w: 300, h: 120, t: 'Confidencialidad', s: 'nadie lee el correo de otro cliente', en: 0.02, tam: 24 },
        { tipo: 'caja', x: 20, y: 380, w: 300, h: 120, t: 'Integridad', s: 'nadie cambia el turno de otro', color: 'acento', en: 0.32, tam: 24 },
        { tipo: 'caja', x: 480, y: 380, w: 300, h: 120, t: 'Disponibilidad', s: 'la agenda responde el sábado a las 9', color: 'malva', en: 0.56, tam: 24 },
        { tipo: 'texto', t: 'CIA', x: 400, y: 280, tam: 46, peso: 800, color: 'accion', en: 0.64 },
        { tipo: 'texto', t: 'Se diseña desde el principio: no es un firewall al final.', x: 400, y: 560, tam: 22, ancho: 760, en: 0.84 }
      ]);
    }
  });
})();
