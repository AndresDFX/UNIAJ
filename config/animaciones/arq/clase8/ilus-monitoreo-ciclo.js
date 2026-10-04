/* Ilustracion (un fotograma): Monitoreo y optimizacion */
(function () {
  FP_ANIMADOR.registrar('ilus-monitoreo-ciclo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Medir antes de optimizar", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 200, "w": 167.5, "h": 200, "t": "Observar", "s": "métricas y logs", "color": "accion", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [189.5, 300], "a": [215.5, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 217.5, "y": 200, "w": 167.5, "h": 200, "t": "Umbral", "s": "qué valor es problema", "color": "acento", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [387.0, 300], "a": [413.0, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 415.0, "y": 200, "w": 167.5, "h": 200, "t": "Alerta", "s": "a quién avisa", "color": "verde", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [584.5, 300], "a": [610.5, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 612.5, "y": 200, "w": 167.5, "h": 200, "t": "Ajustar", "s": "y volver a medir", "color": "malva", "tam": 21, "tamSub": 18, "en": 0}]);
    }
  });
})();
