/* Error de integracion: dos instancias del servicio; se registra en una y se guarda la otra. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('dos-instancias', {
    duracion: 4.5,
    pasos: [0.3, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, W = lz.ancho;
      UJ.caja(ctx, lz, 40, 30, 300, 80, 'main', 'new ServicioClinica()', A, L.tramo(t, 0, 0.1));
      UJ.caja(ctx, lz, 460, 30, 300, 80, 'Ventana', 'new ServicioClinica()', C, L.tramo(t, 0.08, 0.18));
      function servicio(x, nombre, c, lista, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, 170, 300, 120, 14); L.rellena(ctx, L.tono(c, 0.9), c, 3);
          UJ.rotulo(ctx, lz, nombre, x + 150, 184, { tam: 21, peso: 800, color: L.tono(c, -0.3) });
          UJ.rotulo(ctx, lz, lista, x + 150, 232, { tam: 20, ancho: 270, letra: 'Consolas, monospace' });
        });
      }
      var reg = L.tramo(t, 0.36, 0.44);
      servicio(40, 'servicio A', A, 'lista: [ ]', L.tramo(t, 0.04, 0.14));
      servicio(460, 'servicio B', C, reg >= 1 ? 'lista: [Luna]' : 'lista: [ ]', L.tramo(t, 0.12, 0.22));
      var f1 = L.tramo(t, 0.1, 0.2), f2 = L.tramo(t, 0.18, 0.26);
      if (f1 > 0) L.flecha(ctx, 190, 112, 190, 166, A, 4, f1);
      if (f2 > 0) L.flecha(ctx, 610, 112, 610, 166, C, 4, f2);
      UJ.rotulo(ctx, lz, 'dos objetos distintos', W / 2, 220, { tam: 18, peso: 700, color: R, ancho: 110, visible: L.tramo(t, 0.2, 0.28) });
      UJ.rotulo(ctx, lz, 'clic «Registrar Luna» → B', 610, 304, { tam: 18, peso: 700, color: C, visible: L.tramo(t, 0.34, 0.42) });
      UJ.rotulo(ctx, lz, 'al cerrar: A.guardar()', 190, 304, { tam: 18, peso: 700, color: A, visible: L.tramo(t, 0.46, 0.52) });
      var g = L.tramo(t, 0.5, 0.6);
      if (g > 0) L.flecha(ctx, 190, 334, 320, 420, A, 4, g);
      UJ.alfa(ctx, L.tramo(t, 0.58, 0.64), function () {
        L.rectRed(ctx, 300, 420, 200, 70, 10); L.rellena(ctx, L.tono(m.tinta, 0.9), m.tinta, 2);
        UJ.rotulo(ctx, lz, 'mascotas.csv', 400, 428, { tam: 19, peso: 700 });
        UJ.rotulo(ctx, lz, 'igual: sin Luna', 400, 458, { tam: 18, color: R, peso: 700 });
      });
      UJ.sello(ctx, lz, 540, 455, 24, false, L.tramo(t, 0.62, 0.68));
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.9), function () {
        UJ.rotulo(ctx, lz, 'Síntoma: «registra, pero el archivo no cambia».', W / 2, 520, { tam: 20, peso: 700, ancho: W - 40 });
        UJ.rotulo(ctx, lz, 'Una sola instancia: se crea en el main y se pasa a la ventana.', W / 2, 560, { tam: 19, ancho: W - 40, color: m.verde });
      });
    }
  });
})();
