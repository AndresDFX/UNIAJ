/* Ilustracion (un fotograma): Almacenamiento */
(function () {
  FP_ANIMADOR.registrar('ilus-elegir-almacen', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "¿Qué característica tiene el dato?", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 110, "y": 70.0, "w": 580, "h": 148.66666666666666, "t": "Se cruza con otro dato", "s": "→ Relacional · turnos", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 219.66666666666666], "a": [400, 239.66666666666666], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 240.66666666666666, "w": 580, "h": 148.66666666666666, "t": "Lo monta un solo proceso", "s": "→ Bloque · disco de una VM", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "flecha", "de": [400, 390.3333333333333], "a": [400, 410.3333333333333], "grosor": 3, "en": 0}, {"tipo": "caja", "x": 110, "y": 411.3333333333333, "w": 580, "h": 148.66666666666666, "t": "Se recupera entero", "s": "→ Objeto · fotos de perfil", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Sin archivos: «no necesito objeto» es válido", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
