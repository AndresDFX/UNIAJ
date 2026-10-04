/* Ilustracion (un fotograma): De dominio a arquitectura */
(function () {
  FP_ANIMADOR.registrar('ilus-mini-metodo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Del dominio a la arquitectura", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 110, "y": 70.0, "w": 580, "h": 80.4, "t": "1 · Actor y problema", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 151.4], "a": [400, 171.4], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 172.4, "w": 580, "h": 80.4, "t": "2 · Capacidades", "s": "verbos de negocio", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 253.8], "a": [400, 273.8], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 274.8, "w": 580, "h": 80.4, "t": "3 · Contenedores lógicos", "s": "núcleo vs satélite", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 356.20000000000005], "a": [400, 376.20000000000005], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 377.20000000000005, "w": 580, "h": 80.4, "t": "4 · Datos", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 458.6], "a": [400, 478.6], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 479.6, "w": 580, "h": 80.4, "t": "5 · Riesgos", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Nunca empezar por la tecnología", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
