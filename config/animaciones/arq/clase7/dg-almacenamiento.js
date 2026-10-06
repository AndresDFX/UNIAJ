/* Lo que dibuja el flowchart «Que tipo de almacenamiento pide cada componente»: la instancia de
 * la API a la izquierda y los tres almacenes (cilindros) a la derecha, cada flecha con su rotulo.
 * Arriba, la pregunta que decide, que antes era un comentario %% en el codigo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dg-almacenamiento', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      L.texto(ctx, 'Si esta instancia desaparece ahora, ¿qué dato se pierde?', 400, 18,
        { tam: 21, peso: 800, color: lz.marca.accion, alinear: 'center', ancho: 740, letra: lz.letra });
      MF.nodo(ctx, lz, 30, 300, 200, 70, 'API - instancia', { tam: 18 });
      MF.cilindro(ctx, lz, 470, 110, 300, 110, 'Disco de bloque\nse va con la instancia', { tam: 16 });
      MF.cilindro(ctx, lz, 470, 280, 300, 110, 'Almacenamiento de objetos\nfotos y respaldos', { tam: 16 });
      MF.cilindro(ctx, lz, 470, 450, 300, 110, 'Base relacional gestionada\nturnos, con respaldo', { tam: 16 });
      MF.flecha(ctx, lz, [[232, 320], [350, 170], [466, 170]], { rot: 'cache y temporales', en: [330, 205] });
      MF.flecha(ctx, lz, [[232, 335], [466, 335]], { rot: 'HTTPS', en: [350, 335] });
      MF.flecha(ctx, lz, [[232, 350], [350, 505], [466, 505]], { rot: 'TCP 5432', en: [330, 470] });
      L.texto(ctx, 'Se pierde', 620, 228, { tam: 14, peso: 800, color: lz.marca.malva || '#A02030', alinear: 'center', letra: lz.letra });
      L.texto(ctx, 'Sobrevive', 620, 398, { tam: 14, peso: 800, color: '#1B7A3A', alinear: 'center', letra: lz.letra });
      L.texto(ctx, 'Sobrevive', 620, 568, { tam: 14, peso: 800, color: '#1B7A3A', alinear: 'center', letra: lz.letra });
    }
  });
})();
