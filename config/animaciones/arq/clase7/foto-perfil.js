/* La foto de perfil: la solucion ingenua la mete en una columna binaria; el diseno correcto pone
 * el archivo en almacenamiento de objetos y deja en la base una fila con la clave. Y no se guarda
 * en el disco del contenedor, que es efimero. */
(function () {
  FP_ANIMADOR.registrar('foto-perfil', {
    duracion: 5,
    pasos: [0.34, 0.72, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        { tipo: 'caja', x: 20, y: 30, w: 170, h: 110, t: 'foto.jpg', s: '2 MB', color: 'sello', en: 0 },
        { tipo: 'flecha', de: [195, 85], a: [300, 85], color: 'malva', en: 0.08, sale: 0.36 },
        { tipo: 'cilindro', x: 305, y: 20, w: 300, h: 140, t: 'Base de datos', s: 'columna binaria con la foto', color: 'malva', en: 0.12, sale: 0.36 },
        { tipo: 'tacha', x: 300, y: 20, w: 310, h: 140, en: 0.24, sale: 0.36 },
        { tipo: 'flecha', de: [195, 85], a: [450, 85], r: 'el archivo', dy: -32, en: 0.4 },
        { tipo: 'cilindro', x: 455, y: 20, w: 320, h: 150, t: 'Objetos', s: 'perfiles/ana-7f3c.jpg', color: 'acento', en: 0.44 },
        { tipo: 'cilindro', x: 80, y: 230, w: 400, h: 150, t: 'Base de datos', s: 'cliente 42 · foto = perfiles/ana-7f3c.jpg', color: 'accion', en: 0.56 },
        { tipo: 'flecha', de: [485, 300], a: [610, 175], r: 'solo la clave', dx: 70, dy: 10, ancho: 150, en: 0.62 },
        { tipo: 'caja', x: 80, y: 440, w: 300, h: 100, t: 'disco del contenedor', s: 'se pierde al reemplazarlo', color: 'gris', en: 0.76 },
        { tipo: 'tacha', x: 90, y: 530, w: 280, h: -80, simple: true, grosor: 4, en: 0.82 },
        { tipo: 'texto', t: 'Si no hay archivos, la respuesta correcta es «no necesito objetos».', x: 600, y: 455, tam: 20, ancho: 340, en: 0.9 }
      ]);
    }
  });
})();
