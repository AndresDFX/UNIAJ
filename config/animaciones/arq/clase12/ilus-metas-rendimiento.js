/* Ilustracion (un fotograma): Rendimiento sin stress-tool */
(function () {
  FP_ANIMADOR.registrar('ilus-metas-rendimiento', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Metas que se verifican", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Carga", "s": "150 RPS en hora pico", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Latencia", "s": "p95 < 300 ms", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Errores", "s": "< 1 %", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Cuello probable", "s": "base · autenticación · I/O", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Un solo usuario no mide concurrencia", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
