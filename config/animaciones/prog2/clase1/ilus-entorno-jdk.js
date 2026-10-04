/* Ilustracion: el entorno en tres piezas. 1) JDK de soporte extendido (17 o 21), verificado con
 * java -version en la consola. 2) Una clase publica por archivo, con el mismo nombre caracter por
 * caracter: Mascota vive en Mascota.java (mascota.java no compila, con el mensaje real de javac).
 * 3) javac compila el .java a .class (bytecode) y java lo ejecuta en la JVM; el IDE hace ambos
 * pasos por dentro. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-entorno-jdk', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, V = m.verde || A, R = m.malva || '#A02030', W = lz.ancho;
      var MONO = 'Consolas, monospace', OSC = L.tono(m.tinta, -0.55);
      function mono(s, x, y, tam, color, peso, alinear) {
        L.texto(ctx, s, x, y, { tam: tam, peso: peso || 500, color: color || m.tinta, letra: MONO, alinear: alinear || 'left' });
      }
      function archivo(x, y, w, h, nombre, color) {
        // Hoja con la esquina doblada
        var d = 22;
        ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + w - d, y); ctx.lineTo(x + w, y + d);
        ctx.lineTo(x + w, y + h); ctx.lineTo(x, y + h); ctx.closePath();
        L.rellena(ctx, m.papel, color, 3);
        ctx.beginPath(); ctx.moveTo(x + w - d, y); ctx.lineTo(x + w - d, y + d); ctx.lineTo(x + w, y + d);
        L.rellena(ctx, L.tono(color, 0.8), color, 2);
        mono(nombre, x + 14, y + 10, 18, color, 800);
      }

      // ---------------- 1 · El JDK
      UJ.rotulo(ctx, lz, '1 · JDK 17 o 21 (soporte extendido)', 24, 14, { tam: 21, peso: 800, color: A, alinear: 'left' });
      L.rectRed(ctx, 24, 52, 440, 84, 10); L.rellena(ctx, OSC);
      mono('> java -version', 40, 64, 18, '#E8F4FA', 700);
      mono('openjdk version "21.0.4" … LTS', 40, 96, 17, L.tono(m.sello || C, 0.2), 500);
      UJ.sello(ctx, lz, 500, 94, 22, true, 1);
      UJ.rotulo(ctx, lz, 'se verifica en la consola,', 530, 70, { tam: 17, peso: 600, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'no en el instalador', 530, 96, { tam: 17, peso: 600, alinear: 'left' });

      // ---------------- 2 · Nombre de clase = nombre de archivo
      UJ.rotulo(ctx, lz, '2 · Una clase pública por archivo, con el mismo nombre', 24, 160, { tam: 21, peso: 800, color: A, alinear: 'left' });
      archivo(24, 198, 360, 100, 'Mascota.java', V);
      mono('public class Mascota {', 40, 240, 17, m.tinta, 600);
      mono('  …  }', 40, 266, 17, m.gris, 500);
      UJ.sello(ctx, lz, 370, 204, 22, true, 1);
      archivo(416, 198, 360, 100, 'mascota.java', R);
      mono('public class Mascota {', 432, 240, 17, m.tinta, 600);
      mono('  …  }', 432, 266, 17, m.gris, 500);
      UJ.sello(ctx, lz, 762, 204, 22, false, 1);
      UJ.rotulo(ctx, lz, 'error: class Mascota is public, should be declared in a file named Mascota.java',
                416, 306, { tam: 14, peso: 600, color: R, alinear: 'left', ancho: 360 });

      // ---------------- 3 · javac compila, java ejecuta
      UJ.rotulo(ctx, lz, '3 · javac compila, java ejecuta', 24, 362, { tam: 21, peso: 800, color: A, alinear: 'left' });
      var y = 404, h = 104;
      // .java
      archivo(24, y, 190, h, 'Mascota.java', A);
      UJ.rotulo(ctx, lz, 'código fuente', 119, y + 46, { tam: 16, peso: 600 });
      UJ.rotulo(ctx, lz, 'lo escribes tú', 119, y + 70, { tam: 15, color: m.gris });
      // flecha javac
      L.flecha(ctx, 220, y + 52, 296, y + 52, A, 4, 1);
      mono('javac', 258, y + 18, 17, A, 800, 'center');
      // .class
      archivo(302, y, 190, h, 'Mascota.class', C);
      UJ.rotulo(ctx, lz, 'bytecode', 397, y + 46, { tam: 16, peso: 600 });
      UJ.rotulo(ctx, lz, 'no se edita', 397, y + 70, { tam: 15, color: m.gris });
      // flecha java
      L.flecha(ctx, 498, y + 52, 574, y + 52, A, 4, 1);
      mono('java', 536, y + 18, 17, A, 800, 'center');
      // JVM
      L.rectRed(ctx, 580, y, 196, h, 14); L.rellena(ctx, L.tono(V, 0.86), V, 3);
      UJ.rotulo(ctx, lz, 'la JVM', 678, y + 14, { tam: 19, peso: 800, color: V });
      UJ.rotulo(ctx, lz, 'ejecuta el main', 678, y + 46, { tam: 16, peso: 600 });
      UJ.rotulo(ctx, lz, 'el programa corre', 678, y + 70, { tam: 15, color: m.gris });
      // Los dos comandos
      L.rectRed(ctx, 24, 524, 470, 40, 8); L.rellena(ctx, OSC);
      mono('> javac Mascota.java      > java Mascota', 38, 535, 16, '#E8F4FA', 600);
      // El IDE
      L.trazo(ctx, [[220, 580], [220, 592], [574, 592], [574, 580]], 1, L.tono(m.tinta, 0.35), 2);
      UJ.rotulo(ctx, lz, 'el IDE (el botón ▶) hace los dos pasos por dentro', 397, 600, { tam: 17, peso: 700, color: m.tinta });
    }
  });
})();
