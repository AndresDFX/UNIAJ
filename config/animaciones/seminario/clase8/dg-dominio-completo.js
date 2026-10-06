/* Lo que dibuja el codigo de «Modelo de dominio completo en Mermaid»: las cinco clases con sus
 * atributos y metodos, y las cuatro asociaciones con rotulo y multiplicidades. */
(function () {
  var L = FP_LIENZO;
  function mult(ctx, lz, s, x, y) { L.texto(ctx, s, x, y, { tam: 15, peso: 800, color: '#333', letra: lz.letra }); }
  FP_ANIMADOR.registrar('dg-dominio-completo', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var o = { tam: 13 }, xl = 15, wl = 355, xr = 445, wr = 340;
      var hD = DG.clase(ctx, lz, xl, 10, wl, 'Dueno', ['-documento: String', '-nombre: String'], ['+registrarMascota(m: Mascota) void'], o);
      var yM = 10 + hD + 70;
      var hM = DG.clase(ctx, lz, xl, yM, wl, 'Mascota', ['-codigo: String', '-especie: String', '-fechaNacimiento: Date'], ['+calcularEdad() int'], o);
      var yC = yM + hM + 70;
      var hC = DG.clase(ctx, lz, xl, yC, wl, 'Cita', ['-fechaHora: DateTime', '-estado: String'], ['+reprogramar(nuevaFecha: DateTime) void'], o);
      var yV = yM;
      var hV = DG.clase(ctx, lz, xr, yV, wr, 'Veterinario', ['-tarjetaProfesional: String', '-especialidad: String'], [], o);
      var hA = DG.clase(ctx, lz, xr, yC + 6, wr, 'Atencion', ['-diagnostico: String', '-tratamiento: String'], [], o);
      var cx = xl + wl / 2;
      DG.flecha(ctx, lz, [[cx, 10 + hD], [cx, yM - 1]], { abierta: true, rotulo: 'es dueno de', en: [cx, 10 + hD + 35] });
      mult(ctx, lz, '1', cx - 26, 10 + hD + 2); mult(ctx, lz, '0..*', cx - 46, yM - 22);
      DG.flecha(ctx, lz, [[cx, yM + hM], [cx, yC - 1]], { abierta: true, rotulo: 'tiene agendada', en: [cx, yM + hM + 35] });
      mult(ctx, lz, '1', cx - 26, yM + hM + 2); mult(ctx, lz, '0..*', cx - 46, yC - 22);
      DG.flecha(ctx, lz, [[xr + 60, yV + hV], [xr + 60, yC - 30], [xl + wl - 40, yC - 30], [xl + wl - 40, yC - 1]],
                { abierta: true, rotulo: 'atiende', en: [xr + 60, yV + hV + 30] });
      mult(ctx, lz, '1', xr + 68, yV + hV + 2); mult(ctx, lz, '0..*', xl + wl - 32, yC - 24);
      var ya = yC + 50;
      DG.flecha(ctx, lz, [[xl + wl, ya], [xr - 1, ya]], { abierta: true, rotulo: 'genera', en: [(xl + wl + xr) / 2, ya - 18] });
      mult(ctx, lz, '1', xl + wl + 6, ya + 4); mult(ctx, lz, '0..1', xr - 36, ya + 4);
      DG.marca(ctx, lz, 40, 580, 1, 'En Mermaid +calcularEdad() int  =  en UML +calcularEdad(): int', 700);
    }
  });
})();
