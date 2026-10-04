/* La prueba de tres capas sobre una decision: el QUE, el POR QUE y A CAMBIO DE QUE. */
(function () {
  FP_ANIMADOR.registrar('tres-capas', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 200, h: 140, t: '1 · QUÉ', lleno: true, tam: 26, en: 0.02 },
        { tipo: 'caja', x: 235, y: 30, w: 545, h: 140, t: '', s: '«La app corre con un contenedor por servicio.»', tamSub: 22, en: 0.06 },
        { tipo: 'caja', x: 20, y: 200, w: 200, h: 140, t: '2 · POR QUÉ', lleno: true, color: 'acento', tam: 26, en: 0.32 },
        { tipo: 'caja', x: 235, y: 200, w: 545, h: 140, t: '', s: '«Porque la sostiene una sola persona sin presupuesto de nube.»', color: 'acento', tamSub: 22, en: 0.36 },
        { tipo: 'caja', x: 20, y: 370, w: 200, h: 140, t: '3 · A CAMBIO DE QUÉ', lleno: true, color: 'malva', tam: 22, en: 0.64 },
        { tipo: 'caja', x: 235, y: 370, w: 545, h: 140, t: '', s: '«Perdemos el aislamiento fuerte de una máquina virtual completa.»', color: 'malva', tamSub: 22, en: 0.68 },
        { tipo: 'texto', t: 'La tercera capa es la que se olvida, y la que sostiene el ADR.', x: 400, y: 560, tam: 22, peso: 700, ancho: 760, en: 0.86 }
      ]);
    }
  });
})();
