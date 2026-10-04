/* Lo que cuesta corregir el mismo error segun la fase en que se descubre: una fraccion en
 * requisitos, mucho en produccion. Es la curva que justifica las metodologias del curso. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('costo-del-error', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.3, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      var fases = ['Requisitos', 'Diseño', 'Construcción', 'Pruebas', 'Producción'];
      var alto = [28, 60, 120, 210, 330];
      var x0 = 70, base = 470, paso = 140, an = 96;
      UJ.rotulo(ctx, lz, 'Costo de corregir el mismo error', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.08) });
      L.trazo(ctx, [[40, base], [W - 30, base]], L.tramo(t, 0.02, 0.12), L.tono(m.tinta, 0.5), 3);
      for (var i = 0; i < 5; i++) {
        var x = x0 + i * paso;
        UJ.rotulo(ctx, lz, fases[i], x + an / 2, base + 12, { tam: 18, peso: 700, visible: L.tramo(t, 0.06 + i * 0.03, 0.12 + i * 0.03) });
        var h = alto[i] * L.tramo(t, 0.32 + i * 0.07, 0.42 + i * 0.07, 'frena');
        if (h > 0) {
          L.rectRed(ctx, x, base - h, an, h, 8);
          L.rellena(ctx, L.mezclaColor(L.tono(A, 0.35), R, i / 4));
        }
      }
      // El error nace en requisitos
      UJ.alfa(ctx, L.tramo(t, 0.14, 0.24), function () {
        UJ.linea(ctx, x0 + an / 2, base - 148, x0 + an / 2, base - 70, R, 2, 1, true);
        UJ.sello(ctx, lz, x0 + an / 2, base - 170, 22, false, 1);
        UJ.rotulo(ctx, lz, 'aquí nace el error', x0 + an / 2 + 32, base - 182, { tam: 18, peso: 700, color: R, alinear: 'left' });
      });
      UJ.alfa(ctx, L.tramo(t, 0.66, 0.72), function () {
        UJ.rotulo(ctx, lz, 'una fracción', x0 + an / 2, base - alto[0] - 34, { tam: 17, peso: 700, color: A });
        UJ.rotulo(ctx, lz, 'usuarios reales encima', x0 + 4 * paso + an / 2 - 30, base - alto[4] - 34, { tam: 17, peso: 700, color: R });
      });
      UJ.rotulo(ctx, lz, 'Programar: que funcione hoy. Ingeniería: que siga funcionando.', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.8, 1) });
    }
  });
})();
