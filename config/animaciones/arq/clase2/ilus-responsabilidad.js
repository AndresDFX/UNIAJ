/* Ilustracion (un fotograma): Responsabilidad compartida */
(function () {
  FP_ANIMADOR.registrar('ilus-responsabilidad', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Responsabilidad compartida", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74, "w": 370.0, "h": 70, "t": "Proveedor: DE la nube", "lleno": true, "color": "accion", "tam": 21, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 160, "w": 354.0, "h": 100, "t": "centro de datos", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 272, "w": 354.0, "h": 100, "t": "hipervisor", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 28.0, "y": 384, "w": 354.0, "h": 100, "t": "cifrado en reposo", "color": "accion", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74, "w": 370.0, "h": 70, "t": "Tú: EN la nube", "lleno": true, "color": "acento", "tam": 21, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 160, "w": 354.0, "h": 100, "t": "configuración", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 272, "w": 354.0, "h": 100, "t": "credenciales", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "caja", "x": 418.0, "y": 384, "w": 354.0, "h": 100, "t": "permisos y datos", "color": "acento", "tam": 20, "r": 10, "en": 0}, {"tipo": "texto", "t": "La causa dominante: configuración del cliente", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
