# Guion docente · Clase 13 · Analisis de casos reales · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo, sin encuentro sincrono)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Informe de caso -> mejoras concretas al PI
- **Entregable de hoy:** Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare
- **Herramienta:** Google Docs
- **Slides:** Clases/Clase 13 - Analisis de casos reales/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Clase autonoma: este texto es fundamento y guia a la vez (1/2)** — 5 vinetas.

**[Slide 5] Clase autonoma: este texto es fundamento y guia a la vez (2/2)** — 3 vinetas.

**[Slide 6] Causa proxima y causa raiz: la distincion que separa el analisis de la anecdota (1/2)** — 6 vinetas.
  - Conviene ademas admitir la existencia de factores contribuyentes, que son condiciones que empeoraron el resultado sin haberlo causado, como que el incidente ocurriera de noche, que la documentacion estuviera desactualizada o que el unico que sabia restaurar estuviera de vacaciones.

**[Slide 7] Causa proxima y causa raiz: la distincion que separa el analisis de la anecdota (2/2)** — 4 vinetas.

**[Slide 8] Caso uno: el respaldo que nunca se restauro (GitLab, 2017) (1/2)** — 4 vinetas.
  - Eso es la causa proxima.
  - Lo que convirtio un error humano corriente en un incidente historico fue que, al intentar recuperar, la compania descubrio que sus cinco mecanismos de respaldo y replicacion fallaban de una u otra forma: entre otras cosas, la herramienta de volcado logico fallaba en silencio por una diferencia de version entre cliente y servidor, y las copias que debian estar en almacenamiento remoto estaban vacias.
  - Terminaron restaurando desde una copia de trabajo de unas seis horas antes y perdieron de forma definitiva la informacion creada en esa ventana, del orden de miles de proyectos y comentarios.

**[Slide 9] Caso uno: el respaldo que nunca se restauro (GitLab, 2017) (2/2)** — 3 vinetas.

**[Slide 10] Caso dos: permisos excesivos (Capital One, 2019) (1/2)** — 3 vinetas.
  - Caso dos, permisos excesivos.
  - Y hay que decir la parte incomoda, porque es la que se repite en los proyectos de curso: casi todos los estudiantes hacen que la aplicacion se conecte con un usuario que tiene todo, porque asi nunca aparece un error de permisos y se avanza mas rapido.

**[Slide 11] Caso dos: permisos excesivos (Capital One, 2019) (2/2)** — 4 vinetas.

**[Slide 12] Caso tres: perdida de datos en una migracion (MySpace, 2019) (1/2)** — 4 vinetas.
  - Caso tres, perdida de datos durante una migracion.

**[Slide 13] Caso tres: perdida de datos en una migracion (MySpace, 2019) (2/2)** — 3 vinetas.

**[Slide 14] Caso cuatro: concurrencia, el que no llega a los titulares (1/2)** — 5 vinetas.
  - Caso cuatro, concurrencia.

**[Slide 15] Caso cuatro: concurrencia, el que no llega a los titulares (2/2)** — 4 vinetas.

**[Slide 16] Lo que decide la calificacion: lecciones accionables (1/3)** — 5 vinetas.
  - Lo que decide la calificacion de hoy no es reunir casos sino escribir lecciones accionables, y esa es la habilidad que el estudiante debe practicar sin ayuda.
  - Compare las dos versiones.

**[Slide 17] Lo que decide la calificacion: lecciones accionables (2/3)** — 5 vinetas.

**[Slide 18] Lo que decide la calificacion: lecciones accionables (3/3)** — 3 vinetas.


**Demo que usted debe poder repetir:** Plantilla: contexto -> fallo -> leccion -> cambio en VetCare.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 13 - Analisis de casos reales/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 13 · Analisis de casos reales · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Clase autonoma: este texto es fundamento y guia a la vez (1/2)
5. Clase autonoma: este texto es fundamento y guia a la vez (2/2)
6. Causa proxima y causa raiz: la distincion que separa el analisis de la anecdota (1/2)
7. Causa proxima y causa raiz: la distincion que separa el analisis de la anecdota (2/2)
8. Caso uno: el respaldo que nunca se restauro (GitLab, 2017) (1/2)
9. Caso uno: el respaldo que nunca se restauro (GitLab, 2017) (2/2)
10. Caso dos: permisos excesivos (Capital One, 2019) (1/2)
11. Caso dos: permisos excesivos (Capital One, 2019) (2/2)
12. Caso tres: perdida de datos en una migracion (MySpace, 2019) (1/2)
13. Caso tres: perdida de datos en una migracion (MySpace, 2019) (2/2)
14. Caso cuatro: concurrencia, el que no llega a los titulares (1/2)
15. Caso cuatro: concurrencia, el que no llega a los titulares (2/2)
16. Lo que decide la calificacion: lecciones accionables (1/3)
17. Lo que decide la calificacion: lecciones accionables (2/3)
18. Lo que decide la calificacion: lecciones accionables (3/3)
19. Demo del dia
20. Herramientas de hoy
21. Actividad autonoma — contexto / por que importa
22. Actividad autonoma — objetivo y criterios
23. Actividad autonoma — escenario / datos de partida
24. Actividad autonoma — pasos guiados
25. Actividad autonoma — pistas (checklist vacio)
26. Criterios de exito / entregable
27. Para el PI esta semana
28. Cierre · Clase 13

> Privado, no se proyecta: `Kit docente/Clase 13/Solucion Taller Clase 13 - VetCare.docx`

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Informe de caso -> mejoras concretas al PI. No es un taller suelto.»
Referencia slides: Agenda + Objetivo PI.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: Google Docs.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
📸 Salida esperada de la demo de la Clase 13 [[captura: cap01_demo.png | receta: 1) Abra Google Docs y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 13/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]

### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar el checklist PI del proyecto.


## Codigo / scripts
Carpeta Codigo/ — archivo N/A.

## Capturas
Carpeta `Kit docente/Clase 13/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
