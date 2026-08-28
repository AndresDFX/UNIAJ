# Revisión de calidad · Talleres y bancos de ExamLab · 2026-2

**Alcance:** Bases de Datos II (FI303215) y Arquitectura de Sistemas Computacionales
(FI303380). Se revisaron las 24 clases con taller de los dos cursos, pregunta por pregunta,
al escribir la solución docente de cada una.
**No incluye** Programación II ni Seminario de Sistemas (ver §5).

**Qué es este documento.** No es un listado de errores para corregir a ciegas. Es el
inventario de lo que se encontró al resolver cada taller de verdad —ejecutando el SQL,
sumando los puntos, simulando los datos— y **qué se hizo con cada hallazgo**. La mayoría
no se «arregló» tocando el banco: se convirtió en material didáctico dentro de la solución
docente, porque un defecto que el estudiante va a encontrar es mejor anunciado que
disimulado. Los que **sí** requieren decisión están marcados en §1.

**Cómo se verificó.** Todo el SQL de las soluciones de BD II se simuló contra la semilla
real de cada pregunta: los conteos de filas, los totales y los mensajes de error que
aparecen en la sección «Salida esperada» son los que devuelve el motor, no estimaciones.
Los puntos de cada pregunta se validaron contra el banco con
`config/slides/` + el verificador `verifica_sol.py`, que compara número de preguntas, tipo,
puntos y totales: **BD II 12/12 clases y Arquitectura 12/12 clases cuadran al 100 %**.

---

## 1. Requiere decisión del docente (5 hallazgos)

Son los únicos que conviene resolver antes del próximo semestre, porque afectan lo que el
estudiante ve o lo que el enunciado promete.

### 1.1 · BD II Clase 12 — las funciones `api_*` no llevan `SECURITY DEFINER`

**Severidad: alta.** Es el hallazgo más importante de la revisión.

La arquitectura que plantea la clase es correcta y es la buena práctica: la aplicación se
conecta con un rol que **solo** tiene `EXECUTE` sobre tres funciones `api_*` y ningún
privilegio directo sobre las tablas. El problema es que, tal como están escritas en el
banco, esas funciones **no pueden funcionar** bajo ese esquema: sin `SECURITY DEFINER` se
ejecutan con los privilegios de quien las llama, y quien las llama es precisamente el rol
que no tiene permiso de escribir en `cita`. El resultado es un `permission denied for table
cita` en la primera llamada.

**Qué se hizo:** la solución docente añade `SECURITY DEFINER` junto con
`SET search_path = public, pg_temp` —el `SET` no es opcional: sin él, una función con
privilegios elevados es un vector de escalada— y el `REVOKE EXECUTE ... FROM PUBLIC` con la
firma exacta. La explicación quedó como el eje conceptual de la clase, con la prueba
negativa vía `SET ROLE` / `RESET ROLE`.

**Decisión pendiente:** añadir `SECURITY DEFINER` al enunciado del banco, o dejarlo fuera
a propósito para que el estudiante choque con el error y lo diagnostique. La segunda opción
es pedagógicamente mejor **si el enunciado avisa** que la primera llamada va a fallar; tal
como está ahora, el estudiante no tiene forma de saber que el fallo es parte del ejercicio.

### 1.2 · BD II Clase 13 — la consulta sugerida de `buscar_mascota_directa` no compila

**Severidad: alta**, porque bloquea al estudiante en mitad del taller.

El enunciado sugiere reescribir la función vulnerable con una consulta estática. Pero la
función es `RETURNS TABLE (nombre TEXT, especie TEXT, ...)`, y en PL/pgSQL esos parámetros
de salida **sombrean las columnas de la tabla**: al primer llamado el motor devuelve
`column reference "nombre" is ambiguous / DETAIL: It could refer to either a PL/pgSQL
variable or a table column`. No falla al crear la función, falla al usarla, que es lo que
hace el diagnóstico difícil.

**Qué se hizo:** la solución usa alias y califica las columnas (`FROM mascota m ... m.nombre`),
explica el mecanismo en una pregunta frecuente y lo anuncia en la nota de actividad para que
el docente lo advierta antes de que empiecen. También se dejó dicho por qué la versión con
`EXECUTE '<cadena>' USING` **no** sufre el problema: la cadena no está sujeta a sustitución
de variables de plpgsql.

**Decisión pendiente:** corregir el enunciado del banco, o mantenerlo y convertir el error
en el ejercicio de diagnóstico (declarándolo).

### 1.3 · BD II Clase 15 — la semilla no ejerce tres de sus propios requisitos

**Severidad: media-alta.**

La rúbrica de la pregunta 2 exige que el KPI de carga por veterinario conserve a los
veterinarios **sin citas**, que el KPI de insumos incluya los **nunca vendidos** y que el de
ingresos **ordene cronológicamente**. Pero en los datos entregados los cuatro veterinarios
tienen citas, los seis insumos aparecen en `detalle_factura` y las tres facturas caen en el
mismo mes. Consecuencia: **la consulta correcta y la incorrecta devuelven exactamente lo
mismo**, y el estudiante no puede distinguirlas ni el docente calificarlas por resultado.

**Qué se hizo:** la solución convierte esto en el deliverable —tres `INSERT` que crean el
caso de borde (un veterinario nuevo, un insumo nuevo y una factura en octubre) y las dos
corridas contrastadas— y le asigna 6 de los 20 puntos, con el criterio explícito de que
también se otorgan si el estudiante solo lo advierte por escrito. La idea de fondo es la
misma de la Clase 13: un KPI que no se ha probado contra su caso de borde es una suposición.

**Decisión pendiente:** añadir esas tres filas a la semilla del banco (lo más simple), o
mantenerlas fuera y dejar la creación del caso de borde como parte del ejercicio.

### 1.4 · BD II Clase 13 — la elección de caso A/B/C no encaja con las preguntas 2 y 3

**Severidad: media.**

La pregunta 1 deja elegir entre tres incidentes reales, pero las preguntas 2 y 3 implementan
las mitigaciones de solo dos de ellos (inyección SQL y respaldo/restauración). Quien elija el
tercer caso llega a la pregunta 5 sin poder conectar su análisis con lo que implementó.

**Qué se hizo:** la nota de actividad recomienda orientar al grupo hacia los dos casos con
mitigación implementada, y para quien haya elegido el tercero se aceptan como evidencia los
artefactos de la Clase 6 (el índice `idx_cita_vet_fecha` y el par de `EXPLAIN`). Quedó
también en la rúbrica de la pregunta 1 y en los errores frecuentes de la 5.

### 1.5 · Arquitectura Clase 11 — la regla de fechas de la pregunta 4 no es aplicable

**Severidad: media (logística).**

La pregunta pide comprometer fechas distintas para los hitos de la Clase 11 y de la Clase
12, pero en el calendario 2026-2 **ambas son la misma sesión doble** (2026-10-26). La regla,
tal como está redactada, no se puede cumplir.

**Qué se hizo:** la nota de actividad de la solución explica el solape y da el criterio de
calificación alternativo. Lo mismo aplica a BD II, donde las Clases 11 y 12 también caen en
el bloque doble del 2026-10-26 y la demo por estudiante no cabe en vivo.

---

## 2. Resueltos en la solución docente (18 hallazgos)

No requieren tocar el banco: la solución los absorbe, los explica y en varios casos los usa
como el punto central de la clase.

| # | Clase | Hallazgo | Cómo se resolvió |
|---|---|---|---|
| 1 | BD II 4 | «Un trigger `AFTER` no puede impedir el cambio» es impreciso: una excepción en un `AFTER` **sí** aborta la sentencia | Corregido en la prosa de la solución, conservando el criterio de calificación del banco |
| 2 | BD II 6 | La consulta de la pregunta 1 ordena por `c.fecha_hora` sin desempate: el orden no es determinista | La solución añade el desempate y explica que sin él la captura del informe puede no reproducirse |
| 3 | BD II 6 | El encuadre de «antipatrón» promete una mejora que no se obtiene sin índice | Reencuadrado: se separa lo que mejora la reescritura de lo que solo mejora el índice |
| 4 | BD II 7 | El resultado de la pregunta 2 depende de la versión del motor | Se aceptan los dos resultados y se muestra que la conclusión es la misma |
| 5 | BD II 7 | «Qué índice eligió el planificador» no tiene respuesta garantizada | Se califica contra el plan que el propio estudiante obtuvo, no contra uno esperado |
| 6 | BD II 7 | El taller crea cinco índices solapados sin decirlo | Hecho explícito en la rúbrica de la pregunta 5: el costo de escritura es parte de la respuesta |
| 7 | BD II 8 | Con una sola sesión, el taller no puede distinguir el patrón seguro del inseguro para el stock | Convertido en el entregable calificable: el estudiante argumenta la diferencia y declara el límite del entorno |
| 8 | BD II 10 | Es **clase autónoma** (2026-10-12): no hay docente en vivo | La retroalimentación de la solución está escrita para leerse sin acompañamiento |
| 9 | BD II 11 | Las facturas 1–3 de la semilla están descuadradas bajo las dos definiciones plausibles, así que la prueba 5 da `cumple = FALSE` legítimamente | Convertido en el punto central de la clase: un `FALSE` bien documentado vale más que un `TRUE` forzado. Reaparece y se cierra en la Clase 15 |
| 10 | BD II 11 | Dos requisitos de la pregunta 3 no son verificables con la semilla | La rúbrica indica leer el SQL en esos dos casos |
| 11 | BD II 11–12 | Misma sesión doble (2026-10-26): la demo por estudiante no cabe en vivo | Declarado en la nota de actividad con el reparto alternativo |
| 12 | BD II 12 | El control de franja de `api_agendar_cita` usa `SELECT COUNT(*)`, que reintroduce el *write skew* de la Clase 10 dentro de la API que el PI va a entregar | Señalado en la solución como el defecto a corregir con el índice único parcial `uq_cita_vet_franja`. Es un buen ejercicio de continuidad entre clases |
| 13 | BD II 12 | `api_facturar` crea una factura por línea de insumo: una visita con tres insumos genera tres facturas, y como `factura.id_consulta` no es `UNIQUE`, el KPI 4 de la Clase 15 duplicaría filas | Documentado con la corrección y con la consecuencia aguas abajo |
| 14 | BD II 13 | El *trigger* de archivo no se dispara en `TRUNCATE`, se puede desactivar con `ALTER TABLE ... DISABLE TRIGGER`, y `respaldo_cita` vive en la **misma** base | Convertido en un extra ejecutable: un `BEFORE TRUNCATE ... FOR EACH STATEMENT` que lanza excepción y se puede probar sin perder datos |
| 15 | ARQ 3 | Títulos de diapositiva casi duplicados (5/8/9 sobre VM vs contenedor; 7/10 sobre el Dockerfile) | Cosmético; el guion referencia cada bloque por número de diapositiva, así que no hay ambigüedad al dictar |
| 16 | ARQ 13 | El rango de ejemplo «2 a 6 réplicas» contradice el techo de 4 réplicas de la política | Se califica «el rango de la política propia» y se aclara en una pregunta frecuente |
| 17 | ARQ 15 | La lámina de referencia incluye un nodo de almacén de adjuntos que el proyecto del estudiante no tiene | Se resuelve por omisión justificada: el estudiante argumenta por qué no aplica |
| 18 | ARQ Corte 1 ↔ 11-15 | La arquitectura del Corte 1 no tiene cola ni *worker*, que sí aparecen en los bancos de las Clases 11–15 | Tratado como evolución documentada del diseño, no como inconsistencia a ocultar |

---

## 3. Corregido en código (1)

**El renderizador de soluciones partía el cierre de clase letra por letra.**
`solucion_taller.render_md` asumía que `cierre` era siempre una lista. Arquitectura lo
entrega como párrafo corrido, y el `for` lo iteraba carácter a carácter: el documento salía
con una viñeta por letra. Corregido con un `isinstance` que admite las dos formas
(`config/slides/solucion_taller.py:131-137`). Afectaba a las 12 soluciones de Arquitectura,
que quedaron regeneradas.

---

## 4. Hallazgo retirado (1)

**«Mojibake en el resumen del banco de Arquitectura Clase 15» — no es un defecto.** Era un
artefacto de la codificación de la consola al volcar el banco, no del archivo. El dato está
correcto en origen. Se deja anotado para no volver a «corregirlo».

---

## 5. Fuera de alcance

La revisión cubrió **Bases de Datos II y Arquitectura de Sistemas Computacionales**, que son
los dos cursos que pidió el encargo. **Programación II y Seminario de Sistemas no se
revisaron** y no hay razón para suponer que estén libres de hallazgos equivalentes: los dos
tienen bancos de ExamLab con el mismo tipo de semillas y rúbricas, y el patrón más frecuente
de esta revisión —una rúbrica que exige un comportamiento que la semilla no ejerce— es
exactamente el que se detecta solo al resolver el taller de verdad.

---

## 6. Estado de los dos cursos

| | Guion con teoría por diapositiva | Solución docente completa | Validación contra el banco |
|---|---|---|---|
| **Bases de Datos II** | 12/12 clases con taller | 12/12 (1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 15) | 100 puntos declarados = 100 del banco, en las 12 |
| **Arquitectura** | 12/12 clases con taller | 12/12 (1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 15) | Totales por corte cuadran en las 12 |

Las Clases 5, 9 y 14 de los dos cursos son parciales y no llevan taller ni solución.

**Reproducir la validación:**

```bash
cd config/slides
python build_uniajc_bd2_all.py
python build_uniajc_arq_clases_batch.py
```

El verificador de correspondencia solución ↔ banco compara, por clase, los números de
pregunta, el tipo, los puntos de cada una, la suma frente al total declarado y frente al
total del banco, y exige cuerpo de respuesta, desglose de calificación, errores frecuentes y
al menos cuatro preguntas frecuentes.
