/* Ilustracion (un fotograma): Red logica para el diagrama */
(function () {
  FP_ANIMADOR.registrar('ilus-tres-zonas', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Tres zonas, no dos", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 200, "w": 233.33333333333334, "h": 200, "t": "Pública", "s": "balanceador · web estática", "color": "accion", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [255.33333333333334, 300], "a": [281.33333333333337, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 283.33333333333337, "y": 200, "w": 233.33333333333334, "h": 200, "t": "Privada", "s": "la API", "color": "acento", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "flecha", "de": [518.6666666666667, 300], "a": [544.6666666666667, 300], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 546.6666666666667, "y": 200, "w": 233.33333333333334, "h": 200, "t": "Datos", "s": "la base: solo acepta a la API", "color": "verde", "tam": 21, "tamSub": 18, "en": 0}, {"tipo": "texto", "t": "La base nunca en la zona pública", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
