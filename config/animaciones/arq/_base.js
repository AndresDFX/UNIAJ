/*
 * Arquitectura: copia de las piezas comunes (config/animaciones/_base.js) mas UJ.escena (al
 * final), que dibuja una escena declarada como lista de elementos con su momento de entrada.
 */
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
 * UJ.escena(ctx, t, lz, elementos): cada elemento aparece en `en` (fundido de `dur`, 0.08 por
 * omision) y, si trae `sale`, se va desde ahi. Colores por NOMBRE de token: accion, acento,
 * verde, sello, malva, gris, tinta. Solo depende de `t`.
 *
 * Tipos: caja · cilindro · flecha · texto · chip · tacha · sello · barra · linea · marco ·
 * persona. Medidas en el lienzo de 800 x 640.
 */
(function (global) {
  'use strict';
  var L = global.FP_LIENZO, UJ = global.UJ;

  function col(lz, c, def) {
    var m = lz.marca;
    if (!c) return def || m.accion;
    if (c.charAt(0) === '#' || c.indexOf('rgb') === 0) return c;
    return m[c] || ({ malva: '#A02030', verde: m.accion, sello: m.acento, gris: '#666666' })[c] || m.accion;
  }

  function lineas(ctx, txt, tam, peso, ancho, letra) {
    ctx.font = (peso || 400) + ' ' + tam + 'px ' + letra;
    var pal = String(txt).split(/\s+/), n = 0, l = '';
    for (var i = 0; i < pal.length; i++) {
      var p = l ? l + ' ' + pal[i] : pal[i];
      if (ancho && ctx.measureText(p).width > ancho && l) { n++; l = pal[i]; } else l = p;
    }
    return n + (l ? 1 : 0);
  }

  /** Titulo y subtitulo centrados, en vertical y en horizontal, dentro de un rectangulo. */
  function centrado(ctx, lz, x, y, w, h, tit, sub, color, tam, tamSub, colorSub) {
    tam = tam || 22; tamSub = tamSub || Math.round(tam * 0.8);
    var nt = tit ? lineas(ctx, tit, tam, 700, w - 18, lz.letra) : 0;
    var ns = sub ? lineas(ctx, sub, tamSub, 500, w - 18, lz.letra) : 0;
    var alto = nt * tam * 1.3 + (sub ? 6 + ns * tamSub * 1.3 : 0);
    var y0 = y + (h - alto) / 2;
    if (tit) L.texto(ctx, tit, x + w / 2, y0, { tam: tam, peso: 700, color: color, alinear: 'center', ancho: w - 18, letra: lz.letra });
    if (sub) L.texto(ctx, sub, x + w / 2, y0 + nt * tam * 1.3 + 6, { tam: tamSub, peso: 500, color: colorSub || lz.marca.tinta, alinear: 'center', ancho: w - 18, letra: lz.letra });
  }

  function flechaR(ctx, lz, e, a) {
    var c = col(lz, e.color, lz.marca.tinta), x1 = e.de[0], y1 = e.de[1], x2 = e.a[0], y2 = e.a[1];
    if (e.punteada) ctx.setLineDash([10, 8]);
    L.flecha(ctx, x1, y1, x2, y2, c, e.grosor || 3, a);
    ctx.setLineDash([]);
    if (e.r && a > 0.6) {
      var mx = (x1 + x2) / 2 + (e.dx || 0), my = (y1 + y2) / 2 + (e.dy === undefined ? -30 : e.dy);
      UJ.alfa(ctx, (a - 0.6) / 0.4, function () {
        L.texto(ctx, e.r, mx, my, { tam: e.tam || 18, peso: 600, color: c, alinear: e.alinear || 'center', ancho: e.ancho || 240, letra: lz.letra });
      });
    }
  }

  function dibujar(ctx, lz, e, a) {
    var m = lz.marca, c = col(lz, e.color);
    switch (e.tipo) {
      case 'caja':
        UJ.alfa(ctx, a, function () {
          L.rectRed(ctx, e.x, e.y, e.w, e.h, e.r === undefined ? 14 : e.r);
          L.rellena(ctx, e.lleno ? c : L.tono(c, 0.88), c, 3);
          centrado(ctx, lz, e.x, e.y, e.w, e.h, e.t, e.s, e.lleno ? (e.color === 'sello' ? m.tinta : m.papel) : (e.color === 'sello' ? m.tinta : c), e.tam, e.tamSub, e.lleno && e.color !== 'sello' ? m.papel : undefined);
        });
        break;
      case 'cilindro':
        UJ.alfa(ctx, a, function () {
          var ry = 14;
          ctx.beginPath();
          ctx.ellipse(e.x + e.w / 2, e.y + ry, e.w / 2, ry, 0, Math.PI, 0);
          ctx.lineTo(e.x + e.w, e.y + e.h - ry);
          ctx.ellipse(e.x + e.w / 2, e.y + e.h - ry, e.w / 2, ry, 0, 0, Math.PI);
          ctx.closePath(); L.rellena(ctx, L.tono(c, 0.85), c, 3);
          ctx.beginPath(); ctx.ellipse(e.x + e.w / 2, e.y + ry, e.w / 2, ry, 0, 0, Math.PI * 2);
          ctx.strokeStyle = c; ctx.lineWidth = 3; ctx.stroke();
          centrado(ctx, lz, e.x, e.y + ry * 1.6, e.w, e.h - ry * 2, e.t, e.s, c, e.tam || 20, e.tamSub);
        });
        break;
      case 'flecha':
        flechaR(ctx, lz, e, a);
        break;
      case 'texto':
        UJ.alfa(ctx, e.escribe ? (a > 0 ? 1 : 0) : a, function () {
          L.texto(ctx, e.t, e.x, e.y, { tam: e.tam || 22, peso: e.peso || 600, color: col(lz, e.color, m.tinta),
            alinear: e.alinear || 'center', ancho: e.ancho, letra: e.mono ? 'Consolas, monospace' : lz.letra,
            visible: e.escribe ? a : undefined });
        });
        break;
      case 'chip':
        UJ.alfa(ctx, a, function () {
          var tam = e.tam || 18;
          ctx.font = '700 ' + tam + 'px ' + lz.letra;
          var w = e.w || ctx.measureText(e.t).width + tam * 1.4, h = tam * 1.8;
          L.rectRed(ctx, e.x - w / 2, e.y, w, h, h / 2);
          L.rellena(ctx, e.lleno === false ? L.tono(c, 0.88) : c, c, 2);
          L.texto(ctx, e.t, e.x, e.y + tam * 0.4, { tam: tam, peso: 700, color: e.lleno === false ? c : (e.tinta ? m.tinta : m.papel), alinear: 'center', letra: lz.letra });
        });
        break;
      case 'tacha':
        UJ.alfa(ctx, a, function () {
          ctx.strokeStyle = e.color ? c : (m.malva || '#A02030'); ctx.lineWidth = e.grosor || 6; ctx.lineCap = 'round';
          ctx.beginPath(); ctx.moveTo(e.x, e.y); ctx.lineTo(e.x + e.w, e.y + e.h);
          if (!e.simple) { ctx.moveTo(e.x + e.w, e.y); ctx.lineTo(e.x, e.y + e.h); }
          ctx.stroke();
        });
        break;
      case 'sello':
        UJ.sello(ctx, lz, e.x, e.y, e.r || 26, e.ok, a);
        break;
      case 'barra':
        UJ.alfa(ctx, Math.min(1, a * 3), function () {
          var val = e.valor === undefined ? 1 : e.valor;
          L.rectRed(ctx, e.x, e.y, e.w, e.h, 6); L.rellena(ctx, L.tono(m.tinta, 0.92));
          var v = val * L.curva.frena(a);
          if (v > 0) { L.rectRed(ctx, e.x, e.y, Math.max(8, e.w * v), e.h, 6); L.rellena(ctx, c); }
          if (e.t) L.texto(ctx, e.t, e.x - 12, e.y + e.h / 2 - (e.tam || 18) * 0.62, { tam: e.tam || 18, peso: 600, color: m.tinta, alinear: 'right', letra: lz.letra });
          if (e.r && a > 0.7) L.texto(ctx, e.r, e.x + Math.max(8, e.w * val) + 10, e.y + e.h / 2 - (e.tam || 18) * 0.62, { tam: e.tam || 18, peso: 700, color: c, letra: lz.letra });
        });
        break;
      case 'linea':
        if (e.punteada) ctx.setLineDash([10, 8]);
        L.trazo(ctx, e.pts, a, col(lz, e.color, m.tinta), e.grosor || 3);
        ctx.setLineDash([]);
        break;
      case 'marco':
        UJ.alfa(ctx, a, function () {
          ctx.setLineDash([12, 8]);
          L.rectRed(ctx, e.x, e.y, e.w, e.h, 18); L.rellena(ctx, L.tono(c, 0.95), c, 2.5);
          ctx.setLineDash([]);
          if (e.t) L.texto(ctx, e.t, e.x + 16, e.y + 10, { tam: e.tam || 18, peso: 700, color: c, letra: lz.letra, ancho: e.w - 30 });
        });
        break;
      case 'persona':
        UJ.alfa(ctx, a, function () {
          var s = e.tam || 60;
          L.circulo(ctx, e.x, e.y + s * 0.22, s * 0.2); L.rellena(ctx, c);
          L.rectRed(ctx, e.x - s * 0.32, e.y + s * 0.48, s * 0.64, s * 0.5, s * 0.25); L.rellena(ctx, c);
          if (e.t) L.texto(ctx, e.t, e.x, e.y + s + 6, { tam: e.tamT || 18, peso: 700, color: m.tinta, alinear: 'center', ancho: e.ancho || 160, letra: lz.letra });
        });
        break;
    }
    if (e.fx) UJ.alfa(ctx, a, function () { e.fx(ctx, a); });
  }

  function escena(ctx, t, lz, elementos) {
    for (var i = 0; i < elementos.length; i++) {
      var e = elementos[i];
      var d = e.dur || (e.tipo === 'flecha' || e.tipo === 'linea' || e.tipo === 'barra' || e.escribe ? 0.12 : 0.08);
      var a = L.tramo(t, e.en || 0, (e.en || 0) + d);
      if (e.sale !== undefined) a = Math.min(a, 1 - L.tramo(t, e.sale, e.sale + 0.06));
      if (a <= 0) continue;
      dibujar(ctx, lz, e, a);
    }
  }

  UJ.escena = escena; UJ.col = col; UJ.centrado = centrado;
})(window);
/*
 * Piezas C4 para dibujar lo que renderiza un C4Container de Mermaid: persona, contenedor,
 * base de datos (cilindro), sistema externo, limite del sistema y relacion con su rotulo.
 * Se cargan junto a `_base.js` desde cada ilustracion de la clase (ver `window.C4`).
 */
(function (global) {
  'use strict';
  var L = global.FP_LIENZO;

  function centrado(ctx, lz, txt, x, y, tam, peso, color, ancho) {
    return L.texto(ctx, txt, x, y, { tam: tam, peso: peso, color: color, alinear: 'center', ancho: ancho, letra: lz.letra });
  }

  function contenedor(ctx, lz, x, y, an, al, nombre, tec, desc, color) {
    var c = color || '#1168BD';
    L.rectRed(ctx, x, y, an, al, 10); L.rellena(ctx, c, L.tono(c, -0.25), 2);
    centrado(ctx, lz, nombre, x + an / 2, y + 12, 18, 800, '#FFFFFF', an - 16);
    centrado(ctx, lz, '[' + tec + ']', x + an / 2, y + 38, 14, 500, '#DCE9F7', an - 16);
    if (desc) centrado(ctx, lz, desc, x + an / 2, y + 60, 13, 400, '#FFFFFF', an - 20);
  }

  function baseDatos(ctx, lz, x, y, an, al, nombre, tec, desc) {
    var c = '#1168BD', e = 14;
    ctx.fillStyle = c; ctx.fillRect(x, y + e, an, al - 2 * e);
    ctx.beginPath(); ctx.ellipse(x + an / 2, y + al - e, an / 2, e, 0, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.ellipse(x + an / 2, y + e, an / 2, e, 0, 0, Math.PI * 2);
    ctx.fillStyle = L.tono(c, 0.25); ctx.fill(); ctx.strokeStyle = L.tono(c, -0.25); ctx.lineWidth = 2; ctx.stroke();
    centrado(ctx, lz, nombre, x + an / 2, y + 2 * e + 4, 17, 800, '#FFFFFF', an - 12);
    centrado(ctx, lz, '[' + tec + ']', x + an / 2, y + 2 * e + 28, 13, 500, '#DCE9F7', an - 12);
    if (desc) centrado(ctx, lz, desc, x + an / 2, y + 2 * e + 48, 13, 400, '#FFFFFF', an - 16);
  }

  function persona(ctx, lz, x, y, nombre, desc) {
    var c = '#08427B';
    L.circulo(ctx, x, y + 18, 18); L.rellena(ctx, c);
    L.rectRed(ctx, x - 60, y + 40, 120, 64, 16); L.rellena(ctx, c);
    centrado(ctx, lz, nombre, x, y + 50, 16, 800, '#FFFFFF', 112);
    if (desc) centrado(ctx, lz, desc, x, y + 74, 12, 400, '#FFFFFF', 112);
  }

  function externo(ctx, lz, x, y, an, al, nombre, desc) {
    L.rectRed(ctx, x, y, an, al, 10); L.rellena(ctx, '#8C8C8C', '#6B6B6B', 2);
    centrado(ctx, lz, nombre, x + an / 2, y + 14, 17, 800, '#FFFFFF', an - 16);
    if (desc) centrado(ctx, lz, desc, x + an / 2, y + 42, 13, 400, '#FFFFFF', an - 16);
  }

  function limite(ctx, lz, x, y, an, al, nombre) {
    ctx.save(); ctx.setLineDash([10, 7]); ctx.strokeStyle = '#444'; ctx.lineWidth = 2;
    L.rectRed(ctx, x, y, an, al, 8); ctx.stroke(); ctx.restore();
    L.texto(ctx, nombre + '  [Sistema]', x + 12, y + al - 26, { tam: 14, peso: 700, color: '#444', letra: lz.letra });
  }

  /** Relacion: flecha de (x1,y1) a (x2,y2) con verbo y [protocolo] junto al punto medio. */
  function rel(ctx, lz, x1, y1, x2, y2, verbo, proto, dx, dy) {
    L.flecha(ctx, x1, y1, x2, y2, '#555', 2.5, 1);
    var mx = (x1 + x2) / 2 + (dx || 0), my = (y1 + y2) / 2 + (dy || 0);
    ctx.font = '700 13px ' + lz.letra;
    // Sin protocolo (una llamada dentro del mismo contenedor) el rotulo es solo el verbo.
    var w = Math.max(ctx.measureText(verbo).width, proto ? ctx.measureText('[' + proto + ']').width : 0) + 12;
    L.rectRed(ctx, mx - w / 2, my - 13, w, proto ? 36 : 22, 4); L.rellena(ctx, 'rgba(255,255,255,0.92)');
    L.texto(ctx, verbo, mx, my - 10, { tam: 13, peso: 700, color: '#333', alinear: 'center', letra: lz.letra });
    if (proto) L.texto(ctx, '[' + proto + ']', mx, my + 6, { tam: 12, peso: 500, color: '#555', alinear: 'center', letra: lz.letra });
  }

  /** Sistema de software (nivel Context): caja azul con [Software System]. */
  function sistema(ctx, lz, x, y, an, al, nombre, desc) {
    var c = '#1168BD';
    L.rectRed(ctx, x, y, an, al, 10); L.rellena(ctx, c, L.tono(c, -0.25), 2);
    centrado(ctx, lz, nombre, x + an / 2, y + 14, 19, 800, '#FFFFFF', an - 16);
    centrado(ctx, lz, '[Software System]', x + an / 2, y + 42, 13, 500, '#DCE9F7', an - 16);
    if (desc) centrado(ctx, lz, desc, x + an / 2, y + 64, 13, 400, '#FFFFFF', an - 20);
  }

  /** Componente (nivel Component): azul claro con texto oscuro. */
  function componente(ctx, lz, x, y, an, al, nombre, tec, desc) {
    var c = '#85BBF0';
    L.rectRed(ctx, x, y, an, al, 10); L.rellena(ctx, c, '#5D82A8', 2);
    centrado(ctx, lz, nombre, x + an / 2, y + 8, 16, 800, '#0B2545', an - 12);
    centrado(ctx, lz, '[' + tec + ']', x + an / 2, y + 30, 12, 500, '#1F3B5C', an - 12);
    if (desc) centrado(ctx, lz, desc, x + an / 2, y + 48, 12, 400, '#0B2545', an - 14);
  }

  /** Cola (ContainerQueue): tubo horizontal. */
  function cola(ctx, lz, x, y, an, al, nombre, tec, desc) {
    var c = '#1168BD', e = 14;
    ctx.fillStyle = c; ctx.fillRect(x + e, y, an - 2 * e, al);
    ctx.beginPath(); ctx.ellipse(x + e, y + al / 2, e, al / 2, 0, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.ellipse(x + an - e, y + al / 2, e, al / 2, 0, 0, Math.PI * 2);
    ctx.fillStyle = L.tono(c, 0.25); ctx.fill(); ctx.strokeStyle = L.tono(c, -0.25); ctx.lineWidth = 2; ctx.stroke();
    centrado(ctx, lz, nombre, x + an / 2 - 6, y + 10, 16, 800, '#FFFFFF', an - 40);
    centrado(ctx, lz, '[' + tec + ']', x + an / 2 - 6, y + 32, 12, 500, '#DCE9F7', an - 40);
    if (desc) centrado(ctx, lz, desc, x + an / 2 - 6, y + 50, 12, 400, '#FFFFFF', an - 40);
  }

  /** Limite de un contenedor abierto (Container_Boundary): punteado con [Container]. */
  function limiteContenedor(ctx, lz, x, y, an, al, nombre, derecha) {
    ctx.save(); ctx.setLineDash([10, 7]); ctx.strokeStyle = '#444'; ctx.lineWidth = 2;
    L.rectRed(ctx, x, y, an, al, 8); ctx.stroke(); ctx.restore();
    L.texto(ctx, nombre + '  [Container]', derecha ? x + an - 12 : x + 12, y + al - 26,
            { tam: 14, peso: 700, color: '#444', alinear: derecha ? 'right' : 'left', letra: lz.letra });
  }

  /** Marca numerada de una regla, sobre el elemento donde se cumple. */
  function marca(ctx, lz, x, y, n, txt, ancho) {
    L.circulo(ctx, x, y, 14); L.rellena(ctx, lz.marca.sello || '#FFD000', '#333', 2);
    L.texto(ctx, String(n), x, y - 10, { tam: 17, peso: 800, color: '#333', alinear: 'center', letra: lz.letra });
    if (txt) L.texto(ctx, txt, x + 22, y - 10, { tam: 14, peso: 700, color: lz.marca.tinta, ancho: ancho || 260, letra: lz.letra });
  }

  global.C4 = { contenedor: contenedor, baseDatos: baseDatos, persona: persona, externo: externo,
                limite: limite, rel: rel, sistema: sistema, componente: componente, cola: cola,
                limiteContenedor: limiteContenedor, marca: marca };
})(window);
/*
 * Piezas de flowchart y sequenceDiagram de Mermaid, con su aspecto por defecto: nodos lila con
 * borde morado, rombo de decision, cilindro, subgraph con su rotulo, flecha (continua o
 * punteada, recta o en codo) con rotulo de fondo blanco; y para secuencia: participante,
 * actor, linea de vida, mensaje (con su numero si hay autonumber), nota y recuadro alt/else.
 */
(function (global) {
  'use strict';
  var L = global.FP_LIENZO;
  var RELL = '#ECECFF', BORDE = '#9370DB', TINTA = '#222';

  function lineas(ctx, lz, txt, cx, cy, tam, peso, ancho, color) {
    var partes = String(txt).split('\n'), al = tam * 1.25, y0 = cy - partes.length * al / 2;
    for (var i = 0; i < partes.length; i++)
      L.texto(ctx, partes[i], cx, y0 + i * al, { tam: tam, peso: peso || 600, color: color || TINTA, alinear: 'center', ancho: ancho, letra: lz.letra });
  }

  function nodo(ctx, lz, x, y, an, al, txt, o) {
    o = o || {};
    L.rectRed(ctx, x, y, an, al, o.radio === undefined ? 6 : o.radio);
    L.rellena(ctx, o.relleno || RELL, o.borde || BORDE, 2);
    lineas(ctx, lz, txt, x + an / 2, y + al / 2, o.tam || 16, o.peso || 600, an - 12, o.color);
  }

  function rombo(ctx, lz, cx, cy, sa, sb, txt, o) {
    o = o || {};
    ctx.beginPath(); ctx.moveTo(cx, cy - sb); ctx.lineTo(cx + sa, cy); ctx.lineTo(cx, cy + sb); ctx.lineTo(cx - sa, cy); ctx.closePath();
    L.rellena(ctx, o.relleno || RELL, o.borde || BORDE, 2);
    lineas(ctx, lz, txt, cx, cy, o.tam || 15, 600, sa * 1.1);
  }

  function cilindro(ctx, lz, x, y, an, al, txt, o) {
    o = o || {};
    var e = 12, r = o.relleno || RELL, b = o.borde || BORDE;
    ctx.beginPath(); ctx.moveTo(x, y + e); ctx.lineTo(x, y + al - e);
    ctx.ellipse(x + an / 2, y + al - e, an / 2, e, 0, Math.PI, 0, true);
    ctx.lineTo(x + an, y + e); ctx.ellipse(x + an / 2, y + e, an / 2, e, 0, 0, Math.PI, true);
    ctx.closePath(); L.rellena(ctx, r, b, 2);
    ctx.beginPath(); ctx.ellipse(x + an / 2, y + e, an / 2, e, 0, 0, Math.PI * 2); ctx.strokeStyle = b; ctx.lineWidth = 2; ctx.stroke();
    lineas(ctx, lz, txt, x + an / 2, y + al / 2 + e / 2, o.tam || 15, 600, an - 12);
  }

  function zona(ctx, lz, x, y, an, al, titulo, o) {
    o = o || {};
    L.rectRed(ctx, x, y, an, al, 4); L.rellena(ctx, o.relleno || '#FFFFDE', o.borde || '#AAAA33', 1.5);
    L.texto(ctx, titulo, x + an / 2, y + 6, { tam: o.tam || 14, peso: 700, color: '#333', alinear: 'center', ancho: an - 10, letra: lz.letra });
  }

  function rotulo(ctx, lz, txt, x, y, tam, color) {
    tam = tam || 13;
    var partes = String(txt).split('\n'), w = 0;
    ctx.font = '600 ' + tam + 'px ' + lz.letra;
    for (var i = 0; i < partes.length; i++) w = Math.max(w, ctx.measureText(partes[i]).width);
    var al = partes.length * tam * 1.25 + 6;
    L.rectRed(ctx, x - w / 2 - 6, y - al / 2, w + 12, al, 4); L.rellena(ctx, 'rgba(255,255,255,0.96)', '#DDD', 1);
    lineas(ctx, lz, txt, x, y + 1, tam, 600, w + 20, color || '#333');
  }

  function punta(ctx, a, b, c, abierta) {
    var ang = Math.atan2(b[1] - a[1], b[0] - a[0]), p = 11;
    ctx.beginPath(); ctx.moveTo(b[0] - p * Math.cos(ang - 0.42), b[1] - p * Math.sin(ang - 0.42));
    ctx.lineTo(b[0], b[1]);
    ctx.lineTo(b[0] - p * Math.cos(ang + 0.42), b[1] - p * Math.sin(ang + 0.42));
    if (abierta) { ctx.strokeStyle = c; ctx.lineWidth = 2; ctx.stroke(); return; }
    ctx.closePath(); ctx.fillStyle = c; ctx.fill();
  }

  /** Flecha por una lista de puntos; `o.punteada`, `o.rot` (texto), `o.en` ([x,y] del rotulo). */
  function flecha(ctx, lz, pts, o) {
    o = o || {};
    var c = o.color || '#333';
    ctx.save();
    if (o.punteada) ctx.setLineDash([7, 6]);
    ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]);
    for (var i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]);
    ctx.strokeStyle = c; ctx.lineWidth = o.grosor || 2; ctx.stroke(); ctx.restore();
    var a = pts[pts.length - 2], b = pts[pts.length - 1];
    punta(ctx, a, b, c);
    if (o.rot) {
      var en = o.en || [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
      rotulo(ctx, lz, o.rot, en[0], en[1], o.tam);
    }
  }

  // ---------------------------------------------------------------- secuencia

  function participante(ctx, lz, cx, y, an, txt) {
    nodo(ctx, lz, cx - an / 2, y, an, 44, txt, { tam: 15, peso: 700, radio: 3 });
  }

  function actor(ctx, lz, cx, y, txt) {
    ctx.strokeStyle = BORDE; ctx.lineWidth = 2.5; ctx.fillStyle = RELL;
    L.circulo(ctx, cx, y + 9, 8); ctx.fill(); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx, y + 17); ctx.lineTo(cx, y + 34);
    ctx.moveTo(cx - 12, y + 23); ctx.lineTo(cx + 12, y + 23);
    ctx.moveTo(cx, y + 34); ctx.lineTo(cx - 10, y + 46); ctx.moveTo(cx, y + 34); ctx.lineTo(cx + 10, y + 46);
    ctx.stroke();
    L.texto(ctx, txt, cx, y + 50, { tam: 15, peso: 700, color: TINTA, alinear: 'center', letra: lz.letra });
  }

  function vida(ctx, cx, y1, y2) {
    ctx.save(); ctx.setLineDash([5, 4]); ctx.strokeStyle = '#999'; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(cx, y1); ctx.lineTo(cx, y2); ctx.stroke(); ctx.restore();
  }

  /** Mensaje de x1 a x2 en la altura y: `->>` continuo, `-->>` punteado (respuesta). */
  function mensaje(ctx, lz, x1, x2, y, txt, o) {
    o = o || {};
    ctx.save(); if (o.respuesta) ctx.setLineDash([7, 5]);
    ctx.beginPath(); ctx.moveTo(x1, y); ctx.lineTo(x2, y); ctx.strokeStyle = '#333'; ctx.lineWidth = 2; ctx.stroke(); ctx.restore();
    punta(ctx, [x1, y], [x2, y], '#333');
    var cx = o.cx === undefined ? (x1 + x2) / 2 : o.cx;
    L.texto(ctx, txt, cx, y - 22, { tam: o.tam || 14, peso: 600, color: TINTA, alinear: 'center', letra: lz.letra });
    if (o.n) {
      L.circulo(ctx, x1, y, 11); L.rellena(ctx, '#333');
      L.texto(ctx, String(o.n), x1, y - 8, { tam: 13, peso: 800, color: '#FFF', alinear: 'center', letra: lz.letra });
    }
  }

  function nota(ctx, lz, x, y, an, al, txt, o) {
    o = o || {};
    L.rectRed(ctx, x, y, an, al, 2); L.rellena(ctx, o.relleno || '#FFF5AD', o.borde || '#AAAA33', o.borde ? 2.5 : 1.5);
    lineas(ctx, lz, txt, x + an / 2, y + al / 2, o.tam || 13, 600, an - 10, o.color);
  }

  /** Recuadro alt / else: `cortes` son las alturas donde empieza cada rama, con su condicion. */
  function alt(ctx, lz, x, y, an, al, ramas) {
    ctx.strokeStyle = '#555'; ctx.lineWidth = 1.5;
    L.rectRed(ctx, x, y, an, al, 2); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + 46, y); ctx.lineTo(x + 46, y + 16); ctx.lineTo(x + 38, y + 24); ctx.lineTo(x, y + 24); ctx.closePath();
    L.rellena(ctx, '#E0E0E0', '#555', 1.5);
    L.texto(ctx, 'alt', x + 21, y + 4, { tam: 14, peso: 800, color: '#222', alinear: 'center', letra: lz.letra });
    for (var i = 0; i < ramas.length; i++) {
      var r = ramas[i];
      if (i > 0) {
        ctx.save(); ctx.setLineDash([6, 5]); ctx.strokeStyle = '#555'; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(x, r.y); ctx.lineTo(x + an, r.y); ctx.stroke(); ctx.restore();
      }
      L.texto(ctx, '[' + r.cond + ']', x + an / 2, r.y + 5, { tam: 14, peso: 700, color: '#555', alinear: 'center', letra: lz.letra });
    }
  }

  global.MF = { nodo: nodo, rombo: rombo, cilindro: cilindro, zona: zona, rotulo: rotulo, flecha: flecha,
                lineas: lineas, participante: participante, actor: actor, vida: vida,
                mensaje: mensaje, nota: nota, alt: alt };
})(window);
