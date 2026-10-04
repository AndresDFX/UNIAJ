/* RPO y RTO sobre una linea de tiempo: ultimo respaldo, la caida, y la base de vuelta. Lo que
 * se pierde es el RPO; lo que dura la caida es el RTO. Ejemplo de la clinica: 4 h de datos son
 * 15 a 20 citas; 8 h de caida un sabado es cerrar el dia. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('rpo-rto', {
    duracion: 5,
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', y = 230;
      var x0 = 50, x1 = W - 50, xr = 200, xc = 420, xv = 680;
      L.trazo(ctx, [[x0, y], [x1, y]], L.tramo(t, 0, 0.15), L.tono(m.tinta, 0.6), 5);
      function hito(x, nombre, color, a) {
        UJ.alfa(ctx, a, function () {
          L.circulo(ctx, x, y, 14); L.rellena(ctx, color, m.papel, 3);
          UJ.rotulo(ctx, lz, nombre, x, y + 26, { tam: 18, peso: 700, color: color, ancho: 170 });
        });
      }
      hito(xr, 'último respaldo', A, L.tramo(t, 0.12, 0.2));
      hito(xc, 'la base se cae', R, L.tramo(t, 0.26, 0.32));
      UJ.rayo(ctx, xc - 22, y - 110, 70, R, L.tramo(t, 0.26, 0.32));
      hito(xv, 'la base vuelve', m.verde || A, L.tramo(t, 0.58, 0.64));
      // RPO
      var p = L.tramo(t, 0.34, 0.5, 'suave');
      if (p > 0) {
        L.rectRed(ctx, xr, y - 60, (xc - xr) * p, 34, 6); L.rellena(ctx, L.tono(R, 0.7));
        UJ.rotulo(ctx, lz, 'RPO · datos perdidos', (xr + xc) / 2, y - 54, { tam: 17, peso: 800, color: R, visible: L.tramo(t, 0.46, 0.52) });
      }
      // RTO
      var q = L.tramo(t, 0.5, 0.66, 'suave');
      if (q > 0) {
        L.rectRed(ctx, xc, y - 100, (xv - xc) * q, 34, 6); L.rellena(ctx, L.tono(C, 0.6));
        UJ.rotulo(ctx, lz, 'RTO · tiempo caída', (xc + xv) / 2, y - 94, { tam: 17, peso: 800, color: L.tono(C, -0.3), visible: L.tramo(t, 0.62, 0.68) });
      }
      UJ.alfa(ctx, L.tramo(t, 0.72, 0.82), function () {
        L.rectRed(ctx, 40, 360, 345, 130, 14); L.rellena(ctx, L.tono(R, 0.9), R, 2);
        UJ.rotulo(ctx, lz, 'RPO = 4 h', 212, 376, { tam: 26, peso: 800, color: R });
        UJ.rotulo(ctx, lz, '≈ 15 a 20 citas sin registro', 212, 420, { tam: 18, ancho: 320 });
        L.rectRed(ctx, 415, 360, 345, 130, 14); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'RTO = 8 h', 587, 376, { tam: 26, peso: 800, color: L.tono(C, -0.3) });
        UJ.rotulo(ctx, lz, 'un sábado: cerrar el día', 587, 420, { tam: 18, ancho: 320 });
      });
      UJ.rotulo(ctx, lz, 'El número lo acuerda el dueño del negocio.', W / 2, 540, { tam: 22, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
