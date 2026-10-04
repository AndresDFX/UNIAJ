/* HashSet: add de Labrador -> true, Criollo -> true, Labrador otra vez -> false; size 2.
 * Por dentro es un HashMap donde solo importan las claves; no garantiza orden. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('hashset-duplicados', {
    duracion: 4.8,
    pasos: [0.34, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'Set<String> razas = new HashSet<>();', L.tramo(t, 0, 0.06), 18);
      // el conjunto
      var cx = 630, cy = 210, r = 120;
      L.circulo(ctx, cx, cy, r); L.rellena(ctx, L.tono(A, 0.92), A, 3);
      UJ.rotulo(ctx, lz, 'razas', cx, cy - r + 14, { tam: 18, peso: 700, color: A });
      function chip(x, y, txt, c) {
        L.rectRed(ctx, x - 70, y - 20, 140, 40, 10); L.rellena(ctx, L.tono(c, 0.84), c, 2);
        UJ.rotulo(ctx, lz, txt, x, y - 11, { tam: 18, peso: 700 });
      }
      function vuela(a0, txt, dx, dy, rebota) {
        var p = L.tramo(t, a0, a0 + 0.1, 'frena');
        if (p <= 0) return;
        var x = L.mezcla(330, dx, p), y = L.mezcla(dy, dy, p);
        if (rebota) {
          var b = L.tramo(t, a0 + 0.1, a0 + 0.18, 'suave');
          x = L.mezcla(L.mezcla(330, 480, p), 330, b);
          UJ.alfa(ctx, 1 - b * 0.6, function () { chip(x, y, txt, R); });
        } else chip(x, y, txt, V);
      }
      vuela(0.08, 'Labrador', cx, 180, false);
      vuela(0.18, 'Criollo', cx, 240, false);
      function linea(y, cod, res, c, a0) {
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.01), function () { UJ.codigo(ctx, lz, 20, y, 300, cod, L.tramo(t, a0, a0 + 0.06), 17); });
        UJ.rotulo(ctx, lz, res, 335, y + 6, { tam: 20, peso: 800, color: c, alinear: 'left', visible: L.tramo(t, a0 + 0.08, a0 + 0.12) });
      }
      linea(110, 'razas.add("Labrador");', 'true', V, 0.04);
      linea(170, 'razas.add("Criollo");', 'true', V, 0.14);
      UJ.alfa(ctx, L.tramo(t, 0.36, 0.37), function () {});
      var p3 = L.tramo(t, 0.38, 0.39);
      if (p3 > 0) {
        UJ.codigo(ctx, lz, 20, 230, 300, 'razas.add("Labrador");', L.tramo(t, 0.38, 0.44), 17);
        var p = L.tramo(t, 0.44, 0.5, 'frena'), b = L.tramo(t, 0.5, 0.56, 'suave');
        var x = L.mezcla(L.mezcla(110, 450, p), 360, b);
        UJ.alfa(ctx, 1 - 0.4 * b, function () { chip(x, 330, 'Labrador', R); });
        UJ.rotulo(ctx, lz, 'false', 335, 236, { tam: 20, peso: 800, color: R, alinear: 'left', visible: L.tramo(t, 0.52, 0.56) });
        UJ.rotulo(ctx, lz, 'ya estaba: rebota y no se agrega', 34, 276, { tam: 16, color: R, alinear: 'left', visible: L.tramo(t, 0.54, 0.58) });
      }
      UJ.sello(ctx, lz, 470, 330, 22, false, L.tramo(t, 0.5, 0.56));
      UJ.rotulo(ctx, lz, 'size() = ' + (t < 0.18 ? 0 : t < 0.28 ? 1 : 2), cx, cy + r + 14, { tam: 20, peso: 700, color: A, visible: L.tramo(t, 0.16, 0.18) });
      UJ.rotulo(ctx, lz, 'Responde al instante «¿esto ya está?».', W / 2, 400, { tam: 20, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.6, 0.66) });
      UJ.rotulo(ctx, lz, 'Por dentro: un HashMap donde solo importan las claves.', W / 2, 470, { tam: 20, color: A, ancho: W - 40, visible: L.tramo(t, 0.72, 0.8) });
      UJ.rotulo(ctx, lz, 'Sin orden garantizado: LinkedHashSet conserva la inserción; TreeSet ordena.', W / 2, 530, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.84, 0.94) });
    }
  });
})();
