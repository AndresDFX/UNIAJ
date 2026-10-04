/* Ilustracion (un fotograma): CI/CD sin tarjeta */
(function () {
  FP_ANIMADOR.registrar('ilus-ci-cd', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Hasta dónde llega el pipeline", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 200, "w": 167.5, "h": 200, "t": "push", "color": "accion", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [189.5, 300], "a": [215.5, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 217.5, "y": 200, "w": 167.5, "h": 200, "t": "build", "s": "CI", "color": "acento", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [387.0, 300], "a": [413.0, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 415.0, "y": 200, "w": 167.5, "h": 200, "t": "test", "s": "CI", "color": "verde", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [584.5, 300], "a": [610.5, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 612.5, "y": 200, "w": 167.5, "h": 200, "t": "listo para desplegar", "s": "entrega continua", "color": "malva", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "texto", "t": "Un paso «deploy» con echo no es despliegue continuo", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
