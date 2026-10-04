/* Ilustracion (un fotograma): YAML minimo */
(function () {
  FP_ANIMADOR.registrar('ilus-yaml-minimo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.codigo(ctx, lz, 20, 76, 470, "on: [push, pull_request]", 1, 20);
      UJ.codigo(ctx, lz, 20, 133, 470, "jobs:", 1, 20);
      UJ.codigo(ctx, lz, 20, 191, 470, "  ci:", 1, 20);
      UJ.codigo(ctx, lz, 20, 249, 470, "    runs-on: ubuntu-latest", 1, 20);
      UJ.codigo(ctx, lz, 20, 307, 470, "    steps:", 1, 20);
      UJ.codigo(ctx, lz, 20, 364, 470, "      - uses: actions/checkout@v4", 1, 20);
      UJ.codigo(ctx, lz, 20, 422, 470, "      - run: npm ci", 1, 20);
      UJ.codigo(ctx, lz, 20, 480, 470, "      - run: npm test", 1, 20);
      UJ.codigo(ctx, lz, 20, 538, 470, "      - run: echo \"deploy simulado\"", 1, 20);
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Tres bloques obligatorios", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 510, "y": 74.0, "w": 270, "h": 44, "t": "disparadores", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 96.0], "a": [507, 96.0], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 247.33333333333334, "w": 270, "h": 44, "t": "entorno", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 269.33333333333337], "a": [507, 269.33333333333337], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 305.1111111111111, "w": 270, "h": 44, "t": "pasos en orden", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 327.1111111111111], "a": [507, 327.1111111111111], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 478.44444444444446, "w": 270, "h": 44, "t": "lo que lo pone rojo", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 500.44444444444446], "a": [507, 500.44444444444446], "grosor": 2, "en": 0}, {"tipo": "texto", "t": "Secretos solo en Settings, nunca en el YAML", "x": 400, "y": 590, "tam": 20, "peso": 600, "color": "malva", "ancho": 740, "en": 0}]);
    }
  });
})();
