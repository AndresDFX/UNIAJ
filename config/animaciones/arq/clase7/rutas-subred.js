/* Una subred es publica o privada por sus RUTAS, no por su nombre: la publica tiene camino de
 * entrada desde internet; a la privada nadie de afuera puede iniciarle una conexion. */
(function () {
  FP_ANIMADOR.registrar('rutas-subred', {
    duracion: 5,
    pasos: [0.35, 0.7, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 300, y: 10, w: 200, h: 70, t: 'Internet', color: 'gris', lleno: true, tam: 24, en: 0 },
        { tipo: 'marco', x: 30, y: 180, w: 340, h: 230, t: 'Subred pública', color: 'sello', en: 0.06 },
        { tipo: 'caja', x: 80, y: 260, w: 240, h: 90, t: 'Balanceador', s: '443', en: 0.1 },
        { tipo: 'flecha', de: [330, 85], a: [230, 255], r: 'hay ruta de entrada', dx: -150, dy: -32, ancho: 190, color: 'accion', grosor: 4, en: 0.18 },
        { tipo: 'sello', x: 345, y: 210, r: 22, ok: true, en: 0.28 },
        { tipo: 'marco', x: 430, y: 180, w: 340, h: 230, t: 'Subred privada', color: 'accion', en: 0.38 },
        { tipo: 'caja', x: 480, y: 260, w: 240, h: 90, t: 'API de turnos', s: '8080', en: 0.42 },
        { tipo: 'flecha', de: [470, 85], a: [560, 170], color: 'malva', punteada: true, grosor: 4, en: 0.48 },
        { tipo: 'tacha', x: 495, y: 110, w: 40, h: 40, en: 0.56 },
        { tipo: 'texto', t: 'sin ruta desde internet', x: 650, y: 95, tam: 19, color: 'malva', ancho: 220, en: 0.58 },
        { tipo: 'flecha', de: [325, 305], a: [475, 305], r: 'solo desde adentro', dy: 20, ancho: 160, en: 0.72 },
        { tipo: 'texto', t: 'Lo que la hace privada es que nadie de afuera puede iniciar la conexión.', x: 400, y: 450, tam: 22, ancho: 740, en: 0.84 },
        { tipo: 'texto', t: 'Llamar «privada» a una subred con ruta de entrada no la protege.', x: 400, y: 540, tam: 21, ancho: 740, color: 'malva', en: 0.9 }
      ]);
    }
  });
})();
