/* La especificacion textual en pares actor-sistema: pasos numerados que alternan, y los flujos
 * alternos que salen de un paso concreto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('pares-responsabilidad', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.5, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'CU-02 Buscar expediente', W / 2, 18, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      UJ.alfa(ctx, L.tramo(t, 0.03, 0.09), function () {
        L.rectRed(ctx, 40, 66, 350, 40, 10); L.rellena(ctx, A);
        UJ.rotulo(ctx, lz, 'Actor', 215, 74, { tam: 20, peso: 800, color: m.papel });
        L.rectRed(ctx, 410, 66, 350, 40, 10); L.rellena(ctx, C);
        UJ.rotulo(ctx, lz, 'Sistema', 585, 74, { tam: 20, peso: 800, color: m.papel });
      });
      var pasos = ['1. Digita código o nombre', '2. Devuelve las coincidencias', '3. Selecciona una mascota', '4. Muestra ficha e historial'];
      for (var i = 0; i < 4; i++) {
        var izq = i % 2 === 0, x = izq ? 40 : 410, y = 124 + i * 62, c = izq ? A : C;
        var a = L.tramo(t, 0.1 + i * 0.08, 0.16 + i * 0.08);
        (function (x, y, c, txt) {
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, x, y, 350, 48, 10); L.rellena(ctx, L.tono(c, 0.88), c, 2);
            UJ.rotulo(ctx, lz, txt, x + 16, y + 13, { tam: 19, peso: 600, alinear: 'left', ancho: 320 });
          });
        })(x, y, c, pasos[i]);
        if (i > 0) {
          var px = izq ? 410 : 390, qx = izq ? 390 : 410;
          UJ.flecha(ctx, lz, px, y - 62 + 34, qx, y + 14, m.gris, L.tramo(t, 0.08 + i * 0.08, 0.13 + i * 0.08), null, { grosor: 2 });
        }
      }
      // Ramas alternas del paso 2
      var yR = 400;
      UJ.alfa(ctx, L.tramo(t, 0.52, 0.58), function () {
        UJ.rotulo(ctx, lz, 'Flujos alternos del paso 2', 585, yR - 34, { tam: 18, peso: 700, color: m.malva });
      });
      UJ.linea(ctx, 770, 210, 770, yR + 92, m.malva, 2, L.tramo(t, 0.54, 0.62), true);
      var ramas = ['2a. Sin coincidencias: ofrece registrar', '2b. Más de 50: pagina los resultados'];
      for (var k = 0; k < 2; k++) {
        (function (k) {
          var y = yR + k * 62;
          UJ.alfa(ctx, L.tramo(t, 0.6 + k * 0.08, 0.66 + k * 0.08), function () {
            L.rectRed(ctx, 300, y, 456, 46, 10); L.rellena(ctx, L.tono(m.malva, 0.9), m.malva, 2);
            UJ.rotulo(ctx, lz, ramas[k], 316, y + 12, { tam: 19, peso: 600, alinear: 'left', ancho: 430 });
          });
        })(k);
      }
      UJ.rotulo(ctx, lz, 'Pasos numerados, sin adjetivos', W / 2, 560,
        { tam: 23, peso: 700, color: A, ancho: W - 40, visible: L.tramo(t, 0.86, 0.98) });
    }
  });
})();
