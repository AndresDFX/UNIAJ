/* Ilustracion (un fotograma): La pila dibujada */
(function () {
  FP_ANIMADOR.registrar('ilus-pila-nombres', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Quién administra cada capa", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74, "w": 240.0, "h": 70, "t": "IaaS", "lleno": true, "color": "accion", "tam": 21, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 160, "w": 224.0, "h": 100, "t": "desde el SO hacia arriba", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 272, "w": 224.0, "h": 100, "t": "ej.: una VM", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 280.0, "y": 74, "w": 240.0, "h": 70, "t": "PaaS", "lleno": true, "color": "acento", "tam": 21, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 160, "w": 224.0, "h": 100, "t": "aplicación y datos", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 272, "w": 224.0, "h": 100, "t": "ej.: plataforma de despliegue", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 540.0, "y": 74, "w": 240.0, "h": 70, "t": "SaaS", "lleno": true, "color": "verde", "tam": 21, "en": 0}, {"tipo": "caja", "x": 548.0, "y": 160, "w": 224.0, "h": 100, "t": "solo configuración", "color": "verde", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 548.0, "y": 272, "w": 224.0, "h": 100, "t": "ej.: correo corporativo", "color": "verde", "tam": 20, "r": 10, "en": 0}, {"tipo": "texto", "t": "Siete capas: red → … → datos", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
