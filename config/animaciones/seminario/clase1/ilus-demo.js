/* Ilustracion: que observar en la demo de la Clase 1. Una frase cruda del cliente se parte en
 * un requisito funcional (QUE hace) y uno no funcional (COMO se comporta), y la palabra
 * «rapido» se cambia por un numero que se puede medir. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });

      // La frase cruda
      L.rectRed(ctx, 60, 60, 680, 96, 16); L.rellena(ctx, L.tono(m.sello, 0.82), L.tono(m.sello, -0.3), 2.5);
      UJ.rotulo(ctx, lz, 'Lo que dijo el cliente', W / 2, 70, { tam: 16, peso: 700, color: m.gris });
      UJ.rotulo(ctx, lz, '«necesito buscar rápido el expediente de un animal»', W / 2, 98, { tam: 22, peso: 700, ancho: 640 });
      // «rapido» marcado: es la palabra que no se puede probar
      UJ.pildora(ctx, lz, W / 2, 170, '«rápido» = ¿cuánto?', R, 1, { tam: 17, centrar: true });

      UJ.flecha(ctx, lz, 300, 160, 210, 238, A, 1, null, { grosor: 3 });
      UJ.flecha(ctx, lz, 500, 160, 590, 238, C, 1, null, { grosor: 3 });

      // RF
      L.rectRed(ctx, 24, 244, 364, 220, 14); L.rellena(ctx, L.tono(A, 0.92), A, 2.5);
      UJ.pildora(ctx, lz, 40, 258, 'RF-01', A, 1, { tam: 16, lleno: true });
      UJ.rotulo(ctx, lz, 'funcional · QUÉ hace', 372, 262, { tam: 16, peso: 700, color: A, alinear: 'right' });
      UJ.rotulo(ctx, lz, 'Buscar expediente por identificador', 206, 312, { tam: 21, peso: 800, color: L.tono(A, -0.3), ancho: 320 });
      UJ.rotulo(ctx, lz, 'Actor: recepcionista, veterinario', 206, 390, { tam: 17, peso: 500, ancho: 330 });

      // RNF
      L.rectRed(ctx, 412, 244, 364, 220, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2.5);
      UJ.pildora(ctx, lz, 428, 258, 'RNF-01', L.tono(C, -0.3), 1, { tam: 16, lleno: true });
      UJ.rotulo(ctx, lz, 'no funcional · CÓMO', 760, 262, { tam: 16, peso: 700, color: L.tono(C, -0.35), alinear: 'right' });
      UJ.rotulo(ctx, lz, 'Responde en menos de 2 s con 500 mascotas', 594, 312, { tam: 21, peso: 800, color: L.tono(C, -0.45), ancho: 320 });
      L.objetos.reloj(ctx, 470, 412, 24, m, 2);
      UJ.rotulo(ctx, lz, 'se mide con cronómetro', 506, 400, { tam: 17, peso: 600, alinear: 'left' });

      // La regla
      L.rectRed(ctx, 24, 498, 752, 70, 14); L.rellena(ctx, L.tono(V, 0.9), V, 2);
      UJ.sello(ctx, lz, 64, 533, 20, true, 1);
      UJ.rotulo(ctx, lz, '«rápido» no se puede probar; «menos de 2 s» sí', 420, 520, { tam: 21, peso: 800, color: L.tono(V, -0.3), ancho: 660 });
    }
  });
})();
