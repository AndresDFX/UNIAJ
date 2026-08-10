# Guion docente · Clase 3 · Procedimientos almacenados · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** >=1 procedimiento de negocio (agendar cita / registrar consulta)
- **Entregable de hoy:** Script proc + casos de prueba (captura o enlace Live SQL)
- **Herramienta:** Oracle Live SQL
- **Slides:** Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Un procedimiento almacenado (stored procedure) es un bloque de codigo SQL/PLSQL con nombre propio, guardado y compilado DENTRO de la base de datos, que se invoca con CALL o EXECUTE en vez de reescribir la logica cada vez.
- Parametros: IN (entra un valor, ej. p_id_mascota), OUT (el proc devuelve un valor al que lo llamo, ej. p_msg con el resultado), IN OUT (ambos). A diferencia de una consulta suelta, un proc puede recibir varios parametros y ejecutar varias sentencias como una sola unidad logica.
- Ventaja central para el PI: sin proc, cada pantalla de la futura app (o cada integrante del equipo) reescribiria la regla 'mascota inactiva no agenda' con su propio SQL, y tarde o temprano alguien la escribe distinto o la olvida. Con el proc, la regla vive UNA vez dentro de la BD; toda la app la respeta sin excepcion.
- Manejo de errores controlado: en vez de dejar que la insercion falle con un error crudo de motor, el proc valida primero (SELECT activa FROM mascota) y responde con un mensaje de negocio claro ('ERROR: mascota inactiva; no se agenda'), y usa EXCEPTION/TRY-CATCH segun el motor para capturar fallos inesperados sin tumbar la transaccion completa.
- Diferencia con una funcion (se vera en Clase 4): el procedimiento se ejecuta como una accion (CALL sp_algo), la funcion se invoca dentro de una expresion SQL y retorna un valor (SELECT fn_algo(x) FROM ...).
- Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre, no resuelve el problema que motiva usar procedimientos.

**Demo que usted debe poder repetir:** CREATE PROCEDURE sp_agendar_cita(...) con validacion de mascota activa.

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

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: >=1 procedimiento de negocio (agendar cita / registrar consulta).
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
- Un procedimiento almacenado (stored procedure) es un bloque de codigo SQL/PLSQL con nombre propio, guardado y compilado DENTRO de la base de datos, que se invoca con CALL o EXECUTE en vez de reescribir la logica cada vez.
- Parametros: IN (entra un valor, ej. p_id_mascota), OUT (el proc devuelve un valor al que lo llamo, ej. p_msg con el resultado), IN OUT (ambos). A diferencia de una consulta suelta, un proc puede recibir varios parametros y ejecutar varias sentencias como una sola unidad logica.
- Ventaja central para el PI: sin proc, cada pantalla de la futura app (o cada integrante del equipo) reescribiria la regla 'mascota inactiva no agenda' con su propio SQL, y tarde o temprano alguien la escribe distinto o la olvida. Con el proc, la regla vive UNA vez dentro de la BD; toda la app la respeta sin excepcion.
- Manejo de errores controlado: en vez de dejar que la insercion falle con un error crudo de motor, el proc valida primero (SELECT activa FROM mascota) y responde con un mensaje de negocio claro ('ERROR: mascota inactiva; no se agenda'), y usa EXCEPTION/TRY-CATCH segun el motor para capturar fallos inesperados sin tumbar la transaccion completa.
- Diferencia con una funcion (se vera en Clase 4): el procedimiento se ejecuta como una accion (CALL sp_algo), la funcion se invoca dentro de una expresion SQL y retorna un valor (SELECT fn_algo(x) FROM ...).
- Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre, no resuelve el problema que motiva usar procedimientos.
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: CREATE PROCEDURE sp_agendar_cita(...) con validacion de mascota activa.
Herramienta: Oracle Live SQL
📸 sp_agendar_cita: caso OK vs caso rechazado por mascota inactiva [[captura: salida-proc-ok-y-error.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Implementar sp_agendar_cita o sp_registrar_consulta en Live SQL.
2. Incluir validacion de negocio del PI (>=1).
3. Ejecutar 2 pruebas: caso OK + caso error.
4. Documentar firma del proc (contrato para la futura app).
Circular por equipos (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script proc + casos de prueba (captura o enlace Live SQL)
📸 Pantallazo: [CAP: avance equipo / playground Clase 3]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 3 - VetCare.docx`. Clave para usted: `Quiz Clase 3 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre
**Decir:** «Queda avanzado: >=1 procedimiento de negocio (agendar cita / registrar consulta). Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 03_procs_vetcare.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
