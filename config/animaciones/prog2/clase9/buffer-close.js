/* Cerrar el recurso: write() llena el buffer en memoria; sin close() el archivo queda en 0 bytes
 * aunque el programa diga «guardado»; con try-with-resources el buffer baja al disco. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('buffer-close', {
    duracion: 4.8,
    pasos: [0.32, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, G = m.gris, S = m.sello, W = lz.ancho;
      function fila(y, titulo, color, a) {
        UJ.alfa(ctx, a, function () {
          UJ.rotulo(ctx, lz, titulo, 20, y, { tam: 21, peso: 800, alinear: 'left', color: color });
          UJ.caja(ctx, lz, 20, y + 40, 170, 100, 'Programa', 'write() × 3', A);
          L.rectRed(ctx, 240, y + 40, 260, 100, 12); L.rellena(ctx, L.tono(S, 0.85), L.tono(S, -0.35), 2);
          UJ.rotulo(ctx, lz, 'buffer (memoria)', 370, y + 46, { tam: 17, peso: 700 });
          L.flecha(ctx, 194, y + 90, 236, y + 90, A, 3);
        });
      }
      function lleno(y, n, a) {
        for (var i = 0; i < 3; i++) {
          var f = L.limitar(n - i, 0, 1) * a;
          UJ.alfa(ctx, f, function () { L.rectRed(ctx, 256 + i * 80, y + 76, 68, 48, 6); L.rellena(ctx, L.tono(A, 0.75), A, 2);
            UJ.rotulo(ctx, lz, 'línea', 290 + i * 80, y + 90, { tam: 15, peso: 700, color: A }); });
        }
      }
      function disco(y, bytes, color) {
        L.rectRed(ctx, 560, y + 40, 220, 100, 12); L.rellena(ctx, L.tono(color, 0.9), color, 3);
        UJ.rotulo(ctx, lz, 'mascotas.csv (disco)', 670, y + 50, { tam: 16, peso: 700 });
        UJ.rotulo(ctx, lz, bytes + ' bytes' + (bytes ? ' (ej.)' : ''), 670, y + 80, { tam: 26, peso: 800, color: color });
      }
      // Fila 1: sin close()
      var y1 = 14;
      fila(y1, 'Sin close()', R, L.tramo(t, 0, 0.06));
      var pierde = L.tramo(t, 0.4, 0.5);
      lleno(y1, L.tramo(t, 0.08, 0.26) * 3, 1 - pierde);
      UJ.alfa(ctx, L.tramo(t, 0.04, 0.08), function () { disco(y1, 0, R); });
      UJ.rotulo(ctx, lz, 'write() llena el buffer; el disco aún no recibe nada.', W / 2, y1 + 152, { tam: 18, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.22, 0.3) });
      // Paso 2: el programa termina sin cerrar
      UJ.alfa(ctx, pierde, function () {
        UJ.rotulo(ctx, lz, 'se pierde al terminar', 370, y1 + 96, { tam: 18, peso: 800, color: R });
      });
      UJ.alfa(ctx, L.tramo(t, 0.46, 0.52), function () {
        UJ.codigo(ctx, lz, 20, y1 + 190, 330, 'Consola: «guardado»', 1, 16);
      });
      UJ.sello(ctx, lz, 400, y1 + 206, 24, false, L.tramo(t, 0.5, 0.56));
      UJ.rotulo(ctx, lz, 'pero el archivo quedó en 0 bytes', 440, y1 + 194, { tam: 18, peso: 700, alinear: 'left', color: R, visible: L.tramo(t, 0.54, 0.62) });
      // Fila 2: con try-with-resources
      var y2 = 270;
      UJ.alfa(ctx, L.tramo(t, 0.68, 0.72), function () {
        UJ.codigo(ctx, lz, 20, y2 - 6, W - 40, 'try (BufferedWriter s = Files.newBufferedWriter(ruta, UTF_8)) { ... }', 1, 15);
      });
      fila(y2 + 40, 'Con try-with-resources', V, L.tramo(t, 0.68, 0.72));
      var baja = L.tramo(t, 0.8, 0.9);
      lleno(y2 + 40, L.tramo(t, 0.72, 0.8) * 3, 1 - baja);
      for (var k = 0; k < 3; k++) {
        var x = L.mezcla(256 + k * 80, 600 + k * 50, baja);
        if (baja > 0 && baja < 1) UJ.alfa(ctx, 1, function () { L.rectRed(ctx, x, y2 + 40 + 76, 40, 30, 6); L.rellena(ctx, L.tono(A, 0.75), A, 2); });
      }
      UJ.alfa(ctx, L.tramo(t, 0.68, 0.72), function () {
        disco(y2 + 40, Math.round(90 * baja), baja >= 1 ? V : G);
      });
      UJ.rotulo(ctx, lz, 'al salir del try se llama close(): el buffer baja al disco', W / 2, y2 + 200, { tam: 18, peso: 700, color: V, ancho: W - 40, visible: L.tramo(t, 0.86, 0.92) });
      UJ.sello(ctx, lz, 670, y2 + 250, 24, true, L.tramo(t, 0.88, 0.94));
      UJ.rotulo(ctx, lz, 'IOException es checked: el compilador obliga a atenderla.', W / 2, 590, { tam: 18, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.92, 0.99) });
    }
  });
})();
