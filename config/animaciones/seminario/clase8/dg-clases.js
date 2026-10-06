/* Lo que dibuja el codigo de «El diagrama de clases en Mermaid»: Dueno y Mascota con sus tres
 * compartimentos y la asociacion «posee» con multiplicidad en los dos extremos. Las tres reglas
 * van marcadas sobre el elemento donde se cumplen. */
(function () {
  FP_ANIMADOR.registrar('dg-clases', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var x = 230, w = 300;
      var h1 = DG.clase(ctx, lz, x, 30, w, 'Dueno', ['-int idDueno', '-String nombre', '-String telefono'], ['+registrar()'], { tam: 16 });
      var y2 = 360;
      DG.clase(ctx, lz, x, y2, w, 'Mascota', ['-int idMascota', '-String nombre', '-String especie', '-char activa'], ['+abrirExpediente()'], { tam: 16 });
      var cx = x + w / 2;
      DG.flecha(ctx, lz, [[cx, 30 + h1], [cx, y2 - 1]], { abierta: true, rotulo: 'posee', en: [cx, (30 + h1 + y2) / 2] });
      FP_LIENZO.texto(ctx, '1', cx + 12, 30 + h1 + 6, { tam: 17, peso: 800, color: '#333', letra: lz.letra });
      FP_LIENZO.texto(ctx, '0..*', cx + 12, y2 - 30, { tam: 17, peso: 800, color: '#333', letra: lz.letra });
      DG.marca(ctx, lz, 560, 64, 1, 'Visibilidad: - privado, + publico', 220);
      DG.marca(ctx, lz, 560, 114, 2, 'El TIPO de cada atributo', 200);
      DG.marca(ctx, lz, 560, (30 + h1 + y2) / 2, 3, 'Multiplicidad en LOS DOS extremos', 200);
    }
  });
})();
