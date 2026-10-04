/* Ilustracion: Qué observar en la demo: el tablero */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, W = lz.ancho;
      var cols = [m.accion, m.acento, m.verde, m.malva];
      var bloques = [["Por hacer", ["Historial clínico", "Recordatorios"], ""], ["Modelando ≤ 2", ["Registrar mascota", "Agendar cita"], ""], ["En revisión", ["más tarjetas", "que el límite:", "se acumulan"], "mal"], ["Aprobado", ["política:", "diagrama", "+ mockup", "+ visto bueno"], "bien"]];
      UJ.rotulo(ctx, lz, "Qué observar en la demo: el tablero", W / 2, 12, { tam: 26, peso: 800, color: m.accion, ancho: W - 40 });
      var n = bloques.length, an = (760 - (n - 1) * 16) / n, tm = n > 3 ? 17 : 19, mx = 0;
      for (var j = 0; j < n; j++) mx = Math.max(mx, bloques[j][1].length);
      var alto = tm + 22 + 24 + mx * tm * 1.65, y0 = Math.max(70, (640 - alto - 120) / 2 + 20);
      for (var i = 0; i < n; i++) {
        var x = 20 + i * (an + 16), c = bloques[i][2] === 'mal' ? m.malva : bloques[i][2] === 'bien' ? m.verde : cols[i % 2];
        UJ.tarjeta(ctx, lz, x, y0, an, bloques[i][0], bloques[i][1], c, 1, undefined, { tam: tm, alto: alto });
        if (bloques[i][2]) UJ.sello(ctx, lz, x + an - 22, y0 + 20, 16, bloques[i][2] === 'bien', 1);
        if (i < n - 1 && true) L.flecha(ctx, x + an + 1, y0 + alto / 2, x + an + 15, y0 + alto / 2, m.tinta, 3, 1);
      }
      L.rectRed(ctx, 20, y0 + alto + 30, 760, 80, 16); L.rellena(ctx, L.tono(m.sello, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, "Límite roto = cuello de botella: se deja de empezar y se ayuda a terminar", W / 2, y0 + alto + 52, { tam: 22, peso: 800, ancho: 720 });
    }
  });
})();
