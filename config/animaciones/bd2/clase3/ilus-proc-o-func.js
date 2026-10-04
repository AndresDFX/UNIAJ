/* Ilustracion: PROCEDURE o FUNCTION como arbol de decision. La pregunta: ¿el resultado tiene que
 * entrar en un SELECT? Si: FUNCTION con RETURNS. No, ejecuta pasos o maneja la transaccion:
 * PROCEDURE con CALL. Abajo, los dos mitos que se tachan. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-proc-o-func', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', W = lz.ancho;
      L.rectRed(ctx, 110, 16, W - 220, 74, 16); L.rellena(ctx, L.tono(m.sello || C, 0.75), m.tinta, 2);
      UJ.rotulo(ctx, lz, '¿El resultado tiene que entrar', W / 2, 24, { tam: 21, peso: 800 });
      UJ.rotulo(ctx, lz, 'en un SELECT, un WHERE o un ORDER BY?', W / 2, 54, { tam: 21, peso: 800 });
      L.flecha(ctx, 300, 94, 200, 140, C, 4, 1);
      L.flecha(ctx, 500, 94, 600, 140, A, 4, 1);
      UJ.rotulo(ctx, lz, 'sí', 232, 102, { tam: 20, peso: 800, color: C });
      UJ.rotulo(ctx, lz, 'no: hace pasos', 650, 100, { tam: 18, peso: 800, color: A });
      // FUNCTION
      L.rectRed(ctx, 20, 146, 370, 250, 14); L.rellena(ctx, L.tono(C, 0.9), C, 3);
      UJ.rotulo(ctx, lz, 'FUNCTION', 205, 158, { tam: 24, peso: 800, color: L.tono(C, -0.3) });
      UJ.rotulo(ctx, lz, 'devuelve un valor', 205, 192, { tam: 17 });
      UJ.codigo(ctx, lz, 32, 228, 346, 'RETURNS NUMERIC ... RETURN v;', 1, 14);
      UJ.codigo(ctx, lz, 32, 270, 346, 'SELECT nombre, fn_precio(especie)', 1, 14);
      UJ.codigo(ctx, lz, 32, 302, 346, '  FROM mascota;', 1, 14);
      UJ.rotulo(ctx, lz, 'corre dentro de la transacción de quien la llama', 205, 346, { tam: 14, ancho: 340 });
      // PROCEDURE
      L.rectRed(ctx, 410, 146, 370, 250, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
      UJ.rotulo(ctx, lz, 'PROCEDURE', 595, 158, { tam: 24, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'ejecuta pasos y cambia datos', 595, 192, { tam: 17 });
      UJ.codigo(ctx, lz, 422, 228, 346, 'CALL sp_agendar_cita(3, 7, ...);', 1, 14);
      UJ.codigo(ctx, lz, 422, 270, 346, 'SELECT sp_agendar_cita(...);', 1, 14);
      UJ.sello(ctx, lz, 752, 284, 13, false, 1);
      UJ.rotulo(ctx, lz, '"is a procedure" · puede COMMIT o ROLLBACK', 595, 312, { tam: 14, ancho: 340, color: L.tono(A, -0.2) });
      UJ.rotulo(ctx, lz, 'admite parámetros OUT, y aun así no entra en un SELECT', 595, 346, { tam: 14, ancho: 340 });
      // Mitos
      UJ.rotulo(ctx, lz, 'Falso:', 30, 422, { tam: 19, peso: 800, color: R, alinear: 'left' });
      var mitos = ['«son sinónimos y las dos se llaman con SELECT o CALL»',
                   '«una función necesita LANGUAGE sql para devolver un valor»',
                   '«un OUT es la única forma de devolver un valor»'];
      for (var i = 0; i < 3; i++) {
        var y = 456 + i * 46;
        L.rectRed(ctx, 30, y, W - 60, 38, 8); L.rellena(ctx, L.tono(R, 0.92), R, 1);
        UJ.rotulo(ctx, lz, mitos[i], 70, y + 9, { tam: 16, alinear: 'left', ancho: W - 120 });
        UJ.sello(ctx, lz, 50, y + 19, 11, false, 1);
      }
      UJ.rotulo(ctx, lz, 'Las dos pueden ser LANGUAGE plpgsql: el lenguaje no decide nada.', W / 2, 600, { tam: 16, peso: 700, ancho: W - 40 });
    }
  });
})();
