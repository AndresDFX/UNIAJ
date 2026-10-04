/* Integrar por capas: UI -> Servicio -> Repositorio -> Modelo; la dependencia hacia arriba se tacha. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('capas-dependencia', {
    duracion: 4.5,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, R = m.malva, W = lz.ancho;
      var capas = [['Interfaz', 'ClinicaApp · JOptionPane'], ['Servicio', 'ServicioClinica · reglas'], ['Repositorio', 'RepositorioMascotasCSV · guardar/cargar'], ['Modelo', 'Mascota · datos']];
      var x = 50, an = 400;
      for (var i = 0; i < 4; i++) {
        var y = 40 + i * 130;
        UJ.caja(ctx, lz, x, y, an, 86, capas[i][0], capas[i][1], L.tono(A, i * 0.12), L.tramo(t, 0.02 + i * 0.07, 0.1 + i * 0.07));
        if (i < 3) {
          var a = L.tramo(t, 0.1 + i * 0.08, 0.2 + i * 0.08);
          if (a > 0) L.flecha(ctx, x + an / 2, y + 90, x + an / 2, y + 124, m.verde, 5, a);
        }
      }
      UJ.rotulo(ctx, lz, 'Cada capa usa solo la de abajo', 490, 300, { tam: 20, peso: 700, alinear: 'left', ancho: 280, color: m.verde, visible: L.tramo(t, 0.3, 0.4) });
      // Dependencia prohibida: servicio -> JOptionPane (hacia arriba)
      var p = L.tramo(t, 0.45, 0.6);
      if (p > 0) {
        ctx.save(); ctx.setLineDash([10, 8]);
        L.trazo(ctx, [[x + an + 6, 213], [x + an + 70, 213], [x + an + 70, 83], [x + an + 30, 83]], p, R, 4);
        ctx.restore();
        L.flecha(ctx, x + an + 40, 83, x + an + 8, 83, R, 4, L.tramo(t, 0.56, 0.6));
      }
      UJ.rotulo(ctx, lz, 'el servicio llama a JOptionPane', 562, 128, { tam: 18, peso: 700, alinear: 'left', ancho: 200, color: R, visible: L.tramo(t, 0.58, 0.68) });
      UJ.sello(ctx, lz, x + an + 70, 150, 26, false, L.tramo(t, 0.78, 0.88));
      UJ.rotulo(ctx, lz, 'La regla no conoce la pantalla: lanza una excepción y la interfaz decide qué mostrar.', W / 2, 568, { tam: 20, ancho: W - 40, visible: L.tramo(t, 0.84, 0.96) });
    }
  });
})();
