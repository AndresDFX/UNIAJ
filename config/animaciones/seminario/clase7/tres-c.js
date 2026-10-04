/* La historia de usuario: rol, acción y «para» resaltados uno a uno, y luego las tres C que la
 * completan (la tarjeta, la charla y los criterios). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('tres-c', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.22, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'La historia de usuario', W / 2, 24, { tam: 26, peso: 800, color: A, visible: L.tramo(t, 0, 0.06) });
      // La tarjeta
      var ap = L.tramo(t, 0.04, 0.16);
      UJ.alfa(ctx, ap, function () {
        L.rectRed(ctx, 60, 76, 680, 250, 14); L.rellena(ctx, L.tono(m.sello, 0.9), L.tono(m.sello, -0.2), 2.5);
      });
      var filas = [
        { et: 'Rol', tx: 'Como auxiliar', c: A },
        { et: 'Acción', tx: 'quiero buscar la ficha por el documento del dueño', c: m.acento },
        { et: 'Para', tx: 'para no revolver la carpeta mientras el paciente espera', c: m.verde }
      ];
      for (var i = 0; i < 3; i++) {
        (function (i) {
          var f = filas[i], y = 96 + i * 72;
          var res = L.tramo(t, 0.26 + i * 0.1, 0.32 + i * 0.1);
          UJ.alfa(ctx, res, function () {
            L.rectRed(ctx, 74, y - 8, 652, 64, 10); L.rellena(ctx, L.tono(f.c, 0.8));
            UJ.pildora(ctx, lz, 86, y + 2, f.et, f.c, 1, { tam: 17, lleno: true });
          });
          UJ.alfa(ctx, ap, function () {
            L.texto(ctx, f.tx, 230, y + 2, { tam: 20, peso: 600, color: m.tinta, ancho: 430, letra: lz.letra });
          });
        })(i);
      }
      UJ.rotulo(ctx, lz, '← lo más valioso', 712, 266, { alinear: 'right', tam: 16, peso: 800, color: L.tono(m.verde, -0.3), visible: L.tramo(t, 0.5, 0.58) });
      // Las tres C
      var cs = [['Card', 'la tarjeta'], ['Conversation', 'la charla'], ['Confirmation', 'los criterios']];
      for (var k = 0; k < 3; k++) {
        var a = L.tramo(t, 0.66 + k * 0.07, 0.74 + k * 0.07);
        var x = 60 + k * 236;
        UJ.tarjeta(ctx, lz, x, 370, 208, cs[k][0], [cs[k][1]], [A, m.acento, m.verde][k], a, 1, { tam: 20 });
      }
      UJ.rotulo(ctx, lz, 'La tarjeta es el recordatorio de una conversación pendiente', W / 2, 560,
                { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
