/* Antes: una aplicacion por servidor fisico, cada uno usado entre el 5 y el 15 %. Despues: un
 * solo servidor con hipervisor y una maquina virtual por aplicacion, cada una con su SO. */
(function () {
  FP_ANIMADOR.registrar('un-servidor-por-app', {
    duracion: 5,
    pasos: [0.42, 1],
    dibujar: function (ctx, t, lz) {
      var els = [{ tipo: 'texto', t: 'Antes', x: 20, y: 14, tam: 26, peso: 800, alinear: 'left', color: 'accion', en: 0, sale: 0.47 }];
      var apps = ['Correo', 'Nómina', 'Web'], uso = [0.08, 0.12, 0.06];
      for (var i = 0; i < 3; i++) {
        var x = 30 + i * 255;
        els.push({ tipo: 'caja', x: x, y: 70, w: 230, h: 120, t: apps[i], s: 'servidor físico propio', color: 'gris', tam: 22, en: 0.03 + i * 0.05, sale: 0.47 });
        els.push({ tipo: 'barra', x: x + 10, y: 205, w: 160, h: 22, valor: uso[i], r: Math.round(uso[i] * 100) + ' %', color: 'malva', en: 0.18 + i * 0.03, sale: 0.47 });
      }
      els.push({ tipo: 'texto', t: 'Cada servidor trabaja entre el 5 y el 15 % de su capacidad.', x: 400, y: 280, tam: 23, ancho: 720, en: 0.3, sale: 0.47 });
      els.push({ tipo: 'texto', t: 'Con virtualización', x: 20, y: 14, tam: 26, peso: 800, alinear: 'left', color: 'accion', en: 0.5 });
      for (var k = 0; k < 3; k++) {
        var vx = 60 + k * 230;
        els.push({ tipo: 'caja', x: vx, y: 70, w: 210, h: 90, t: apps[k], color: 'sello', tam: 22, en: 0.62 + k * 0.05 });
        els.push({ tipo: 'caja', x: vx, y: 170, w: 210, h: 75, t: 'SO completo', s: 'máquina virtual', color: 'acento', tam: 20, tamSub: 16, en: 0.6 + k * 0.05 });
      }
      els.push({ tipo: 'caja', x: 60, y: 260, w: 670, h: 70, t: 'Hipervisor', color: 'acento', lleno: true, tam: 24, en: 0.55 });
      els.push({ tipo: 'caja', x: 60, y: 345, w: 670, h: 80, t: 'UN servidor físico', color: 'gris', lleno: true, tam: 24, en: 0.52 });
      els.push({ tipo: 'texto', t: 'Varias máquinas lógicas sobre el mismo hardware.', x: 400, y: 470, tam: 24, ancho: 720, en: 0.82 });
      els.push({ tipo: 'texto', t: 'Cada máquina virtual carga un sistema operativo entero.', x: 400, y: 530, tam: 22, ancho: 720, color: 'malva', en: 0.9 });
      UJ.escena(ctx, t, lz, els);
    }
  });
})();
