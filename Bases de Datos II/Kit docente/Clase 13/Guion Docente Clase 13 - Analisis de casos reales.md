# Guion docente · Clase 13 · Analisis de casos reales · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Informe de caso -> mejoras concretas al PI
- **Entregable de hoy:** Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare
- **Herramienta:** Google Docs
- **Slides:** Clases/Clase 13 - Analisis de casos reales/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Caso 1 — falta de backup real: una organizacion que 'hacia backup' copiando el archivo de datos una vez al mes sin probar nunca el restore. Cuando el disco fallo, el archivo copiado estaba corrupto (nunca se verifico) y perdieron meses de informacion. Leccion para VetCare: un backup que nunca se restauro de prueba no cuenta como backup funcional (conecta con Clase 4: RPO/RTO y prueba de restore).
- Caso 2 — indices mal disenados: un sistema con un indice sobre CADA columna 'por si acaso', que volvia cada INSERT/UPDATE mas lento de lo aceptable, sin que nadie hubiera medido si esos indices realmente se usaban en consultas reales. Leccion: indexar sin justificar la consulta que lo aprovecha (conecta con Clase 7) desperdicia recursos y no mejora nada.
- Caso 3 — inyeccion SQL: una aplicacion que concatenaba directamente el texto escrito por el usuario dentro de una consulta (ej. "SELECT * FROM usuarios WHERE nombre='" + input + "'"), permitiendo que alguien escribiera un valor que alterara la consulta completa y expusiera o borrara datos ajenos. Leccion: por eso la app llama procedimientos con parametros tipados (Clase 3 y Clase 12) en vez de armar SQL con texto libre.
- Estructura para analizar cualquier caso real: (1) contexto — que sistema era y que se suponia que hacia bien; (2) fallo — que paso exactamente y por que la causa raiz no era 'mala suerte' sino una decision tecnica evitable; (3) leccion — que principio general se puede extraer; (4) cambio concreto — que se ajusta HOY en el VetCare del equipo, no en abstracto.
- Esta clase es autonoma (sin encuentro sincrono) precisamente porque no introduce tecnica nueva: aplica en modo reflexivo/critico todo lo visto en Clases 1-10 sobre un caso real, cerrando el ciclo antes de entrar a integracion y cierre del PI.
- Error de docente que no domina el tema: dejar que el informe describa el caso ajeno sin conectar ninguna leccion con una accion verificable en VetCare — el entregable exige 3 mejoras concretas aplicadas al proyecto propio, no un resumen de noticia.

**Demo que usted debe poder repetir:** Plantilla: contexto -> fallo -> leccion -> cambio en VetCare.

## Referencias a diapositivas
1. Slide 1 portada (Clase N + titulo VetCare)
2. Slide Agenda 120 min
3. Slide Objetivo PI de la clase
4. Slide Teoria Core
5. Slide Demo del dia
6. Slide Herramientas de hoy (logos 3-4)
7. Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas
8. Slide Criterios de exito / entregable
9. Slide Para el PI esta semana
10. Slide Cierre
11. Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en Campus.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Informe de caso -> mejoras concretas al PI. No es un taller suelto.»
Referencia slides: Agenda + Objetivo PI.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: Google Docs.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
📸 Pantallazo: [CAP: demo VetCare Clase 13]

### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar checklist PI del equipo.


## Codigo / scripts
Carpeta Codigo/ — archivo N/A.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
