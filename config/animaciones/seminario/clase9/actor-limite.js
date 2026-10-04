/* El actor es un rol, no una persona, y vive fuera del limite del sistema; lo que va adentro
 * del rectangulo es lo que el equipo construye. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('actor-limite', {
    duracion: 5,
    // Las pausas del docente: en cada una la lamina espera un clic.
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion;
      // Limite del sistema
      UJ.alfa(ctx, L.tramo(t, 0, 0.08), function () {
        L.rectRed(ctx, 250, 40, 340, 450, 16); L.rellena(ctx, L.tono(A, 0.95), A, 3);
        UJ.rotulo(ctx, lz, 'Sistema de la clínica', 420, 54, { tam: 22, peso: 800, color: A });
      });
      var cus = [['Registrar mascota', 140], ['Agendar cita', 240], ['Enviar recordatorio', 340]];
      for (var i = 0; i < cus.length; i++)
        UJ.elipse(ctx, lz, 420, cus[i][1], 140, 38, cus[i][0], A, L.tramo(t, 0.04 + i * 0.03, 0.1 + i * 0.03));

      // Paso 1: la persona se vuelve rol
      var p1 = L.tramo(t, 0.1, 0.16);
      var wM = UJ.pildora(ctx, lz, 120, 40, 'Doña Marta', m.gris, p1, { centrar: true });
      UJ.alfa(ctx, p1, function () { UJ.rayar(ctx, 120 - wM / 2 + 8, 57, wM - 16, m.malva, L.tramo(t, 0.16, 0.22)); });
      UJ.alfa(ctx, L.tramo(t, 0.2, 0.24), function () {
        UJ.rotulo(ctx, lz, 'una persona', 120, 82, { tam: 16, peso: 600, color: m.malva });
      });
      var aR = L.tramo(t, 0.22, 0.3);
      UJ.monigote(ctx, lz, 120, 115, 90, 'Recepcionista', A, aR);
      UJ.monigote(ctx, lz, 120, 285, 90, 'Veterinario', A, L.tramo(t, 0.26, 0.34));
      UJ.linea(ctx, 150, 160, 280, 145, m.tinta, 2, L.tramo(t, 0.28, 0.34));
      UJ.linea(ctx, 150, 165, 280, 235, m.tinta, 2, L.tramo(t, 0.28, 0.34));
      UJ.linea(ctx, 150, 325, 280, 250, m.tinta, 2, L.tramo(t, 0.3, 0.36));

      // Paso 2: actor secundario
      UJ.alfa(ctx, L.tramo(t, 0.4, 0.46), function () {
        UJ.rotulo(ctx, lz, 'actor secundario', 700, 210, { tam: 16, peso: 600, color: m.gris });
      });
      UJ.monigote(ctx, lz, 700, 240, 90, 'Servicio de mensajería', m.acento, L.tramo(t, 0.42, 0.5));
      UJ.linea(ctx, 560, 340, 670, 290, m.tinta, 2, L.tramo(t, 0.5, 0.58));
      UJ.alfa(ctx, L.tramo(t, 0.56, 0.64) * (1 - L.tramo(t, 0.72, 0.76)), function () {
        UJ.rotulo(ctx, lz, 'Los actores son roles, afuera', 420, 512, { tam: 20, peso: 700, color: A });
      });

      // Paso 3: algo que no es nuestro, metido adentro
      var a3 = L.tramo(t, 0.74, 0.82);
      UJ.elipse(ctx, lz, 420, 435, 140, 38, 'Enviar WhatsApp', m.malva, a3);
      UJ.sello(ctx, lz, 560, 410, 22, false, L.tramo(t, 0.82, 0.88));
      UJ.rotulo(ctx, lz, 'Adentro = lo construimos nosotros', 420, 520, { tam: 22, peso: 800, color: m.malva, visible: L.tramo(t, 0.86, 0.96) });
      UJ.rotulo(ctx, lz, 'El envío lo hace el servicio externo: no va adentro', 420, 556, { tam: 18, peso: 600, color: m.tinta, ancho: 740, visible: L.tramo(t, 0.9, 1) });
    }
  });
})();
