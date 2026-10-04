/* La prueba del almuerzo: un caso de uso deja al actor satisfecho con un resultado de valor;
 * un paso interno (validar una fecha) no es un caso de uso. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('prueba-almuerzo', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.4, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'La prueba del almuerzo', W / 2, 22, { tam: 26, peso: 800, color: m.accion, visible: L.tramo(t, 0, 0.08) });
      UJ.rotulo(ctx, lz, '¿El actor se puede ir a almorzar satisfecho?', W / 2, 62, { tam: 19, peso: 600, color: m.gris, visible: L.tramo(t, 0.04, 0.12) });

      function lado(cx, texto, color, ok, a0, l1, l2) {
        var a = L.tramo(t, a0, a0 + 0.08);
        UJ.elipse(ctx, lz, cx, 160, 160, 44, texto, color, a, { tam: 19 });
        UJ.monigote(ctx, lz, cx, 225, 100, 'Recepcionista', m.tinta, L.tramo(t, a0 + 0.06, a0 + 0.14));
        UJ.sello(ctx, lz, cx, 400, 30, ok, L.tramo(t, a0 + 0.14, a0 + 0.22));
        UJ.alfa(ctx, L.tramo(t, a0 + 0.2, a0 + 0.28), function () {
          UJ.rotulo(ctx, lz, l1, cx, 446, { tam: 19, peso: 700, color: ok ? m.verde : m.malva, ancho: 340 });
          UJ.rotulo(ctx, lz, l2, cx, 474, { tam: 18, peso: 500, color: m.tinta, ancho: 340 });
        });
      }
      lado(210, 'Registrar mascota', m.accion, true, 0.08, 'se va satisfecho', 'ficha creada, código asignado');
      lado(590, 'Validar fecha de nacimiento', m.gris, false, 0.44, 'no es un caso de uso', 'nadie llega a la clínica a validar una fecha');
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.5), function () { UJ.linea(ctx, 400, 110, 400, 500, L.tono(m.gris, 0.5), 2, 1, true); });

      UJ.rotulo(ctx, lz, 'Verbo en infinitivo + objeto del dominio', W / 2, 560,
        { tam: 22, peso: 700, color: m.accion, ancho: W - 40, visible: L.tramo(t, 0.8, 0.96) });
    }
  });
})();
