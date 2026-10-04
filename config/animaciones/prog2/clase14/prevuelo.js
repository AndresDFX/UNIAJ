/* La demo blindada: checklist de pre-vuelo que se marca punto por punto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('prevuelo', {
    duracion: 5,
    pasos: [0.3, 0.55, 0.8, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, V = m.verde, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Pre-vuelo: antes de compartir pantalla', W / 2, 24, { tam: 24, peso: 800, visible: L.tramo(t, 0, 0.05) });
      var items = [
        ['Datos sembrados', 'creíbles: tres dueños, cuatro mascotas, tres citas'],
        ['Camino feliz ensayado', 'la ruta ensayada, sin búsquedas improvisadas'],
        ['Pantalla limpia', 'fuente grande, sin notificaciones, el proyecto ya compilado'],
        ['Plan B', 'un video corto de la ruta feliz y capturas listas']
      ];
      var marca = [[0.12, 0.2], [0.38, 0.46], [0.62, 0.7], [0.86, 0.94]];
      for (var i = 0; i < 4; i++) {
        var y = 84 + i * 118;
        var hecho = L.tramo(t, marca[i][0], marca[i][1]);
        UJ.alfa(ctx, L.tramo(t, 0.02 + i * 0.02, 0.06 + i * 0.02), function () {
          L.rectRed(ctx, 40, y, W - 80, 100, 14);
          L.rellena(ctx, L.tono(hecho >= 1 ? V : A, 0.92), hecho >= 1 ? V : L.tono(A, 0.4), hecho >= 1 ? 3 : 2);
          L.rectRed(ctx, 66, y + 30, 40, 40, 8); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.4), 2);
          UJ.rotulo(ctx, lz, items[i][0], 130, y + 16, { tam: 23, peso: 800, alinear: 'left', ancho: W - 200, color: hecho >= 1 ? V : m.tinta });
          UJ.rotulo(ctx, lz, items[i][1], 130, y + 54, { tam: 18, alinear: 'left', ancho: W - 200 });
        });
        if (hecho > 0) {
          ctx.save(); ctx.strokeStyle = V; ctx.lineWidth = 6; ctx.lineCap = 'round';
          L.trazo(ctx, [[74, y + 50], [84, y + 62], [102, y + 36]], hecho, V, 6);
          ctx.restore();
        }
      }
    }
  });
})();
