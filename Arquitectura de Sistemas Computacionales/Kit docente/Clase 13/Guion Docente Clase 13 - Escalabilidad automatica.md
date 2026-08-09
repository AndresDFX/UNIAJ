# Guion docente — Clase 13: Escalabilidad automática

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Distinguir escala vertical vs horizontal y cuándo aplicarlas.
- Definir triggers cualitativos (CPU, cola, RPS) sin cloud de pago.
- Actualizar el informe PI con la política de escala.

## Hoy avanzamos el PI en…
**Documentar política de autoescalado conceptual de CloudLite**

**Entregable concreto:** Sección Escalabilidad: triggers, límites, qué escala y qué no

**Herramienta:** Google Docs · draw.io (opcional nota en Deployment)

## Fundamento teórico para el docente
Escalar verticalmente = darle mas recursos a la MISMA maquina (mas CPU, mas RAM) — simple pero tiene un techo fisico y usualmente requiere reiniciar el servicio. Escalar horizontalmente = agregar MAS instancias iguales corriendo en paralelo, repartiendo la carga entre ellas (requiere que el sistema soporte multiples instancias sin pisarse, ej. no guardar estado de sesion solo en memoria local).

Autoescalado (mencion conceptual): un trigger (ej. uso de CPU sobre 70% durante 5 minutos) dispara automaticamente el arranque de una instancia adicional; y un limite maximo evita que el sistema escale sin control (y sin control de costo, conexion directa con Clase 10).

Punto que suele generar "magia" en las sustentaciones: los datos NO escalan igual que la capa de API. Agregar mas instancias de la aplicacion es relativamente simple; escalar una base de datos relacional (que necesita mantener consistencia) es fundamentalmente mas dificil — por eso el entregable de hoy exige documentar explicitamente QUE NO se escala en el diseño actual de CloudLite, no solo lo que si.

Error de docente que no domina el tema: presentar el autoescalado como si resolviera cualquier problema de rendimiento automaticamente — sin identificar primero el bottleneck (Clase 12), escalar la pieza equivocada no mejora nada y aumenta el costo sin razon.

Referencia de slides: `Clases/Clase 13 - Escalabilidad automatica/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### Modalidad autónoma (festivo)
No hay encuentro síncrono obligatorio. El estudiante trabaja con Presentacion.pptx + Taller.docx.

### Guion del docente (asíncrono)
1. Publica en ExamLab (y Campus Virtual si aplica): diapositivas + taller + recordatorio del PI.
2. Mensaje sugerido: «Clase 13 autónoma. Hoy avanzamos el PI en: Documentar política de autoescalado conceptual de CloudLite.
   Entregable: Sección Escalabilidad: triggers, límites, qué escala y qué no. Duda por foro/correo institucional.»
3. Revisa entregas domingo 23:59; deja feedback breve orientado a la rúbrica PI.

### Si ofreces office hours voluntario (opcional, 20–30 min)
Resuelve bloqueos de diagrama/ADR; no adelantes Parcial.


## Actividad / taller (detalle)
1. Describan qué componente escala y por qué.
2. Definan 2 triggers + min/max + qué NO se escala.
3. Anoten impacto en costos/sostenibilidad.
4. Opcional: marca «ASG/replicas» en diagrama Deployment.
5. Entrega domingo 23:59 (sección Escalabilidad).

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 13/Quiz Clase 13 - Escalabilidad automatica.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase13.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). Campus Virtual sigue siendo el canal institucional.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
