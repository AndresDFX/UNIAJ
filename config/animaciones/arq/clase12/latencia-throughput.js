/* Latencia (cuanto tarda UNA peticion), throughput (cuantas por segundo) y concurrencia (cuantas
 * estan dentro a la vez) se unen en una identidad: concurrencia = throughput x latencia.
 * 5 RPS x 0,3 s = 1,5 peticiones simultaneas en promedio. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('latencia-throughput', {
    duracion: 5,
    // Pasos LOGICOS: 1) la latencia, 2) el throughput, 3) la concurrencia y la identidad que las
    // une, con el ejemplo de 5 RPS x 0,3 s, 4) la advertencia: latencia y throughput no se mueven
    // juntas. Antes el paso 3 juntaba tres ideas y la bolita de la animacion quedaba en el borde.
    pasos: [0.22, 0.44, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca;
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 240, h: 130, t: 'Latencia', s: 'cuánto tarda UNA petición', en: 0.02 },
        { tipo: 'caja', x: 280, y: 30, w: 240, h: 130, t: 'Throughput', s: 'cuántas atiende por segundo', color: 'acento', en: 0.24 },
        { tipo: 'caja', x: 540, y: 30, w: 240, h: 130, t: 'Concurrencia', s: 'cuántas hay dentro a la vez', color: 'malva', en: 0.46 },
        { tipo: 'texto', t: 'concurrencia = throughput × latencia', x: 400, y: 200, tam: 28, peso: 800, color: 'accion', ancho: 760, en: 0.52 },
        { tipo: 'texto', t: '5 RPS × 0,3 s = 1,5 peticiones dentro del sistema', x: 400, y: 262, tam: 24, ancho: 760, en: 0.58 },
        { tipo: 'flecha', de: [140, 410], a: [244, 410], r: '5 por s', dy: -32, color: 'accion', en: 0.6 },
        { tipo: 'flecha', de: [556, 410], a: [660, 410], r: 'salen', dy: -32, color: 'accion', en: 0.6 },
        { tipo: 'texto', t: 'No se mueven juntas: 500 RPS con latencia terrible es posible si todo espera en cola.', x: 400, y: 520, tam: 21, ancho: 740, color: 'malva', en: 0.86 }
      ]);
      // Peticiones que entran, pasan 0,3 s dentro y salen: en cada instante hay una o dos dentro.
      var a = L.tramo(t, 0.6, 0.68);
      if (a > 0) UJ.alfa(ctx, a, function () {
        L.rectRed(ctx, 250, 340, 300, 120, 14); L.rellena(ctx, L.tono(m.accion, 0.9), m.accion, 3);
        UJ.rotulo(ctx, lz, 'sistema · cada una dura 0,3 s', 400, 352, { tam: 17, color: m.accion });
        var fase = L.tramo(t, 0.6, 0.78);
        for (var k = 0; k < 4; k++) {
          var x = 120 + fase * 400 - k * 150;
          if (x >= 266 && x <= 534) { L.circulo(ctx, x, 418, 12); L.rellena(ctx, m.malva || m.acento); }
        }
      });
    }
  });
})();
