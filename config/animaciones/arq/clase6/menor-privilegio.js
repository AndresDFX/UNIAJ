/* Menor privilegio es una RESTA: el rol de la API puede leer, insertar y actualizar sus tablas, y
 * NO puede borrar, alterar la estructura ni leer otros esquemas. Si hay una inyeccion de SQL, el
 * atacante hereda esos permisos, no los del dueno de la base. */
(function () {
  FP_ANIMADOR.registrar('menor-privilegio', {
    duracion: 5,
    pasos: [0.3, 0.62, 1],
    dibujar: function (ctx, t, lz) {
      var si = ['SELECT', 'INSERT', 'UPDATE'], no = ['DELETE', 'ALTER TABLE', 'otro esquema'];
      var e = [{ tipo: 'caja', x: 250, y: 20, w: 300, h: 90, t: 'Rol de la API de turnos', lleno: true, tam: 22, en: 0 }];
      for (var i = 0; i < 3; i++) {
        e.push({ tipo: 'caja', x: 60, y: 150 + i * 80, w: 260, h: 64, t: si[i], r: 10, tam: 22, en: 0.08 + i * 0.05 });
        e.push({ tipo: 'sello', x: 360, y: 182 + i * 80, r: 22, ok: true, en: 0.1 + i * 0.05 });
        e.push({ tipo: 'caja', x: 450, y: 150 + i * 80, w: 260, h: 64, t: no[i], color: 'malva', r: 10, tam: 22, en: 0.34 + i * 0.06 });
        e.push({ tipo: 'sello', x: 750, y: 182 + i * 80, r: 22, ok: false, en: 0.37 + i * 0.06 });
      }
      e.push({ tipo: 'texto', t: 'puede', x: 190, y: 118, tam: 20, color: 'accion', en: 0.08 });
      e.push({ tipo: 'texto', t: 'deja de poder', x: 580, y: 118, tam: 20, color: 'malva', en: 0.34 });
      e.push({ tipo: 'caja', x: 60, y: 430, w: 680, h: 100, t: 'Si aparece una inyección de SQL…', s: '…el atacante hereda los permisos del rol: hace daño, pero no borra el rastro ni tumba el esquema.', color: 'malva', tam: 22, tamSub: 18, en: 0.68 });
      e.push({ tipo: 'texto', t: 'No evita el ataque: acota el daño.', x: 400, y: 570, tam: 24, peso: 800, color: 'accion', en: 0.88 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
