/* INVEST como lista de chequeo: seis letras, y una historia que impone la solución y es una épica
 * disfrazada falla N y S, así que se vuelve a partir. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('invest', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.52, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'INVEST: una historia bien cortada', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      var fichas = [['I', 'Independiente'], ['N', 'Negociable'], ['V', 'Valiosa'], ['E', 'Estimable'], ['S', 'Small · pequeña'], ['T', 'Testeable']];
      var falla = L.tramo(t, 0.56, 0.7);
      for (var i = 0; i < 6; i++) {
        (function (i) {
          var x = 40 + (i % 3) * 245, y = 76 + Math.floor(i / 3) * 92, a = L.tramo(t, 0.04 + i * 0.035, 0.1 + i * 0.035);
          var mala = (i === 1 || i === 4) ? falla : 0;
          UJ.alfa(ctx, a, function () {
            L.rectRed(ctx, x, y, 230, 76, 12);
            L.rellena(ctx, L.mezclaColor(L.tono(A, 0.88), L.tono(R, 0.85), mala), L.mezclaColor(A, R, mala), 2.5);
            L.texto(ctx, fichas[i][0], x + 16, y + 16, { tam: 38, peso: 800, color: L.mezclaColor(A, R, mala), letra: lz.letra });
            L.texto(ctx, fichas[i][1], x + 56, y + 27, { tam: 18, peso: 700, color: m.tinta, letra: lz.letra });
            if (mala > 0) UJ.sello(ctx, lz, x + 208, y + 22, 14, false, mala);
          });
        })(i);
      }
      UJ.tarjeta(ctx, lz, 40, 278, 720, 'Historia propuesta',
        ['«Quiero un combo con autocompletar en JavaScript para todo el historial clínico»'],
        m.gris, L.tramo(t, 0.32, 0.42), 1, { tam: 19, fila: 52 });
      // Los dos fallos
      var f1 = L.tramo(t, 0.6, 0.7), f2 = L.tramo(t, 0.7, 0.8);
      UJ.sello(ctx, lz, 66, 412, 15, false, f1);
      UJ.alfa(ctx, f1, function () {
        L.texto(ctx, 'N: impone la solución, no describe la necesidad', 92, 401, { tam: 19, peso: 700, color: R, letra: lz.letra });
      });
      UJ.sello(ctx, lz, 66, 458, 15, false, f2);
      UJ.alfa(ctx, f2, function () {
        L.texto(ctx, 'S: tres semanas de trabajo, una épica disfrazada', 92, 447, { tam: 19, peso: 700, color: R, letra: lz.letra });
      });
      UJ.rotulo(ctx, lz, 'Falla dos letras: no se planea, se vuelve a partir', W / 2, 555,
                { tam: 23, peso: 800, color: R, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
