/* RAISE EXCEPTION: el % se sustituye en orden, y la excepcion aborta: lo escrito se deshace. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('raise-aborta', {
    duracion: 5,
    pasos: [0.32, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      UJ.codigo(ctx, lz, 20, 20, W - 40, "RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id;", L.tramo(t, 0, 0.14), 17);
      UJ.rotulo(ctx, lz, '%  ←  p_id = 99', W / 2, 82, { tam: 20, peso: 700, color: C, visible: L.tramo(t, 0.12, 0.2) });
      UJ.alfa(ctx, L.tramo(t, 0.16, 0.26, 'suave'), function () {
        L.rectRed(ctx, 20, 120, W - 40, 50, 10); L.rellena(ctx, L.tono(R, 0.88), R, 2);
        UJ.rotulo(ctx, lz, 'ERROR: la mascota 99 no existe', W / 2, 132, { tam: 22, peso: 700, color: R });
      });
      UJ.rotulo(ctx, lz, '%% imprime un porcentaje literal', W / 2, 182, { tam: 17, visible: L.tramo(t, 0.24, 0.3) });
      UJ.rotulo(ctx, lz, 'Dentro del CALL', 200, 228, { tam: 22, peso: 800, color: A, visible: L.tramo(t, 0.32, 0.36) });
      var pasos = ['1 · INSERT INTO cita', '2 · validación falla', '3 · RAISE EXCEPTION'];
      for (var i = 0; i < 3; i++) {
        UJ.caja(ctx, lz, 40, 270 + i * 76, 320, 60, pasos[i], null, i === 0 ? A : R, L.tramo(t, 0.36 + i * 0.08, 0.42 + i * 0.08));
      }
      var filas = ['1 · Firulais · 09:00', '2 · Mishi · 10:00', '3 · Luna · 11:00'];
      var nueva = L.tramo(t, 0.4, 0.46), borra = L.tramo(t, 0.62, 0.72);
      UJ.alfa(ctx, L.tramo(t, 0.34, 0.4), function () {
        UJ.tabla(ctx, lz, 420, 270, 340, 'cita', filas, 2 + nueva * (1 - borra), A, nueva > 0.5 && borra < 0.5 ? 2 : -1);
      });
      UJ.rotulo(ctx, lz, 'la fila 3 se deshizo', 590, 446, { tam: 19, peso: 700, color: R, visible: L.tramo(t, 0.68, 0.72) });
      UJ.sello(ctx, lz, 740, 270, 26, false, L.tramo(t, 0.6, 0.68));
      UJ.rotulo(ctx, lz, 'Aborta: no puede quedar una cita a medias.', W / 2, 520, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.74, 0.86) });
      UJ.rotulo(ctx, lz, 'El mensaje es interfaz: lo lee quien usa la aplicación.', W / 2, 566, { tam: 19, ancho: W - 40, visible: L.tramo(t, 0.86, 1) });
    }
  });
})();
