/* Ilustracion: que observar en la demo — en consola, buscar H-5000 (la ultima de 5.000 fichas)
 * recorriendo un ArrayList contra get() de un HashMap, medido con System.nanoTime(); despues la
 * misma busqueda desde la ventana Swing: un ID que existe y uno que no. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-demo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A,
          S = m.sello || C, G = m.gris || m.tinta, W = lz.ancho;
      var MONO = 'Consolas, monospace';
      UJ.rotulo(ctx, lz, 'Qué observar en la demo', W / 2, 12, { tam: 26, peso: 800, color: A });

      // 1 · Consola: lineal contra get
      UJ.rotulo(ctx, lz, '1 · Consola: buscar H-5000', 200, 64, { tam: 20, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'la última de 5.000 fichas: peor caso', 200, 96, { tam: 16 });
      // ArrayList
      UJ.rotulo(ctx, lz, 'ArrayList: recorre las 5.000', 24, 136, { tam: 17, peso: 700, color: R, alinear: 'left' });
      L.rectRed(ctx, 24, 166, 352, 34, 6); L.rellena(ctx, L.tono(R, 0.82), R, 2);
      UJ.rotulo(ctx, lz, 'muchos ns', 200, 172, { tam: 17, peso: 700 });
      // HashMap
      UJ.rotulo(ctx, lz, 'HashMap: get("H-5000")', 24, 222, { tam: 17, peso: 700, color: V, alinear: 'left' });
      L.rectRed(ctx, 24, 252, 34, 34, 6); L.rellena(ctx, L.tono(V, 0.75), V, 2);
      UJ.rotulo(ctx, lz, 'pocos ns: va directo', 70, 258, { tam: 17, peso: 700, alinear: 'left' });
      UJ.codigo(ctx, lz, 24, 312, 352, 'long t1 = System.nanoTime();', 1, 16);
      UJ.rotulo(ctx, lz, 'los ns exactos varían en cada corrida', 200, 364, { tam: 16, color: G });

      // separador
      ctx.strokeStyle = L.tono(m.tinta, 0.8); ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(400, 64); ctx.lineTo(400, 520); ctx.stroke();

      // 2 · La ventana
      UJ.rotulo(ctx, lz, '2 · Ventana: la misma búsqueda', 600, 64, { tam: 20, peso: 800, color: C });
      L.rectRed(ctx, 424, 100, 352, 150, 8); L.rellena(ctx, m.papel, m.tinta, 2);
      L.rectRed(ctx, 424, 100, 352, 32, 8); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'Buscar expediente', 438, 106, { tam: 16, peso: 700, color: m.papel, alinear: 'left' });
      L.rectRed(ctx, 440, 146, 150, 38, 4); L.rellena(ctx, m.papel, m.tinta, 2);
      L.texto(ctx, ' m-004 ', 448, 156, { tam: 18, peso: 600, color: m.tinta, letra: MONO });
      L.rectRed(ctx, 602, 146, 158, 38, 8); L.rellena(ctx, A);
      UJ.rotulo(ctx, lz, 'Buscar', 681, 155, { tam: 17, peso: 700, color: m.papel });
      L.rectRed(ctx, 440, 196, 320, 42, 6); L.rellena(ctx, L.tono(V, 0.86), V, 2);
      UJ.rotulo(ctx, lz, 'Nieve (Persa) · Sara Diaz', 600, 206, { tam: 17, peso: 700 });
      UJ.rotulo(ctx, lz, 'trim() + toUpperCase() → "M-004"', 600, 262, { tam: 16, peso: 700, color: A });
      // ID que no existe
      UJ.rotulo(ctx, lz, 'Un ID que no existe:', 600, 306, { tam: 17, peso: 700, color: R });
      L.rectRed(ctx, 444, 340, 312, 112, 10); L.rellena(ctx, m.papel, R, 2);
      L.rectRed(ctx, 444, 340, 312, 32, 10); L.rellena(ctx, L.tono(R, 0.82));
      UJ.rotulo(ctx, lz, 'Sin resultados', 458, 345, { tam: 16, peso: 700, color: R, alinear: 'left' });
      // icono de advertencia
      ctx.beginPath(); ctx.moveTo(484, 386); ctx.lineTo(504, 422); ctx.lineTo(464, 422); ctx.closePath();
      ctx.fillStyle = S; ctx.fill(); ctx.strokeStyle = m.tinta; ctx.lineWidth = 2; ctx.stroke();
      UJ.rotulo(ctx, lz, '!', 484, 398, { tam: 18, peso: 800 });
      UJ.rotulo(ctx, lz, 'No existe expediente', 520, 386, { tam: 17, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'con ID M-999', 520, 410, { tam: 17, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'get devolvió null: se avisa', 600, 466, { tam: 16, color: G });

      UJ.rotulo(ctx, lz, 'El botón solo lee el ID y llama a get(); el mapa hace la búsqueda.', W / 2, 560,
                { tam: 19, peso: 700, ancho: W - 40 });
    }
  });
})();
