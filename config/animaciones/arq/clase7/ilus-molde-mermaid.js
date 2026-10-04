/* Ilustracion (un fotograma): El molde de Mermaid */
(function () {
  FP_ANIMADOR.registrar('ilus-molde-mermaid', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.codigo(ctx, lz, 20, 76, 470, "flowchart LR", 1, 17);
      UJ.codigo(ctx, lz, 20, 122, 470, "  subgraph Publica", 1, 17);
      UJ.codigo(ctx, lz, 20, 169, 470, "    lb[Balanceador :443]", 1, 17);
      UJ.codigo(ctx, lz, 20, 216, 470, "  end", 1, 17);
      UJ.codigo(ctx, lz, 20, 262, 470, "  subgraph Privada", 1, 17);
      UJ.codigo(ctx, lz, 20, 309, 470, "    api[API :8080]", 1, 17);
      UJ.codigo(ctx, lz, 20, 356, 470, "  end", 1, 17);
      UJ.codigo(ctx, lz, 20, 402, 470, "  subgraph Datos", 1, 17);
      UJ.codigo(ctx, lz, 20, 449, 470, "    db[(Base :5432)]", 1, 17);
      UJ.codigo(ctx, lz, 20, 496, 470, "  end", 1, 17);
      UJ.codigo(ctx, lz, 20, 542, 470, "  lb -->|HTTP 8080| api", 1, 17);
      UJ.codigo(ctx, lz, 20, 589, 470, "  api -->|PostgreSQL 5432| db", 1, 17);
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "El molde, línea por línea", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 510, "y": 74.0, "w": 270, "h": 38, "t": "izquierda a derecha", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 93.0], "a": [507, 93.0], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 120.66666666666666, "w": 270, "h": 38, "t": "una zona = subgraph", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 139.66666666666666], "a": [507, 139.66666666666666], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 214.0, "w": 270, "h": 38, "t": "cada zona con su end", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 233.0], "a": [507, 233.0], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 447.3333333333333, "w": 270, "h": 38, "t": "[( )] = base", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 466.3333333333333], "a": [507, 466.3333333333333], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 540.6666666666666, "w": 270, "h": 38, "t": "protocolo y puerto", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 559.6666666666666], "a": [507, 559.6666666666666], "grosor": 2, "en": 0}]);
    }
  });
})();
