/* Ilustracion (un fotograma): Construir, correr y verificar */
(function () {
  FP_ANIMADOR.registrar('ilus-construir-correr', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.codigo(ctx, lz, 20, 76, 470, "docker build -t turnos-api:0.1.0 .", 1, 20);
      UJ.codigo(ctx, lz, 20, 138, 470, "docker run -d -p 8081:8080 \\", 1, 20);
      UJ.codigo(ctx, lz, 20, 200, 470, "  --name api turnos-api:0.1.0", 1, 20);
      UJ.codigo(ctx, lz, 20, 262, 470, "curl localhost:8081/health", 1, 20);
      UJ.codigo(ctx, lz, 20, 324, 470, "→ 200 {\"estado\":\"ok\"}", 1, 20);
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Construir → correr → verificar", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 510, "y": 74, "w": 270, "h": 44, "t": "nombre y etiqueta", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 96], "a": [507, 96], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 136, "w": 270, "h": 44, "t": "anfitrión : contenedor", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 158], "a": [507, 158], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 260, "w": 270, "h": 44, "t": "ruta · código · cuerpo", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 282], "a": [507, 282], "grosor": 2, "en": 0}, {"tipo": "texto", "t": "Un 200 con cuerpo vacío no prueba nada", "x": 400, "y": 590, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
