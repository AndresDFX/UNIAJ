/* Ilustracion (un fotograma): Ejercicio guiado */
(function () {
  FP_ANIMADOR.registrar('ilus-cadena-control', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Amenaza → control → dónde se ve", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74, "w": 240.0, "h": 70, "t": "Amenaza", "lleno": true, "color": "accion", "tam": 21, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 160, "w": 224.0, "h": 100, "t": "API sin autenticar", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 272, "w": 224.0, "h": 100, "t": "llave en el Dockerfile", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 384, "w": 224.0, "h": 100, "t": "mil GET por minuto", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 280.0, "y": 74, "w": 240.0, "h": 70, "t": "Control", "lleno": true, "color": "acento", "tam": 21, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 160, "w": 224.0, "h": 100, "t": "token verificado", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 272, "w": 224.0, "h": 100, "t": "variable de entorno", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 288.0, "y": 384, "w": 224.0, "h": 100, "t": "límite de tasa", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 540.0, "y": 74, "w": 240.0, "h": 70, "t": "Dónde se ve", "lleno": true, "color": "verde", "tam": 21, "en": 0}, {"tipo": "caja", "x": 548.0, "y": 160, "w": 224.0, "h": 100, "t": "flecha App → API", "color": "verde", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 548.0, "y": 272, "w": 224.0, "h": 100, "t": "flecha API → Avisos", "color": "verde", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 548.0, "y": 384, "w": 224.0, "h": 100, "t": "caja App web", "color": "verde", "tam": 20, "r": 10, "en": 0}]);
    }
  });
})();
