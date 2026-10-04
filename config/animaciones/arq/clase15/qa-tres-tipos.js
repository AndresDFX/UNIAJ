/* El Q&A tecnico tiene tres tipos de pregunta: verificacion, profundizacion e hipotetica. Si no se
 * sabe, «no lo medimos» mas como se mediria; inventar un dato se detecta con una pregunta. */
(function () {
  FP_ANIMADOR.registrar('qa-tres-tipos', {
    duracion: 5,
    pasos: [0.3, 0.6, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 20, w: 760, h: 120, t: 'Verificación', s: '«¿En qué línea del Dockerfile está la imagen base?»', tam: 24, tamSub: 20, en: 0.02 },
        { tipo: 'caja', x: 20, y: 160, w: 760, h: 120, t: 'Profundización', s: '«¿Por qué la base no está en el mismo contenedor que la API?»', color: 'acento', tam: 24, tamSub: 20, en: 0.32 },
        { tipo: 'caja', x: 20, y: 300, w: 760, h: 120, t: 'Hipotética', s: '«Si el tráfico se multiplica por diez, ¿qué se rompe primero?»', color: 'malva', tam: 24, tamSub: 20, en: 0.62 },
        { tipo: 'texto', t: '¿Y si no sé? «No lo medimos» + cómo se mediría.', x: 400, y: 460, tam: 22, peso: 700, color: 'accion', ancho: 760, en: 0.76 },
        { tipo: 'texto', t: 'Un dato inventado se cae con una pregunta de seguimiento.', x: 400, y: 530, tam: 21, color: 'malva', ancho: 760, en: 0.86 }
      ]);
    }
  });
})();
