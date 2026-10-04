/* JUnit: cada caso es un metodo @Test; antes de cada uno, @BeforeEach rearma el estado limpio;
 * los casos se ponen en verde uno a uno, solos y repetibles. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('junit-resultados', {
    duracion: 4.8,
    // Pasos LOGICOS: 1) los casos son metodos @Test (aun sin correr), 2) @BeforeEach rearma el
    // estado antes de cada caso y los cuatro corren, cada uno desde cero, 3) la conclusion: 4 de 4,
    // los assert y «automatica y repetible». La linea @BeforeEach ya no se ve en el paso 1.
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, G = m.gris, S = m.sello, W = lz.ancho;
      // Paso 1: un caso = un metodo @Test
      UJ.rotulo(ctx, lz, 'Un caso = un método @Test', 20, 66, { tam: 22, peso: 800, alinear: 'left', color: A, visible: L.tramo(t, 0, 0.08) });
      var casos = ['agendaMascotaActiva', 'rechazaMascotaInactiva', 'rechazaFechaPasada', 'cancelaCitaExistente'];
      // Paso 2: momento en que corre cada caso (los cuatro, uno tras otro) y cuanto dura
      var corre = [0.39, 0.45, 0.51, 0.57], d = 0.05;
      var y0 = 110, al = 66;
      for (var i = 0; i < casos.length; i++) {
        var y = y0 + i * al, ok = L.tramo(t, corre[i] + 0.03, corre[i] + d);
        UJ.alfa(ctx, L.tramo(t, 0.08 + i * 0.03, 0.14 + i * 0.03), function () {
          var activo = t >= corre[i] && t < corre[i] + d;
          L.rectRed(ctx, 20, y, 440, al - 12, 10);
          L.rellena(ctx, activo ? L.tono(S, 0.75) : (ok > 0 ? L.tono(V, 0.9) : m.papel), ok > 0 ? V : L.tono(G, 0.2), 2);
          UJ.rotulo(ctx, lz, '@Test', 36, y + 6, { tam: 15, peso: 700, alinear: 'left', color: L.tono(m.tinta, 0.35) });
          L.texto(ctx, casos[i] + '()', 36, y + 25, { tam: 18, peso: 600, color: m.tinta, letra: 'Consolas, monospace' });
          if (ok <= 0) { L.circulo(ctx, 425, y + 27, 16); L.rellena(ctx, null, L.tono(G, 0.1), 3); }
          UJ.sello(ctx, lz, 425, y + 27, 18, true, ok);
        });
      }
      // Paso 2: @BeforeEach (la linea y lo que hace) rearma el estado antes de cada caso
      UJ.codigo(ctx, lz, 20, 16, W - 40, '@BeforeEach void preparar() { servicio = new ServicioCitas(); }', L.tramo(t, 0.31, 0.37), 15);
      var vueltas = 0;
      for (var k = 0; k < corre.length; k++) if (t >= corre[k]) vueltas++;
      UJ.alfa(ctx, L.tramo(t, 0.33, 0.37), function () {
        L.rectRed(ctx, 490, 110, 290, 190, 14); L.rellena(ctx, L.tono(C, 0.9), C, 3);
        UJ.rotulo(ctx, lz, '@BeforeEach', 635, 122, { tam: 22, peso: 800, color: C });
        UJ.rotulo(ctx, lz, 'estado limpio antes de cada caso:', 635, 156, { tam: 16, peso: 500, ancho: 270 });
        UJ.rotulo(ctx, lz, 'un ServicioCitas nuevo, sin citas', 635, 200, { tam: 17, peso: 700, ancho: 270 });
        UJ.rotulo(ctx, lz, 'ejecutado ' + vueltas + (vueltas === 1 ? ' vez' : ' veces'), 635, 246, { tam: 20, peso: 800, color: A });
      });
      for (var j = 0; j < corre.length; j++) {
        var f = L.tramo(t, corre[j] - 0.01, corre[j] + 0.015) * (1 - L.tramo(t, corre[j] + 0.04, corre[j] + d));
        if (f > 0) L.flecha(ctx, 488, 205, 466, y0 + j * al + 27, C, 3, f);
      }
      UJ.rotulo(ctx, lz, 'Ningún caso hereda lo que dejó el anterior.', 635, 320, { tam: 17, peso: 600, ancho: 280, visible: L.tramo(t, 0.58, 0.63) });
      // Paso 3: todos en verde, con que se comprueba y por que vale la pena
      UJ.alfa(ctx, L.tramo(t, 0.7, 0.76), function () {
        L.rectRed(ctx, 20, 390, W - 40, 50, 10); L.rellena(ctx, V);
        UJ.rotulo(ctx, lz, '4 de 4 pruebas pasaron', W / 2, 402, { tam: 22, peso: 800, color: m.papel });
      });
      UJ.rotulo(ctx, lz, 'assertEquals · assertTrue · assertThrows', W / 2, 470, { tam: 20, peso: 700, color: A, visible: L.tramo(t, 0.78, 0.86) });
      UJ.rotulo(ctx, lz, 'Automática y repetible: se corre igual cada vez.', W / 2, 510, { tam: 20, peso: 600, ancho: W - 40, visible: L.tramo(t, 0.87, 0.97) });
    }
  });
})();
