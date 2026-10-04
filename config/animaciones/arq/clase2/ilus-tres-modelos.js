/* Ilustracion (un fotograma): IaaS · PaaS · SaaS */
(function () {
  FP_ANIMADOR.registrar('ilus-tres-modelos', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "¿Qué administras tú?", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74, "w": 240.0, "h": 70, "t": "IaaS", "lleno": true, "color": "accion", "tam": 21, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 160, "w": 224.0, "h": 100, "t": "SO", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 272, "w": 224.0, "h": 100, "t": "runtime", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 384, "w": 224.0, "h": 100, "t": "app y datos", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 280.0, "y": 74, "w": 240.0, "h": 70, "t": "PaaS", "lleno": true, "color": "acento", "tam": 21, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 160, "w": 224.0, "h": 100, "t": "app", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 272, "w": 224.0, "h": 100, "t": "datos", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 540.0, "y": 74, "w": 240.0, "h": 70, "t": "SaaS", "lleno": true, "color": "verde", "tam": 21, "en": 0}, {"tipo": "caja", "x": 548.0, "y": 160, "w": 224.0, "h": 100, "t": "solo configuración", "color": "verde", "tam": 20, "r": 10, "en": 0}, {"tipo": "texto", "t": "Ej.: VM · plataforma de despliegue · correo", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
