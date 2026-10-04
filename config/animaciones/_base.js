/*
 * Piezas comunes de las animaciones de Bases de Datos II: caja, tabla, linea de codigo, rotulo,
 * marca de rechazo y de aceptado. Todo sale de `lienzo.marca` (la paleta UNIAJC la pone
 * `capturar.mjs`) y depende solo de lo que se le pasa: nada de azar ni de reloj.
 */
(function (global) {
  'use strict';
  var L = global.FP_LIENZO;

  function alfa(ctx, a, fn) { if (a <= 0) return; ctx.save(); ctx.globalAlpha *= Math.min(1, a); fn(); ctx.restore(); }

  /** Una caja redondeada con titulo y subtitulo centrados. `a` la hace aparecer (0..1). */
  function caja(ctx, lz, x, y, an, al, titulo, sub, color, a) {
    alfa(ctx, a === undefined ? 1 : a, function () {
      var c = color || lz.marca.accion;
      L.rectRed(ctx, x, y, an, al, 14); L.rellena(ctx, L.tono(c, 0.88), c, 3);
      var tam = Math.min(26, al * 0.34);
      L.texto(ctx, titulo, x + an / 2, y + (sub ? al * 0.2 : al / 2 - tam * 0.62), { tam: tam, peso: 700, color: c, alinear: 'center', ancho: an - 16, letra: lz.letra });
      if (sub) L.texto(ctx, sub, x + an / 2, y + al * 0.2 + tam * 1.35, { tam: tam * 0.72, peso: 500, color: lz.marca.tinta, alinear: 'center', ancho: an - 20, letra: lz.letra });
    });
  }

  /** Una tabla: cabecera con su nombre y `filas` (texto por fila); `n` cuantas se ven (puede ser fraccion). */
  function tabla(ctx, lz, x, y, an, nombre, filas, n, color, resalta) {
    var c = color || lz.marca.accion, fila = 40, cab = 46;
    L.rectRed(ctx, x, y, an, cab, 10); L.rellena(ctx, c);
    L.texto(ctx, nombre, x + 16, y + 11, { tam: 22, peso: 700, color: lz.marca.papel, letra: lz.letra });
    var visibles = n === undefined ? filas.length : n;
    for (var i = 0; i < filas.length; i++) {
      var a = Math.max(0, Math.min(1, visibles - i));
      var fy = y + cab + i * fila;
      L.rectRed(ctx, x, fy, an, fila, 0);
      L.rellena(ctx, i % 2 ? L.tono(c, 0.94) : lz.marca.papel, L.tono(c, 0.6), 1);
      if (a > 0) alfa(ctx, a, function () {
        if (resalta === i) { L.rectRed(ctx, x + 2, fy + 2, an - 4, fila - 4, 4); L.rellena(ctx, L.tono(lz.marca.sello || c, 0.55)); }
        L.texto(ctx, filas[i], x + 16, fy + 9, { tam: 19, peso: 500, color: lz.marca.tinta, letra: 'Consolas, monospace', ancho: an - 24 });
      });
    }
    return y + cab + filas.length * fila;
  }

  /** Una linea de codigo en banda oscura, que se escribe con `visible` (0..1). */
  function codigo(ctx, lz, x, y, an, linea, visible, tam) {
    // Una linea que aun no empieza a escribirse no se dibuja: una banda vacia en pantalla
    // anuncia algo que el docente todavia no explico.
    if (visible !== undefined && visible <= 0) return;
    tam = tam || 20;
    L.rectRed(ctx, x, y, an, tam * 2, 8); L.rellena(ctx, L.tono(lz.marca.tinta, -0.55));
    // Sin `L.texto`: ese parte por espacios y se comia la sangria, que en codigo es contenido.
    var v = visible === undefined ? 1 : Math.max(0, Math.min(1, visible));
    ctx.font = '500 ' + tam + 'px Consolas, monospace'; ctx.fillStyle = '#E8F4FA';
    ctx.textAlign = 'left'; ctx.textBaseline = 'top';
    ctx.fillText(String(linea).slice(0, Math.round(String(linea).length * v)), x + 14, y + tam * 0.45, an - 24);
  }

  function rotulo(ctx, lz, frase, x, y, o) {
    o = o || {};
    return L.texto(ctx, frase, x, y, { tam: o.tam || 24, peso: o.peso || 600, color: o.color || lz.marca.tinta, alinear: o.alinear || 'center', ancho: o.ancho, letra: lz.letra, visible: o.visible });
  }

  /** Circulo con aspa (rechazado) o con visto (aceptado), que crece con `a`. */
  function sello(ctx, lz, x, y, r, ok, a) {
    if (a <= 0) return;
    var c = ok ? (lz.marca.verde || lz.marca.accion) : (lz.marca.malva || '#A02030');
    var e = L.curva.atras(Math.min(1, a));
    L.circulo(ctx, x, y, r * e); L.rellena(ctx, c);
    ctx.lineWidth = r * 0.22; ctx.strokeStyle = lz.marca.papel; ctx.lineCap = 'round';
    ctx.beginPath();
    if (ok) { ctx.moveTo(x - r * 0.45, y); ctx.lineTo(x - r * 0.1, y + r * 0.38); ctx.lineTo(x + r * 0.5, y - r * 0.35); }
    else { ctx.moveTo(x - r * 0.4, y - r * 0.4); ctx.lineTo(x + r * 0.4, y + r * 0.4); ctx.moveTo(x + r * 0.4, y - r * 0.4); ctx.lineTo(x - r * 0.4, y + r * 0.4); }
    if (e > 0.6) ctx.stroke();
  }

  /** Un rayo: el evento que dispara. */
  function rayo(ctx, x, y, h, color, a) {
    alfa(ctx, a, function () {
      ctx.beginPath();
      ctx.moveTo(x + h * 0.15, y); ctx.lineTo(x - h * 0.2, y + h * 0.55); ctx.lineTo(x + h * 0.05, y + h * 0.55);
      ctx.lineTo(x - h * 0.15, y + h); ctx.lineTo(x + h * 0.3, y + h * 0.4); ctx.lineTo(x + h * 0.05, y + h * 0.4);
      ctx.lineTo(x + h * 0.3, y); ctx.closePath(); ctx.fillStyle = color; ctx.fill();
    });
  }

  global.UJ = { alfa: alfa, caja: caja, tabla: tabla, codigo: codigo, rotulo: rotulo, sello: sello, rayo: rayo };
})(window);
