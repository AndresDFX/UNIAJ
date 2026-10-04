/* Ilustracion (un fotograma): La regla de los 60 segundos */
(function () {
  FP_ANIMADOR.registrar('ilus-regla-60', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Cualquiera explica cualquier parte", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 110, "y": 70.0, "w": 580, "h": 168.66666666666666, "t": "Falla a las 11 p. m.", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 239.66666666666666], "a": [400, 259.66666666666663], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 260.66666666666663, "w": 580, "h": 168.66666666666666, "t": "Contesta quien está", "s": "no el autor", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 430.33333333333326], "a": [400, 450.33333333333326], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 451.3333333333333, "w": 580, "h": 168.66666666666666, "t": "Sistema que solo uno entiende", "s": "= riesgo operativo", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}]);
    }
  });
})();
