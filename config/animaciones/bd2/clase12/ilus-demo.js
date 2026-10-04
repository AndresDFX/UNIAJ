/* Ilustracion: que observar en la demo de integracion. 1) La busqueda armada concatenando texto
 * devuelve las 8 mascotas con ' OR 1=1 --. 2) La misma entrada como parametro devuelve 0 filas.
 * 3) La aplicacion solo conoce la firma: el CALL con una mascota inactiva aborta con su mensaje y
 * no deja nada escrito. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 8, { tam: 26, peso: 800, color: A });
      function banda(y, n, titulo, color) {
        L.rectRed(ctx, 20, y, 760, 172, 16); L.rellena(ctx, L.tono(color, 0.93), color, 2);
        L.circulo(ctx, 52, y + 30, 18); L.rellena(ctx, color);
        UJ.rotulo(ctx, lz, String(n), 52, y + 18, { tam: 20, peso: 800, color: m.papel });
        UJ.rotulo(ctx, lz, titulo, 82, y + 16, { tam: 21, peso: 800, color: color, alinear: 'left', ancho: 680 });
      }
      function resultado(y, texto, sub, color) {
        L.rectRed(ctx, 520, y, 240, 84, 12); L.rellena(ctx, L.tono(color, 0.85), color, 2);
        UJ.rotulo(ctx, lz, texto, 640, y + 12, { tam: 24, peso: 800, color: L.tono(color, -0.3), ancho: 230 });
        UJ.rotulo(ctx, lz, sub, 640, y + 50, { tam: 14, ancho: 230 });
      }
      // 1 · Concatenado
      banda(52, 1, 'Texto concatenado: el dato se vuelve código', R);
      UJ.codigo(ctx, lz, 40, 104, 460, "… WHERE nombre = '' OR 1=1 --'", 1, 16);
      UJ.rotulo(ctx, lz, "la entrada fue  ' OR 1=1 --", 270, 152, { tam: 15, ancho: 440 });
      L.flecha(ctx, 504, 140, 516, 140, R, 4, 1);
      resultado(98, '8 filas', 'todas las mascotas', R);
      // 2 · Parametro
      banda(236, 2, 'Parámetro: la misma entrada es solo un dato', V);
      UJ.codigo(ctx, lz, 40, 288, 460, '… WHERE nombre = $1', 1, 16);
      UJ.rotulo(ctx, lz, "$1 = ' OR 1=1 --   (texto literal)", 270, 336, { tam: 15, ancho: 440 });
      L.flecha(ctx, 504, 324, 516, 324, V, 4, 1);
      resultado(282, '0 filas', 'ninguna mascota se llama así', V);
      // 3 · El contrato
      banda(420, 3, 'La aplicación solo conoce la firma', A);
      UJ.codigo(ctx, lz, 40, 472, 460, 'CALL sp_agendar_cita(3, 1, …);', 1, 16);
      UJ.rotulo(ctx, lz, 'la mascota 3 está inactiva', 270, 520, { tam: 15, ancho: 440 });
      L.flecha(ctx, 504, 508, 516, 508, A, 4, 1);
      L.rectRed(ctx, 520, 466, 240, 116, 12); L.rellena(ctx, L.tono(A, 0.88), A, 2);
      UJ.rotulo(ctx, lz, 'mensaje literal:', 640, 474, { tam: 14, peso: 700, color: A, ancho: 230 });
      UJ.rotulo(ctx, lz, 'la mascota 3 esta inactiva; no se agenda cita', 640, 496, { tam: 15, peso: 700, ancho: 226 });
      UJ.rotulo(ctx, lz, 'COUNT(*) de cita: igual', 640, 552, { tam: 14, color: L.tono(m.tinta, 0.2), ancho: 230 });
    }
  });
})();
