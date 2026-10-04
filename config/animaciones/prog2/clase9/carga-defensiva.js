/* Carga defensiva: las lineas del CSV pasan por cargar(); las sanas entran a la lista, la de 4
 * campos y la de edad «dos» (NumberFormatException) se avisan y se saltan; la app abre con el resto. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('carga-defensiva', {
    duracion: 4.8,
    pasos: [0.32, 0.64, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, G = m.gris, W = lz.ancho;
      var lineas = [
        ['M001;Luna;perro;3;1144556677', true, 'Luna'],
        ['M002;Michi;gato;2;1144556677', true, 'Michi'],
        ['M003;Rocky;perro;5', false, null],
        ['M004;Kira;gato;dos;1133224455', false, null],
        ['M005;Firulais;perro;7;1122334455', true, 'Firulais']
      ];
      var corre = [0.08, 0.17, 0.38, 0.5, 0.72];
      UJ.codigo(ctx, lz, 20, 14, W - 40, 'main: repo.cargar();  → solo después se muestra la ventana', L.tramo(t, 0, 0.06), 15);
      // El archivo
      UJ.alfa(ctx, L.tramo(t, 0, 0.05), function () {
        L.rectRed(ctx, 20, 64, 400, 300, 14); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.3), 3);
        UJ.rotulo(ctx, lz, 'mascotas.csv (ejemplo)', 220, 74, { tam: 18, peso: 800 });
        // La lista
        L.rectRed(ctx, 560, 64, 220, 300, 14); L.rellena(ctx, L.tono(V, 0.92), V, 3);
        UJ.rotulo(ctx, lz, 'lista en memoria', 670, 74, { tam: 18, peso: 800, color: V });
        L.rectRed(ctx, 440, 190, 100, 50, 10); L.rellena(ctx, L.tono(C, 0.88), C, 2);
        UJ.rotulo(ctx, lz, 'cargar()', 490, 204, { tam: 17, peso: 800, color: C });
      });
      var dentro = 0, avisos = [];
      for (var i = 0; i < lineas.length; i++) {
        var y = 110 + i * 50, ln = lineas[i], hecho = L.tramo(t, corre[i], corre[i] + 0.08);
        var activa = t >= corre[i] && t < corre[i] + 0.08;
        if (activa) { L.rectRed(ctx, 26, y - 6, 388, 34, 6); L.rellena(ctx, L.tono(m.sello, 0.6)); }
        UJ.rotulo(ctx, lz, (i + 1) + '', 40, y, { tam: 15, peso: 700, color: L.tono(m.tinta, 0.45) });
        L.texto(ctx, ln[0], 58, y, { tam: 16, peso: 500, color: hecho >= 1 && !ln[1] ? R : m.tinta, letra: 'Consolas, monospace' });
        if (hecho >= 1 && !ln[1]) { ctx.strokeStyle = R; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(58, y + 10); ctx.lineTo(58 + ln[0].length * 8.8, y + 10); ctx.stroke(); }
        if (activa) L.flecha(ctx, 420, y + 10, 438, 214, C, 3);
        if (ln[1]) {
          var a = L.tramo(t, corre[i] + 0.04, corre[i] + 0.08);
          if (a > 0) {
            var fy = 112 + dentro * 56;
            UJ.alfa(ctx, a, function () {
              L.rectRed(ctx, 580, fy, 180, 44, 10); L.rellena(ctx, m.papel, V, 2);
              UJ.rotulo(ctx, lz, ln[2], 670, fy + 11, { tam: 18, peso: 700, color: V });
            });
            dentro++;
          }
        } else if (hecho >= 1) avisos.push(i);
      }
      // Avisos en consola
      var textos = { 2: 'línea 3 ignorada: tiene 4 campos, se esperan 5', 3: 'línea 4 ignorada: edad «dos» → NumberFormatException' };
      UJ.alfa(ctx, L.tramo(t, 0.44, 0.48), function () {
        L.rectRed(ctx, 20, 384, W - 40, 100, 10); L.rellena(ctx, L.tono(m.tinta, -0.55));
        UJ.rotulo(ctx, lz, 'Consola', 36, 392, { tam: 15, peso: 700, alinear: 'left', color: L.tono(m.papel, 0, 0.7) });
      });
      for (var k = 0; k < avisos.length; k++) {
        L.texto(ctx, textos[avisos[k]], 36, 418 + k * 30, { tam: 16, peso: 600, color: L.tono(m.sello, 0.3), letra: 'Consolas, monospace' });
      }
      UJ.rotulo(ctx, lz, 'Se captura, se avisa y se sigue con el resto.', W / 2, 500, { tam: 19, peso: 700, color: R, ancho: W - 40, visible: L.tramo(t, 0.56, 0.62) });
      // Paso 3: la app abre
      UJ.alfa(ctx, L.tramo(t, 0.86, 0.92), function () {
        L.rectRed(ctx, 20, 540, W - 40, 80, 12); L.rellena(ctx, L.tono(V, 0.88), V, 3);
        UJ.rotulo(ctx, lz, 'La ventana abre con 3 mascotas', W / 2, 552, { tam: 22, peso: 800, color: V });
        UJ.rotulo(ctx, lz, 'Sin archivo: lista vacía, sin error.', W / 2, 586, { tam: 17, peso: 600 });
      });
    }
  });
})();
