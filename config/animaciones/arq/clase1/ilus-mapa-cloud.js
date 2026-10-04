/* Ilustracion (un fotograma): Que es arquitectura cloud */
(function () {
  FP_ANIMADOR.registrar('ilus-mapa-cloud', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Arquitectura cloud = cuatro cosas", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Componentes", "s": "cliente · API · lógica · datos", "color": "accion", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 74.0, "w": 370.0, "h": 234.0, "t": "Relaciones", "s": "quién llama a quién y cómo", "color": "acento", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 20.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Despliegue", "s": "dónde corre cada pieza", "color": "verde", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "caja", "x": 410.0, "y": 326.0, "w": 370.0, "h": 234.0, "t": "Calidad", "s": "seguridad · escala · costo", "color": "malva", "tam": 23, "tamSub": 19, "en": 0}, {"tipo": "texto", "t": "Decisión de arquitectura = cara de revertir", "x": 400, "y": 580, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
