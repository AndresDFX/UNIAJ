/* Ilustracion (un fotograma): Clase autonoma: escalabilidad */
(function () {
  FP_ANIMADOR.registrar('ilus-escala-vs-rendimiento', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Al duplicar los recursos…", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74, "w": 370.0, "h": 70, "t": "Escala bien", "lleno": true, "color": "accion", "tam": 21, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 160, "w": 354.0, "h": 100, "t": "≈ 2× trabajo", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74, "w": 370.0, "h": 70, "t": "Escala mal", "lleno": true, "color": "acento", "tam": 21, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 160, "w": 354.0, "h": 100, "t": "+20 % trabajo", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 272, "w": 354.0, "h": 100, "t": "el dinero no lo arregla", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "texto", "t": "Rendimiento: qué tan rápido · Escalabilidad: cuánto más", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
