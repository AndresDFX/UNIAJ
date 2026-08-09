# Guion docente · Clase 8 · Tuning · Transacciones · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Transaccion de negocio (factura + stock) + notas de tuning
- **Entregable de hoy:** Script transaccional + checklist tuning del PI (1 pag.)
- **Herramienta:** Oracle Live SQL / DB Fiddle
- **Slides:** Clases/Clase 8 - Tuning y transacciones/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Una transaccion agrupa varias sentencias SQL en una sola unidad de todo-o-nada: si facturar implica INSERT en factura, INSERT en detalle_factura Y UPDATE de stock en insumo, las tres deben aplicarse juntas o ninguna — nunca queda una factura sin descontar stock, ni stock descontado sin factura.
- Propiedades ACID en una frase cada una: Atomicidad (todo o nada, ya explicado), Consistencia (la BD pasa de un estado valido a otro, respetando reglas como stock>=0), Aislamiento (transacciones concurrentes no se pisan entre si — se profundiza en Clase 10), Durabilidad (una vez hecho COMMIT, el dato sobrevive aunque el sistema se caiga un segundo despues).
- COMMIT confirma la transaccion de forma permanente; ROLLBACK deshace todo lo hecho desde el ultimo COMMIT si algo salio mal (ej. el insumo no tenia stock suficiente). Sin ROLLBACK explicito ante el error, quedaria una factura registrada sin el descuento real de stock: inconsistencia de datos.
- Dirty read (lectura sucia): una transaccion lee un dato que otra transaccion modifico pero AUN NO ha confirmado con COMMIT; si esa segunda transaccion hace ROLLBACK despues, la primera trabajo con un dato que nunca existio de verdad. Es uno de los problemas que el nivel de aislamiento intenta evitar.
- Tuning en este contexto no es magia, son habitos concretos: mantener estadisticas del optimizador actualizadas (para que EXPLAIN elija bien), apoyarse en los indices ya justificados en Clase 7, y mantener las transacciones lo mas CORTAS posible — una transaccion larga retiene bloqueos (locks) sobre filas y puede frenar a otras transacciones que esperan esas mismas filas.
- Error de docente que no domina el tema: envolver TODA la sesion de trabajo en una sola transaccion gigante 'para no perder nada' — eso maximiza el tiempo que otros usuarios quedan bloqueados esperando esas filas, exactamente el problema que Clase 10 (concurrencia) va a diagnosticar.

**Demo que usted debe poder repetir:** BEGIN... INSERT factura/detalle... UPDATE stock... COMMIT/ROLLBACK.

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
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Transaccion de negocio (factura + stock) + notas de tuning.
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
- Una transaccion agrupa varias sentencias SQL en una sola unidad de todo-o-nada: si facturar implica INSERT en factura, INSERT en detalle_factura Y UPDATE de stock en insumo, las tres deben aplicarse juntas o ninguna — nunca queda una factura sin descontar stock, ni stock descontado sin factura.
- Propiedades ACID en una frase cada una: Atomicidad (todo o nada, ya explicado), Consistencia (la BD pasa de un estado valido a otro, respetando reglas como stock>=0), Aislamiento (transacciones concurrentes no se pisan entre si — se profundiza en Clase 10), Durabilidad (una vez hecho COMMIT, el dato sobrevive aunque el sistema se caiga un segundo despues).
- COMMIT confirma la transaccion de forma permanente; ROLLBACK deshace todo lo hecho desde el ultimo COMMIT si algo salio mal (ej. el insumo no tenia stock suficiente). Sin ROLLBACK explicito ante el error, quedaria una factura registrada sin el descuento real de stock: inconsistencia de datos.
- Dirty read (lectura sucia): una transaccion lee un dato que otra transaccion modifico pero AUN NO ha confirmado con COMMIT; si esa segunda transaccion hace ROLLBACK despues, la primera trabajo con un dato que nunca existio de verdad. Es uno de los problemas que el nivel de aislamiento intenta evitar.
- Tuning en este contexto no es magia, son habitos concretos: mantener estadisticas del optimizador actualizadas (para que EXPLAIN elija bien), apoyarse en los indices ya justificados en Clase 7, y mantener las transacciones lo mas CORTAS posible — una transaccion larga retiene bloqueos (locks) sobre filas y puede frenar a otras transacciones que esperan esas mismas filas.
- Error de docente que no domina el tema: envolver TODA la sesion de trabajo en una sola transaccion gigante 'para no perder nada' — eso maximiza el tiempo que otros usuarios quedan bloqueados esperando esas filas, exactamente el problema que Clase 10 (concurrencia) va a diagnosticar.
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: BEGIN... INSERT factura/detalle... UPDATE stock... COMMIT/ROLLBACK.
Herramienta: Oracle Live SQL / DB Fiddle
📸 Transaccion con stock insuficiente: el ROLLBACK deja todo como estaba [[captura: salida-rollback-stock.png]]
Dejar script/enlace en el chat o Campus.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Implementar bloque/proc que facture y descuente stock atomicamente.
2. Probar fallo a mitad (stock insuficiente) -> ROLLBACK.
3. Completar checklist tuning del PI.
4. Actualizar informe PI: seccion transacciones.
Circular por equipos (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script transaccional + checklist tuning del PI (1 pag.)
📸 Pantallazo: [CAP: avance equipo / playground Clase 8]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 8 - VetCare.docx`. Clave para usted: `Quiz Clase 8 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre
**Decir:** «Queda avanzado: Transaccion de negocio (factura + stock) + notas de tuning. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 08_transacciones_vetcare.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
