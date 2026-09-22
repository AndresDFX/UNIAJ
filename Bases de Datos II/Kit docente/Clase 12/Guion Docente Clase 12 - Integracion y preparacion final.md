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

**[Slide 4] Integrar no es conectarse: cual es la unica puerta de entrada (1/2)** — 4 vinetas.
  - Esa puerta es la interfaz app-BD y el documento que la describe es el contrato.
  - Hay exactamente dos formas de construirla.
  - Todo lo demas de esta clase se deriva de esa decision.

**[Slide 5] Integrar no es conectarse: cual es la unica puerta de entrada (2/2)** — 4 vinetas.

**[Slide 6] Inyeccion SQL: cuando el dato se interpreta como codigo (1/2)** — 4 vinetas.
  - Concretemoslo en VetCare.
  - El buscador de mascotas de la recepcion arma la consulta pegando la entrada del usuario, de modo que el motor recibe
  - Si la recepcionista escribe Luna, el motor recibe WHERE nombre = 'Luna', devuelve una fila, todo parece correcto y la aplicacion pasa a produccion.
  - Conviene una precision honesta, porque la hara un estudiante: en Oracle no se apilan dos sentencias en una misma llamada, asi que el clasico punto y coma seguido de DROP TABLE Cita no se comporta como en otros motores; lo que si funciona, y basta para un incidente reportable, es leer datos ajenos, saltarse un acceso o modificar informacion cuando la aplicacion ejecuta PL/SQL dinamico.

**[Slide 7] Inyeccion SQL: cuando el dato se interpreta como codigo (2/2)** — 3 vinetas.

**[Slide 8] Inyeccion SQL: cuando el dato se interpreta... — sintaxis** — 3 vinetas.

**[Slide 9] Por que el parametro lo evita por construccion (1/2)** — 4 vinetas.
  - La inyeccion queda imposible, no improbable, y esa diferencia entre imposible e improbable es la que hay que instalar.
  - La respuesta honesta es que si mientras use los metodos del ORM o consultas con parametros nombrados, y que no en el momento en que arme una consulta nativa concatenando texto, porque el ORM no revisa lo que usted le entrega.
  - La vulnerabilidad no la produce la tecnologia sino la concatenacion.

**[Slide 10] Por que el parametro lo evita por construccion (2/2)** — 4 vinetas.

**[Slide 11] El contrato y sus seis partes, que se exigen en el entregable (1/2)** — 6 vinetas.
  - La lista de errores posibles con codigo y significado.
  - Y la version.
  - Idempotente significa que ejecutar la operacion dos veces con los mismos datos deja el sistema igual que ejecutarla una sola vez.

**[Slide 12] El contrato y sus seis partes, que se exigen en el entregable (2/2)** — 5 vinetas.

**[Slide 13] El manejo de errores entre capas: las tres reglas (1/2)** — 4 vinetas.
  - El manejo de errores entre capas se resuelve con tres reglas.
  - La operacion de negocio completa, con todas sus validaciones y sus insercciones, vive dentro de un solo procedimiento, y ese procedimiento hace COMMIT si todo salio bien o ROLLBACK si algo fallo; la aplicacion no confirma a la mitad.

**[Slide 14] El manejo de errores entre capas: las tres reglas (2/2)** — 4 vinetas.

**[Slide 15] El pool de conexiones: que es y por que se agota (1/3)** — 5 vinetas.
  - Tomar una conexion prestada del pool cuesta una fraccion de milisegundo.
  - De ahi salen dos consecuencias.

**[Slide 16] El pool de conexiones: que es y por que se agota (2/3)** — 4 vinetas.

**[Slide 17] El pool de conexiones: que es y por que se agota (3/3)** — 4 vinetas.

**[Slide 18] Logica en la base o en la aplicacion: honestidad y no propaganda (1/2)** — 4 vinetas.
  - El trade-off de poner logica en la base o en la aplicacion merece honestidad y no propaganda, porque el estudiante encontrara equipos reales que defienden lo contrario de lo que oye hoy.
  - La orquestacion, la presentacion, los formatos de fecha y el envio de correos van en la aplicacion.

**[Slide 19] Logica en la base o en la aplicacion: honestidad y no propaganda (2/2)** — 3 vinetas.

**[Slide 20] Cambiar el esquema sin romper la aplicacion que ya corre (1/2)** — 5 vinetas.
  - Suponga que VetCare necesita registrar la fecha en que una mascota fue inactivada, dato que hoy no existe.
  - Cuatro, mover lecturas y reportes a la columna nueva.
  - Cada paso deja funcionando al mismo tiempo la version vieja y la nueva.
  - Eso mismo entra en el informe y en el pitch de hoy, porque el estudiante no muestra pantallas: muestra su contrato, un caso de exito, un caso de error visto por el usuario y su plan de cambio de esquema, que es lo que la Clase 13 mirara desde el lado de los fallos reales y lo que la Clase 15 va a evaluar.

**[Slide 21] Cambiar el esquema sin romper la aplicacion que ya corre (2/2)** — 4 vinetas.

**[Slide 22] Cambiar el esquema sin romper la aplicacion... — sintaxis** — 1 vinetas.

**[Slide 23] El contrato de la capa de API: siempre parametros ligados** — 13 vinetas.

**[Slide 24] La inyeccion de SQL, explicada con las dos versiones** — 11 vinetas.


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
8. Inyeccion SQL: cuando el dato se interpreta... — sintaxis
9. Por que el parametro lo evita por construccion (1/2)
10. Por que el parametro lo evita por construccion (2/2)
11. El contrato y sus seis partes, que se exigen en el entregable (1/2)
12. El contrato y sus seis partes, que se exigen en el entregable (2/2)
13. El manejo de errores entre capas: las tres reglas (1/2)
14. El manejo de errores entre capas: las tres reglas (2/2)
15. El pool de conexiones: que es y por que se agota (1/3)
16. El pool de conexiones: que es y por que se agota (2/3)
17. El pool de conexiones: que es y por que se agota (3/3)
18. Logica en la base o en la aplicacion: honestidad y no propaganda (1/2)
19. Logica en la base o en la aplicacion: honestidad y no propaganda (2/2)
20. Cambiar el esquema sin romper la aplicacion que ya corre (1/2)
21. Cambiar el esquema sin romper la aplicacion que ya corre (2/2)
22. Cambiar el esquema sin romper la aplicacion... — sintaxis
23. El contrato de la capa de API: siempre parametros ligados
24. La inyeccion de SQL, explicada con las dos versiones
25. El contrato que la app consume (no SQL suelto)
26. Demo del dia
27. Herramientas de hoy
28. Del boceto a ExamLab (diagrama)
29. Taller PI VetCare — contexto / por que importa
30. Taller PI VetCare — objetivo y criterios
31. Taller PI VetCare — escenario / datos de partida
32. Taller PI VetCare — pasos guiados
33. Taller PI VetCare — pistas (checklist vacio)
34. Criterios de exito / entregable
35. Para el PI esta semana
36. Cierre · Clase 12

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

### 35-55 · Demo paso a paso · [Slide 26][Slide 28]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Plantilla contrato sp_agendar_cita + storyboard 6 slides.
Herramienta: Google Docs + Live SQL + Excalidraw

**Cierre la demo dentro de ExamLab** [Slide 28] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `sequenceDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Salida esperada de la demo de la Clase 12 [[captura: cap01_demo.png | receta: 1) Abra Google Docs + Live SQL + Excalidraw y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 12/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 32]
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

### 105-115 · Criterios de exito + quiz corto · [Slide 34]
Repasar checklist del dia con [Slide 34] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 12 - VetCare.docx`. Clave para usted: `Quiz Clase 12 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 36]
**Decir:** «Queda avanzado: Contrato integracion + preparacion de entrega/sustentacion. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 36] slide de cierre. Dudas finales.


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
