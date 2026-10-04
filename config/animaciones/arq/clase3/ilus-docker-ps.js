/* Ilustracion (un fotograma): Segundo ejemplo: leer las siete */
(function () {
  FP_ANIMADOR.registrar('ilus-docker-ps', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "docker ps: siete columnas", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 108.0, "t": "CONTAINER ID", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 108.0, "t": "IMAGE", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 200.0, "w": 370.0, "h": 108.0, "t": "COMMAND", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 200.0, "w": 370.0, "h": 108.0, "t": "CREATED", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 326.0, "w": 370.0, "h": 108.0, "t": "STATUS", "s": "Up = vive · Exited (n) = murió", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 326.0, "w": 370.0, "h": 108.0, "t": "PORTS", "s": "0.0.0.0:8081->8080", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 452.0, "w": 370.0, "h": 108.0, "t": "NAMES", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Se mira STATUS primero", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
