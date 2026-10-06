/* Lo que dibuja el molde «El Despliegue en Mermaid»: tres subgraph (zona publica, privada y de
 * datos), cada caja con su puerto, la base como cilindro y la pasarela de pagos fuera de las
 * zonas. Marcas: la base va en la zona de datos; la flecha al externo es la frontera de confianza. */
(function () {
  FP_ANIMADOR.registrar('dg-despliegue', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      MF.zona(ctx, lz, 20, 20, 300, 330, 'Zona publica - internet');
      MF.nodo(ctx, lz, 60, 70, 220, 80, 'App web\nReact estatico - 443');
      MF.nodo(ctx, lz, 60, 240, 220, 80, 'Edge / balanceador\n443 HTTPS');
      MF.zona(ctx, lz, 420, 20, 360, 170, 'Zona privada - solo desde el edge');
      MF.nodo(ctx, lz, 490, 80, 220, 80, 'API de turnos\n8080 HTTP');
      MF.zona(ctx, lz, 420, 260, 360, 190, 'Zona de datos - sin internet');
      MF.cilindro(ctx, lz, 500, 310, 200, 110, 'Base de turnos\n5432 TCP');
      MF.nodo(ctx, lz, 60, 520, 250, 70, 'Pasarela de pagos externa');
      MF.flecha(ctx, lz, [[170, 152], [170, 236]], { rot: 'HTTPS 443' });
      MF.flecha(ctx, lz, [[282, 280], [350, 280], [350, 110], [486, 110]], { rot: 'HTTP 8080', en: [350, 200] });
      MF.flecha(ctx, lz, [[600, 162], [600, 306]], { rot: 'TCP 5432', en: [600, 230] });
      MF.flecha(ctx, lz, [[488, 145], [400, 145], [400, 555], [314, 555]], { rot: 'HTTPS 443 -\nfrontera de confianza', en: [400, 505] });
      C4.marca(ctx, lz, 720, 300, 1, '');
      C4.marca(ctx, lz, 400, 455, 2, '');
      C4.marca(ctx, lz, 470, 540, 1, 'La base va aquí: sin internet, solo la API llega por el 5432', 290);
      C4.marca(ctx, lz, 470, 598, 2, 'La flecha al externo cruza la frontera de confianza', 290);
    }
  });
})();
