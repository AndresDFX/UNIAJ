/* Ilustracion: que observar en la demo. Un molde (class Mascota), dos new con datos distintos y
 * la consola con dos mascotas diferentes; al final setEdad(-2) se rechaza y la edad sigue en 3.
 * Los textos son los del programa de la demo (Kit docente/Clase 1/Codigo/Mascota.java). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var MONO = 'Consolas, monospace', OSC = L.tono(m.tinta, -0.55);
      function mono(s, x, y, tam, color, peso, alinear) {
        L.texto(ctx, s, x, y, { tam: tam, peso: peso || 500, color: color || m.tinta, letra: MONO, alinear: alinear || 'left' });
      }
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });

      // 1 · El molde y dos objetos
      UJ.rotulo(ctx, lz, '1 · Un molde, dos objetos', 24, 56, { tam: 20, peso: 800, color: A, alinear: 'left' });
      L.rectRed(ctx, 24, 90, 270, 158, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
      L.rectRed(ctx, 24, 90, 270, 40, 14); L.rellena(ctx, A);
      mono('class Mascota', 159, 99, 19, m.papel, 800, 'center');
      var campos = ['private String id;', 'private String nombre;', 'private String especie;', 'private int edad;'];
      for (var i = 0; i < campos.length; i++) mono(campos[i], 40, 140 + i * 26, 16);
      var objs = [['luna', '"M-001" · "Luna" · "Canino" · 3'], ['michi', '"M-002" · "Michi" · "Felino" · 5']];
      for (var k = 0; k < 2; k++) {
        var oy = 90 + k * 86;
        L.flecha(ctx, 298, 169, 410, oy + 36, C, 4, 1);
        L.rectRed(ctx, 416, oy, 360, 72, 12); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        mono(objs[k][0], 432, oy + 8, 18, V, 800);
        mono(objs[k][1], 432, oy + 38, 16, m.tinta, 600);
      }
      UJ.rotulo(ctx, lz, 'new', 342, 116, { tam: 17, peso: 800, color: C });
      UJ.rotulo(ctx, lz, 'new', 342, 200, { tam: 17, peso: 800, color: C });

      // 2 · main los crea
      UJ.rotulo(ctx, lz, '2 · main los crea con datos distintos', 24, 268, { tam: 20, peso: 800, color: A, alinear: 'left' });
      UJ.codigo(ctx, lz, 24, 302, 752, 'Mascota luna  = new Mascota("M-001", "Luna", "Canino", 3);', 1, 16);
      UJ.codigo(ctx, lz, 24, 338, 752, 'Mascota michi = new Mascota("M-002", "Michi", "Felino", 5);', 1, 16);
      UJ.codigo(ctx, lz, 24, 374, 752, 'luna.setEdad(-2);', 1, 16);

      // 3 · La consola
      UJ.rotulo(ctx, lz, '3 · La consola', 24, 424, { tam: 20, peso: 800, color: A, alinear: 'left' });
      L.rectRed(ctx, 24, 456, 440, 166, 10); L.rellena(ctx, OSC);
      var sal = ['Pacientes registrados hoy en la clinica:', 'M-001 - Luna (Canino, 3 anios)', 'M-002 - Michi (Felino, 5 anios)', 'Edad invalida, se conserva la anterior: 3'];
      var colS = ['#E8F4FA', L.tono(V, 0.55), L.tono(V, 0.55), L.tono(m.sello || C, 0.2)];
      for (var j = 0; j < sal.length; j++) mono(sal[j], 38, 470 + j * 36, 16, colS[j], j ? 700 : 500);
      // Lo que se mira
      L.trazo(ctx, [[470, 518], [478, 518], [478, 574], [470, 574]], 1, V, 3);
      L.rectRed(ctx, 490, 500, 286, 64, 12); L.rellena(ctx, L.tono(V, 0.88), V, 2);
      UJ.rotulo(ctx, lz, 'mismo molde,', 633, 508, { tam: 17, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'cada objeto con sus datos', 633, 534, { tam: 16, peso: 600 });
      L.rectRed(ctx, 490, 574, 286, 48, 12); L.rellena(ctx, L.tono(m.sello || C, 0.75), L.tono(m.sello || C, -0.4), 2);
      UJ.rotulo(ctx, lz, 'setEdad(-2): el objeto se defiende', 633, 588, { tam: 15, peso: 700, ancho: 270 });
    }
  });
})();
