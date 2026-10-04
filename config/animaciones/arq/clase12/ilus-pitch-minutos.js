/* Ilustracion (un fotograma): Preparacion de presentacion */
(function () {
  FP_ANIMADOR.registrar('ilus-pitch-minutos', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "5 a 8 minutos, una idea por lámina", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 200, "w": 128.0, "h": 200, "t": "1 min", "s": "problema", "color": "accion", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [150.0, 300], "a": [176.0, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 178.0, "y": 200, "w": 128.0, "h": 200, "t": "2 min", "s": "arquitectura", "color": "acento", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [308.0, 300], "a": [334.0, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 336.0, "y": 200, "w": 128.0, "h": 200, "t": "1 min", "s": "contenedor", "color": "verde", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [466.0, 300], "a": [492.0, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 494.0, "y": 200, "w": 128.0, "h": 200, "t": "1 min", "s": "CI", "color": "malva", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [624.0, 300], "a": [650.0, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 652.0, "y": 200, "w": 128.0, "h": 200, "t": "1 min", "s": "seguridad y costos", "color": "accion", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "texto", "t": "Cerrar con el punto débil declarado", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
