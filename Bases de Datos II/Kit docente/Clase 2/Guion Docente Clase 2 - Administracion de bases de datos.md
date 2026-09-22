# Guion docente · Clase 2 · Administracion de BD · Roles VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Plan de roles/privilegios de VetCare
- **Entregable de hoy:** Documento Roles_VetCare + script GRANT/REVOKE ejecutado en ExamLab
- **Herramienta:** ExamLab (PostgreSQL) + Google Docs
- **Slides:** Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx
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

**[Slide 4] Los cuatro terminos que se confunden todo el tiempo (1/2)** — 5 vinetas.
  - Conviene aprovechar precisamente eso, porque los permisos son el tema del curso donde el estudiante mas necesita que alguien le diga en el momento por que su GRANT no surtio efecto.

**[Slide 5] Los cuatro terminos que se confunden todo el tiempo (2/2)** — 5 vinetas.

**[Slide 6] Privilegio: la unidad atomica, y la frontera DDL/DML (1/2)** — 7 vinetas.
  - Vale la pena decirlo porque el estudiante que busque en internet va a encontrar GRANT CREATE SESSION, que es sintaxis de Oracle y en PostgreSQL no existe.

**[Slide 7] Privilegio: la unidad atomica, y la frontera DDL/DML (2/2)** — 5 vinetas.

**[Slide 8] Rol: por que existe, con la aritmetica en el tablero** — 8 vinetas.
  - Ese es el argumento real que el docente debe transmitir: el rol no ahorra tipeo, ahorra olvidos, y los olvidos en materia de permisos son precisamente los que producen incidentes de seguridad.

**[Slide 9] En PostgreSQL usuario y rol son lo mismo, y por eso hoy se escribe NOLOGIN (1/2)** — 7 vinetas.
  - Conviene decir esto tal cual, porque un estudiante despierto va a preguntar por que el sufijo y merece la respuesta correcta y no una inventada.

**[Slide 10] En PostgreSQL usuario y rol son lo mismo, y por eso hoy se escribe NOLOGIN (2/2)** — 3 vinetas.

**[Slide 11] Minimo privilegio aplicado a VetCare: la matriz defendible (1/2)** — 6 vinetas.
  - Conviene escribir esos dos valores en el tablero, porque el estudiante que suponga activa = 0 escribira un UPDATE que el CHECK va a rechazar y perdera diez minutos buscando el error en otra parte.

**[Slide 12] Minimo privilegio aplicado a VetCare: la matriz defendible (2/2)** — 4 vinetas.

**[Slide 13] Separacion de funciones: el ejemplo de la factura** — 7 vinetas.
  - La respuesta que el docente debe dar es que el problema no es la confianza en la persona sino el dano posible por un error o por una sesion robada.

**[Slide 14] GRANT y REVOKE: la sintaxis exacta que se va a escribir hoy (1/2)** — 7 vinetas.

**[Slide 15] GRANT y REVOKE: la sintaxis exacta que se va a escribir hoy (2/2)** — 4 vinetas.

**[Slide 16] WITH GRANT OPTION y PUBLIC: los dos que hacen dano sin avisar** — 6 vinetas.

**[Slide 17] Cuando el GRANT es demasiado: vista y privilegio por columna (1/2)** — 8 vinetas.

**[Slide 18] Cuando el GRANT es demasiado: vista y privilegio por columna (2/2)** — 5 vinetas.

**[Slide 19] La matriz como hecho verificable: information_schema** — 7 vinetas.
  - Estas dos consultas son la evidencia que la rubrica exige tres veces, y el docente deberia proyectar su salida en la demo: ver la matriz salir del motor, y no de un documento, es lo que convence al grupo de que los permisos son verificables.

**[Slide 20] La politica de altas y bajas: el ciclo de vida de una cuenta (1/3)** — 5 vinetas.

**[Slide 21] La politica de altas y bajas: el ciclo de vida de una cuenta (2/3)** — 7 vinetas.

**[Slide 22] La politica de altas y bajas: el ciclo de vida de una cuenta (3/3)** — 5 vinetas.

**[Slide 23] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (1/3)** — 6 vinetas.

**[Slide 24] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (2/3)** — 7 vinetas.

**[Slide 25] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (3/3)** — 6 vinetas.

**[Slide 26] La matriz es el entregable, no el script (1/2)** — 6 vinetas.

**[Slide 27] La matriz es el entregable, no el script (2/2)** — 2 vinetas.

**[Slide 28] Como amarra con las clases vecinas y con la rubrica del PI** — 6 vinetas.

**[Slide 29] Preguntas frecuentes del grupo (1/2)** — 6 vinetas.

**[Slide 30] Preguntas frecuentes del grupo (2/2)** — 6 vinetas.


**Demo que usted debe poder repetir:** Los 4 roles de VetCare con CREATE ROLE/GRANT/REVOKE en ExamLab, verificados con information_schema.role_table_grants.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 2 · Administracion de BD · Roles VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Los cuatro terminos que se confunden todo el tiempo (1/2)
5. Los cuatro terminos que se confunden todo el tiempo (2/2)
6. Privilegio: la unidad atomica, y la frontera DDL/DML (1/2)
7. Privilegio: la unidad atomica, y la frontera DDL/DML (2/2)
8. Rol: por que existe, con la aritmetica en el tablero
9. En PostgreSQL usuario y rol son lo mismo, y por eso hoy se escribe NOLOGIN (1/2)
10. En PostgreSQL usuario y rol son lo mismo, y por eso hoy se escribe NOLOGIN (2/2)
11. Minimo privilegio aplicado a VetCare: la matriz defendible (1/2)
12. Minimo privilegio aplicado a VetCare: la matriz defendible (2/2)
13. Separacion de funciones: el ejemplo de la factura
14. GRANT y REVOKE: la sintaxis exacta que se va a escribir hoy (1/2)
15. GRANT y REVOKE: la sintaxis exacta que se va a escribir hoy (2/2)
16. WITH GRANT OPTION y PUBLIC: los dos que hacen dano sin avisar
17. Cuando el GRANT es demasiado: vista y privilegio por columna (1/2)
18. Cuando el GRANT es demasiado: vista y privilegio por columna (2/2)
19. La matriz como hecho verificable: information_schema
20. La politica de altas y bajas: el ciclo de vida de una cuenta (1/3)
21. La politica de altas y bajas: el ciclo de vida de una cuenta (2/3)
22. La politica de altas y bajas: el ciclo de vida de una cuenta (3/3)
23. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (1/3)
24. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (2/3)
25. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (3/3)
26. La matriz es el entregable, no el script (1/2)
27. La matriz es el entregable, no el script (2/2)
28. Como amarra con las clases vecinas y con la rubrica del PI
29. Preguntas frecuentes del grupo (1/2)
30. Preguntas frecuentes del grupo (2/2)
31. Minimo privilegio, en concreto
32. Reducir la superficie: vista y privilegio por columna
33. Ciclo de vida de una cuenta: alta, cambio, baja, revision
34. Demo del dia
35. Herramientas de hoy
36. Taller PI VetCare — contexto / por que importa
37. Taller PI VetCare — objetivo y criterios
38. Taller PI VetCare — escenario / datos de partida
39. Taller PI VetCare — pasos guiados
40. Taller PI VetCare — pistas (checklist vacio)
41. Criterios de exito / entregable
42. Para el PI esta semana
43. Cierre · Clase 2

> Privado, no se proyecta: `Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Plan de roles/privilegios de VetCare.
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
- Administracion de BD = gestionar QUIEN puede hacer QUE sobre CADA objeto. Tres piezas: usuario (identidad que se conecta), rol (paquete de privilegios con nombre, ej. recepcion), privilegio (permiso atomico: SELECT, INSERT, UPDATE, DELETE, EXECUTE sobre un objeto concreto). En PostgreSQL usuario y rol son la misma cosa: un usuario es un rol con LOGIN.
- Principio de minimo privilegio: cada rol recibe solo lo que necesita para su funcion, ni un privilegio mas. No es paranoia, es reduccion de superficie de dano: si roban la sesion de un recepcionista, no debe poder borrar el historial clinico ni ver nomina.
- Separacion de funciones (segregation of duties): quien disena/modifica el esquema (DDL: CREATE/ALTER/DROP) no deberia ser la misma cuenta que opera datos del dia a dia (DML: INSERT/UPDATE/DELETE), y quien audita solo deberia leer (SELECT), nunca escribir.
- GRANT otorga un privilegio a un rol o usuario; REVOKE lo retira. Un rol se puede asignar a varios usuarios (todos los recepcionistas heredan el rol recepcion) y modificar en un solo lugar en vez de uno por uno.
- Un GRANT no es todo-o-nada: se puede recortar la superficie con una vista (CREATE VIEW deja fuera filas y columnas) o con privilegios por columna (GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol). Asi el rol llega al dato que necesita sin ver el resto de la tabla.
- Un permiso no vale nada sin evidencia: information_schema.role_table_grants y information_schema.column_privileges son las dos consultas que prueban que la matriz quedo como se decidio. Sin ellas la matriz es una intencion, no un hecho verificable.
- Error de docente que no domina el tema: crear un unico usuario 'admin' que todos comparten (rompe la trazabilidad de auditoria) o dar ALL PRIVILEGES a todo el mundo 'para que no falle nada' — exactamente lo opuesto a minimo privilegio.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 34]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Los 4 roles de VetCare con CREATE ROLE/GRANT/REVOKE en ExamLab, verificados con information_schema.role_table_grants.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 Salida esperada de la demo de la Clase 2 [[captura: cap01_demo.png | receta: 1) Abra ExamLab (PostgreSQL) + Google Docs y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 2/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 39]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Crear los 4 roles (admin_bd, recepcion, veterinario_rol, auditor) con GRANT/REVOKE que corran.
2. Recortar la superficie: vista v_agenda_recepcion + privilegio por columna sobre dueno.
3. Matriz rol x objeto x privilegio de los 10 objetos, justificando privilegio minimo.
4. Redactar 1 pagina: politica de altas/bajas de usuarios, con la prueba negativa (SET ROLE) corrida y su mensaje de error.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Documento Roles_VetCare + script GRANT/REVOKE ejecutado en ExamLab
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 2/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 41]
Repasar checklist del dia con [Slide 41] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 2 - VetCare.docx`. Clave para usted: `Quiz Clase 2 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 43]
**Decir:** «Queda avanzado: Plan de roles/privilegios de VetCare. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 43] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 02_roles_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 2/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
