/* Ilustracion: que trae dentro cada paquete. La imagen de una maquina virtual lleva todo, kernel
 * incluido; la imagen de contenedor son capas de solo lectura SIN kernel (usa el del anfitrion), y
 * el contenedor es la capa escribible que se pone encima al ejecutarla. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-vm-vs-contenedor', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, S = m.sello || C, R = m.malva || '#A02030',
          G = m.gris || '#666666', W = lz.ancho;
      UJ.rotulo(ctx, lz, '¿Qué trae dentro cada uno?', W / 2, 14, { tam: 26, peso: 800, color: A });

      function bloque(x, y, w, h, tit, sub, color, lleno) {
        UJ.escena(ctx, 1, lz, [{ tipo: 'caja', x: x, y: y, w: w, h: h, t: tit, s: sub, color: color, lleno: lleno, tam: 19, tamSub: 15, r: 10 }]);
      }
      function llave(x, y1, y2, texto, color) {
        ctx.strokeStyle = color; ctx.lineWidth = 3; ctx.lineCap = 'round';
        ctx.beginPath(); ctx.moveTo(x, y1); ctx.lineTo(x + 10, y1); ctx.lineTo(x + 10, y2); ctx.lineTo(x, y2);
        ctx.moveTo(x + 10, (y1 + y2) / 2); ctx.lineTo(x + 18, (y1 + y2) / 2); ctx.stroke();
        UJ.rotulo(ctx, lz, texto, x + 24, (y1 + y2) / 2 - 30, { tam: 16, peso: 700, color: color, alinear: 'left', ancho: 92 });
      }

      // Maquina virtual: todo viaja dentro, kernel incluido
      UJ.rotulo(ctx, lz, 'Máquina virtual', 150, 72, { tam: 22, peso: 800, color: R });
      UJ.escena(ctx, 1, lz, [{ tipo: 'chip', x: 330, y: 72, t: 'GB', color: 'malva', tam: 17 }]);
      bloque(24, 116, 260, 62, 'Aplicación', null, 'sello', false);
      bloque(24, 186, 260, 62, 'Librerías', null, 'acento', false);
      bloque(24, 256, 260, 62, 'SO completo', 'servicios, utilidades', 'malva', false);
      bloque(24, 326, 260, 62, 'Kernel propio', null, 'malva', true);
      llave(292, 116, 388, 'todo va en la imagen', R);

      // Contenedor: capas de solo lectura, sin kernel; la capa escribible es el contenedor
      UJ.rotulo(ctx, lz, 'Contenedor', 540, 72, { tam: 22, peso: 800, color: A });
      UJ.escena(ctx, 1, lz, [{ tipo: 'chip', x: 680, y: 72, t: 'MB', color: 'accion', tam: 17 }]);
      ctx.setLineDash([10, 7]);
      L.rectRed(ctx, 410, 116, 260, 62, 10); L.rellena(ctx, L.tono(S, 0.75), L.tono(m.tinta, 0.2), 3);
      ctx.setLineDash([]);
      UJ.centrado(ctx, lz, 410, 116, 260, 62, 'Capa escribible', '= el contenedor', m.tinta, 19, 15);
      bloque(410, 186, 260, 62, 'Código de la app', null, 'accion', false);
      bloque(410, 256, 260, 62, 'Dependencias', null, 'accion', false);
      bloque(410, 326, 260, 62, 'Base, p. ej. Alpine', 'sin kernel', 'accion', false);
      llave(678, 186, 388, 'imagen: capas de solo lectura', A);
      llave(678, 116, 178, 'al ejecutar', G);

      // El kernel que usa el contenedor esta FUERA de su imagen
      L.flecha(ctx, 540, 392, 540, 446, A, 4, 1);
      UJ.rotulo(ctx, lz, 'lo usa prestado', 552, 404, { tam: 16, peso: 700, color: A, alinear: 'left' });
      bloque(410, 450, 260, 58, 'Kernel del anfitrión', null, 'gris', true);

      // Regla
      L.rectRed(ctx, 24, 530, 752, 92, 14); L.rellena(ctx, L.tono(C, 0.9), C, 2);
      UJ.rotulo(ctx, lz, 'Imagen Linux → necesita un kernel Linux debajo', W / 2, 546, { tam: 21, peso: 800, color: L.tono(C, -0.45) });
      UJ.rotulo(ctx, lz, 'En Windows o macOS lo pone una VM Linux.', W / 2, 584, { tam: 17 });
    }
  });
})();
