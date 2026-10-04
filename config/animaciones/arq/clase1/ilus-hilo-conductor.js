/* Ilustracion (un fotograma): CloudLite App */
(function () {
  FP_ANIMADOR.registrar('ilus-hilo-conductor', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Un mismo sistema, todo el semestre", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 110, "y": 70.0, "w": 580, "h": 106.0, "t": "Dominio acotado", "s": "la app de turnos: reservar, agenda, horarios", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 177.0], "a": [400, 197.0], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 198.0, "w": 580, "h": 106.0, "t": "Diagramas", "s": "contexto → contenedores → despliegue", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 305.0], "a": [400, 325.0], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 326.0, "w": 580, "h": 106.0, "t": "Contenedor y CI/CD", "s": "en laboratorios gratuitos", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 433.0], "a": [400, 453.0], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 454.0, "w": 580, "h": 106.0, "t": "Informe y sustentación", "s": "decisiones documentadas", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Un dominio infinito no cabe en un semestre", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
