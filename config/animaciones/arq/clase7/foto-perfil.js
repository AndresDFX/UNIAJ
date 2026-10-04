/* La foto de perfil: la solucion ingenua la mete en una columna binaria; el diseno correcto pone
 * el archivo en almacenamiento de objetos y deja en la base una fila con la clave. Y no se guarda
 * en el disco del contenedor, que es efimero. Si no hay archivos, no se necesita objeto. */
(function () {
  FP_ANIMADOR.registrar('foto-perfil', {
    duracion: 5,
    // Pasos LOGICOS: 1) la solucion ingenua (el binario dentro de la base) y por que no,
    // 2) el diseno correcto (archivo en objetos, la base guarda solo la clave), 3) tampoco en el
    // disco del contenedor, que es efimero, 4) sin archivos, la respuesta es «no necesito objeto».
    pasos: [0.3, 0.66, 0.84, 1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [
        // 1) Ingenua: la foto dentro de la base (se va antes del paso 2)
        { tipo: 'caja', x: 20, y: 30, w: 170, h: 110, t: 'foto.jpg', s: '2 MB', color: 'sello', en: 0 },
        { tipo: 'flecha', de: [195, 85], a: [300, 85], color: 'malva', en: 0.04, sale: 0.34 },
        { tipo: 'cilindro', x: 305, y: 20, w: 300, h: 140, t: 'Base de datos', s: 'columna binaria con la foto', color: 'malva', en: 0.08, sale: 0.34 },
        { tipo: 'sello', x: 640, y: 90, r: 26, ok: false, en: 0.16, sale: 0.34 },
        { tipo: 'texto', t: 'infla la base y cada respaldo', x: 455, y: 175, tam: 19, color: 'malva', ancho: 340, en: 0.18, sale: 0.34 },
        // 2) Correcto: el archivo a objetos, la clave a la base
        { tipo: 'flecha', de: [195, 85], a: [450, 85], r: 'el archivo', dy: -32, en: 0.42 },
        { tipo: 'cilindro', x: 455, y: 20, w: 320, h: 150, t: 'Objetos', s: 'perfiles/ana-7f3c.jpg', color: 'acento', en: 0.44 },
        { tipo: 'cilindro', x: 80, y: 230, w: 400, h: 150, t: 'Base de datos', s: 'cliente 42 · foto = perfiles/ana-7f3c.jpg', color: 'accion', en: 0.48 },
        { tipo: 'flecha', de: [485, 300], a: [610, 175], r: 'solo la clave', dx: 70, dy: 10, ancho: 150, en: 0.52 },
        // 3) Tampoco en el disco del contenedor
        { tipo: 'caja', x: 80, y: 440, w: 300, h: 100, t: 'disco del contenedor', s: 'se pierde al reemplazarlo', color: 'gris', en: 0.7 },
        { tipo: 'sello', x: 380, y: 440, r: 24, ok: false, en: 0.74 },
        // 4) Sin archivos, no se necesita objeto
        { tipo: 'texto', t: 'Si no hay archivos, la respuesta correcta es «no necesito objeto».', x: 600, y: 455, tam: 20, ancho: 340, en: 0.88 }
      ]);
    }
  });
})();
