/* Ilustracion (un fotograma): Costos sin factura real */
(function () {
  FP_ANIMADOR.registrar('ilus-drivers-costo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Lo que mueve el costo", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Siempre encendido", "s": "la base: Medio", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Egress", "s": "datos que salen, por GB", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Almacenamiento caliente", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Builds frecuentes de CI", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Un worker que corre bajo demanda: Bajo", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
