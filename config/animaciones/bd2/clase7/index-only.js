/* Index Only Scan: si todas las columnas que pide la consulta estan en el indice, el motor no
 * toca la tabla. Si se agrega id_mascota, se pierde; se recupera con la clave o con INCLUDE. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('index-only', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.codigo(ctx, lz, 30, 26, W - 60, 'SELECT estado, fecha_hora FROM cita', L.tramo(t, 0, 0.08), 17);
      UJ.codigo(ctx, lz, 30, 70, W - 60, "WHERE estado = 'PROGRAMADA' AND fecha_hora >= …", L.tramo(t, 0.06, 0.14), 17);
      UJ.caja(ctx, lz, 30, 150, 300, 110, 'índice', '(estado, fecha_hora)', C, L.tramo(t, 0.14, 0.22));
      UJ.caja(ctx, lz, 470, 150, 300, 110, 'tabla cita', 'filas completas', A, L.tramo(t, 0.14, 0.22));
      var cruza = t > 0.48 && t < 0.74;
      UJ.alfa(ctx, L.tramo(t, 0.24, 0.32) * (cruza ? 0.3 : 1), function () {
        UJ.sello(ctx, lz, 400, 205, 26, true, 1);
        UJ.rotulo(ctx, lz, 'Index Only Scan', 180, 274, { tam: 20, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'responde sin tocar la tabla', 180, 302, { tam: 17 });
      });
      // agrega id_mascota
      UJ.codigo(ctx, lz, 30, 360, W - 60, 'SELECT estado, fecha_hora, id_mascota …', L.tramo(t, 0.44, 0.52), 17);
      if (cruza) L.flecha(ctx, 334, 205, 466, 205, R, 4, L.tramo(t, 0.52, 0.6, 'frena'));
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.64) * (cruza ? 1 : 0.4), function () { UJ.rotulo(ctx, lz, 'vuelve a buscar cada fila a la tabla', W / 2, 420, { tam: 18, peso: 700, color: R }); });
      UJ.alfa(ctx, L.tramo(t, 0.76, 0.88), function () {
        L.rectRed(ctx, 30, 470, W - 60, 130, 14); L.rellena(ctx, L.tono(V, 0.88), V, 2);
        UJ.rotulo(ctx, lz, 'Dos maneras de recuperarlo', W / 2, 482, { tam: 21, peso: 800, color: V });
        L.texto(ctx, 'agregar id_mascota a la clave', W / 2, 522, { tam: 18, peso: 600, color: m.tinta, alinear: 'center', letra: lz.letra });
        L.texto(ctx, 'o  … INCLUDE (id_mascota)', W / 2, 556, { tam: 18, peso: 700, color: m.tinta, alinear: 'center', letra: 'Consolas, monospace' });
      });
    }
  });
})();
