/* Ilustracion: la inyeccion de SQL. El mismo texto del usuario por dos caminos: pegado dentro de
 * la sentencia (el OR pasa a ser codigo y salen todos los duenos) o ligado como parametro (se
 * compara como valor y salen cero filas). */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-inyeccion', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, W = lz.ancho, R = m.malva || '#A02030', V = m.verde || A;
      UJ.rotulo(ctx, lz, 'El mismo texto del usuario, dos caminos', W / 2, 10, { tam: 25, peso: 800, color: A });
      // Lo que escribio el usuario
      L.rectRed(ctx, 150, 52, 500, 44, 10); L.rellena(ctx, L.tono(A, 0.92), A, 2);
      UJ.rotulo(ctx, lz, 'el usuario escribe:', 160, 64, { tam: 17, peso: 700, alinear: 'left', color: A });
      ctx.font = '700 20px Consolas, monospace'; ctx.fillStyle = m.tinta; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText("x' OR '1'='1", 380, 63);
      // Camino 1: concatenar
      UJ.rotulo(ctx, lz, '1 · Pegado dentro de la sentencia', 30, 120, { tam: 21, peso: 800, color: R, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 158, 500, "WHERE nombre = 'x' OR '1'='1'", 1, 18);
      L.rectRed(ctx, 30, 204, 500, 56, 8); L.rellena(ctx, L.tono(R, 0.92), R, 1);
      UJ.rotulo(ctx, lz, 'el OR quedó como parte del código: la condición es siempre verdadera', 280, 210, { tam: 16, peso: 600, ancho: 470 });
      L.flecha(ctx, 536, 190, 566, 190, R, 4, 1);
      L.rectRed(ctx, 572, 140, 200, 120, 14); L.rellena(ctx, L.tono(R, 0.9), R, 3);
      UJ.rotulo(ctx, lz, 'todos', 672, 156, { tam: 30, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'los dueños', 672, 200, { tam: 18, peso: 700 });
      UJ.sello(ctx, lz, 762, 142, 20, false, 1);
      // Separador
      ctx.strokeStyle = L.tono(m.tinta, 0.75); ctx.lineWidth = 2; ctx.setLineDash([8, 8]);
      ctx.beginPath(); ctx.moveTo(30, 300); ctx.lineTo(770, 300); ctx.stroke(); ctx.setLineDash([]);
      // Camino 2: parametro ligado
      UJ.rotulo(ctx, lz, '2 · Ligado como parámetro', 30, 322, { tam: 21, peso: 800, color: V, alinear: 'left' });
      UJ.codigo(ctx, lz, 30, 360, 500, 'WHERE nombre = $1   USING p_nombre', 1, 18);
      L.rectRed(ctx, 30, 406, 500, 56, 8); L.rellena(ctx, L.tono(V, 0.9), V, 1);
      UJ.rotulo(ctx, lz, "$1 vale «x' OR '1'='1» entero: se compara como un valor, nunca se ejecuta", 280, 412, { tam: 16, peso: 600, ancho: 470 });
      L.flecha(ctx, 536, 392, 566, 392, V, 4, 1);
      L.rectRed(ctx, 572, 342, 200, 120, 14); L.rellena(ctx, L.tono(V, 0.88), V, 3);
      UJ.rotulo(ctx, lz, '0 filas', 672, 358, { tam: 30, peso: 800, color: L.tono(V, -0.3) });
      UJ.rotulo(ctx, lz, 'nadie se llama así', 672, 402, { tam: 17, peso: 700 });
      UJ.sello(ctx, lz, 762, 344, 20, true, 1);
      // Regla
      L.rectRed(ctx, 30, 500, 740, 110, 14); L.rellena(ctx, L.tono(A, 0.9), A, 2);
      UJ.rotulo(ctx, lz, 'Escapar comillas a mano no equivale: basta olvidarlo una vez.', W / 2, 514, { tam: 19, peso: 700, ancho: 700 });
      UJ.rotulo(ctx, lz, 'El dato viaja aparte y el motor nunca lo lee como SQL.', W / 2, 562, { tam: 20, peso: 800, color: A, ancho: 700 });
    }
  });
})();
