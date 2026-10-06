/* Lo que dibuja el codigo de «Flujo de tarea con caminos alternos en Mermaid»: registrar dueno y
 * mascota con sus dos decisiones (dueno registrado, campos completos), la confirmacion y la
 * busqueda con sus tres salidas (cero, varios, uno). */
(function () {
  FP_ANIMADOR.registrar('dg-flujo-tarea', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var o = { tam: 14 };
      DG.nodo(ctx, lz, 160, 34, 270, 52, 'Recepcion: llega el dueño\ncon su mascota', 'rect', o);
      DG.nodo(ctx, lz, 160, 135, 220, 90, 'Dueño ya\nregistrado?', 'rombo', o);
      DG.nodo(ctx, lz, 455, 135, 220, 50, 'Pantalla Registrar dueño', 'rect', o);
      DG.nodo(ctx, lz, 160, 245, 250, 50, 'Pantalla Registrar mascota', 'rect', o);
      DG.nodo(ctx, lz, 160, 360, 240, 100, 'Campos obligatorios\ncompletos?', 'rombo', o);
      DG.nodo(ctx, lz, 455, 360, 230, 60, 'Guardar deshabilitado +\nayuda en el campo', 'rect', o);
      DG.nodo(ctx, lz, 160, 475, 250, 56, 'Confirmacion: Ficha guardada,\ncodigo M-0421', 'rect', o);
      DG.nodo(ctx, lz, 440, 475, 170, 56, 'Pantalla Buscar\nexpediente', 'rect', o);
      DG.nodo(ctx, lz, 680, 475, 190, 90, 'Cuantos\nresultados?', 'rombo', o);
      DG.nodo(ctx, lz, 140, 597, 260, 54, 'Sin resultados +\nBuscar por otro criterio', 'rect', o);
      DG.nodo(ctx, lz, 415, 597, 250, 54, 'Lista con especie,\nedad y dueño', 'rect', o);
      DG.nodo(ctx, lz, 680, 597, 190, 54, 'Ficha del paciente', 'rect', o);
      DG.flecha(ctx, lz, [[160, 60], [160, 89]]);
      DG.flecha(ctx, lz, [[270, 135], [344, 135]], { rotulo: 'No', en: [305, 135] });
      DG.flecha(ctx, lz, [[160, 180], [160, 219]], { rotulo: 'Si', en: [160, 199] });
      DG.flecha(ctx, lz, [[455, 160], [455, 232], [286, 232]]);
      DG.flecha(ctx, lz, [[160, 270], [160, 309]]);
      DG.flecha(ctx, lz, [[280, 360], [339, 360]], { rotulo: 'No', en: [308, 360] });
      DG.flecha(ctx, lz, [[455, 330], [455, 258], [286, 258]]);
      DG.flecha(ctx, lz, [[160, 410], [160, 446]], { rotulo: 'Si', en: [160, 428] });
      DG.flecha(ctx, lz, [[285, 475], [354, 475]]);
      DG.flecha(ctx, lz, [[525, 475], [584, 475]]);
      DG.flecha(ctx, lz, [[680, 520], [680, 569]], { rotulo: 'Uno', en: [680, 545] });
      DG.flecha(ctx, lz, [[660, 510], [430, 569]], { rotulo: 'Varios', en: [540, 541] });
      DG.flecha(ctx, lz, [[640, 500], [150, 569]], { rotulo: 'Cero', en: [300, 548] });
    }
  });
})();
