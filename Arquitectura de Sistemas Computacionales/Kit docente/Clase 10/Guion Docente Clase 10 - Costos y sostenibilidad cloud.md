# Guion docente — Clase 10: Costos y sostenibilidad cloud

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Identificar drivers de costo (cómputo, datos, transferencia, idle).
- Proponer 3 apalancamientos de ahorro sin romper el diseño.
- Redactar sostenibilidad (apagado de labs, imágenes ligeras, sobredimensionamiento).

## Hoy avanzamos el PI en…
**Estimación cualitativa de costos + notas de sostenibilidad**

**Entregable concreto:** Sección Costos/Sostenibilidad del informe (bajo/medio + drivers)

**Herramienta:** Google Docs

## Fundamento teórico para el docente
Costo en la nube se analiza aunque no haya facturacion real: cualitativamente en niveles Bajo/Medio/Alto por componente (ej. una base de datos gestionada = costo medio-alto por almacenamiento+computo constante; una funcion serverless que casi no se usa = costo bajo), identificando los DRIVERS de costo (que factor especifico hace subir el gasto: numero de instancias, volumen de datos, trafico de red saliente).

Sostenibilidad tecnica (no ambiental en este contexto) = right-sizing: no sobre-aprovisionar recursos "por si acaso" (una maquina grande corriendo al 5% de uso es desperdicio puro), usar labs/entornos temporales que se apagan cuando no se usan en vez de dejar todo corriendo 24/7, e imagenes de contenedor "slim" (minimas, sin paquetes innecesarios) que consumen menos storage y arrancan mas rapido.

Conexion directa con Clase 13 (escalabilidad): escalar automaticamente HACIA ARRIBA sin un limite o politica de apagado tambien escala el costo sin control — el diseño de autoescalado y el analisis de costo son la misma decision vista desde dos angulos.

Error de docente que no domina el tema: tratar el costo como un tema "de negocio, no tecnico" — las decisiones que mas impactan el costo (tipo de instancia, almacenamiento elegido, arquitectura con o sin colas/cache) son decisiones de arquitectura, tomadas por quien diseña el sistema.

Referencia de slides: `Clases/Clase 10 - Costos y sostenibilidad cloud/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### Modalidad autónoma (festivo)
No hay encuentro síncrono obligatorio. El estudiante trabaja con Presentacion.pptx + Taller.docx.

### Guion del docente (asíncrono)
1. Publica en ExamLab: diapositivas + taller + recordatorio del PI.
2. Mensaje sugerido: «Clase 10 autónoma. Hoy avanzamos el PI en: Estimación cualitativa de costos + notas de sostenibilidad.
   Entregable: Sección Costos/Sostenibilidad del informe (bajo/medio + drivers). Duda por foro/correo institucional.»
3. Revisa entregas domingo 23:59; deja feedback breve orientado a la rúbrica PI.

### Si ofreces office hours voluntario (opcional, 20–30 min)
Resuelve bloqueos de diagrama/ADR; no adelantes Parcial.


## Actividad / taller (detalle)
1. Tabla componente → driver de costo → nivel (B/M/A) → apalancamiento.
2. 3 acciones de sostenibilidad aplicables al diseño.
3. Integre en el informe PI (1 página).
4. Entrega domingo 23:59.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 10/Quiz Clase 10 - Costos y sostenibilidad cloud.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase10.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). La UNIAJC no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
