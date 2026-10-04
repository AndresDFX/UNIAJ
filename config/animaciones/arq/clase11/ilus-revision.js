/* Ilustracion (un fotograma): La teoria propia del dia */
(function () {
  FP_ANIMADOR.registrar('ilus-revision', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Una revisión de arquitectura busca", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74, "w": 240.0, "h": 70, "t": "Decisiones", "lleno": true, "color": "accion", "tam": 21, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 160, "w": 224.0, "h": 100, "t": "sin argumento", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 280.0, "y": 74, "w": 240.0, "h": 70, "t": "Artefactos", "lleno": true, "color": "acento", "tam": 21, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 160, "w": 224.0, "h": 100, "t": "incoherentes entre sí", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 540.0, "y": 74, "w": 240.0, "h": 70, "t": "Riesgos", "lleno": true, "color": "verde", "tam": 21, "en": 0}, {"tipo": "caja", "x": 548.0, "y": 160, "w": 224.0, "h": 100, "t": "sin nombrar", "color": "verde", "tam": 20, "r": 10, "en": 0}, {"tipo": "texto", "t": "Alguien distinto del autor, antes de implementar", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
