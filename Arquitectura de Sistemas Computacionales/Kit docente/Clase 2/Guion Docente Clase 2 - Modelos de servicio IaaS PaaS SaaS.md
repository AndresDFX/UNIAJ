# Guion docente — Clase 2: Modelos de servicio: IaaS, PaaS, SaaS

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Comparar IaaS, PaaS y SaaS con criterios de control, operación y velocidad.
- Elegir el modelo dominante de CloudLite con justificación.
- Documentar la decisión como ADR reutilizable en el informe PI.

## Hoy avanzamos el PI en…
**Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve**

**Entregable concreto:** ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio

**Herramienta:** Google Docs · draw.io (opcional)

## Fundamento teórico para el docente
IaaS, PaaS y SaaS son niveles de abstraccion sobre la infraestructura, y cada uno mueve la linea de responsabilidad compartida (shared responsibility model): en IaaS (Infrastructure as a Service) el proveedor da solo maquinas/red/almacenamiento y el cliente administra sistema operativo, runtime y aplicacion; en PaaS (Platform as a Service) el proveedor tambien administra el sistema operativo y el runtime, el cliente solo sube su codigo; en SaaS (Software as a Service) el proveedor entrega la aplicacion completa y el cliente solo la usa (ej. Gmail).

Regla practica: mientras mas alto el nivel de abstraccion (SaaS > PaaS > IaaS), menos control tiene el cliente pero menos trabajo operativo asume. Para un MVP academico como CloudLite, un enfoque PaaS conceptual + contenedores suele ser el punto dulce: control suficiente para aprender arquitectura, sin la carga operativa de administrar servidores completos.

Un ADR (Architecture Decision Record) es un documento corto que registra UNA decision arquitectonica: el contexto/problema, las opciones consideradas, la decision tomada y las consecuencias (trade-offs aceptados). Obliga a hacer explicito el trade-off control-vs-velocidad en vez de elegir "porque si".

Error de docente que no domina el tema: presentar IaaS/PaaS/SaaS como si fueran productos especificos de una marca en vez de un modelo conceptual de responsabilidad — el modelo aplica igual a cualquier proveedor, la pregunta siempre es "quien administra que capa".

Referencia de slides: `Clases/Clase 2 - Modelos de servicio IaaS PaaS SaaS/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### Modalidad autónoma (festivo)
No hay encuentro síncrono obligatorio. El estudiante trabaja con Presentacion.pptx + Taller.docx.

### Guion del docente (asíncrono)
1. Publica en ExamLab: diapositivas + taller + recordatorio del PI.
2. Mensaje sugerido: «Clase 2 autónoma. Hoy avanzamos el PI en: Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve.
   Entregable: ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio. Duda por foro/correo institucional.»
3. Revisa entregas domingo 23:59; deja feedback breve orientado a la rúbrica PI.

### Si ofreces office hours voluntario (opcional, 20–30 min)
Resuelve bloqueos de diagrama/ADR; no adelantes Parcial.


## Actividad / taller (detalle)
1. Lea las diapositivas y el enunciado del PI (Clases/Proyecto Integrador).
2. Complete una matriz IaaS/PaaS/SaaS vs su dominio (control, costo cualitativo, operación, time-to-demo).
3. Redacte ADR-001 (decisión dominante + 2 alternativas descartadas).
4. Actualice el informe PI (sección «Modelo de servicio»).
5. Entrega domingo 23:59 en **ExamLab** (Talleres) — mismo doc del PI o anexo.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 2/Quiz Clase 2 - Modelos de servicio IaaS PaaS SaaS.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase02.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). La UNIAJC no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
