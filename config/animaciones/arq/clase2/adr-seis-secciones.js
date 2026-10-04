/* El ADR: un documento corto que registra UNA decision, en seis secciones rotuladas y en orden. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('adr-seis-secciones', {
    duracion: 5,
    // Pasos LOGICOS: 1) la identificacion: el documento, su Titulo con numero y su Estado con
    // fecha; 2) el porque y el que: Contexto (restricciones) y Decision (una frase); 3) el costo
    // de decidir: las dos Alternativas descartadas y las Consecuencias; 4) la regla: un ADR = una
    // decision.
    pasos: [0.26, 0.5, 0.74, 1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca;
      UJ.alfa(ctx, L.tramo(t, 0, 0.06), function () {
        L.rectRed(ctx, 150, 20, 500, 560, 16); L.rellena(ctx, m.papel, L.tono(m.tinta, 0.5), 2);
        UJ.rotulo(ctx, lz, 'ADR-001', 400, 40, { tam: 30, peso: 800, color: m.accion });
      });
      var sec = [['1 · Título', 'número consecutivo y tema'], ['2 · Estado', 'Aceptado + fecha'],
                 ['3 · Contexto', 'las restricciones'], ['4 · Decisión', 'una frase, un modelo'],
                 ['5 · Alternativas descartadas', 'exactamente dos, con motivo'], ['6 · Consecuencias', 'lo que se gana y lo que se pierde']];
      // Momento de entrada de cada seccion, agrupadas por idea (pares 1-2, 3-4, 5-6).
      var en = [0.08, 0.14, 0.3, 0.38, 0.54, 0.62];
      var els = [];
      for (var i = 0; i < 6; i++) {
        els.push({ tipo: 'caja', x: 180, y: 95 + i * 78, w: 440, h: 66, t: sec[i][0], s: sec[i][1], r: 10, tam: 21, tamSub: 17,
                   color: i === 3 ? 'malva' : 'accion', en: en[i] });
      }
      els.push({ tipo: 'texto', t: 'Un ADR = UNA decisión', x: 400, y: 588, tam: 26, peso: 800, color: 'malva', en: 0.8 });
      UJ.escena(ctx, t, lz, els);
    }
  });
})();
