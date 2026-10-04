/* Ilustracion (un fotograma): Checklist del diagrama Deployment */
(function () {
  FP_ANIMADOR.registrar('ilus-checklist-deploy', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Un diagrama de despliegue completo", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Tres zonas rotuladas", "s": "cada componente en la suya", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Puerto en cada caja", "s": "443 · 8080 · 5432", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Protocolo en cada flecha", "s": "HTTPS · HTTP · PostgreSQL", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Frontera de confianza", "s": "externos fuera de las zonas", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Mismos nombres que el C4 Containers", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
