/* Refactorizar: un manejador de 90 lineas se parte en validar, generarId, aLineaCsv y
 * escribirArchivo. Con los mismos datos, la salida antes y despues es la misma. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('refactor-misma-salida', {
    duracion: 4.8,
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, G = m.gris, W = lz.ancho;
      var partes = ['validar()', 'generarId()', 'aLineaCsv()', 'escribirArchivo()'];
      var colores = [A, C, m.malva, V];
      var abre = L.tramo(t, 0.38, 0.54, 'suave');
      // Titulo de la columna izquierda
      UJ.rotulo(ctx, lz, abre < 0.5 ? 'registrarMascota() · 90 líneas' : 'registrarMascota() llama a:', 200, 20, { tam: 20, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      // El bloque: cuatro tramos pegados que se separan
      UJ.alfa(ctx, L.tramo(t, 0.02, 0.1), function () {
        for (var i = 0; i < 4; i++) {
          var y = 60 + i * L.mezcla(110, 120, abre), al = L.mezcla(110, 100, abre);
          L.rectRed(ctx, 30, y, 340, al, abre > 0.05 ? 12 : 2);
          L.rellena(ctx, L.tono(abre > 0.05 ? colores[i] : G, 0.88), L.tono(abre > 0.05 ? colores[i] : G, -0.1 * abre), 2);
          // lineas de codigo apretadas
          UJ.alfa(ctx, 1 - abre, function () {
            for (var k = 0; k < 8; k++) {
              L.rectRed(ctx, 46 + (k % 3) * 14, y + 10 + k * 12, 200 + ((k * 37 + i * 53) % 90), 6, 3);
              L.rellena(ctx, L.tono(G, 0.3));
            }
          });
          UJ.alfa(ctx, abre, function () {
            L.texto(ctx, partes[i], 200, y + al / 2 - 14, { tam: 24, peso: 700, color: colores[i], alinear: 'center', letra: 'Consolas, monospace' });
          });
        }
      });
      // Salida antes
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.22), function () {
        UJ.rotulo(ctx, lz, 'Salida antes', 590, 60, { tam: 20, peso: 800, color: G });
        UJ.codigo(ctx, lz, 410, 96, 370, 'Mascota registrada con ID M004', 1, 16);
      });
      UJ.alfa(ctx, 1 - abre, function () { UJ.rotulo(ctx, lz, 'Método largo: todo en un solo bloque.', 590, 160, { tam: 18, peso: 600, ancho: 360, visible: L.tramo(t, 0.22, 0.3) }); });
      // Paso 2
      UJ.rotulo(ctx, lz, 'Misma conducta, mejor forma:', 590, 230, { tam: 20, peso: 800, color: A, ancho: 360, visible: L.tramo(t, 0.54, 0.6) });
      UJ.rotulo(ctx, lz, 'cada método hace una sola cosa.', 590, 260, { tam: 18, peso: 600, ancho: 360, visible: L.tramo(t, 0.56, 0.62) });
      // Paso 3: salida despues
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.78), function () {
        UJ.rotulo(ctx, lz, 'Salida después', 590, 330, { tam: 20, peso: 800, color: V });
        UJ.codigo(ctx, lz, 410, 366, 370, 'Mascota registrada con ID M004', 1, 16);
      });
      UJ.sello(ctx, lz, 590, 452, 28, true, L.tramo(t, 0.78, 0.86));
      UJ.rotulo(ctx, lz, 'Mismos datos → mismas salidas', 590, 494, { tam: 20, peso: 800, color: V, ancho: 360, visible: L.tramo(t, 0.84, 0.9) });
      UJ.rotulo(ctx, lz, 'No es agregar funciones, corregir lógica ni reescribir desde cero.', W / 2, 560, { tam: 18, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.9, 0.98) });
    }
  });
})();
