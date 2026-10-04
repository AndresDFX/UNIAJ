/* Persistencia: la lista en RAM se evapora al cerrar; persistir es convertir cada objeto en una
 * linea CSV y escribirla en un archivo, que sobrevive al cierre y se vuelve a cargar. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ram-a-disco', {
    duracion: 4.8,
    pasos: [0.32, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, G = m.gris, S = m.sello, W = lz.ancho;
      var nombres = ['Luna', 'Michi', 'Rocky'];
      function ram(x, y, an, al, titulo, color) {
        L.rectRed(ctx, x, y, an, al, 14); L.rellena(ctx, L.tono(color, 0.92), color, 3);
        UJ.rotulo(ctx, lz, titulo, x + an / 2, y + 10, { tam: 18, peso: 800, color: color });
      }
      function ficha(x, y, nombre, color, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, x, y, 92, 44, 10); L.rellena(ctx, m.papel, color, 2);
          UJ.rotulo(ctx, lz, nombre, x + 46, y + 11, { tam: 18, peso: 700, color: color });
        });
      }
      // Paso 1: sin persistir, se evapora
      UJ.rotulo(ctx, lz, 'Sin persistir', 20, 18, { tam: 22, peso: 800, alinear: 'left', color: R, visible: L.tramo(t, 0, 0.05) });
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () { ram(20, 56, 340, 120, 'RAM · lista de mascotas', A); });
      var evap = L.tramo(t, 0.14, 0.26, 'suave');
      for (var i = 0; i < 3; i++) ficha(34 + i * 108, 104 - evap * 40, nombres[i], A, L.tramo(t, 0.03, 0.08) * (1 - evap));
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.14), function () {
        L.rectRed(ctx, 400, 70, 160, 50, 10); L.rellena(ctx, L.tono(R, 0.85), R, 2);
        UJ.rotulo(ctx, lz, 'cerrar ventana', 480, 84, { tam: 17, peso: 700, color: R });
      });
      UJ.rotulo(ctx, lz, '(vacía)', 190, 116, { tam: 20, peso: 600, color: L.tono(m.tinta, 0.4), visible: L.tramo(t, 0.24, 0.28) });
      UJ.rotulo(ctx, lz, 'Al cerrar, las mascotas se evaporan.', 400, 140, { tam: 18, peso: 700, alinear: 'left', color: R, ancho: 380, visible: L.tramo(t, 0.24, 0.3) });
      // Paso 2: cada objeto -> linea CSV -> archivo
      var y2 = 230;
      UJ.rotulo(ctx, lz, 'Persistiendo', 20, y2 - 34, { tam: 22, peso: 800, alinear: 'left', color: V, visible: L.tramo(t, 0.36, 0.4) });
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.42), function () {
        ram(20, y2, 140, 200, 'RAM', A);
        L.rectRed(ctx, 300, y2, 480, 200, 14); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.3), 3);
        UJ.rotulo(ctx, lz, 'mascotas.csv (ejemplo)', 540, y2 + 10, { tam: 18, peso: 800 });
        L.texto(ctx, 'id;nombre;especie;edad;cedula_dueno', 316, y2 + 44, { tam: 15, peso: 700, color: L.tono(m.tinta, 0.35), letra: 'Consolas, monospace' });
      });
      var csv = ['M001;Luna;perro;3;1144556677', 'M002;Michi;gato;2;1144556677', 'M003;Rocky;perro;5;1133224455'];
      for (var k = 0; k < 3; k++) {
        var a = L.tramo(t, 0.42 + k * 0.06, 0.48 + k * 0.06);
        ficha(44, y2 + 40 + k * 52, nombres[k], A, L.tramo(t, 0.38, 0.42));
        L.flecha(ctx, 140, y2 + 62 + k * 52, 300, y2 + 84 + k * 36, C, 3, a);
        L.texto(ctx, csv[k], 316, y2 + 74 + k * 36, { tam: 15, peso: 500, color: m.tinta, letra: 'Consolas, monospace', visible: a });
      }
      UJ.rotulo(ctx, lz, 'guardar(): una línea por objeto', 165, y2 + 210, { tam: 17, peso: 700, alinear: 'left', color: C, visible: L.tramo(t, 0.58, 0.64) });
      // Paso 3: el archivo sobrevive y se vuelve a cargar
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.76), function () {
        L.rectRed(ctx, 20, 500, 760, 120, 14); L.rellena(ctx, L.tono(V, 0.9), V, 3);
        UJ.rotulo(ctx, lz, 'Se cierra y se vuelve a abrir:', 40, 514, { tam: 19, peso: 800, alinear: 'left', color: V });
        UJ.rotulo(ctx, lz, 'el archivo sigue en disco', 40, 544, { tam: 18, peso: 600, alinear: 'left' });
        UJ.rotulo(ctx, lz, 'cargar(): línea → objeto', 40, 576, { tam: 18, peso: 700, alinear: 'left', color: C });
      });
      UJ.sello(ctx, lz, 330, 560, 26, true, L.tramo(t, 0.76, 0.84));
      for (var j = 0; j < 3; j++) ficha(400 + j * 124, 538, nombres[j], V, L.tramo(t, 0.82 + j * 0.04, 0.88 + j * 0.04));
    }
  });
})();
