/* Trazabilidad: cada caja del Containers tiene su par en el Despliegue y su zona. El cliente y el
 * proveedor de correo son filas sin par: aparecen en los diagramas pero no se despliegan. */
(function () {
  FP_ANIMADOR.registrar('trazabilidad-tabla', {
    duracion: 5,
    pasos: [0.44, 0.75, 1],
    dibujar: function (ctx, t, lz) {
      var f = [['App web', 'App web (estático, 443)', 'Pública'],
               ['API de turnos', 'API de turnos (contenedor, 8080)', 'Privada'],
               ['Base de turnos', 'Base de turnos (gestionada, 5432)', 'Datos']];
      var e = [
        { tipo: 'caja', x: 20, y: 20, w: 240, h: 60, t: 'C4 Containers', lleno: true, r: 8, tam: 20, en: 0 },
        { tipo: 'caja', x: 270, y: 20, w: 330, h: 60, t: 'Despliegue', lleno: true, r: 8, tam: 20, en: 0.02 },
        { tipo: 'caja', x: 610, y: 20, w: 170, h: 60, t: 'Zona', lleno: true, color: 'acento', r: 8, tam: 20, en: 0.04 }
      ];
      for (var i = 0; i < 3; i++) {
        var y = 95 + i * 84, en = 0.08 + i * 0.1;
        e.push({ tipo: 'caja', x: 20, y: y, w: 240, h: 72, t: f[i][0], r: 8, tam: 19, en: en });
        e.push({ tipo: 'flecha', de: [262, y + 36], a: [268, y + 36], en: en + 0.02 });
        e.push({ tipo: 'caja', x: 270, y: y, w: 330, h: 72, t: f[i][1], r: 8, tam: 18, en: en + 0.03 });
        e.push({ tipo: 'caja', x: 610, y: y, w: 170, h: 72, t: f[i][2], color: 'acento', r: 8, tam: 19, en: en + 0.05 });
      }
      e.push({ tipo: 'caja', x: 20, y: 370, w: 240, h: 72, t: 'Cliente', color: 'gris', r: 8, tam: 19, en: 0.5 });
      e.push({ tipo: 'caja', x: 20, y: 452, w: 240, h: 72, t: 'Proveedor de correo', color: 'gris', r: 8, tam: 19, en: 0.54 });
      e.push({ tipo: 'texto', t: 'sin par: aparecen en los diagramas, no se despliegan dentro del sistema', x: 520, y: 420, tam: 20, ancho: 480, color: 'malva', en: 0.6 });
      e.push({ tipo: 'texto', t: 'El nombre se escribe igual en los dos diagramas.', x: 400, y: 570, tam: 23, peso: 800, color: 'accion', ancho: 760, en: 0.84 });
      UJ.escena(ctx, t, lz, e);
    }
  });
})();
