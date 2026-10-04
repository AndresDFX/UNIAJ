/* Ilustracion: abstraccion y encapsulamiento, lado a lado. Abstraccion: de la mascota real se
 * queda lo que importa a la clinica (modelar es decidir que se ignora). Encapsulamiento: edad es
 * private; luna.edad = -2 no compila desde afuera y luna.setEdad(-2) entra por el metodo, que la
 * rechaza (la edad sigue en 3), como en el codigo de la demo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-abstraccion-encapsulamiento', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var MONO = 'Consolas, monospace';
      function mono(s, x, y, tam, color, peso, alinear) {
        L.texto(ctx, s, x, y, { tam: tam, peso: peso || 500, color: color || m.tinta, letra: MONO, alinear: alinear || 'left' });
      }
      // Divisor
      L.trazo(ctx, [[400, 20], [400, 520]], 1, L.tono(m.gris, 0.6), 2);

      // ---------------- Abstraccion (izquierda)
      UJ.rotulo(ctx, lz, 'Abstracción', 200, 14, { tam: 26, peso: 800, color: A });
      UJ.rotulo(ctx, lz, 'modelar es decidir qué se ignora', 200, 50, { tam: 17, peso: 600 });
      // La mascota real
      L.rectRed(ctx, 24, 84, 352, 214, 14); L.rellena(ctx, L.tono(m.gris, 0.9), m.gris, 2);
      UJ.rotulo(ctx, lz, 'La mascota real', 200, 94, { tam: 18, peso: 700, color: m.gris });
      var rasgos = [['nombre', 1], ['especie', 1], ['edad', 1], ['historial', 1], ['color favorito', 0], ['juguete preferido', 0]];
      for (var i = 0; i < rasgos.length; i++) {
        var col = i % 2, fila = Math.floor(i / 2);
        var x = 44 + col * 168, y = 132 + fila * 52;
        var queda = rasgos[i][1];
        L.rectRed(ctx, x, y, 156, 40, 8); L.rellena(ctx, queda ? L.tono(V, 0.85) : m.papel, queda ? V : L.tono(m.gris, 0.4), 2);
        UJ.rotulo(ctx, lz, rasgos[i][0], x + 78, y + 9, { tam: 16, peso: queda ? 700 : 500, color: queda ? m.tinta : m.gris, ancho: 150 });
        if (!queda) {
          ctx.font = '500 16px ' + lz.letra; var an = ctx.measureText(rasgos[i][0]).width;
          L.trazo(ctx, [[x + 78 - an / 2 - 4, y + 20], [x + 78 + an / 2 + 4, y + 20]], 1, R, 2);
        }
      }
      L.flecha(ctx, 200, 302, 200, 344, A, 4, 1);
      UJ.rotulo(ctx, lz, 'lo que importa a la clínica', 214, 312, { tam: 15, peso: 600, color: A, alinear: 'left' });
      // La clase que queda
      L.rectRed(ctx, 50, 350, 300, 166, 14); L.rellena(ctx, L.tono(A, 0.9), A, 3);
      L.rectRed(ctx, 50, 350, 300, 42, 14); L.rellena(ctx, A);
      mono('class Mascota', 200, 360, 20, m.papel, 800, 'center');
      var campos = ['String nombre;', 'String especie;', 'int edad;', 'String historial;'];
      for (var k = 0; k < campos.length; k++) mono(campos[k], 70, 402 + k * 27, 17);

      // ---------------- Encapsulamiento (derecha)
      UJ.rotulo(ctx, lz, 'Encapsulamiento', 600, 14, { tam: 26, peso: 800, color: C });
      UJ.rotulo(ctx, lz, 'los datos no se tocan desde afuera', 600, 50, { tam: 17, peso: 600 });
      // Los dos intentos, desde afuera
      UJ.codigo(ctx, lz, 424, 86, 160, 'luna.edad = -2;', 1, 16);
      UJ.codigo(ctx, lz, 596, 86, 180, 'luna.setEdad(-2);', 1, 16);
      // El objeto, con su pared
      var ox = 424, oy = 214, ow = 352, oh = 206;
      L.rectRed(ctx, ox, oy, ow, oh, 16); L.rellena(ctx, L.tono(V, 0.9), A, 7);
      UJ.rotulo(ctx, lz, 'objeto luna', 506, oy + 18, { tam: 18, peso: 800, color: V });
      // La puerta: el metodo, que valida
      L.rectRed(ctx, 596, oy + 18, 164, 92, 10); L.rellena(ctx, A);
      mono('setEdad(int)', 678, oy + 28, 17, m.papel, 700, 'center');
      mono('if (edad < 0)', 678, oy + 54, 16, m.sello || m.papel, 700, 'center');
      UJ.rotulo(ctx, lz, 'rechaza', 678, oy + 80, { tam: 15, peso: 700, color: m.papel });
      // El dato, adentro
      L.flecha(ctx, 678, oy + 112, 678, oy + 144, A, 3, 1);
      UJ.rotulo(ctx, lz, 'si es válida, asigna', 664, oy + 118, { tam: 15, peso: 600, color: A, alinear: 'right' });
      L.rectRed(ctx, 444, oy + 148, 312, 44, 10); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.5), 2);
      mono('private int edad = 3;', 600, oy + 159, 18, m.tinta, 700, 'center');
      // Flecha 1: choca con la pared
      L.flecha(ctx, 504, 126, 504, oy - 8, R, 4, 1);
      UJ.sello(ctx, lz, 504, 164, 20, false, 1);
      // Flecha 2: entra por la puerta
      L.flecha(ctx, 686, 126, 686, oy + 14, A, 4, 1);
      UJ.rotulo(ctx, lz, 'entra por', 700, 146, { tam: 15, peso: 700, color: A, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'el método', 700, 166, { tam: 15, peso: 700, color: A, alinear: 'left' });
      // Resultados
      L.rectRed(ctx, 424, 434, 170, 88, 12); L.rellena(ctx, L.tono(R, 0.9), R, 2);
      UJ.rotulo(ctx, lz, 'luna.edad = -2', 509, 444, { tam: 16, peso: 800, color: R });
      UJ.rotulo(ctx, lz, 'no compila: edad es private', 509, 470, { tam: 16, ancho: 156 });
      L.rectRed(ctx, 606, 434, 170, 88, 12); L.rellena(ctx, L.tono(V, 0.88), V, 2);
      UJ.rotulo(ctx, lz, 'setEdad(-2)', 691, 444, { tam: 16, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'rechazada: la edad sigue en 3', 691, 470, { tam: 16, ancho: 156 });

      // Cierre
      L.rectRed(ctx, 24, 540, W - 48, 84, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Abstracción: QUÉ datos tiene la clase.', W / 2, 552, { tam: 20, peso: 800 });
      UJ.rotulo(ctx, lz, 'Encapsulamiento: QUIÉN puede cambiarlos, y con qué control.', W / 2, 586, { tam: 18, peso: 600, ancho: W - 80 });
    }
  });
})();
