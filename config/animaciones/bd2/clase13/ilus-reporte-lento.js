/* Ilustracion: el reporte que tumba el servicio. Se programa cada minuto y cada ejecucion tarda
 * mas de un minuto: se apilan, ocupan las conexiones y la aplicacion se queda sin ninguna. El plan
 * de ejecucion delata la causa y dice el arreglo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-reporte-lento', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.rotulo(ctx, lz, 'Programado cada minuto, tarda más de un minuto', W / 2, 8, { tam: 24, peso: 800, color: A });
      // Linea de tiempo: minutos 0..5
      var x0 = 70, esc = 120;
      ctx.strokeStyle = L.tono(m.tinta, 0.4); ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(x0, 238); ctx.lineTo(x0 + 5.9 * esc, 238); ctx.stroke();
      for (var k = 0; k <= 5; k++) {
        ctx.beginPath(); ctx.moveTo(x0 + k * esc, 232); ctx.lineTo(x0 + k * esc, 244); ctx.stroke();
        UJ.rotulo(ctx, lz, 'min ' + k, x0 + k * esc, 248, { tam: 15, peso: 600 });
      }
      // Cada ejecucion empieza en su minuto y dura mas que la anterior (compiten entre si)
      var dura = [1.3, 1.7, 2.2, 2.8, 3.5, 4.3];
      for (var i = 0; i < 6; i++) {
        var xi = x0 + i * esc, fin = Math.min(x0 + 5.9 * esc, xi + dura[i] * esc), y = 50 + i * 30;
        L.rectRed(ctx, xi, y, fin - xi, 24, 6); L.rellena(ctx, L.tono(i < 2 ? A : R, 0.25 + 0.05 * (5 - i)));
        UJ.rotulo(ctx, lz, 'reporte ' + (i + 1), xi + 8, y + 3, { tam: 14, peso: 700, alinear: 'left', color: m.papel });
      }
      // Conexiones
      UJ.rotulo(ctx, lz, 'Minuto 5, hora pico: 3 reportes a la vez + la aplicación (esquema)', 30, 282, { tam: 18, peso: 800, color: A, alinear: 'left', ancho: 740 });
      for (var s = 0; s < 10; s++) {
        var sx = 30 + s * 74;
        L.rectRed(ctx, sx, 316, 64, 46, 8);
        L.rellena(ctx, s < 3 ? L.tono(R, 0.7) : L.tono(A, 0.75), s < 3 ? R : A, 2);
        UJ.rotulo(ctx, lz, s < 3 ? 'reporte' : 'app', sx + 32, 330, { tam: 14, peso: 700 });
      }
      UJ.rotulo(ctx, lz, 'Las 10 conexiones ocupadas: la siguiente petición de recepción no consigue ninguna.', 30, 374, { tam: 17, peso: 700, color: R, alinear: 'left', ancho: 690 });
      UJ.sello(ctx, lz, 752, 384, 18, false, 1);
      // Diagnostico y arreglo
      L.rectRed(ctx, 30, 420, 360, 196, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
      UJ.rotulo(ctx, lz, 'Lo que dice el plan', 210, 432, { tam: 20, peso: 800, color: L.tono(C, -0.35) });
      UJ.codigo(ctx, lz, 46, 470, 328, 'Seq Scan on cita', 1, 16);
      UJ.rotulo(ctx, lz, 'recorre la tabla entera para quedarse con pocas filas: falta un índice', 210, 518, { tam: 16, peso: 600, ancho: 330 });
      L.rectRed(ctx, 410, 420, 360, 196, 14); L.rellena(ctx, L.tono(V, 0.88), V, 2);
      UJ.rotulo(ctx, lz, 'La lección accionable', 590, 432, { tam: 20, peso: 800, color: L.tono(V, -0.3) });
      UJ.rotulo(ctx, lz, '1 · Pedir solo las columnas que se muestran (adiós SELECT *)', 590, 470, { tam: 16, peso: 600, ancho: 330 });
      UJ.rotulo(ctx, lz, '2 · Índice en el filtro, con EXPLAIN ANALYZE antes y después', 590, 540, { tam: 16, peso: 600, ancho: 330 });
    }
  });
})();
