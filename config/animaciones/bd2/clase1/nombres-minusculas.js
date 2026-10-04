/* PostgreSQL pliega a minuscula los identificadores sin comillas: CREATE TABLE Mascota crea
 * mascota, y consultar "Mascota" entre comillas falla. Regla: minusculas, singular, sin tildes,
 * guion bajo y nunca comillas dobles. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('nombres-minusculas', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.codigo(ctx, lz, 30, 30, 440, 'CREATE TABLE Mascota (...);', L.tramo(t, 0, 0.1), 19);
      L.flecha(ctx, 480, 50, 560, 50, L.tono(m.tinta, 0.4), 3, L.tramo(t, 0.12, 0.18));
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.24), function () {
        L.rectRed(ctx, 570, 26, 200, 50, 10); L.rellena(ctx, L.tono(A, 0.88), A, 2);
        L.texto(ctx, 'mascota', 670, 39, { tam: 20, peso: 700, color: A, alinear: 'center', letra: 'Consolas, monospace' });
        UJ.rotulo(ctx, lz, 'el motor pliega a minúscula', 670, 86, { tam: 16, color: L.tono(m.tinta, 0.2) });
      });
      UJ.codigo(ctx, lz, 30, 150, 440, 'SELECT * FROM "Mascota";', L.tramo(t, 0.32, 0.42), 19);
      UJ.sello(ctx, lz, 510, 170, 20, false, L.tramo(t, 0.44, 0.5));
      UJ.rotulo(ctx, lz, 'ERROR: relation "Mascota" does not exist', 540, 158, { tam: 17, peso: 700, color: R, alinear: 'left', ancho: 240, visible: L.tramo(t, 0.46, 0.58) });
      UJ.rotulo(ctx, lz, 'Con comillas, el nombre se respeta letra a letra', W / 2, 232, { tam: 18, visible: L.tramo(t, 0.52, 0.6) });
      var reglas = [['todo en minúsculas, nunca comillas dobles', 'mascota'], ['tabla en singular, sin tildes ni eñes', 'dueno'],
                    ['compuestas con guion bajo, no camelCase', 'detalle_factura'], ['la FK se lee sola', 'cita.id_mascota → mascota']];
      for (var i = 0; i < 4; i++) {
        UJ.alfa(ctx, L.tramo(t, 0.64 + i * 0.07, 0.7 + i * 0.07), function () {
          var y = 284 + i * 72;
          L.rectRed(ctx, 30, y, W - 60, 60, 10); L.rellena(ctx, L.tono(V, 0.9), V, 2);
          UJ.rotulo(ctx, lz, reglas[i][0], 50, y + 18, { tam: 18, peso: 600, alinear: 'left', ancho: 400 });
          L.texto(ctx, reglas[i][1], W - 50, y + 19, { tam: 17, peso: 700, color: A, alinear: 'right', letra: 'Consolas, monospace' });
        });
      }
    }
  });
})();
