/* La secuencia exacta: el rol nace en cero, recibe privilegios sobre tablas, y se otorga a la
 * persona. REVOKE quita lo otorgado. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('grant-revoke', {
    duracion: 5,
    pasos: [0.22, 0.6, 0.82, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030';
      var lineas = [
        ['CREATE ROLE recepcion NOLOGIN;', 0, 'nace con cero privilegios'],
        ['GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;', 0.26, 'varios privilegios en un GRANT'],
        ['GRANT SELECT ON dueno, mascota, veterinario TO recepcion;', 0.42, 'varias tablas en un GRANT'],
        ['GRANT recepcion TO ana_gomez;', 0.64, 'la persona recibe el paquete']
      ];
      for (var i = 0; i < 4; i++) {
        var y = 30 + i * 112;
        UJ.codigo(ctx, lz, 30, y, W - 60, lineas[i][0], L.tramo(t, lineas[i][1], lineas[i][1] + 0.12), 18);
        UJ.rotulo(ctx, lz, '→ ' + lineas[i][2], 50, y + 50, { tam: 18, peso: 600, alinear: 'left', color: L.tono(C, -0.3), visible: L.tramo(t, lineas[i][1] + 0.1, lineas[i][1] + 0.16) });
      }
      UJ.codigo(ctx, lz, 30, 478, W - 60, 'REVOKE INSERT ON cita FROM recepcion;', L.tramo(t, 0.84, 0.94), 18);
      UJ.rotulo(ctx, lz, '→ quita lo otorgado; afecta a todos los que tienen el rol', 50, 528, { tam: 18, peso: 600, alinear: 'left', color: R, ancho: W - 80, visible: L.tramo(t, 0.92, 1) });
    }
  });
})();
