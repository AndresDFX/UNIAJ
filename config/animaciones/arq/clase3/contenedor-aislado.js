/* El contenedor es un proceso aislado dentro del SO que ya existe: los namespaces le dan su
 * propia vista. Sin SO propio, el tamano cambia de escala: GB contra MB. */
(function () {
  FP_ANIMADOR.registrar('contenedor-aislado', {
    duracion: 5,
    pasos: [0.45, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'marco', x: 30, y: 20, w: 740, h: 330, t: 'Un solo sistema operativo anfitrión (kernel compartido)', color: 'acento', en: 0 },
        { tipo: 'caja', x: 60, y: 80, w: 210, h: 240, t: 'Contenedor A', s: 'sus procesos · su red · sus archivos', color: 'accion', tam: 22, tamSub: 18, en: 0.1 },
        { tipo: 'caja', x: 295, y: 80, w: 210, h: 240, t: 'Contenedor B', s: 'sus procesos · su red · sus archivos', color: 'accion', tam: 22, tamSub: 18, en: 0.18 },
        { tipo: 'caja', x: 530, y: 80, w: 210, h: 240, t: 'Contenedor C', s: 'sus procesos · su red · sus archivos', color: 'accion', tam: 22, tamSub: 18, en: 0.26 },
        { tipo: 'texto', t: 'Namespaces: cada uno ve solo lo suyo.', x: 400, y: 368, tam: 23, ancho: 740, en: 0.36 },
        { tipo: 'texto', t: 'Tamaño típico', x: 30, y: 430, tam: 23, peso: 800, alinear: 'left', color: 'accion', en: 0.5 },
        { tipo: 'barra', x: 250, y: 480, w: 440, h: 34, valor: 1, t: 'Máquina virtual', color: 'malva', en: 0.56, tam: 20 },
        { tipo: 'texto', t: 'GB', x: 705, y: 482, tam: 24, peso: 800, alinear: 'left', color: 'malva', en: 0.66 },
        { tipo: 'barra', x: 250, y: 545, w: 440, h: 34, valor: 0.02, t: 'Imagen Alpine', r: '5 a 10 MB', color: 'accion', en: 0.7, tam: 20 }
      ]);
    }
  });
})();
