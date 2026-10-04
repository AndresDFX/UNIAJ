/* Asegurar un sistema es preservar tres propiedades: confidencialidad, integridad y
 * disponibilidad. Cada una con un ejemplo en una app de turnos. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('triada-cia', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, P = [[400, 70], [150, 420], [650, 420]];
      L.trazo(ctx, [P[0], P[1], P[2], P[0]], L.tramo(t, 0, 0.2), L.tono(m.tinta, 0.6), 4);
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 250, y: 20, w: 300, h: 120, t: 'Confidencialidad', s: 'nadie lee el correo de otro cliente', en: 0.12, tam: 24 },
        { tipo: 'caja', x: 20, y: 380, w: 300, h: 120, t: 'Integridad', s: 'nadie cambia el turno de otro', color: 'acento', en: 0.36, tam: 24 },
        { tipo: 'caja', x: 480, y: 380, w: 300, h: 120, t: 'Disponibilidad', s: 'la agenda responde el sábado a las 9', color: 'malva', en: 0.6, tam: 24 },
        { tipo: 'texto', t: 'CIA', x: 400, y: 270, tam: 46, peso: 800, color: 'accion', en: 0.2 },
        { tipo: 'texto', t: 'Se diseña desde el principio: no es un firewall al final.', x: 400, y: 560, tam: 22, ancho: 760, en: 0.86 }
      ]);
    }
  });
})();
