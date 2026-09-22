# Guion docente · Clase 12 · Integracion app <-> BD · Prep. presentacion

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Contrato integracion + preparacion de entrega/sustentacion
- **Entregable de hoy:** Contrato app<->BD + outline de slides de sustentacion (5-8 min)
- **Herramienta:** Google Docs + Live SQL + Excalidraw
- **Slides:** Clases/Clase 12 - Integracion y preparacion final/Presentacion.pptx
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

**[Slide 4] Integrar no es conectarse: cual es la unica puerta de entrada (1/2)** — 6 vinetas.

**[Slide 5] Integrar no es conectarse: cual es la unica puerta de entrada (2/2)** — 5 vinetas.

**[Slide 6] Inyeccion SQL: cuando el dato se interpreta como codigo (1/2)** — 6 vinetas.
  - Conviene una precision honesta, porque la hara un estudiante: en Oracle no se apilan dos sentencias en una misma llamada, asi que el clasico punto y coma seguido de DROP TABLE Cita no se comporta como en otros motores; lo que si funciona, y basta para un incidente reportable, es leer datos ajenos, saltarse un acceso o modificar informacion cuando la aplicacion ejecuta PL/SQL dinamico.

**[Slide 7] Inyeccion SQL: cuando el dato se interpreta como codigo (2/2)** — 4 vinetas.

**[Slide 8] Por que el parametro lo evita por construccion (1/2)** — 6 vinetas.

**[Slide 9] Por que el parametro lo evita por construccion (2/2)** — 5 vinetas.

**[Slide 10] El contrato y sus seis partes, que se exigen en el entregable (1/2)** — 8 vinetas.

**[Slide 11] El contrato y sus seis partes, que se exigen en el entregable (2/2)** — 6 vinetas.

**[Slide 12] El manejo de errores entre capas: las tres reglas (1/2)** — 6 vinetas.

**[Slide 13] El manejo de errores entre capas: las tres reglas (2/2)** — 4 vinetas.

**[Slide 14] El pool de conexiones: que es y por que se agota (1/2)** — 8 vinetas.

**[Slide 15] El pool de conexiones: que es y por que se agota (2/2)** — 7 vinetas.

**[Slide 16] Logica en la base o en la aplicacion: honestidad y no propaganda (1/2)** — 5 vinetas.

**[Slide 17] Logica en la base o en la aplicacion: honestidad y no propaganda (2/2)** — 4 vinetas.

**[Slide 18] Cambiar el esquema sin romper la aplicacion que ya corre (1/2)** — 8 vinetas.

**[Slide 19] Cambiar el esquema sin romper la aplicacion que ya corre (2/2)** — 6 vinetas.


**Demo que usted debe poder repetir:** Plantilla contrato sp_agendar_cita + storyboard 6 slides.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 12 - Integracion y preparacion final/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 12 · Integracion app <-> BD · Prep. presentacion
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Integrar no es conectarse: cual es la unica puerta de entrada (1/2)
5. Integrar no es conectarse: cual es la unica puerta de entrada (2/2)
6. Inyeccion SQL: cuando el dato se interpreta como codigo (1/2)
7. Inyeccion SQL: cuando el dato se interpreta como codigo (2/2)
8. Por que el parametro lo evita por construccion (1/2)
9. Por que el parametro lo evita por construccion (2/2)
10. El contrato y sus seis partes, que se exigen en el entregable (1/2)
11. El contrato y sus seis partes, que se exigen en el entregable (2/2)
12. El manejo de errores entre capas: las tres reglas (1/2)
13. El manejo de errores entre capas: las tres reglas (2/2)
14. El pool de conexiones: que es y por que se agota (1/2)
15. El pool de conexiones: que es y por que se agota (2/2)
16. Logica en la base o en la aplicacion: honestidad y no propaganda (1/2)
17. Logica en la base o en la aplicacion: honestidad y no propaganda (2/2)
18. Cambiar el esquema sin romper la aplicacion que ya corre (1/2)
19. Cambiar el esquema sin romper la aplicacion que ya corre (2/2)
20. El contrato que la app consume (no SQL suelto)
21. Demo del dia
22. Herramientas de hoy
23. Del boceto a ExamLab (diagrama)
24. Taller PI VetCare — contexto / por que importa
25. Taller PI VetCare — objetivo y criterios
26. Taller PI VetCare — escenario / datos de partida
27. Taller PI VetCare — pasos guiados
28. Taller PI VetCare — pistas (checklist vacio)
29. Criterios de exito / entregable
30. Para el PI esta semana
31. Cierre · Clase 12

> Privado, no se proyecta: `Kit docente/Clase 12/Solucion Taller Clase 12 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Contrato integracion + preparacion de entrega/sustentacion.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · desde 
**Decir:** «Solo lo necesario para el entregable de hoy.»
Proyecte estas diapositivas, en este orden, ~25 min cada una. Son la teoria
completa del dia: **ninguna se salta**, porque el taller cobra puntos por lo que se
proyecta en todas ellas.


El desarrollo completo de cada una esta arriba, en «Fundamento teorico», dividido por
diapositiva: esa seccion esta escrita para dictarla sin consultar otra fuente.
Ideas que tienen que quedar dichas:
- Integrar app<->BD significa que la aplicacion NUNCA arma SQL dinamico contra las tablas directamente; llama procedimientos y funciones ya construidos (Clases 3-4). Esto evita SQL injection (nadie concatena texto de usuario dentro de una consulta), centraliza la regla de negocio en un solo lugar, y permite cambiar el esquema interno sin romper la app mientras el contrato del proc se mantenga igual.
- Un contrato de integracion documenta, por cada operacion: nombre del proc, parametros de entrada con su tipo, que retorna (valor OUT o codigo de resultado), y que errores puede lanzar y con que significado (ej. 'ERROR: mascota inactiva' vs una excepcion no controlada del motor). Sin este contrato, cualquier desarrollador que use la BD debe adivinar el comportamiento leyendo el codigo SQL directamente.
- Manejo de errores en la frontera app-BD: la app no deberia mostrar al usuario final un error crudo de base de datos (ej. 'ORA-00001: unique constraint violated'); el proc devuelve un mensaje o codigo de negocio legible, y la app lo traduce a un mensaje humano ('Ya existe una cita en ese horario').
- Autenticacion/autorizacion en este punto es conceptual, no de implementacion: la app se conecta con una cuenta de servicio que respeta los roles definidos en Clase 2 (principio de minimo privilegio) — la app de recepcion no deberia poder ejecutar procs reservados a auditoria o administracion.
- Preparar la sustentacion no es 'hacer diapositivas bonitas': es organizar la evidencia tecnica en una narrativa logica -> problema real que resuelve VetCare, modelo de datos (ER + normalizacion), seguridad (roles), automatizacion (procs/triggers), rendimiento (indices/optimizacion), y una demo en vivo que conecte todo eso con una operacion real (agendar una cita, facturar).
- Error de docente que no domina el tema: dejar que la 'integracion' quede como una idea abstracta sin contrato escrito — el entregable de hoy exige documentar minimo 3 operaciones con su firma completa, no solo mencionarlas de palabra.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 21][Slide 23]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Plantilla contrato sp_agendar_cita + storyboard 6 slides.
Herramienta: Google Docs + Live SQL + Excalidraw

**Cierre la demo dentro de ExamLab** [Slide 23] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `sequenceDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Salida esperada de la demo de la Clase 12 [[captura: cap01_demo.png | receta: 1) Abra Google Docs + Live SQL + Excalidraw y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 12/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 27]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Redactar contrato de >=3 operaciones.
2. Diagrama flujo app->BD (Excalidraw) opcional.
3. Outline presentacion 5-8 min + quien habla que.
4. Empaquetar borrador entrega final.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Contrato app<->BD + outline de slides de sustentacion (5-8 min)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 12/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 29]
Repasar checklist del dia con [Slide 29] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 12 - VetCare.docx`. Clave para usted: `Quiz Clase 12 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 31]
**Decir:** «Queda avanzado: Contrato integracion + preparacion de entrega/sustentacion. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 31] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 12_contrato_ops.sql.

## Capturas
Carpeta `Kit docente/Clase 12/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
