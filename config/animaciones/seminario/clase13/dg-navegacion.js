/* Lo que dibuja el codigo de «El mapa de navegacion del prototipo»: del ingreso al menu, las tres
 * pantallas del menu, las dos vueltas de Registrar al menu y los tres caminos de la busqueda
 * (uno, varios, ninguno). */
(function () {
  FP_ANIMADOR.registrar('dg-navegacion', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var o = { tam: 15 };
      DG.nodo(ctx, lz, 60, 300, 100, 50, 'Ingreso', 'rect', o);
      DG.nodo(ctx, lz, 200, 300, 120, 56, 'Menu\nprincipal', 'rect', o);
      DG.nodo(ctx, lz, 380, 100, 160, 56, 'Registrar\nmascota', 'rect', o);
      DG.nodo(ctx, lz, 380, 300, 160, 56, 'Buscar\nexpediente', 'rect', o);
      DG.nodo(ctx, lz, 380, 560, 160, 50, 'Agendar cita', 'rect', o);
      DG.nodo(ctx, lz, 715, 170, 140, 60, 'Detalle del\nexpediente', 'rect', o);
      DG.nodo(ctx, lz, 600, 300, 150, 56, 'Lista de\nresultados', 'rect', o);
      DG.nodo(ctx, lz, 640, 455, 210, 60, 'Estado vacio\ncon accion sugerida', 'rect', o);
      DG.flecha(ctx, lz, [[110, 300], [139, 300]]);
      DG.flecha(ctx, lz, [[200, 272], [200, 100], [299, 100]]);
      DG.flecha(ctx, lz, [[260, 300], [299, 300]]);
      DG.flecha(ctx, lz, [[200, 328], [200, 560], [299, 560]]);
      DG.flecha(ctx, lz, [[380, 128], [380, 190], [245, 190], [245, 271]], { rotulo: 'guardar', en: [312, 190] });
      DG.flecha(ctx, lz, [[380, 72], [380, 30], [160, 30], [160, 271]], { rotulo: 'cancelar', en: [270, 30] });
      DG.flecha(ctx, lz, [[460, 285], [644, 185]], { rotulo: '1 resultado', en: [545, 232] });
      DG.flecha(ctx, lz, [[460, 300], [524, 300]], { rotulo: 'varios', en: [492, 328] });
      DG.flecha(ctx, lz, [[640, 272], [690, 201]]);
      DG.flecha(ctx, lz, [[440, 328], [534, 425]], { rotulo: 'ninguno', en: [482, 380] });
      DG.marca(ctx, lz, 560, 560, 1, 'El «ninguno» es el camino que se olvida', 210);
    }
  });
})();
