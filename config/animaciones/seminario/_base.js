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

/*
 * DG: piezas para dibujar lo que renderiza un codigo Mermaid (flowchart, classDiagram,
 * sequenceDiagram, gantt) junto a la lamina que lo proyecta. Formas de nodo, subgrafos,
 * flechas con rotulo sobre fondo blanco, clases con compartimentos, lineas de vida y marcas
 * numeradas para las reglas. Todo estatico: se usan con `pasos: [1]`.
 */
(function (global) {
  'use strict';
  var L = global.FP_LIENZO;
  var NODO = '#E3EEF8', BORDE = '#095292', TXT = '#1A2B3C';

  /** Texto centrado en (cx,cy); `s` puede traer varias lineas separadas por salto. */
  function txtc(ctx, lz, s, cx, cy, tam, peso, color, ancho) {
    var lineas = String(s).split('\n'), alto = tam * 1.25 * lineas.length;
    for (var i = 0; i < lineas.length; i++)
      L.texto(ctx, lineas[i], cx, cy - alto / 2 + i * tam * 1.25, { tam: tam, peso: peso || 600, color: color || TXT, alinear: 'center', letra: lz.letra, ancho: ancho });
  }

  /** Nodo centrado en (cx,cy). forma: rect | redondo (stadium) | circulo | rombo. */
  function nodo(ctx, lz, cx, cy, w, h, texto, forma, o) {
    o = o || {};
    var f = o.relleno || NODO, b = o.borde || BORDE;
    ctx.save();
    if (forma === 'rombo') {
      ctx.beginPath(); ctx.moveTo(cx, cy - h / 2); ctx.lineTo(cx + w / 2, cy); ctx.lineTo(cx, cy + h / 2); ctx.lineTo(cx - w / 2, cy); ctx.closePath();
      L.rellena(ctx, o.relleno || '#FFF6D6', o.borde || '#B8860B', 2.5);
    } else if (forma === 'circulo') {
      ctx.beginPath(); ctx.ellipse(cx, cy, w / 2, h / 2, 0, 0, Math.PI * 2); L.rellena(ctx, f, b, 2.5);
    } else {
      L.rectRed(ctx, cx - w / 2, cy - h / 2, w, h, forma === 'redondo' ? h / 2 : 8); L.rellena(ctx, f, b, 2.5);
    }
    ctx.restore();
    txtc(ctx, lz, texto, cx, cy, o.tam || 16, o.peso || 600, o.color, o.ancho);
  }

  /** Subgrafo: recuadro claro con su titulo arriba. */
  function grupo(ctx, lz, x, y, w, h, titulo, o) {
    o = o || {};
    L.rectRed(ctx, x, y, w, h, 10); L.rellena(ctx, o.relleno || '#F6F8FB', o.borde || '#8FA6BD', 2);
    if (titulo) L.texto(ctx, titulo, x + w / 2, y + 8, { tam: o.tam || 15, peso: 700, color: o.color || '#3A5068', alinear: 'center', letra: lz.letra, ancho: w - 12 });
  }

  /** Rotulo sobre fondo blanco centrado en (x,y): la linea no lo cruza. */
  function etiqueta(ctx, lz, s, x, y, o) {
    o = o || {};
    var tam = o.tam || 14, lineas = String(s).split('\n'), w = 0;
    var letra = o.mono ? 'Consolas, monospace' : lz.letra;
    ctx.save(); ctx.font = (o.peso || 600) + ' ' + tam + 'px ' + letra;
    for (var i = 0; i < lineas.length; i++) w = Math.max(w, ctx.measureText(lineas[i]).width);
    ctx.restore();
    var h = tam * 1.25 * lineas.length + 6;
    L.rectRed(ctx, x - w / 2 - 6, y - h / 2, w + 12, h, 4); L.rellena(ctx, o.fondo || '#FFFFFF', o.marco || null, 1);
    for (var k = 0; k < lineas.length; k++)
      L.texto(ctx, lineas[k], x, y - h / 2 + 3 + k * tam * 1.25, { tam: tam, peso: o.peso || 600, color: o.color || '#333', alinear: 'center', letra: letra });
  }

  /**
   * Flecha por una polilinea `pts` ([[x,y],...]) con punta al final. `o`: { punteada, color,
   * grosor, rotulo, en: [x,y] del rotulo (por defecto el medio del tramo central), abierta,
   * sinPunta }.
   */
  function flecha(ctx, lz, pts, o) {
    o = o || {};
    var c = o.color || '#4A5A6A', g = o.grosor || 2.4;
    ctx.save(); ctx.strokeStyle = c; ctx.lineWidth = g; ctx.lineJoin = 'round';
    if (o.punteada) ctx.setLineDash([8, 6]);
    ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]);
    for (var i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]);
    ctx.stroke(); ctx.setLineDash([]);
    if (!o.sinPunta) {
      var a = pts[pts.length - 2], b = pts[pts.length - 1], ang = Math.atan2(b[1] - a[1], b[0] - a[0]), t = 12;
      ctx.beginPath(); ctx.moveTo(b[0], b[1]);
      ctx.lineTo(b[0] - t * Math.cos(ang - 0.42), b[1] - t * Math.sin(ang - 0.42));
      if (o.abierta) { ctx.moveTo(b[0], b[1]); ctx.lineTo(b[0] - t * Math.cos(ang + 0.42), b[1] - t * Math.sin(ang + 0.42)); ctx.stroke(); }
      else { ctx.lineTo(b[0] - t * Math.cos(ang + 0.42), b[1] - t * Math.sin(ang + 0.42)); ctx.closePath(); ctx.fillStyle = c; ctx.fill(); }
    }
    ctx.restore();
    if (o.rotulo) {
      var p = o.en;
      if (!p) { var m = Math.floor((pts.length - 1) / 2), p0 = pts[m], p1 = pts[m + 1]; p = [(p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2]; }
      etiqueta(ctx, lz, o.rotulo, p[0], p[1], { tam: o.tam || 14, color: o.colorRotulo || '#333', mono: o.mono });
    }
  }

  /** Marca numerada (circulo amarillo) con su regla al lado (a la izquierda con `izq`). */
  function marca(ctx, lz, x, y, n, txt, ancho, izq) {
    L.circulo(ctx, x, y, 14); L.rellena(ctx, lz.marca.sello || '#FFD000', '#333', 2);
    L.texto(ctx, String(n), x, y - 10, { tam: 17, peso: 800, color: '#333', alinear: 'center', letra: lz.letra });
    if (txt) L.texto(ctx, txt, izq ? x - 22 : x + 22, y - 10, { tam: 14, peso: 700, color: lz.marca.tinta, ancho: ancho || 220, alinear: izq ? 'right' : 'left', letra: lz.letra });
  }

  /** Clase UML con compartimentos: nombre, atributos, metodos. Devuelve la altura. */
  function clase(ctx, lz, x, y, w, nombre, atrs, mets, o) {
    o = o || {};
    var tam = o.tam || 14, fila = tam * 1.45, cab = 34;
    var vacia = !atrs && !mets;
    var hA = atrs && atrs.length ? atrs.length * fila + 10 : 12, hM = mets && mets.length ? mets.length * fila + 10 : 12;
    var h = vacia ? cab + 4 : cab + hA + hM;
    L.rectRed(ctx, x, y, w, h, 4); L.rellena(ctx, NODO, BORDE, 2.5);
    L.texto(ctx, nombre, x + w / 2, y + 8, { tam: 17, peso: 800, color: TXT, alinear: 'center', letra: lz.letra });
    if (!vacia) {
      L.trazo(ctx, [[x, y + cab], [x + w, y + cab]], 1, BORDE, 2);
      L.trazo(ctx, [[x, y + cab + hA], [x + w, y + cab + hA]], 1, BORDE, 2);
      (atrs || []).forEach(function (s, i) { L.texto(ctx, s, x + 10, y + cab + 6 + i * fila, { tam: tam, peso: 500, color: TXT, letra: 'Consolas, monospace' }); });
      (mets || []).forEach(function (s, i) { L.texto(ctx, s, x + 10, y + cab + hA + 6 + i * fila, { tam: tam, peso: 500, color: TXT, letra: 'Consolas, monospace' }); });
    }
    return h;
  }

  /** Participante de secuencia (caja o monigote) con su linea de vida hasta `yFin`. */
  function participante(ctx, lz, cx, y, w, nombre, yFin, actor) {
    ctx.save(); ctx.setLineDash([6, 6]); ctx.strokeStyle = '#8FA6BD'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(cx, y + 50); ctx.lineTo(cx, yFin); ctx.stroke(); ctx.restore();
    if (actor) {
      UJ.monigote(ctx, lz, cx, y - 8, 34, null, TXT);
      L.texto(ctx, nombre, cx, y + 30, { tam: 14, peso: 700, color: TXT, alinear: 'center', letra: lz.letra });
    } else nodo(ctx, lz, cx, y + 24, w, 46, nombre, 'rect', { tam: 13, ancho: w - 8 });
  }

  /** Mensaje de secuencia en la fila `y`: continuo (llamada) o punteado (respuesta). */
  function mensaje(ctx, lz, x1, x2, y, texto, resp, num) {
    flecha(ctx, lz, [[x1, y], [x2 + (x2 > x1 ? -2 : 2), y]], { punteada: resp, abierta: resp, color: '#333', grosor: 2 });
    // El rotulo se centra en la flecha, pero sin salirse del lienzo.
    ctx.save(); ctx.font = '600 13px ' + lz.letra; var mw = ctx.measureText(texto).width / 2 + 10; ctx.restore();
    var mx = Math.max(mw, Math.min(lz.ancho - mw, (x1 + x2) / 2));
    etiqueta(ctx, lz, texto, mx, y - 17, { tam: 13, peso: 600 });
    if (num) {
      var nx = x1 + (x2 > x1 ? 13 : -13);
      L.circulo(ctx, nx, y, 10); L.rellena(ctx, '#333');
      L.texto(ctx, String(num), nx, y - 8, { tam: 12, peso: 800, color: '#FFF', alinear: 'center', letra: lz.letra });
    }
  }

  /** Nota amarilla (note for de classDiagram). */
  function nota(ctx, lz, x, y, w, h, texto) {
    L.rectRed(ctx, x, y, w, h, 4); L.rellena(ctx, '#FFF5AD', '#C9B037', 2);
    txtc(ctx, lz, texto, x + w / 2, y + h / 2, 14, 500, '#333', w - 12);
  }

  global.DG = { nodo: nodo, grupo: grupo, etiqueta: etiqueta, flecha: flecha, marca: marca,
                clase: clase, participante: participante, mensaje: mensaje, nota: nota, txtc: txtc };
})(window);
