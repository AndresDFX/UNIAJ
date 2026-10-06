/* Lo que dibuja el codigo de «El modelo en V con trazabilidad»: la cadena de nueve niveles en
 * forma de V (diseno bajando, pruebas subiendo) y las cuatro flechas punteadas «verifica» que
 * unen cada nivel de diseno con su nivel de prueba. */
(function () {
  FP_ANIMADOR.registrar('dg-modelo-v', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var izq = ['Requisitos', 'Analisis\nfuncional', 'Diseno de\narquitectura', 'Diseno\ndetallado'];
      var der = ['Pruebas de\naceptacion', 'Pruebas de\nsistema', 'Pruebas de\nintegracion', 'Pruebas\nunitarias'];
      var w = 190, h = 62, ys = [60, 175, 290, 405], xl = 125, xr = 675;
      var verde = { relleno: '#E2F2EA', borde: '#1B7A4E' };
      for (var i = 0; i < 4; i++) {
        DG.nodo(ctx, lz, xl + i * 22, ys[i], w, h, izq[i], 'rect', { tam: 16 });
        DG.nodo(ctx, lz, xr - i * 22, ys[i], w, h, der[i], 'rect', { tam: 16, relleno: verde.relleno, borde: verde.borde });
        if (i < 3) {
          DG.flecha(ctx, lz, [[xl + i * 22, ys[i] + h / 2], [xl + (i + 1) * 22, ys[i + 1] - h / 2 - 1]]);
          DG.flecha(ctx, lz, [[xr - (i + 1) * 22, ys[i + 1] - h / 2], [xr - i * 22, ys[i] + h / 2 + 1]]);
        }
        DG.flecha(ctx, lz, [[xl + i * 22 + w / 2, ys[i]], [xr - i * 22 - w / 2 - 1, ys[i]]],
                  { punteada: true, color: '#1B7A4E', rotulo: 'verifica', colorRotulo: '#1B7A4E' });
      }
      DG.nodo(ctx, lz, 400, 560, 200, 58, 'Codificacion', 'rect', { tam: 17 });
      DG.flecha(ctx, lz, [[xl + 66, ys[3] + h / 2], [310, 560]]);
      DG.flecha(ctx, lz, [[490, 560], [xr - 66, ys[3] + h / 2 + 1]]);
      DG.marca(ctx, lz, 250, 18, 1, 'Cada nivel de diseno tiene su nivel de prueba', 420);
    }
  });
})();
