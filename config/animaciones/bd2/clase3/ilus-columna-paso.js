/* Ilustracion: la columna paso. Arriba, por que no basta WHEN OTHERS (se verifica el TEXTO con
 * SQLERRM ILIKE). Abajo, la misma tabla resultado_prueba con las dos lecturas legitimas de paso:
 * «coincidio con lo esperado» o «la operacion se completo». Se elige una y se declara. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-columna-paso', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'No basta con que falle: tiene que fallar por lo esperado', W / 2, 12, { tam: 20, peso: 800, color: A, ancho: W - 40 });
      UJ.codigo(ctx, lz, 20, 52, 370, 'paso := TRUE;  -- hubo error', 1, 15);
      UJ.sello(ctx, lz, 400, 67, 15, false, 1);
      UJ.codigo(ctx, lz, 430, 52, 350, "paso := SQLERRM ILIKE '%inactiva%';", 1, 15);
      UJ.sello(ctx, lz, 770, 67, 15, true, 1);
      UJ.rotulo(ctx, lz, 'un nombre de columna mal escrito también lanza error', 205, 92, { tam: 14, color: R, ancho: 360 });
      UJ.rotulo(ctx, lz, 'afirma que falló Y por qué', 605, 92, { tam: 14, color: V, ancho: 340 });
      // Las dos lecturas
      var casos = ['activa', 'inactiva', 'no existe', 'franja'];
      var lect = [['Lectura A · «coincidió con lo esperado»', ['t', 't', 't', 't'], A],
                  ['Lectura B · «la operación se completó»', ['t', 'f', 'f', 'f'], C]];
      for (var k = 0; k < 2; k++) {
        var x0 = 20 + k * 390;
        UJ.rotulo(ctx, lz, lect[k][0], x0 + 180, 140, { tam: 16, peso: 800, color: lect[k][2], ancho: 370 });
        L.rectRed(ctx, x0, 172, 370, 40, 8); L.rellena(ctx, lect[k][2]);
        L.texto(ctx, 'caso', x0 + 16, 182, { tam: 17, peso: 700, color: m.papel, letra: 'Consolas, monospace' });
        L.texto(ctx, 'paso', x0 + 290, 182, { tam: 17, peso: 700, color: m.papel, letra: 'Consolas, monospace' });
        for (var i = 0; i < 4; i++) {
          var y = 212 + i * 38;
          L.rectRed(ctx, x0, y, 370, 38, 0); L.rellena(ctx, i % 2 ? L.tono(lect[k][2], 0.94) : m.papel, L.tono(lect[k][2], 0.6), 1);
          L.texto(ctx, casos[i], x0 + 16, y + 9, { tam: 17, color: m.tinta, letra: 'Consolas, monospace' });
          L.texto(ctx, lect[k][1][i], x0 + 300, y + 9, { tam: 17, peso: 800, color: lect[k][1][i] === 't' ? V : R, letra: 'Consolas, monospace' });
        }
      }
      UJ.rotulo(ctx, lz, 'con el procedimiento correcto, las dos tablas son válidas', W / 2, 376, { tam: 16, ancho: W - 40 });
      // La regla
      L.rectRed(ctx, 20, 414, W - 40, 106, 14); L.rellena(ctx, L.tono(m.sello || C, 0.8), m.tinta, 2);
      UJ.rotulo(ctx, lz, 'Se elige UNA lectura para las cuatro filas', W / 2, 428, { tam: 21, peso: 800, ancho: W - 80 });
      UJ.rotulo(ctx, lz, 'y se declara en una línea junto a la tabla', W / 2, 464, { tam: 18, ancho: W - 80 });
      UJ.codigo(ctx, lz, 20, 540, W - 40, 'resultado_prueba(id_prueba SERIAL, caso, esperado, obtenido, paso BOOLEAN)', 1, 15);
      UJ.rotulo(ctx, lz, 'Un caso de error con paso = f en la lectura A es un hallazgo: el procedimiento dejó pasar algo.', W / 2, 584, { tam: 14, ancho: W - 40, color: R });
    }
  });
})();
