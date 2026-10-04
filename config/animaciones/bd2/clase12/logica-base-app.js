/* Logica en la base o en la aplicacion: los dos platillos, con honestidad. A favor de la base:
 * una sola vez para todos, misma transaccion, menos viajes. En contra: mas dificil de probar,
 * ata al motor, CPU cara de escalar. Y el criterio para decidir: lo que protege la integridad de
 * los datos va en la base; la presentacion y la orquestacion, en la aplicacion. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('logica-base-app', {
    duracion: 5,
    // Pasos LOGICOS: 1) lo que pesa a favor de la base; 2) lo que pesa en contra (la balanza se
    // equilibra); 3) el criterio de decision.
    pasos: [0.36, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      // Balanza: se inclina con los pros y vuelve al equilibrio con los contras
      var inc = L.claves(t, [[0, 0], [0.3, 0.07, 'suave'], [0.4, 0.07], [0.68, 0, 'suave'], [1, 0]]);
      var cx = W / 2, cy = 70, brazo = 300;
      ctx.save(); ctx.translate(cx, cy); ctx.rotate(inc);
      L.trazo(ctx, [[-brazo, 0], [brazo, 0]], 1, m.tinta, 6);
      ctx.restore();
      L.trazo(ctx, [[cx, cy], [cx, cy + 46]], 1, m.tinta, 6);
      L.circulo(ctx, cx, cy, 9); L.rellena(ctx, m.tinta);
      var yi = cy - Math.sin(inc) * brazo, yd = cy + Math.sin(inc) * brazo;
      UJ.rotulo(ctx, lz, 'A favor de la base', cx - brazo + 60, yi + 12, { tam: 20, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'En contra', cx + brazo - 50, yd + 12, { tam: 20, peso: 800, color: R });
      var pro = ['la regla, una vez para todos los clientes', 'misma transacción: sin ventana', 'menos viajes de red'];
      var con = ['más difícil de probar y versionar', 'ata el proyecto al motor elegido', 'CPU de la base: la más cara de escalar'];
      for (var i = 0; i < 3; i++) UJ.caja(ctx, lz, 20, 140 + i * 96, 360, 84, '+', pro[i], V, L.tramo(t, 0.04 + i * 0.08, 0.11 + i * 0.08));
      for (var k = 0; k < 3; k++) UJ.caja(ctx, lz, 420, 140 + k * 96, 360, 84, '−', con[k], R, L.tramo(t, 0.4 + k * 0.08, 0.47 + k * 0.08));
      // 3 · El criterio
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.86), function () {
        L.rectRed(ctx, 20, 440, 760, 180, 16); L.rellena(ctx, L.tono(A, 0.92), A, 2);
        UJ.rotulo(ctx, lz, 'Criterio: lo que protege la integridad va en la base', W / 2, 456, { tam: 21, peso: 800, color: A, ancho: 720 });
        UJ.rotulo(ctx, lz, 'mascota inactiva no agenda · stock nunca negativo · auditoría', W / 2, 500, { tam: 18, peso: 700, color: V, ancho: 720 });
        UJ.rotulo(ctx, lz, 'presentación, orquestación, formatos y correos: en la aplicación', W / 2, 540, { tam: 18, ancho: 720 });
        UJ.rotulo(ctx, lz, 'Se pesan los dos lados; no se hace propaganda.', W / 2, 580, { tam: 16, color: L.tono(m.tinta, 0.25), ancho: 720 });
      });
    }
  });
})();
