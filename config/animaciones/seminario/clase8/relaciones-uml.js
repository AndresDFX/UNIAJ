/* Las líneas entre clases: asociación con multiplicidades y su leyenda, y luego composición,
 * agregación y herencia, cada una con lo que significa. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('relaciones-uml', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.55, 0.78, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, T = m.tinta, W = lz.ancho;
      function rombo(x, y, lleno, a) {   // x = punta que toca la clase (a la izquierda)
        UJ.alfa(ctx, a, function () {
          ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + 14, y - 9); ctx.lineTo(x + 28, y); ctx.lineTo(x + 14, y + 9); ctx.closePath();
          L.rellena(ctx, lleno ? T : m.papel, T, 2.5);
        });
      }
      function nota(txt, y, a) {
        UJ.alfa(ctx, a, function () { L.texto(ctx, txt, 596, y, { tam: 18, peso: 700, color: L.tono(m.sello, -0.4), ancho: 190, letra: lz.letra }); });
      }
      // Asociacion
      var a1 = L.tramo(t, 0.02, 0.12);
      UJ.caja(ctx, lz, 60, 30, 180, 56, 'Dueño', null, A, a1);
      UJ.caja(ctx, lz, 560, 30, 180, 56, 'Mascota', null, A, a1);
      UJ.linea(ctx, 240, 58, 560, 58, T, 3, L.tramo(t, 0.1, 0.18));
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.22), function () {
        UJ.rotulo(ctx, lz, '1', 256, 64, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, '0..*', 526, 64, { tam: 22, peso: 800, color: R });
        UJ.rotulo(ctx, lz, 'tiene ▸', 400, 66, { tam: 18, peso: 600, color: m.gris });
      });
      var ley = ['1 exactamente uno', '0..1 opcional', '1..* uno o más', '0..* cero o más'];
      var ws = 0, gap = 12, anchos = [];
      for (var i = 0; i < 4; i++) { anchos[i] = UJ.medir(ctx, lz, ley[i], 17, 700) + 28; ws += anchos[i]; }
      var px = (W - ws - 3 * gap) / 2;
      for (var j = 0; j < 4; j++) {
        UJ.pildora(ctx, lz, px, 120, ley[j], A, L.tramo(t, 0.2 + j * 0.02, 0.24 + j * 0.02), { tam: 17 });
        px += anchos[j] + gap;
      }
      // Composicion
      var c = L.tramo(t, 0.32, 0.42);
      UJ.caja(ctx, lz, 40, 196, 170, 54, 'Mascota', null, A, c);
      UJ.caja(ctx, lz, 400, 196, 170, 54, 'Atención', null, A, c);
      UJ.alfa(ctx, c, function () {
        UJ.linea(ctx, 238, 223, 400, 223, T, 3);
        UJ.rotulo(ctx, lz, 'composición', 318, 192, { tam: 17, peso: 700, color: m.gris });
      });
      rombo(210, 223, true, c);
      nota('no vive sin la mascota', 204, L.tramo(t, 0.42, 0.5));
      // Agregacion
      var g = L.tramo(t, 0.58, 0.66);
      UJ.caja(ctx, lz, 40, 296, 170, 54, 'Sede', null, A, g);
      UJ.caja(ctx, lz, 400, 296, 170, 54, 'Veterinario', null, A, g);
      UJ.alfa(ctx, g, function () {
        UJ.linea(ctx, 238, 323, 400, 323, T, 3);
        UJ.rotulo(ctx, lz, 'agregación', 318, 292, { tam: 17, peso: 700, color: m.gris });
      });
      rombo(210, 323, false, g);
      nota('el veterinario sobrevive solo', 304, L.tramo(t, 0.66, 0.74));
      // Herencia
      var h = L.tramo(t, 0.8, 0.88);
      UJ.caja(ctx, lz, 40, 430, 170, 54, 'Persona', null, A, h);
      UJ.caja(ctx, lz, 400, 396, 170, 50, 'Dueño', null, A, h);
      UJ.caja(ctx, lz, 400, 470, 170, 50, 'Veterinario', null, A, h);
      UJ.alfa(ctx, h, function () {
        ctx.beginPath(); ctx.moveTo(210, 457); ctx.lineTo(232, 445); ctx.lineTo(232, 469); ctx.closePath(); L.rellena(ctx, m.papel, T, 2.5);
        L.trazo(ctx, [[232, 457], [300, 457]], 1, T, 3);
        L.trazo(ctx, [[300, 421], [300, 495]], 1, T, 3);
        L.trazo(ctx, [[300, 421], [400, 421]], 1, T, 3);
        L.trazo(ctx, [[300, 495], [400, 495]], 1, T, 3);
        UJ.rotulo(ctx, lz, 'herencia', 256, 474, { tam: 17, peso: 700, color: m.gris });
      });
      nota('solo si hay un «es-un»', 446, L.tramo(t, 0.88, 0.94));
      UJ.rotulo(ctx, lz, 'Rombo relleno, rombo vacío, triángulo: cada línea dice algo', W / 2, 565,
                { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
