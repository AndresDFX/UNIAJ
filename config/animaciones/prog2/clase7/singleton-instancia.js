/* Singleton: las tres piezas. La 1.a llamada a getInstancia() encuentra null y crea; la 2.a
 * devuelve el mismo objeto (mismo identityHashCode); un new desde afuera no compila porque el
 * constructor es private. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('singleton-instancia', {
    duracion: 4.8,
    pasos: [0.36, 0.68, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, S = m.sello, W = lz.ancho;
      var lineas = [
        'class RepositorioClinica {',
        '  private static RepositorioClinica instancia;',
        '  private RepositorioClinica() { }',
        '  public static synchronized RepositorioClinica getInstancia() {',
        '    if (instancia == null) instancia = new RepositorioClinica();',
        '    return instancia;',
        '  }',
        '}'
      ];
      var y0 = 20, al = 28;
      for (var i = 0; i < lineas.length; i++) UJ.codigo(ctx, lz, 20, y0 + i * al, W - 40, lineas[i], L.tramo(t, 0, 0.1), 14);
      // Las tres piezas numeradas
      var piezas = [[1, 1], [2, 2], [3, 3]];
      function marca(n, fila, a) {
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, 18, y0 + fila * al, W - 36, al, 6); L.rellena(ctx, null, S, 3);
          L.circulo(ctx, W - 40, y0 + fila * al + al / 2, 12); L.rellena(ctx, S);
          UJ.rotulo(ctx, lz, String(n), W - 40, y0 + fila * al + 4, { tam: 16, peso: 800 });
        });
      }
      marca(1, 1, L.tramo(t, 0.1, 0.14));
      marca(3, 3, L.tramo(t, 0.12, 0.16));
      marca(2, 2, L.tramo(t, 0.72, 0.76));
      // Paso 1: primera llamada
      var yA = 270;
      UJ.caja(ctx, lz, 20, yA, 200, 70, '1.ª llamada', 'getInstancia()', A, L.tramo(t, 0.14, 0.2));
      L.flecha(ctx, 224, yA + 35, 268, yA + 35, A, 3, L.tramo(t, 0.18, 0.22));
      UJ.caja(ctx, lz, 272, yA, 260, 70, 'instancia == null', 'sí → se crea con new', A, L.tramo(t, 0.2, 0.26));
      L.flecha(ctx, 536, yA + 35, 586, yA + 50, A, 3, L.tramo(t, 0.24, 0.28));
      UJ.alfa(ctx, L.tramo(t, 0.26, 0.32), function () {
        L.rectRed(ctx, 590, yA, 190, 160, 18); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'el objeto', 685, yA + 26, { tam: 20, peso: 700, color: V });
        UJ.rotulo(ctx, lz, 'identityHashCode', 685, yA + 66, { tam: 16, peso: 500 });
        UJ.rotulo(ctx, lz, '1b6d3586 (ejemplo)', 685, yA + 92, { tam: 16, peso: 800, color: V });
      });
      // Paso 2: segunda llamada, el mismo
      var yB = 360;
      UJ.caja(ctx, lz, 20, yB, 200, 70, '2.ª llamada', 'getInstancia()', C, L.tramo(t, 0.4, 0.46));
      L.flecha(ctx, 224, yB + 35, 268, yB + 35, C, 3, L.tramo(t, 0.44, 0.48));
      UJ.caja(ctx, lz, 272, yB, 260, 70, 'instancia != null', 'no crea: return instancia', C, L.tramo(t, 0.46, 0.52));
      L.flecha(ctx, 536, yB + 35, 586, yB + 10, C, 3, L.tramo(t, 0.5, 0.54));
      UJ.rotulo(ctx, lz, 'el mismo objeto: mismo identityHashCode', 685, yB + 92, { tam: 18, peso: 700, color: V, ancho: 190, visible: L.tramo(t, 0.54, 0.64) });
      // Paso 3: new desde afuera
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.82), function () {
        UJ.codigo(ctx, lz, 20, 540, 520, 'new RepositorioClinica();   // otra clase', 1, 16);
      });
      UJ.sello(ctx, lz, 580, 557, 26, false, L.tramo(t, 0.82, 0.9));
      UJ.rotulo(ctx, lz, 'No compila: el constructor es private.', 20, 590, { tam: 19, peso: 700, alinear: 'left', color: R, visible: L.tramo(t, 0.86, 0.97) });
    }
  });
})();
