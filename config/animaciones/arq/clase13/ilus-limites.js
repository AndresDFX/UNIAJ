/* Ilustracion (un fotograma): Limites y costos */
(function () {
  FP_ANIMADOR.registrar('ilus-limites', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Los límites también se diseñan", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 760.0, "h": 150.0, "t": "min réplicas", "s": "capacidad base = costo fijo", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 242.0, "w": 760.0, "h": 150.0, "t": "max réplicas", "s": "techo de gasto y de conexiones", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 410.0, "w": 760.0, "h": 150.0, "t": "cooldown", "s": "≈ 5 min para no oscilar", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Sin max, un pico se vuelve factura", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
