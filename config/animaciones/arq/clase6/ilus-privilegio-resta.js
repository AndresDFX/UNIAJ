/* Ilustracion (un fotograma): Menor privilegio: que deja */
(function () {
  FP_ANIMADOR.registrar('ilus-privilegio-resta', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Rol de la API sobre la base", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74, "w": 370.0, "h": 70, "t": "Puede", "lleno": true, "color": "accion", "tam": 21, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 160, "w": 354.0, "h": 100, "t": "leer turnos", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 272, "w": 354.0, "h": 100, "t": "insertar turnos", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 384, "w": 354.0, "h": 100, "t": "actualizar turnos", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74, "w": 370.0, "h": 70, "t": "Ya no puede", "lleno": true, "color": "acento", "tam": 21, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 160, "w": 354.0, "h": 100, "t": "borrar filas", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 272, "w": 354.0, "h": 100, "t": "cambiar la estructura", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 384, "w": 354.0, "h": 100, "t": "leer otro esquema", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "texto", "t": "Una inyección hereda el rol, no al dueño", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
