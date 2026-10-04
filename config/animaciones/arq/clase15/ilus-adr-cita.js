/* Ilustracion (un fotograma): El ADR: el artefacto */
(function () {
  FP_ANIMADOR.registrar('ilus-adr-cita', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "El ADR se cita, no se lee", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 110, "y": 70.0, "w": 580, "h": 168.66666666666666, "t": "Pregunta del jurado", "s": "¿por qué PaaS?", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 239.66666666666666], "a": [400, 259.66666666666663], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 260.66666666666663, "w": 580, "h": 168.66666666666666, "t": "Cita", "s": "«está en el ADR-002»", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 430.33333333333326], "a": [400, 450.33333333333326], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 451.3333333333333, "w": 580, "h": 168.66666666666666, "t": "Trade-off", "s": "lo que se aceptó perder", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}]);
    }
  });
})();
