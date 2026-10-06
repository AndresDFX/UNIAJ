/* Lo que dibuja el codigo de «Las tres reglas del C4 Container»: la API, la base y su relacion,
 * con cada regla marcada sobre el elemento donde se cumple. */
(function () {
  var L = FP_LIENZO;
  function marca(ctx, lz, x, y, n, txt, ancho) {
    L.circulo(ctx, x, y, 15); L.rellena(ctx, lz.marca.sello || '#FFD000', '#333', 2);
    L.texto(ctx, String(n), x, y - 10, { tam: 18, peso: 800, color: '#333', alinear: 'center', letra: lz.letra });
    L.texto(ctx, txt, x + 24, y - 11, { tam: 15, peso: 700, color: lz.marca.tinta, ancho: ancho || 300, letra: lz.letra });
  }
  FP_ANIMADOR.registrar('ilus-c4-reglas', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.rotulo(ctx, lz, 'Tres reglas del nivel Container', lz.ancho / 2, 14, { tam: 24, peso: 800, color: lz.marca.accion });
      C4.contenedor(ctx, lz, 230, 90, 340, 100, 'API de turnos', 'Node.js', '');
      C4.baseDatos(ctx, lz, 270, 360, 260, 140, 'Base de turnos', 'PostgreSQL', '');
      C4.rel(ctx, lz, 400, 192, 400, 356, 'INSERT y SELECT', 'TCP/SQL', 0, 0);
      marca(ctx, lz, 600, 128, 1, 'Cada contenedor dice su tecnología', 180);
      marca(ctx, lz, 560, 420, 2, 'Lo que guarda datos es ContainerDb: se dibuja como cilindro', 220);
      marca(ctx, lz, 70, 262, 3, 'Cada relación: verbo, protocolo y formato', 160);
      UJ.rotulo(ctx, lz, 'Mal: Container(api, "API")  ·  Rel(api, db, "usa")', lz.ancho / 2, 560,
                { tam: 15, peso: 600, color: lz.marca.malva || '#A02030' });
      UJ.rotulo(ctx, lz, 'Los mismos nombres se repiten en el Despliegue y en el Component.', lz.ancho / 2, 592,
                { tam: 14, peso: 500 });
    }
  });
})();
