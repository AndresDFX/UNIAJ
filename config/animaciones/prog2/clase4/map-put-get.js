/* La API de Map y sus trampas: put con una clave que ya existe reemplaza en silencio (y devuelve
 * el valor anterior); get de una clave que no existe devuelve null. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('map-put-get', {
    duracion: 4.8,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, V = m.verde, W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, 'Map<String, String> mapa = new HashMap<>();', L.tramo(t, 0, 0.06), 18);
      // el mapa a la derecha
      var mx = 520, my = 100;
      L.rectRed(ctx, mx, my, 260, 44, 8); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'mapa', mx + 130, my + 10, { tam: 20, peso: 700, color: m.papel });
      L.rectRed(ctx, mx, my + 44, 260, 50, 0); L.rellena(ctx, m.papel, L.tono(A, 0.5), 1);
      ctx.beginPath(); ctx.moveTo(mx + 120, my + 44); ctx.lineTo(mx + 120, my + 94); ctx.stroke();
      var reemplaza = L.tramo(t, 0.46, 0.52);
      UJ.alfa(ctx, L.tramo(t, 0.12, 0.18), function () {
        UJ.rotulo(ctx, lz, '"M-001"', mx + 60, my + 58, { tam: 19, peso: 700 });
        UJ.alfa(ctx, 1 - reemplaza, function () { UJ.rotulo(ctx, lz, '"Luna"', mx + 190, my + 58, { tam: 19, peso: 700, color: A }); });
        UJ.alfa(ctx, reemplaza, function () {
          L.rectRed(ctx, mx + 124, my + 48, 132, 42, 6); L.rellena(ctx, L.tono(R, 0.85));
          UJ.rotulo(ctx, lz, '"Rocky"', mx + 190, my + 58, { tam: 19, peso: 700, color: R });
        });
      });
      UJ.rotulo(ctx, lz, 'una sola fila: no hay claves repetidas', mx + 130, my + 104, { tam: 16, ancho: 260, visible: L.tramo(t, 0.54, 0.6) });
      function linea(y, cod, res, c, a0) {
        UJ.alfa(ctx, L.tramo(t, a0, a0 + 0.01), function () { UJ.codigo(ctx, lz, 20, y, 480, cod, L.tramo(t, a0, a0 + 0.07), 17); });
        UJ.rotulo(ctx, lz, res, 34, y + 44, { tam: 18, peso: 700, color: c, alinear: 'left', ancho: 470, visible: L.tramo(t, a0 + 0.07, a0 + 0.13) });
      }
      linea(100, 'mapa.put("M-001", "Luna");', 'devuelve null: la clave no existía', V, 0.06);
      linea(200, 'mapa.put("M-001", "Rocky");', 'devuelve "Luna" y la reemplaza en silencio', R, 0.36);
      linea(300, 'mapa.get("M-999");', 'null: la clave no existe', R, 0.68);
      linea(380, 'mapa.getOrDefault("M-999", "sin dato");', 'un valor por defecto en vez de null', V, 0.76);
      UJ.rotulo(ctx, lz, 'Recorrer: entrySet() con getKey() y getValue(), o keySet() y values().', W / 2, 500, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.88, 0.94) });
      UJ.rotulo(ctx, lz, 'Clave de clase propia: sobrescribir equals y hashCode juntos.', W / 2, 560, { tam: 19, peso: 700, color: A, ancho: W - 40, visible: L.tramo(t, 0.92, 0.99) });
    }
  });
})();
