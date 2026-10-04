/* Que es una transaccion: varias sentencias que describen UN hecho de negocio, tratadas como
 * indivisibles frente a dos amenazas: la falla (no puede quedar a medias) y las demas sesiones
 * (nadie ve el estado intermedio). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('transaccion-unidad', {
    duracion: 4.8,
    // Pasos LOGICOS: 1) la transaccion como un solo hecho de negocio; 2) amenaza 1, la falla;
    // 3) amenaza 2, las otras sesiones; 4) donde empieza y termina en cada motor.
    pasos: [0.4, 0.6, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      // El bloque de la transaccion
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, 30, 40, 450, 360, 18); L.rellena(ctx, L.tono(A, 0.94), A, 3);
        UJ.rotulo(ctx, lz, 'Una transacción', 255, 54, { tam: 24, peso: 800, color: A });
      });
      UJ.codigo(ctx, lz, 50, 100, 410, 'BEGIN', L.tramo(t, 0.06, 0.1), 18);
      var lineas = ['INSERT INTO factura ...', 'INSERT INTO detalle_factura ...', 'UPDATE insumo SET stock = ...'];
      for (var i = 0; i < 3; i++) {
        var a = L.tramo(t, 0.1 + i * 0.07, 0.16 + i * 0.07);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 70, 152 + i * 52, 390, 40, 8); L.rellena(ctx, lz.marca.papel, L.tono(A, 0.5), 2);
          L.texto(ctx, lineas[i], 84, 162 + i * 52, { tam: 17, peso: 600, color: m.tinta, letra: 'Consolas, monospace', ancho: 370 });
        });
      }
      UJ.codigo(ctx, lz, 50, 312, 410, 'COMMIT;   -- o ROLLBACK;', L.tramo(t, 0.3, 0.34), 18);
      UJ.rotulo(ctx, lz, 'un solo hecho de negocio', 255, 362, { tam: 19, peso: 700, color: C, visible: L.tramo(t, 0.34, 0.38) });
      // Amenaza 1: la falla
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.52), function () {
        L.rectRed(ctx, 505, 40, 270, 170, 16); L.rellena(ctx, L.tono(R, 0.92), R, 2);
        UJ.rotulo(ctx, lz, 'Amenaza 1: la falla', 640, 54, { tam: 20, peso: 800, color: R, ancho: 250 });
        UJ.rotulo(ctx, lz, 'no puede quedar aplicada a medias', 640, 130, { tam: 18, ancho: 240 });
      });
      UJ.rayo(ctx, 620, 84, 42, R, L.tramo(t, 0.48, 0.56));
      // Amenaza 2: las otras sesiones
      UJ.alfa(ctx, L.tramo(t, 0.64, 0.72), function () {
        L.rectRed(ctx, 505, 230, 270, 170, 16); L.rellena(ctx, L.tono(C, 0.9), C, 2);
        UJ.rotulo(ctx, lz, 'Amenaza 2: otras sesiones', 640, 244, { tam: 20, peso: 800, color: L.tono(C, -0.35), ancho: 250 });
        UJ.rotulo(ctx, lz, 'nadie ve el estado intermedio', 640, 320, { tam: 18, ancho: 240 });
      });
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.76), function () {
        ctx.save(); ctx.setLineDash([10, 8]);
        L.trazo(ctx, [[505, 305], [482, 305]], 1, L.tono(C, -0.2), 3); ctx.restore();
      });
      // Donde empieza
      UJ.alfa(ctx, L.tramo(t, 0.84, 0.94), function () {
        L.rectRed(ctx, 30, 430, 745, 150, 16); L.rellena(ctx, L.tono(m.tinta, 0.94), L.tono(m.tinta, 0.6), 2);
        UJ.rotulo(ctx, lz, 'PostgreSQL sin BEGIN: cada sentencia es su propia transacción y se confirma sola.', 402, 450, { tam: 19, ancho: 700 });
        UJ.rotulo(ctx, lz, 'Oracle: empieza sola con la primera DML; termina con COMMIT o ROLLBACK.', 402, 520, { tam: 19, ancho: 700 });
      });
    }
  });
})();
