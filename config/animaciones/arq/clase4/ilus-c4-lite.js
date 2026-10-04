/* Ilustracion (un fotograma): C4-lite */
(function () {
  FP_ANIMADOR.registrar('ilus-c4-lite', {
    duracion: 1,
    pasos: [1],
    dibujar: function (ctx, t, lz) {
      UJ.escena(ctx, t, lz, [{"tipo": "texto", "t": "Del Context a los Containers", "x": 400, "y": 16, "tam": 28, "peso": 800, "color": "accion", "en": 0}, {"tipo": "persona", "x": 80, "y": 90, "tam": 70, "t": "Cliente", "color": "sello", "en": 0}, {"tipo": "marco", "x": 190, "y": 70, "w": 420, "h": 450, "t": "Sistema de turnos", "color": "accion", "en": 0}, {"tipo": "caja", "x": 220, "y": 120, "w": 360, "h": 100, "t": "App web", "s": "React · muestra la agenda", "tam": 20, "tamSub": 15, "en": 0}, {"tipo": "caja", "x": 220, "y": 270, "w": 360, "h": 100, "t": "API de turnos", "s": "Node · reglas de reserva", "tam": 20, "tamSub": 15, "en": 0}, {"tipo": "cilindro", "x": 300, "y": 400, "w": 200, "h": 100, "t": "Base de turnos", "color": "acento", "tam": 18, "en": 0}, {"tipo": "flecha", "de": [400, 222], "a": [400, 268], "r": "HTTPS/JSON", "dx": 70, "dy": -10, "tam": 15, "en": 0}, {"tipo": "flecha", "de": [400, 372], "a": [400, 398], "r": "TCP/SQL", "dx": 60, "dy": -6, "tam": 15, "en": 0}, {"tipo": "flecha", "de": [120, 170], "a": [218, 170], "en": 0}, {"tipo": "caja", "x": 640, "y": 270, "w": 145, "h": 100, "t": "Correo", "s": "System_Ext", "color": "gris", "tam": 18, "en": 0}, {"tipo": "flecha", "de": [582, 320], "a": [638, 320], "en": 0}, {"tipo": "texto", "t": "nombre · tecnología · responsabilidad", "x": 400, "y": 548, "tam": 20, "color": "malva", "en": 0}, {"tipo": "texto", "t": "Entre 2 y 5 cajas; mismos nombres que el Context", "x": 400, "y": 590, "tam": 18, "color": "tinta", "en": 0}]);
    }
  });
})();
