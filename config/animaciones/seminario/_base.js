/* Copia de config/animaciones/_base.js (piezas comunes) + las piezas de Seminario al final. */
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
    L.texto(ctx, linea, x + 14, y + tam * 0.45, { tam: tam, peso: 500, color: '#E8F4FA', letra: 'Consolas, monospace', visible: visible, ancho: an - 20 });
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

/*
 * Piezas propias de Seminario de Sistemas (analisis y diseño): flechas con rotulo, tarjetas con
 * lista, pildoras, tachado, actor de casos de uso y elipse. Se cargan DESPUES de las comunes y
 * las amplian: `UJ.caja`, `UJ.tabla`, `UJ.rotulo`, `UJ.sello`… siguen igual.
 * Todo depende solo de los argumentos: nada de azar ni de reloj.
 */
(function (global) {
  'use strict';
  var L = global.FP_LIENZO, UJ = global.UJ;

  /** Ancho en px de un texto con la letra del lienzo. */
  function medir(ctx, lz, texto, tam, peso) {
    ctx.save(); ctx.font = (peso || 600) + ' ' + (tam || 20) + 'px ' + lz.letra;
    var w = ctx.measureText(String(texto)).width; ctx.restore(); return w;
  }

  /** Linea (continua o punteada) que se dibuja hasta la fraccion `p`. */
  function linea(ctx, x1, y1, x2, y2, color, grosor, p, punteada) {
    if (p !== undefined && p <= 0) return;
    ctx.save();
    if (punteada) ctx.setLineDash([10, 8]);
    L.trazo(ctx, [[x1, y1], [x1 + (x2 - x1) * (p === undefined ? 1 : p), y1 + (y2 - y1) * (p === undefined ? 1 : p)]], 1, color, grosor || 3);
    ctx.restore();
  }

  /**
   * Flecha que avanza con `p` (0..1), con un rotulo opcional en su punto medio que aparece al
   * final. `o`: { grosor, punteada, tam, colorRotulo, dy } .
   */
  function flecha(ctx, lz, x1, y1, x2, y2, color, p, rotulo, o) {
    o = o || {};
    if (p <= 0) return;
    var g = o.grosor || 3;
    if (o.punteada) {
      var a = Math.atan2(y2 - y1, x2 - x1), q = Math.min(1, p);
      var fx = x1 + (x2 - x1) * q, fy = y1 + (y2 - y1) * q;
      linea(ctx, x1, y1, fx - Math.cos(a) * g * 2, fy - Math.sin(a) * g * 2, color, g, 1, true);
      L.flecha(ctx, fx - Math.cos(a) * g * 3, fy - Math.sin(a) * g * 3, fx, fy, color, g, 1);
    } else {
      L.flecha(ctx, x1, y1, x2, y2, color, g, p);
    }
    if (rotulo && p >= 0.95) {
      var mx = (x1 + x2) / 2, my = (y1 + y2) / 2 + (o.dy === undefined ? -28 : o.dy);
      var tam = o.tam || 17, w = medir(ctx, lz, rotulo, tam, 600) + 16;
      L.rectRed(ctx, mx - w / 2, my - 2, w, tam + 10, 6); L.rellena(ctx, lz.marca.papel);
      UJ.rotulo(ctx, lz, rotulo, mx, my + 2, { tam: tam, peso: 600, color: o.colorRotulo || color });
    }
  }

  /** Pildora: texto dentro de un rectangulo redondeado a su medida. Devuelve su ancho. */
  function pildora(ctx, lz, x, y, texto, color, a, o) {
    o = o || {};
    var tam = o.tam || 18, w = medir(ctx, lz, texto, tam, o.peso || 700) + 28, h = tam + 16;
    var cx = o.centrar ? x - w / 2 : x;
    UJ.alfa(ctx, a === undefined ? 1 : a, function () {
      L.rectRed(ctx, cx, y, w, h, h / 2);
      if (o.lleno) L.rellena(ctx, color, null);
      else L.rellena(ctx, L.tono(color, 0.86), color, 2);
      UJ.rotulo(ctx, lz, texto, cx + w / 2, y + 8, { tam: tam, peso: o.peso || 700, color: o.lleno ? lz.marca.papel : L.tono(color, -0.25) });
    });
    return w;
  }

  /**
   * Tarjeta: banda de titulo y debajo una lista de lineas que aparecen una a una con `n`
   * (cuantas se ven; puede ser fraccion). `o`: { tam, mono, alto }.
   */
  function tarjeta(ctx, lz, x, y, an, titulo, lineas, color, a, n, o) {
    o = o || {};
    var tam = o.tam || 18, fila = o.fila || tam * 1.65, cab = tam + 22;
    var al = o.alto || (cab + 12 + lineas.length * fila + 6);
    UJ.alfa(ctx, a === undefined ? 1 : a, function () {
      L.rectRed(ctx, x, y, an, al, 12); L.rellena(ctx, lz.marca.papel, color, 2.5);
      L.rectRed(ctx, x, y, an, cab, 12); L.rellena(ctx, color);
      L.rectRed(ctx, x, y + cab - 12, an, 12, 0); L.rellena(ctx, color);
      UJ.rotulo(ctx, lz, titulo, x + an / 2, y + 10, { tam: tam + 1, peso: 800, color: lz.marca.papel, ancho: an - 16 });
      var vis = n === undefined ? lineas.length : n;
      for (var i = 0; i < lineas.length; i++) {
        var k = Math.max(0, Math.min(1, vis - i));
        if (k <= 0) continue;
        (function (i, k) {
          UJ.alfa(ctx, k, function () {
            L.texto(ctx, lineas[i], x + 14, y + cab + 10 + i * fila, { tam: tam, peso: 500, color: lz.marca.tinta,
              letra: o.mono ? 'Consolas, monospace' : lz.letra, ancho: an - 24 });
          });
        })(i, k);
      }
    });
    return y + al;
  }

  /** Tachado en aspa sobre un rectangulo, que crece con `p`. */
  function tachar(ctx, x, y, an, al, color, p) {
    if (p <= 0) return;
    var q1 = Math.min(1, p * 2), q2 = Math.max(0, p * 2 - 1);
    L.trazo(ctx, [[x, y], [x + an * q1, y + al * q1]], 1, color, 5);
    if (q2 > 0) L.trazo(ctx, [[x + an, y], [x + an - an * q2, y + al * q2]], 1, color, 5);
  }

  /** Raya horizontal sobre un texto (tachado de palabra), que avanza con `p`. */
  function rayar(ctx, x, y, an, color, p) {
    if (p <= 0) return;
    L.trazo(ctx, [[x, y], [x + an * Math.min(1, p), y]], 1, color, 4);
  }

  /** Actor de casos de uso (monigote) con su nombre debajo. `y` es la cabeza. */
  function monigote(ctx, lz, x, y, h, nombre, color, a) {
    UJ.alfa(ctx, a === undefined ? 1 : a, function () {
      var c = color || lz.marca.tinta, r = h * 0.14;
      ctx.lineWidth = 3; ctx.strokeStyle = c; ctx.lineCap = 'round';
      L.circulo(ctx, x, y + r, r); L.rellena(ctx, lz.marca.papel, c, 3);
      ctx.beginPath();
      ctx.moveTo(x, y + 2 * r); ctx.lineTo(x, y + h * 0.62);
      ctx.moveTo(x - h * 0.24, y + h * 0.38); ctx.lineTo(x + h * 0.24, y + h * 0.38);
      ctx.moveTo(x, y + h * 0.62); ctx.lineTo(x - h * 0.2, y + h);
      ctx.moveTo(x, y + h * 0.62); ctx.lineTo(x + h * 0.2, y + h);
      ctx.stroke();
      if (nombre) UJ.rotulo(ctx, lz, nombre, x, y + h + 6, { tam: 17, peso: 700, color: c, ancho: 150 });
    });
  }

  /** Elipse de caso de uso con su nombre centrado (una o dos lineas). */
  function elipse(ctx, lz, cx, cy, rx, ry, texto, color, a, o) {
    o = o || {};
    UJ.alfa(ctx, a === undefined ? 1 : a, function () {
      var c = color || lz.marca.accion;
      ctx.beginPath(); ctx.ellipse(cx, cy, rx, ry, 0, 0, Math.PI * 2);
      L.rellena(ctx, o.relleno || L.tono(c, 0.88), c, 2.5);
      var tam = o.tam || 17;
      var alto = L.texto(ctx, texto, -9999, -9999, { tam: tam, peso: 700, letra: lz.letra, ancho: rx * 1.6 });
      UJ.rotulo(ctx, lz, texto, cx, cy - alto / 2, { tam: tam, peso: 700, color: L.tono(c, -0.25), ancho: rx * 1.6 });
    });
  }

  UJ.medir = medir; UJ.linea = linea; UJ.flecha = flecha; UJ.pildora = pildora; UJ.tarjeta = tarjeta;
  UJ.tachar = tachar; UJ.rayar = rayar; UJ.monigote = monigote; UJ.elipse = elipse;
})(window);
