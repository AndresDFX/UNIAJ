/* Caso Capital One, 2019: una mala configuracion del cortafuegos de aplicaciones (causa proxima)
 * dio credenciales de un rol que podia leer TODOS los buckets, mucho mas de lo que necesitaba
 * (causa raiz: privilegio excesivo). ~100 millones de personas en EE. UU. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('capital-one', {
    duracion: 5,
    pasos: [0.36, 0.76, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      var cad = [['Cortafuegos', 'mal configurado · causa próxima'], ['Peticiones internas', 'en nombre del servidor'], ['Credenciales temporales', 'de un rol de servicio']];
      for (var i = 0; i < 3; i++) {
        var y = 20 + i * 100;
        UJ.caja(ctx, lz, 30, y, 330, 80, cad[i][0], cad[i][1], i === 0 ? R : A, L.tramo(t, i * 0.1, 0.08 + i * 0.1));
        if (i < 2) L.flecha(ctx, 195, y + 82, 195, y + 98, m.tinta, 4, L.tramo(t, 0.08 + i * 0.1, 0.1 + i * 0.1));
      }
      // Los buckets
      UJ.rotulo(ctx, lz, 'el rol podía listar y leer…', 590, 20, { tam: 19, peso: 700, visible: L.tramo(t, 0.38, 0.44) });
      L.flecha(ctx, 364, 260, 400, 260, C, 4, L.tramo(t, 0.36, 0.4));
      for (var b = 0; b < 12; b++) {
        var bx = 420 + (b % 4) * 90, by = 60 + Math.floor(b / 4) * 90, necesita = b < 2;
        var a = L.tramo(t, 0.4 + b * 0.02, 0.46 + b * 0.02);
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, bx, by, 74, 70, 10); L.rellena(ctx, necesita ? L.tono(V, 0.7) : L.tono(R, 0.75), necesita ? V : R, 2);
          UJ.rotulo(ctx, lz, 'bucket', bx + 37, by + 24, { tam: 16, peso: 700 });
        });
      }
      UJ.rotulo(ctx, lz, 'verde: lo que necesitaba · rojo: lo que además podía leer (esquema, no a escala)', 590, 340, { tam: 16, peso: 700, ancho: 360, visible: L.tramo(t, 0.66, 0.74) });
      UJ.alfa(ctx, L.tramo(t, 0.78, 0.86), function () {
        L.rectRed(ctx, 30, 400, 740, 90, 12); L.rellena(ctx, L.tono(C, 0.88), C, 3);
        UJ.rotulo(ctx, lz, 'Causa raíz: privilegio mucho mayor que su función', 400, 412, { tam: 21, peso: 800, color: L.tono(C, -0.35), ancho: 700 });
        UJ.rotulo(ctx, lz, '≈ 100 millones de personas afectadas en EE. UU.', 400, 450, { tam: 18, ancho: 700 });
      });
      UJ.rotulo(ctx, lz, 'Sin hazaña: un permiso de más.', W / 2, 545, { tam: 22, peso: 700, ancho: W - 40, visible: L.tramo(t, 0.88, 1) });
    }
  });
})();
