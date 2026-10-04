/* Latencia (cuanto tarda UNA peticion), throughput (cuantas por segundo) y concurrencia (cuantas
 * estan dentro a la vez) se unen en una identidad: concurrencia = throughput x latencia.
 * 5 RPS x 0,3 s = 1,5 peticiones simultaneas en promedio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('latencia-throughput', {
    duracion: 5,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca;
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 240, h: 130, t: 'Latencia', s: 'cuánto tarda UNA petición', en: 0.02 },
        { tipo: 'caja', x: 280, y: 30, w: 240, h: 130, t: 'Throughput', s: 'cuántas atiende por segundo', color: 'acento', en: 0.3 },
        { tipo: 'caja', x: 540, y: 30, w: 240, h: 130, t: 'Concurrencia', s: 'cuántas hay dentro a la vez', color: 'malva', en: 0.6 },
        { tipo: 'texto', t: 'concurrencia = throughput × latencia', x: 400, y: 210, tam: 28, peso: 800, color: 'accion', ancho: 760, en: 0.66 },
        { tipo: 'texto', t: '5 RPS × 0,3 s = 1,5 peticiones dentro del sistema', x: 400, y: 275, tam: 24, ancho: 760, en: 0.74 },
        { tipo: 'texto', t: 'No se mueven juntas: 500 RPS con latencia terrible es posible si todo espera en cola.', x: 400, y: 520, tam: 21, ancho: 740, color: 'malva', en: 0.9 }
      ]);
      // Peticiones que entran, cruzan el sistema en 0,3 s y salen: siempre hay una o dos dentro.
      var a = L.tramo(t, 0.76, 0.84);
      if (a > 0) UJ.alfa(ctx, a, function () {
        L.rectRed(ctx, 250, 350, 300, 110, 14); L.rellena(ctx, L.tono(m.accion, 0.9), m.accion, 3);
        UJ.rotulo(ctx, lz, 'sistema', 400, 365, { tam: 18, color: m.accion });
        var fase = L.tramo(t, 0.76, 1);
        for (var k = 0; k < 4; k++) {
          var x = 200 + ((fase * 2.2 + k * 0.33) % 1.3) * 400;
          if (x > 180 && x < 620) { L.circulo(ctx, x, 420, 12); L.rellena(ctx, m.malva || m.acento); }
        }
      });
    }
  });
})();
