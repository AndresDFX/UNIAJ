/* Lo que dibuja el sequenceDiagram «El flujo de la operacion ... con alt y else»: el actor y
 * los tres participantes con su linea de vida, los tres mensajes de ida, el recuadro alt con sus
 * dos ramas (ok = false / ok = true) y la nota sobre Aplicacion y Capa de API.
 * Las piezas MF (flowchart y secuencia de Mermaid) van aqui: Bases de Datos II usa el _base.js
 * comun, que no las trae. */
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
(function () {
  var X = { R: 90, A: 300, B: 510, T: 710 };
  FP_ANIMADOR.registrar('dg-cancelar-cita', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      var k;
      for (k in X) MF.vida(ctx, X[k], k === 'R' ? 74 : 52, 615);
      MF.actor(ctx, lz, X.R, 4, 'Recepcionista');
      MF.participante(ctx, lz, X.A, 6, 150, 'Aplicacion');
      MF.participante(ctx, lz, X.B, 6, 150, 'Capa de API');
      MF.participante(ctx, lz, X.T, 6, 130, 'Tabla cita');
      MF.mensaje(ctx, lz, X.R, X.A, 125, 'Cancelar la cita 3');
      MF.mensaje(ctx, lz, X.A, X.B, 190, 'api_cancelar_cita(3) como parametro', { tam: 13 });
      MF.mensaje(ctx, lz, X.B, X.T, 255, 'UPDATE solo si esta PROGRAMADA', { tam: 12, cx: 600 });
      MF.alt(ctx, lz, 30, 285, 740, 250, [{ y: 285, cond: 'ok = false' }, { y: 410, cond: 'ok = true' }]);
      MF.mensaje(ctx, lz, X.B, X.A, 340, 'false, No se puede cancelar', { respuesta: true });
      MF.mensaje(ctx, lz, X.A, X.R, 385, 'Muestra el mensaje y no sigue', { respuesta: true, tam: 13 });
      MF.mensaje(ctx, lz, X.B, X.A, 465, 'true, Cita cancelada, 3', { respuesta: true });
      MF.mensaje(ctx, lz, X.A, X.R, 510, 'Confirma la cancelacion', { respuesta: true });
      MF.nota(ctx, lz, X.A - 90, 558, X.B - X.A + 180, 40, 'La aplicacion no hace UPDATE directo sobre cita', { tam: 14 });
    }
  });
})();
