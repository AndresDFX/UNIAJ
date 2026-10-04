/* Ilustracion (un fotograma): Dockerfile minimo */
(function () {
  FP_ANIMADOR.registrar('ilus-dockerfile-minimo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.codigo(ctx, lz, 20, 76, 470, "FROM node:20-alpine", 1, 20);
      UJ.codigo(ctx, lz, 20, 138, 470, "WORKDIR /app", 1, 20);
      UJ.codigo(ctx, lz, 20, 200, 470, "COPY package*.json ./", 1, 20);
      UJ.codigo(ctx, lz, 20, 262, 470, "RUN npm ci", 1, 20);
      UJ.codigo(ctx, lz, 20, 324, 470, "COPY . .", 1, 20);
      UJ.codigo(ctx, lz, 20, 386, 470, "EXPOSE 8080", 1, 20);
      UJ.codigo(ctx, lz, 20, 448, 470, "CMD [\"node\", \"server.js\"]", 1, 20);
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Siete instrucciones, en este orden", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 510, "y": 74, "w": 270, "h": 44, "t": "etiqueta fija, nunca latest", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 96], "a": [507, 96], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 198, "w": 270, "h": 44, "t": "dependencias primero", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 220], "a": [507, 220], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 322, "w": 270, "h": 44, "t": "con .dockerignore", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 344], "a": [507, 344], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 384, "w": 270, "h": 44, "t": "documenta, no publica", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 406], "a": [507, 406], "grosor": 2, "en": 0}, {"tipo": "texto", "t": "Nunca un secreto en una capa", "x": 400, "y": 590, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
