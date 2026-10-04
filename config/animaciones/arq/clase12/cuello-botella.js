/* Siempre hay un cuello de botella. Los tres candidatos tipicos: N+1 (50 registros, 51 viajes a la
 * base), el pool de conexiones (10 conexiones, 40 peticiones: 30 esperan con la CPU al 20 %) y el
 * proveedor externo llamado dentro de la peticion. */
(function () {
  FP_ANIMADOR.registrar('cuello-botella', {
    duracion: 5,
    // Pasos LOGICOS: 1) N+1 (51 viajes a la base), 2) el pool de conexiones agotado con la CPU
    // holgada, 3) el proveedor externo en la ruta y la conclusion. Cada candidato entero en su paso.
    pasos: [0.34, 0.66, 1],
    dibujar: function (ctx, t, lz) {
      var e = [
        { tipo: 'texto', t: 'N + 1', x: 30, y: 14, tam: 24, peso: 800, alinear: 'left', color: 'malva', en: 0 },
        { tipo: 'caja', x: 30, y: 60, w: 160, h: 90, t: 'API', s: 'listado', en: 0.02 },
        { tipo: 'cilindro', x: 600, y: 50, w: 170, h: 110, t: 'Base', color: 'acento', en: 0.04 }
      ];
      for (var i = 0; i < 6; i++) {
        e.push({ tipo: 'flecha', de: [195, 70 + i * 13], a: [595, 70 + i * 13], color: i ? 'malva' : 'accion', grosor: 2, en: 0.05 + i * 0.025 });
      }
      e.push({ tipo: 'texto', t: '50 registros = 51 viajes a la base', x: 400, y: 160, tam: 20, color: 'malva', en: 0.22 });
      e.push({ tipo: 'texto', t: 'Pool de conexiones', x: 30, y: 220, tam: 24, peso: 800, alinear: 'left', color: 'malva', en: 0.37 });
      e.push({ tipo: 'barra', x: 250, y: 270, w: 480, h: 32, valor: 1, t: 'pool (10)', r: '', color: 'malva', en: 0.4, tam: 19 });
      e.push({ tipo: 'texto', t: '10 ocupadas · 30 peticiones esperan turno', x: 490, y: 312, tam: 19, color: 'malva', ancho: 480, en: 0.46 });
      e.push({ tipo: 'barra', x: 250, y: 350, w: 480, h: 32, valor: 0.2, t: 'CPU de la API', r: '20 %', color: 'accion', en: 0.5, tam: 19 });
      e.push({ tipo: 'texto', t: 'Proveedor externo en la ruta', x: 30, y: 420, tam: 24, peso: 800, alinear: 'left', color: 'malva', en: 0.68 });
      e.push({ tipo: 'caja', x: 30, y: 465, w: 220, h: 80, t: 'POST /turnos', tam: 20, en: 0.7 });
      e.push({ tipo: 'flecha', de: [255, 505], a: [395, 505], r: 'espera al correo', dy: -30, color: 'malva', en: 0.72 });
      e.push({ tipo: 'caja', x: 400, y: 465, w: 170, h: 80, t: 'Correo', color: 'gris', tam: 20, en: 0.74 });
      e.push({ tipo: 'chip', x: 680, y: 485, t: 'sacarlo a una cola', color: 'accion', en: 0.8 });
      e.push({ tipo: 'texto', t: '«Todo está lento» no es un diagnóstico.', x: 400, y: 580, tam: 22, peso: 800, color: 'accion', en: 0.88 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
