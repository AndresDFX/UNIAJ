/* Separar la logica de la interfaz: Vista / Servicio / Modelo. Se cambia la vista (Swing ->
 * consola) y el servicio y el modelo no se tocan. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('tres-capas', {
    duracion: 4.8,
    pasos: [0.3, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, W = lz.ancho;
      var cambia = L.tramo(t, 0.36, 0.46);
      UJ.alfa(ctx, 1 - 0.65 * cambia, function () {
        UJ.caja(ctx, lz, 40, 30, 440, 120, 'Vista · Swing', 'VentanaRegistroMascota: pinta campos, lee texto, muestra mensajes', C, L.tramo(t, 0, 0.08));
      });
      UJ.sello(ctx, lz, 480, 36, 22, false, L.tramo(t, 0.42, 0.48));
      UJ.caja(ctx, lz, 40, 220, 440, 120, 'Servicio', 'ControladorRegistro, RepositorioMascotas: validaciones, búsqueda y la lista', A, L.tramo(t, 0.08, 0.16));
      UJ.caja(ctx, lz, 40, 410, 440, 120, 'Modelo', 'Mascota: datos y comportamiento propio', V, L.tramo(t, 0.16, 0.24));
      UJ.alfa(ctx, L.tramo(t, 0.1, 0.16), function () { L.flecha(ctx, 260, 154, 260, 214, m.tinta, 3, 1); });
      UJ.alfa(ctx, L.tramo(t, 0.18, 0.24), function () { L.flecha(ctx, 260, 344, 260, 404, m.tinta, 3, 1); });
      // vista nueva
      var nv = L.tramo(t, 0.46, 0.56, 'frena');
      UJ.caja(ctx, lz, L.mezcla(800, 530, nv), 30, 240, 120, 'Vista nueva', 'consola o JavaFX', C, nv);
      UJ.alfa(ctx, L.tramo(t, 0.54, 0.6), function () { L.flecha(ctx, 620, 154, 486, 250, C, 3, 1); });
      // sin cambios
      UJ.sello(ctx, lz, 540, 280, 24, true, L.tramo(t, 0.68, 0.74));
      UJ.rotulo(ctx, lz, 'sin cambios', 576, 268, { tam: 20, peso: 700, color: V, alinear: 'left', visible: L.tramo(t, 0.7, 0.76) });
      UJ.sello(ctx, lz, 540, 470, 24, true, L.tramo(t, 0.74, 0.8));
      UJ.rotulo(ctx, lz, 'sin cambios', 576, 458, { tam: 20, peso: 700, color: V, alinear: 'left', visible: L.tramo(t, 0.76, 0.82) });
      UJ.rotulo(ctx, lz, 'Prueba ácida: si cambia la pantalla, solo se reescribe la ventana.', W / 2, 568, { tam: 21, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.86, 0.96) });
    }
  });
})();
