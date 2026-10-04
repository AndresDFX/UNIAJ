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
