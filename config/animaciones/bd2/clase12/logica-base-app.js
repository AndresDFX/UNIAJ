/* Logica en la base o en la aplicacion: los dos platillos, con honestidad. A favor: una sola vez
 * para todos, misma transaccion, menos viajes. En contra: mas dificil de probar, CPU cara. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('logica-base-app', {
    duracion: 4.8,
    pasos: [0.4, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // Balanza
      var inc = L.claves(t, [[0, 0], [0.36, 0.08, 'suave'], [0.76, -0.04, 'suave'], [0.84, 0, 'suave']]);
      var cx = W / 2, cy = 90, brazo = 300;
      ctx.save(); ctx.translate(cx, cy); ctx.rotate(inc);
      L.trazo(ctx, [[-brazo, 0], [brazo, 0]], 1, m.tinta, 6);
      ctx.restore();
      L.trazo(ctx, [[cx, cy], [cx, cy + 50]], 1, m.tinta, 6);
      L.circulo(ctx, cx, cy, 9); L.rellena(ctx, m.tinta);
      var yi = cy - Math.sin(inc) * brazo, yd = cy + Math.sin(inc) * brazo;
      UJ.rotulo(ctx, lz, 'A favor de la base', cx - brazo + 40, yi + 12, { tam: 21, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'En contra', cx + brazo - 40, yd + 12, { tam: 21, peso: 800, color: R });
      var pro = ['la regla, una vez para todos los clientes', 'misma transacción: sin ventana entre validar y escribir', 'menos viajes de red'];
      var con = ['más difícil de probar automáticamente', 'la CPU de la base: el recurso más caro de escalar'];
      for (var i = 0; i < 3; i++) UJ.caja(ctx, lz, 20, 170 + i * 112, 360, 96, '+', pro[i], V, L.tramo(t, 0.06 + i * 0.1, 0.14 + i * 0.1));
      for (var k = 0; k < 2; k++) UJ.caja(ctx, lz, 420, 170 + k * 112, 360, 96, '−', con[k], R, L.tramo(t, 0.44 + k * 0.14, 0.52 + k * 0.14));
      UJ.rotulo(ctx, lz, 'Se pesan los dos lados, no se hace propaganda.', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.84, 1) });
    }
  });
})();
