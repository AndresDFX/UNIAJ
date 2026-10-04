/* Right-sizing: la metrica es la utilizacion (lo pagado que de verdad se usa); la convencion apunta
 * al 40-70 % sostenido. Las tres acciones: reducir tamano o replicas, apagar por horario lo que no
 * es produccion y adelgazar la imagen. */
(function () {
  FP_ANIMADOR.registrar('right-sizing', {
    duracion: 5,
    // Pasos LOGICOS: 1) la metrica y el problema: hoy se usa el 12 % de lo pagado, 2) el ajuste:
    // con 1 vCPU la utilizacion entra al rango sano, 3) las tres acciones, cada una anclada en una
    // observacion. (El titulo de la lamina promete tres acciones: la tercera, adelgazar la imagen,
    // es la de las notas.)
    pasos: [0.36, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'texto', t: 'Utilización = lo que se usa / lo que se paga', x: 400, y: 14, tam: 23, peso: 800, color: 'accion', ancho: 760, en: 0 },
        { tipo: 'barra', x: 230, y: 90, w: 480, h: 40, valor: 0.12, t: 'Hoy: 4 vCPU', r: '12 %', color: 'malva', en: 0.06, tam: 20 },
        { tipo: 'texto', t: 'se paga capacidad que nadie usa', x: 470, y: 145, tam: 20, color: 'malva', en: 0.16 },
        { tipo: 'barra', x: 230, y: 230, w: 480, h: 40, valor: 0.48, t: 'Con 1 vCPU', r: '48 %', color: 'accion', en: 0.4, tam: 20 },
        { tipo: 'linea', pts: [[230 + 480 * 0.4, 215], [230 + 480 * 0.4, 285]], color: 'verde', grosor: 3, punteada: true, en: 0.46 },
        { tipo: 'linea', pts: [[230 + 480 * 0.7, 215], [230 + 480 * 0.7, 285]], color: 'verde', grosor: 3, punteada: true, en: 0.46 },
        { tipo: 'texto', t: 'rango sano: 40-70 % (convención)', x: 470, y: 295, tam: 19, en: 0.5 },
        { tipo: 'caja', x: 20, y: 370, w: 245, h: 130, t: '1 · Reducir', s: 'tamaño o número de réplicas', tam: 22, tamSub: 17, en: 0.72 },
        { tipo: 'caja', x: 278, y: 370, w: 245, h: 130, t: '2 · Apagar por horario', s: 'lo que no es producción', color: 'acento', tam: 22, tamSub: 17, en: 0.77 },
        { tipo: 'caja', x: 536, y: 370, w: 245, h: 130, t: '3 · Adelgazar la imagen', s: 'slim o alpine: menos MB por despliegue', color: 'verde', tam: 22, tamSub: 17, en: 0.82 },
        { tipo: 'texto', t: 'Cada acción, anclada en una observación.', x: 400, y: 560, tam: 22, peso: 700, ancho: 760, en: 0.9 }
      ]);
    }
  });
})();
