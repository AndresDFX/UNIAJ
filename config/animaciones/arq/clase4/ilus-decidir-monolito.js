/* Ilustracion (un fotograma): Monolito vs microservicios */
(function () {
  FP_ANIMADOR.registrar('ilus-decidir-monolito', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "La decisión, en una frase", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 110, "y": 70.0, "w": 580, "h": 106.0, "t": "Criterio 1 · Equipo", "s": "cuántas personas y qué plazo", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 177.0], "a": [400, 197.0], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 198.0, "w": 580, "h": 106.0, "t": "Criterio 2 · Acoplamiento", "s": "qué partes cambian juntas", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 305.0], "a": [400, 325.0], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 326.0, "w": 580, "h": 106.0, "t": "Se elige UNA", "s": "monolito modular o microservicios", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 433.0], "a": [400, 453.0], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 454.0, "w": 580, "h": 106.0, "t": "Se gana / se pierde", "s": "las dos mitades", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "12 servicios para 3 personas = teatro", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
