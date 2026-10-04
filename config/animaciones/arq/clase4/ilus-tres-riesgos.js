/* Ilustracion (un fotograma): Distribuido implica fallos */
(function () {
  FP_ANIMADOR.registrar('ilus-tres-riesgos', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Cada flecha es una llamada de red", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "1 · Qué se cae", "s": "una caja: qué deja y qué sigue funcionando", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "2 · Cuántos saltos", "s": "contados en el diagrama", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "3 · Dato en dos pasos", "s": "¿y si falla el segundo?", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Mitigación", "s": "timeout · reintento · idempotencia · circuit breaker", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "«Es más complejo» no es un riesgo", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
