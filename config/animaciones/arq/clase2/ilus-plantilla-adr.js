/* Ilustracion (un fotograma): Plantilla ADR-001 */
(function () {
  FP_ANIMADOR.registrar('ilus-plantilla-adr', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "ADR-001: un documento, una página", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 110, "y": 70.0, "w": 580, "h": 92.4, "t": "Título · Estado", "s": "Aceptado + fecha", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 163.4], "a": [400, 183.4], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 184.4, "w": 580, "h": 92.4, "t": "Contexto", "s": "restricciones reales", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 277.8], "a": [400, 297.8], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 298.8, "w": 580, "h": 92.4, "t": "Decisión", "s": "una frase, un modelo", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 392.20000000000005], "a": [400, 412.20000000000005], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 413.20000000000005, "w": 580, "h": 92.4, "t": "Alternativas descartadas", "s": "exactamente 2, con motivo", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 506.6], "a": [400, 526.6], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 527.6, "w": 580, "h": 92.4, "t": "Consecuencias", "s": "lo que se gana y se pierde", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}]);
    }
  });
})();
