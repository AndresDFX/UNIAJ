/* Las dos pilas, de abajo hacia arriba: maquina virtual a la izquierda, contenedor a la derecha.
 * La caja que desaparece al pasar a contenedores es el sistema operativo invitado. */
(function () {
  FP_ANIMADOR.registrar('dos-pilas', {
    duracion: 5,
    pasos: [0.4, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Máquina virtual', x: 200, y: 14, tam: 26, peso: 800, color: 'accion', en: 0 },
        { tipo: 'caja', x: 30, y: 490, w: 340, h: 70, t: 'Hardware físico', color: 'gris', lleno: true, en: 0.03 },
        { tipo: 'caja', x: 30, y: 410, w: 340, h: 70, t: 'Hipervisor', color: 'acento', lleno: true, en: 0.09 },
        { tipo: 'caja', x: 30, y: 270, w: 165, h: 130, t: 'SO invitado A', s: 'completo', color: 'malva', en: 0.16 },
        { tipo: 'caja', x: 205, y: 270, w: 165, h: 130, t: 'SO invitado B', s: 'completo', color: 'malva', en: 0.2 },
        { tipo: 'caja', x: 30, y: 180, w: 165, h: 80, t: 'App A', color: 'sello', en: 0.26 },
        { tipo: 'caja', x: 205, y: 180, w: 165, h: 80, t: 'App B', color: 'sello', en: 0.3 },
        { tipo: 'texto', t: 'Contenedor', x: 600, y: 14, tam: 26, peso: 800, color: 'accion', en: 0.42 },
        { tipo: 'caja', x: 430, y: 490, w: 340, h: 70, t: 'Hardware físico', color: 'gris', lleno: true, en: 0.44 },
        { tipo: 'caja', x: 430, y: 410, w: 340, h: 70, t: 'SO anfitrión + motor', s: 'un solo kernel', color: 'acento', lleno: true, tamSub: 16, en: 0.5 },
        { tipo: 'caja', x: 430, y: 270, w: 340, h: 130, t: 'sin SO invitado', color: 'gris', en: 0.56, tam: 20 },
        { tipo: 'caja', x: 430, y: 180, w: 165, h: 80, t: 'App A', color: 'sello', en: 0.62 },
        { tipo: 'caja', x: 605, y: 180, w: 165, h: 80, t: 'App B', color: 'sello', en: 0.66 },
        { tipo: 'texto', t: 'Lo que desaparece es el sistema operativo invitado.', x: 400, y: 585, tam: 23, ancho: 760, color: 'malva', en: 0.8 }
      ]);
    }
  });
})();
