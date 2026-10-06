/* Lo que dibuja el flowchart TD «La maquina de decision del autoescalado»: observar, dos rombos
 * de decision (subir / bajar), scale out y scale in, el enfriamiento que vuelve a observar, y la
 * base primaria con su flecha punteada: el limite del diseno, lo que no escala. */
(function () {
  FP_ANIMADOR.registrar('dg-autoescalado', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      MF.nodo(ctx, lz, 290, 20, 220, 56, 'Observar CPU cada 60 s');
      MF.nodo(ctx, lz, 20, 20, 200, 56, 'No escala: base primaria', { relleno: '#F3E3E3', borde: '#A02030' });
      MF.rombo(ctx, lz, 400, 175, 150, 62, 'CPU sobre 70 por\nciento 5 min?');
      MF.rombo(ctx, lz, 400, 345, 150, 62, 'CPU bajo 30 por\nciento 10 min?');
      MF.nodo(ctx, lz, 30, 250, 200, 56, 'Scale out: +1, max 6');
      MF.nodo(ctx, lz, 295, 460, 210, 56, 'Scale in: -1, min 2');
      MF.nodo(ctx, lz, 295, 570, 210, 56, 'Enfriamiento 5 min');
      // obs --> up
      MF.flecha(ctx, lz, [[400, 78], [400, 110]]);
      // bd -.-> obs
      MF.flecha(ctx, lz, [[222, 48], [286, 48]], { punteada: true, color: '#A02030', rot: 'limite del\ndiseno', en: [254, 92] });
      // up -- Si --> out ; up -- No --> down
      MF.flecha(ctx, lz, [[250, 175], [130, 175], [130, 246]], { rot: 'Si', en: [190, 175] });
      MF.flecha(ctx, lz, [[400, 239], [400, 280]], { rot: 'No', en: [400, 258] });
      // down -- Si --> inn ; down -- No --> obs
      MF.flecha(ctx, lz, [[400, 409], [400, 456]], { rot: 'Si', en: [400, 432] });
      MF.flecha(ctx, lz, [[550, 345], [700, 345], [700, 40], [514, 40]], { rot: 'No', en: [700, 200] });
      // out --> cool ; inn --> cool ; cool --> obs
      MF.flecha(ctx, lz, [[130, 308], [130, 598], [291, 598]]);
      MF.flecha(ctx, lz, [[400, 518], [400, 566]]);
      MF.flecha(ctx, lz, [[507, 598], [770, 598], [770, 62], [514, 62]]);
    }
  });
})();
