/* Ilustracion (un fotograma): Controles practicos */
(function () {
  FP_ANIMADOR.registrar('ilus-controles', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Controles gratuitos, por familia", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 264.0, "t": "Identidad", "s": "token · rol · menor privilegio", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 264.0, "t": "Red", "s": "solo el punto de entrada es público", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 356.0, "w": 370.0, "h": 264.0, "t": "Aplicación", "s": "validar en servidor · límite de tasa", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 356.0, "w": 370.0, "h": 264.0, "t": "Secretos", "s": "secrets del repo → variable de entorno", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}]);
    }
  });
})();
