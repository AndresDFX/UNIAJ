/* Ilustracion (un fotograma): Errores frecuentes a corregir */
(function () {
  FP_ANIMADOR.registrar('ilus-errores', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Errores frecuentes", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 170.0, "t": "Microservicios teatro", "s": "base compartida, despliegue junto", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 170.0, "t": "Nombres distintos", "s": "rompen la trazabilidad", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 262.0, "w": 370.0, "h": 170.0, "t": "Secreto en la imagen", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 262.0, "w": 370.0, "h": 170.0, "t": "CI sin tests", "s": "no puede fallar", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 450.0, "w": 370.0, "h": 170.0, "t": "Diagrama sin puertos", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 450.0, "w": 370.0, "h": 170.0, "t": "Dominio infinito", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}]);
    }
  });
})();
