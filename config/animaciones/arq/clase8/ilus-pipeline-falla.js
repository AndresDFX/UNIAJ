/* Ilustracion (un fotograma): El pipeline del stub */
(function () {
  FP_ANIMADOR.registrar('ilus-pipeline-falla', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Un pipeline sano falla rápido", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 200, "w": 167.5, "h": 200, "t": "checkout", "s": "exit 0", "color": "accion", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [189.5, 300], "a": [215.5, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 217.5, "y": 200, "w": 167.5, "h": 200, "t": "build", "s": "exit 0", "color": "acento", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [387.0, 300], "a": [413.0, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 415.0, "y": 200, "w": 167.5, "h": 200, "t": "test", "s": "exit 1 → rojo", "color": "verde", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [584.5, 300], "a": [610.5, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 612.5, "y": 200, "w": 167.5, "h": 200, "t": "deploy", "s": "no se ejecuta", "color": "malva", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "texto", "t": "Código de salida ≠ 0 detiene el job", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
