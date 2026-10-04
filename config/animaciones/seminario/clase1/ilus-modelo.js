/* Ilustracion: que es un modelo. Lo real lo tiene todo a la vez; el modelo deja fuera lo que no
 * responde SU pregunta. Un diagrama de casos de uso responde «quien hace que» para el dueño de
 * la clinica, y no responde cuanto tarda una busqueda: esa es otra pregunta, con otro modelo. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-modelo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva, V = m.verde, G = m.gris, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Un modelo responde una pregunta', W / 2, 12, { tam: 26, peso: 800, color: A });

      // Lo real: todo a la vez
      L.rectRed(ctx, 20, 64, 290, 330, 14); L.rellena(ctx, L.tono(G, 0.93), L.tono(G, 0.4), 2);
      UJ.rotulo(ctx, lz, 'Lo real: la clínica', 165, 76, { tam: 20, peso: 800, color: m.tinta });
      var cosas = ['dueños', 'mascotas', 'citas', 'vacunas', 'pagos', 'horarios', 'teléfonos', 'facturas',
                   'insumos', 'turnos', 'recetas', 'llamadas'];
      for (var i = 0; i < cosas.length; i++) {
        var col = i % 3, fil = Math.floor(i / 3);
        UJ.pildora(ctx, lz, 70 + col * 95, 118 + fil * 60, cosas[i], G, 1, { tam: 15, centrar: true });
      }
      UJ.rotulo(ctx, lz, 'todo, a la vez', 165, 360, { tam: 17, peso: 700, color: G });

      UJ.flecha(ctx, lz, 316, 230, 384, 230, A, 1, null, { grosor: 4 });
      UJ.rotulo(ctx, lz, 'deja fuera', 350, 250, { tam: 15, peso: 700, color: A });

      // El modelo: un diagrama de casos de uso
      L.rectRed(ctx, 392, 64, 388, 330, 14); L.rellena(ctx, L.tono(A, 0.94), A, 2.5);
      UJ.rotulo(ctx, lz, 'Diagrama de casos de uso', 586, 76, { tam: 20, peso: 800, color: A });
      UJ.monigote(ctx, lz, 450, 130, 92, 'Recepcionista', m.tinta, 1);
      UJ.elipse(ctx, lz, 650, 140, 110, 30, 'Agendar cita', A, 1, { tam: 16 });
      UJ.elipse(ctx, lz, 650, 218, 110, 30, 'Registrar mascota', A, 1, { tam: 16 });
      UJ.linea(ctx, 474, 168, 540, 144, m.tinta, 2);
      UJ.linea(ctx, 474, 168, 540, 214, m.tinta, 2);
      L.rectRed(ctx, 410, 270, 352, 44, 10); L.rellena(ctx, m.papel, L.tono(A, 0.5), 1.5);
      UJ.rotulo(ctx, lz, 'Pregunta: ¿quién hace qué?', 586, 281, { tam: 18, peso: 700, color: m.tinta });
      L.rectRed(ctx, 410, 324, 352, 44, 10); L.rellena(ctx, m.papel, L.tono(A, 0.5), 1.5);
      UJ.rotulo(ctx, lz, 'La hace: el dueño de la clínica', 586, 335, { tam: 18, peso: 700, color: m.tinta });

      // Lo que responde y lo que no
      L.rectRed(ctx, 20, 418, 760, 56, 12); L.rellena(ctx, L.tono(V, 0.9), V, 2);
      UJ.sello(ctx, lz, 52, 446, 18, true, 1);
      UJ.rotulo(ctx, lz, '¿Quién agenda las citas?', 84, 432, { tam: 19, peso: 700, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'lo responde', 764, 432, { tam: 18, peso: 800, color: V, alinear: 'right' });
      L.rectRed(ctx, 20, 486, 760, 56, 12); L.rellena(ctx, L.tono(R, 0.92), R, 2);
      UJ.sello(ctx, lz, 52, 514, 18, false, 1);
      UJ.rotulo(ctx, lz, '¿Cuánto tarda buscar un expediente?', 84, 500, { tam: 19, peso: 700, alinear: 'left' });
      UJ.rotulo(ctx, lz, 'otra pregunta, otro modelo', 764, 500, { tam: 18, peso: 800, color: R, alinear: 'right' });

      UJ.pildora(ctx, lz, W / 2, 568, 'El mapa no es el territorio', m.sello, 1, { tam: 20, centrar: true });
    }
  });
})();
