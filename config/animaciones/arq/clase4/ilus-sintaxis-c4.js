/* Ilustracion (un fotograma): C4Container en Mermaid: la sintaxis */
(function () {
  FP_ANIMADOR.registrar('ilus-sintaxis-c4', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.codigo(ctx, lz, 20, 76, 470, "C4Container", 1, 20);
      UJ.codigo(ctx, lz, 20, 138, 470, "Person(cli, \"Cliente\")", 1, 20);
      UJ.codigo(ctx, lz, 20, 200, 470, "System_Ext(mail, \"Correo\")", 1, 20);
      UJ.codigo(ctx, lz, 20, 262, 470, "System_Boundary(s, \"Turnos\") {", 1, 20);
      UJ.codigo(ctx, lz, 20, 324, 470, "  Container(api, \"API\", \"Node\")", 1, 20);
      UJ.codigo(ctx, lz, 20, 386, 470, "  ContainerDb(db, \"Base\", \"PostgreSQL\")", 1, 20);
      UJ.codigo(ctx, lz, 20, 448, 470, "}", 1, 20);
      UJ.codigo(ctx, lz, 20, 510, 470, "Rel(cli, api, \"Reserva\", \"HTTPS/JSON\")", 1, 20);
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Anatomía de un C4Container", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "ancho": 760, "en": 0}, {"tipo": "caja", "x": 510, "y": 74, "w": 270, "h": 44, "t": "primera línea", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 96], "a": [507, 96], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 136, "w": 270, "h": 44, "t": "fuera del bloque", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 158], "a": [507, 158], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 384, "w": 270, "h": 44, "t": "almacén ≠ caja", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 406], "a": [507, 406], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 446, "w": 270, "h": 44, "t": "la llave se cierra", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 468], "a": [507, 468], "grosor": 2, "en": 0}, {"tipo": "caja", "x": 510, "y": 508, "w": 270, "h": 44, "t": "origen·destino·qué·protocolo", "color": "acento", "tam": 17, "r": 10, "en": 0}, {"tipo": "flecha", "de": [493, 530], "a": [507, 530], "grosor": 2, "en": 0}]);
    }
  });
})();
