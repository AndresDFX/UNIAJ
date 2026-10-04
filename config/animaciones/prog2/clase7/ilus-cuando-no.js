/* Ilustracion: cuando el patron estorba. El Singleton pedido por dentro esconde la dependencia y
 * ensucia las pruebas; inyectarlo por constructor la deja a la vista. Una fabrica sin reglas es
 * ruido. Y la regla: primero el problema, despues el patron. */
(function () {
  var L = FP_LIENZO;
  FP_ANIMADOR.registrar('ilus-cuando-no', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var m = lz.marca, A = m.accion, C = m.acento, R = m.malva || '#A02030', V = m.verde || A, W = lz.ancho;
      UJ.rotulo(ctx, lz, 'Cuándo el patrón estorba', W / 2, 12, { tam: 26, peso: 800, color: A });
      function consecuencia(x, y, ok, frase) {
        UJ.sello(ctx, lz, x + 14, y + 12, 13, ok, 1);
        UJ.rotulo(ctx, lz, frase, x + 36, y, { tam: 17, peso: 600, alinear: 'left', color: ok ? V : R });
      }
      // 1. Singleton pedido por dentro
      UJ.rotulo(ctx, lz, 'El Singleton es una variable global', 24, 58, { tam: 20, peso: 800, alinear: 'left', color: R });
      UJ.codigo(ctx, lz, 24, 90, W - 48, 'ServicioCitas() { repo = RepositorioClinica.getInstancia(); }', 1, 16);
      consecuencia(24, 132, false, 'la firma esconde la dependencia');
      consecuencia(404, 132, false, 'la prueba hereda el estado anterior');
      // 2. Inyectar por constructor
      UJ.rotulo(ctx, lz, 'Mejor: inyectar por constructor', 24, 180, { tam: 20, peso: 800, alinear: 'left', color: V });
      UJ.codigo(ctx, lz, 24, 212, W - 48, 'ServicioCitas(RepositorioClinica repo) { this.repo = repo; }', 1, 16);
      consecuencia(24, 254, true, 'la firma dice lo que necesita');
      consecuencia(404, 254, true, 'la prueba le pasa uno limpio');
      // 3. Una fabrica sin reglas
      L.trazo(ctx, [[24, 298], [W - 24, 298]], 1, L.tono(m.tinta, 0.75), 2);
      UJ.rotulo(ctx, lz, 'Una fábrica sin reglas', 24, 312, { tam: 20, peso: 800, alinear: 'left', color: R });
      UJ.codigo(ctx, lz, 24, 344, W - 48, 'static Mascota crear(String nombre) { return new Mascota(nombre); }', 1, 16);
      consecuencia(24, 386, false, 'no decide nada: es una capa más de ruido');
      // 4. La regla: primero el problema
      L.trazo(ctx, [[24, 430], [W - 24, 430]], 1, L.tono(m.tinta, 0.75), 2);
      function flujo(x, a, b, ok) {
        var c = ok ? V : R;
        L.rectRed(ctx, x, 452, 130, 56, 12); L.rellena(ctx, L.tono(c, 0.88), c, 2);
        UJ.rotulo(ctx, lz, a, x + 65, 468, { tam: 19, peso: 800, color: c });
        L.flecha(ctx, x + 136, 480, x + 170, 480, c, 3, 1);
        L.rectRed(ctx, x + 176, 452, 130, 56, 12); L.rellena(ctx, L.tono(c, 0.88), c, 2);
        UJ.rotulo(ctx, lz, b, x + 241, 468, { tam: 19, peso: 800, color: c });
        UJ.sello(ctx, lz, x + 336, 480, 18, ok, 1);
      }
      flujo(24, 'problema', 'patrón', true);
      flujo(412, 'patrón', '¿problema?', false);
      UJ.rotulo(ctx, lz, 'Primero el problema, después el patrón; nunca al revés.', W / 2, 548,
                { tam: 22, peso: 800, color: A, ancho: W - 40 });
    }
  });
})();
